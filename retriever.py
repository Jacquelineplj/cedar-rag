"""Transparent keyword baseline and real CPU embedding retrieval for Cedar Lab."""
import argparse
from dataclasses import dataclass
from importlib.metadata import version
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent
MODEL = 'sentence-transformers/all-MiniLM-L6-v2'
STOPWORDS = set('a an the is are to of in at for and or may can i it be'.split())
QUESTIONS = {
    'Q1': 'May a trained graduate student operate the laser alone at 19:00?',
    'Q2': 'Can I use the laser without another person present?',
    'Q3': 'How frequently must I refresh my laser qualification?',
    'Q4': 'What is the laser wavelength?',
}
REQUIRED = {'Q1': ['A1', 'A2'], 'Q2': ['A2'], 'Q3': ['T1'], 'Q4': []}

@dataclass(frozen=True)
class Chunk:
    id: str
    filename: str
    text: str

def load_chunks():
    """Load one labeled paragraph per chunk, keeping labels out of search text."""
    chunks = []
    for path in sorted((ROOT / 'docs').glob('*.txt')):
        for paragraph in path.read_text().strip().split('\n\n'):
            match = re.fullmatch(r'\[([A-Z][0-9]+)\]\s+(.+)', paragraph, re.DOTALL)
            if not match:
                raise ValueError(f'Malformed paragraph in {path.name}')
            chunks.append(Chunk(match[1], path.name, match[2]))
    if sorted(c.id for c in chunks) != ['A1', 'A2', 'B1', 'B2', 'T1', 'T2']:
        raise ValueError('Expected exactly the six Cedar Lab chunk IDs')
    return sorted(chunks, key=lambda c: c.id)

def words(text):
    return set(re.findall(r'[a-z0-9]+', text.lower())) - STOPWORDS

def keyword_rank(chunks, question):
    query_words = words(question)
    scored = [(c, len(query_words & words(c.text)), sorted(query_words & words(c.text)))
              for c in chunks]
    return sorted(scored, key=lambda row: (-row[1], row[0].id))

def print_keyword(chunks, question, k=2):
    ranking = keyword_rank(chunks, question)
    print(f'Question: {question}\nMethod: keyword; k={k}')
    for chunk, score, matches in ranking:
        print(f'{chunk.id}: score={score}; matched words={", ".join(matches) or "(none)"}')
    selected = [(c, s) for c, s, _ in ranking if s > 0][:k]
    print_selected(selected)
    if not selected:
        print('No matching passages.')
    return selected

def print_selected(selected):
    print('Selected IDs: ' + (', '.join(c.id for c, _ in selected) or '(none)'))
    for chunk, score in selected:
        print(f'[{chunk.id}] {chunk.filename}\n{chunk.text}')

class EmbeddingRetriever:
    def __init__(self, chunks):
        import numpy as np
        from sentence_transformers import SentenceTransformer
        self.np, self.chunks = np, chunks
        self.model = SentenceTransformer(MODEL, device='cpu')
        self.documents = self.model.encode_document(
            [c.text for c in chunks], normalize_embeddings=True, convert_to_numpy=True)
        if self.documents.shape != (6, 384):
            raise ValueError(f'Unexpected shape: {self.documents.shape}')
        assert np.allclose(np.linalg.norm(self.documents, axis=1), 1, atol=1e-6)
        print(f'Model: {MODEL}\nDevice: cpu')
        for package in ('sentence-transformers', 'numpy', 'torch', 'transformers', 'huggingface-hub'):
            print(f'{package}=={version(package)}')
        print(f'Document matrix shape: {self.documents.shape}')
        print('All 384 coordinates are used in retrieval; only the first 12 are displayed.')
        print('Individual coordinates are not assigned semantic names.')
        for chunk, vector in zip(chunks, self.documents):
            print(f'{chunk.id}: first 12={np.array2string(vector[:12], precision=4, floatmode="fixed")}; length={np.linalg.norm(vector):.8f}')

    def retrieve(self, question, k=2, inspect=False):
        np = self.np
        query = self.model.encode_query(question, normalize_embeddings=True, convert_to_numpy=True)
        print(f'\nQuestion: {question}\nMethod: embedding; k={k}')
        print(f'Question vector shape: {query.shape}')
        print(f'Question first 12={np.array2string(query[:12], precision=4, floatmode="fixed")}')
        print(f'Question length: {np.linalg.norm(query):.8f}')
        assert np.isclose(np.linalg.norm(query), 1, atol=1e-6)
        scores = self.documents @ query
        cosine = scores / (np.linalg.norm(self.documents, axis=1) * np.linalg.norm(query))
        assert np.allclose(scores, cosine, atol=1e-6, rtol=0)
        print(f'Dot products agree with direct cosine within tolerance 1e-6: {np.allclose(scores, cosine, atol=1e-6, rtol=0)}')
        ranking = sorted(zip(self.chunks, scores), key=lambda row: (-float(row[1]), row[0].id))
        for chunk, score in ranking:
            print(f'{chunk.id}: similarity={float(score):.8f}')
        selected = ranking[:k]
        print_selected(selected)
        if inspect:
            top = ranking[0][0]
            products = self.documents[self.chunks.index(top)] * query
            print(f'Q1 top passage {top.id}: first 12 products={np.array2string(products[:12], precision=8, floatmode="fixed")}')
            print(f'First 12 subtotal: {products[:12].sum():.8f}')
            print(f'Remaining 372 subtotal: {products[12:].sum():.8f}')
            print(f'Full similarity: {products.sum():.8f}')
            displayed = np.concatenate([self.documents[:, :12].ravel(), query[:12]])
            print(f'Largest displayed coordinate (documents and Q1): {displayed.max():.4f}')
            print(f'Smallest displayed coordinate (documents and Q1): {displayed.min():.4f}')
        return selected

def positive_k(value):
    value = int(value)
    if value < 1:
        raise argparse.ArgumentTypeError('k must be positive')
    return value

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('question', help='Question text or Q1 through Q4')
    parser.add_argument('--method', choices=['keyword', 'embedding'], default='keyword')
    parser.add_argument('-k', type=positive_k, default=2)
    args = parser.parse_args()
    chunks = load_chunks()
    question = QUESTIONS.get(args.question, args.question)
    if args.method == 'keyword':
        print_keyword(chunks, question, args.k)
    else:
        EmbeddingRetriever(chunks).retrieve(question, args.k, question == QUESTIONS['Q1'])

if __name__ == '__main__':
    main()
