# Cedar Lab RAG

**Student:** Jacqueline Pan

Prepared with Codex assistance. All numerical evidence comes from local runs of the real model; no borrowed output or fabricated scores are used.

## Run

From the `cedar-rag` directory:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-lock.txt
export HF_HOME="$PWD/.cache/huggingface"
.venv/bin/python retriever.py Q1 --method keyword -k 2
.venv/bin/python retriever.py Q1 --method embedding -k 2
.venv/bin/python run_experiments.py
```

The CLI accepts `Q1` through `Q4` or a quoted question. For example:

```sh
.venv/bin/python retriever.py 'Can I use the laser without another person present?' --method keyword -k 2
.venv/bin/python retriever.py Q1 --method embedding -k 1
.venv/bin/python retriever.py Q1 --method embedding -k 3
```

The first embedding run downloads the model and requires internet. Later runs can use `HF_HUB_OFFLINE=1`. Inference runs on CPU with no API key or GPU. Keyword retrieval uses only Python's standard library.

`run_experiments.py` encodes the six passages once and reuses them for all four questions and the k experiment. It saves vector inspection, retrieval runs, k results, and answer inputs. New comparison results have blank audit fields; unchanged results preserve completed judgments in `results.csv`. Changed IDs or scores reset those judgments for review.

Answer generation is a manual handoff: paste each saved `q1-answer-input.txt` or `q4-answer-input.txt` into a fresh conversation without project access. Use only its supplied passages and instruction. The saved audits contain the actual generated answers and claim checks, including Q1's original failure and one revision.

## Environment

| Component | Recorded version |
| --- | --- |
| Python | 3.12.8 |
| Model | sentence-transformers/all-MiniLM-L6-v2 |
| Model revision | 1110a243fdf4706b3f48f1d95db1a4f5529b4d41 |
| sentence-transformers | 6.1.0 |
| numpy | 2.5.4 |
| torch | 2.14.1 |
| transformers | 5.20.2 |
| huggingface-hub | 1.33.0 |

All installed dependency versions are pinned in `requirements-lock.txt`.

## Code explanation

In `retriever.py`, lines 25-36 load each labeled paragraph as one chunk and keep its ID and filename separate from searchable text. The three files produce exactly six chunks.

Lines 38-45 lowercase text, extract alphanumeric words, remove exactly the handout's stopwords, and count distinct shared query words. Sets prevent repeated words from increasing a score. Line 45 sorts by descending score and ascending ID; line 52 selects up to k positive scores. There is no stemming or synonym matching.

Lines 68-73 load the pretrained model on CPU and encode passage text as a normalized `(6,384)` matrix. Line 85 encodes a question as a normalized `(384,)` vector. Both use the same model and compatible coordinates; individual coordinates do not have reliable semantic names. This model uses the same underlying encoding behavior for `encode_document` and `encode_query`.

Line 91 computes all six dot products using every coordinate. Unit vector lengths make these scores agree with cosine similarity; lines 92-94 check this numerically. Lines 95-98 sort the scores and select the first k with no relevance threshold. Lines 100-106 expose the first 12 products and both subtotals for Q1's top passage. Computation uses unrounded values.

Retrieval chooses candidate evidence; the language model writes a cited answer from that context. No model is trained on these six paragraphs, and RAG does not change the generator's weights. Similarity alone establishes neither truth nor answerability. Keyword counts and embedding similarities have different scales.

## Results and evidence

- `docs/`: the six verbatim paragraphs in the three required source files.
- `results.csv`: four comparisons with selected IDs, scores, evidence judgments, and observations.
- `evidence/keyword-q1.txt` and `keyword-audit.md`: actual baseline output, prior evidence prediction, and manual score check.
- `evidence/embedding-inspection.txt`: real vectors, dimensions, lengths, six scores, coordinate products, and cosine verification.
- `evidence/retrieval-runs.txt` and `retrieval-audit.md`: all questions through both methods and interpretation of the results.
- `evidence/k-experiment.txt`: Q1 at k=1,2,3 with evidence coverage.
- `evidence/q1-answer-input.txt` and `q4-answer-input.txt`: exact prompts and retrieved passages for answer generation.
- `evidence/q1-answer-audit.md` and `q4-answer-audit.md`: original answers, citations, missing-information checks, and Q1's preserved failure plus one revision.
- `REFLECTION.md`: 104-word reflection, with Codex assistance disclosed.

Q1's keyword evidence covers A1 and A2; embeddings retrieve A2 and T1, leaving access hours missing. Both methods find the required evidence for Q2 and Q3. No source specifies Q4's wavelength, so both Q4 completeness fields are false.

## Submission status

Repository: [Jacquelineplj/cedar-rag](https://github.com/Jacquelineplj/cedar-rag), currently private. The grader needs repository access.

The code and evidence are present. The course sign-up sheet has not been updated. Submit the repository URL through the [course sheet](https://docs.google.com/spreadsheets/d/1ZewIG5udWWpk3Kdrab5yDbsWDV4gnH3liKobIAp7HG4/edit?usp=sharing).

The assignment asks for a personal reflection written by the student. The current AI-assisted reflection still needs Jacqueline's own review and revision. The work runs in the existing `ps5` Codex Project; a separate `cedar-rag` Project has not been registered.
