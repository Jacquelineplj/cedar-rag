# Cedar Lab RAG challenge

A teaching workflow using six fictional Cedar Lab paragraphs. Document preparation, retrieval, and answer generation are separate steps. The corpus is classroom material.

## Setup and run

Python 3.12.8 was used. From this directory:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-lock.txt
export HF_HOME="$PWD/.cache/huggingface"
.venv/bin/python retriever.py Q1
.venv/bin/python retriever.py 'May a trained graduate student operate the laser alone at 19:00?' --method keyword -k 2
.venv/bin/python retriever.py Q1 --method embedding -k 2
.venv/bin/python run_experiments.py
```

The first embedding run downloads `sentence-transformers/all-MiniLM-L6-v2` and needs internet access. It runs on CPU with no API key or GPU. After download, set `HF_HUB_OFFLINE=1` to use the local cache. Installed versions are pinned in `requirements-lock.txt` and printed in `evidence/embedding-inspection.txt`. The keyword command uses only Python's standard library and works without installing the embedding dependencies.

`run_experiments.py` encodes the six documents once and reuses that matrix for Q1-Q4 and the k experiment. It regenerates evidence and writes the initially blank audit sheet to `results-template.csv`. It preserves completed judgments in `results.csv` when the recorded IDs and scores are unchanged; changed retrieval results reset those judgments for a new audit. It writes fresh answer inputs; the answers themselves use separate Codex conversations.

## Recorded environment

| Component | Version or setting |
| --- | --- |
| Python | 3.12.8 |
| Model | sentence-transformers/all-MiniLM-L6-v2 |
| Model revision | 1110a243fdf4706b3f48f1d95db1a4f5529b4d41 |
| Device | CPU |
| sentence-transformers | 6.1.0 |
| numpy | 2.5.4 |
| torch | 2.14.1 |
| transformers | 5.20.2 |
| huggingface-hub | 1.33.0 |

All installed dependency versions are in `requirements-lock.txt`. The model was loaded before the new sequential Task 1 rerun; the sequence is recorded in `evidence/sequential-run.txt`.

## How the code works

In `retriever.py`, lines 25-36 load the three files and split them into exactly six paragraphs. Each `Chunk` stores its ID, filename, and text in separate fields. Only text enters either search method.

Lines 38-45 implement the exact keyword rule: lowercase, extract alphanumeric tokens, remove the handout's exact stopwords, and intersect sets of words. Sets count a word only once. Lines 43-44 count matches; line 45 ranks by decreasing score, then increasing ID. Line 52 keeps up to k positive scores. There is no stemming or synonym matching.

Lines 68-73 load the pretrained model on CPU and encode the six document texts as a normalized 6 by 384 matrix. Each row is one passage. This is inference with learned model parameters, not training on the six paragraphs.

Line 85 encodes the question as a normalized vector with 384 coordinates. Both sides must use the same model and compatible representation so that matching positions can be multiplied meaningfully. `encode_document` and `encode_query` distinguish the roles; this model uses the same underlying encoding behavior for both.

Line 91 multiplies matching coordinates and sums them for each passage. Because the vectors have length approximately 1, this dot product agrees with cosine similarity; lines 92-94 verify it directly. Lines 95-98 sort six scores and select the first k, including low-scoring passages. This method always returns top k; a nearest passage need not contain an answer. Lines 100-106 expose the coordinate products for Q1's highest-ranked passage. All 384 values enter the calculation, with rounding only in printed output.

An individual coordinate has no reliable standalone meaning. The whole vector and its alignment with another vector carry the useful relationship. Similarity scores are neither probabilities nor proof that an answer is present. Keyword counts and cosine scores have different scales; compare retrieved evidence rather than their numerical magnitudes.

The embedding model retrieves candidate evidence. A separate Codex conversation writes a cited answer from selected passages. This changes the context supplied to the generator, not its learned weights. No answer-generation API, vector database, or web interface is used.

## Evidence and submission

- `docs/`: the six paragraphs, verbatim, in the three requested files.
- `evidence/prediction.md`: Q1 evidence prediction recorded before retrieval.
- `evidence/keyword-q1.txt` and `keyword-audit.md`: actual baseline run and manual score check.
- `evidence/embedding-inspection.txt`: model versions, real vectors, shapes, norms, scores, coordinate products, and cosine verification.
- `evidence/retrieval-runs.txt`: all four questions through both methods at k=2.
- `results-template.csv`: four comparison rows with blank judgment fields, preserving prompt 3's initial output.
- `results.csv`: final comparison rows with completed evidence judgments and observations.
- `evidence/k-experiment.txt`: Q1 at k=1, 2, and 3 with required evidence coverage.
- `evidence/q1-answer-input.txt` and `q4-answer-input.txt`: only prompt, question, and selected passages for fresh answer conversations.
- `evidence/retrieval-audit.md`: Codex observations for you to verify.
- `evidence/submission-completion.md`: current rubric checklist and remaining external setup/submission status.
- `evidence/final-pass/`: fresh Q1/Q4 answers and Q1 revision generated after the sequential retrieval run.
- `evidence/q1-answer-audit.md` and `q4-answer-audit.md`: claim audits, exact original answers, conversation records, and Q1's preserved failure plus one revision.
- `REFLECTION.md`: a 104-word individual reflection prepared with Codex assistance.

Student: **Jacqueline Pan**. No partner was listed.

Evidence judgments and audits were completed with Codex assistance at the user's request. The reflection identifies Codex assistance. No partner participation is claimed. All numerical run output is generated locally; no borrowed output is used.

## Remaining student work

Review the completed evidence judgments and reflection, ensure the grader can access the private repository, and submit the repository URL through the course sign-up sheet. If paired, each partner needs a separate individual reflection. The current Codex Project is `ps5`, containing this repository; a separate `cedar-rag` Project has not been registered because the available app tools do not create projects.

## GitHub publication

Repository: https://github.com/Jacquelineplj/cedar-rag (private), branch `main`. Ensure the grader has repository access.

Course submission sheet: https://docs.google.com/spreadsheets/d/1ZewIG5udWWpk3Kdrab5yDbsWDV4gnH3liKobIAp7HG4/edit?usp=sharing

The repository has been pushed. For a separate new checkout that has not yet been published:

```sh
gh auth login -h github.com
gh repo create cedar-rag --private --source=. --remote=origin --push
```

Choose visibility appropriate for the course and submit the repository link using the sign-up sheet linked in the handout. If `cedar-rag` already exists on your account, connect its remote instead of creating a duplicate. Do not commit `.venv/` or the model cache.
