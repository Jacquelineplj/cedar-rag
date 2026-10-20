# Assignment and rubric recheck - historical snapshot

This records the state before the requested completion work. See submission-completion.md for the current state.

Rechecked on October 20, 2026. This report separates verified technical work from unfinished student submission work. It does not assign an instructor's grade.

## Verification performed again

- Read the assignment tasks, prompts, submission instructions, and rubric again.
- Compared all six paragraph texts directly with page 2 of the PDF, ignoring PDF layout whitespace only: passed.
- Loaded the real cached all-MiniLM-L6-v2 model on CPU and reran the experiment script into a temporary directory, leaving original evidence untouched.
- Reproduced the selected IDs for all four questions and both retrieval methods. Saved selected scores agreed within absolute tolerance 1e-6.
- Reproduced Q1 at k=1,2,3. Matrix/vector shape, normalization, and direct-cosine assertions passed.
- Rechecked exact stopword set, repeated-token behavior, zero-match output, and ID tie ordering: passed.
- Compared saved original/revised answers with their conversation records. They match; no answer-side tool calls are recorded.

## Rubric

| Criterion | Weight | Current assessment |
| --- | --- | --- |
| Visible embedding process | 3 | Technical evidence complete: real vectors, shapes, lengths, 384-coordinate similarity, first-12 products and remaining subtotal, cosine comparison. |
| Retrieval comparison | 3 | Four runs and k experiment complete; Codex observations are in retrieval-audit.md. Submission incomplete because results.csv judgment and observation cells are still blank. |
| Grounded answer audit | 2 | Both audits present. Original Q1 failure retained; one revised instruction with unchanged evidence fixed the missing-hours acknowledgment. Q4 correctly abstains. Student verification remains requested. |
| Reproducibility and explanation | 2 | Existing environment rerun succeeds; README commands and code explanations present; dependency lockfile present. Names and personal reflection are missing. A brand-new dependency installation was not repeated in this recheck. |

Full credit cannot be claimed while these submission fields remain incomplete.

## Prompt-by-prompt check

### Setup

- PASS: cedar-rag directory, Git initialization, Python 3.12.8, local .venv, sentence-transformers and numpy, CPU model, recorded installed versions.
- PASS: code and evidence committed and pushed to the GitHub repository during the original work.
- NOT COMPLETED: no separate Codex Project was created or registered for cedar-rag. A local working folder and repository were created instead.
- ORDER DIFFERENCE: the model was loaded after the baseline run, rather than confirmed before Task 1 as described in initial setup. The later embedding experiments did use the installed real model.

### Prompt 1: keyword baseline

- PASS: verbatim source paragraphs in the three requested docs files; exactly six chunks; separate IDs and filenames excluded from searched text.
- PASS: lowercase alphanumeric tokens, exact stopwords, distinct-word overlap, no stemming or synonyms.
- PASS: descending score, ascending ID ties, all six scores and matched words, positive-only top k, default k=2, no-match message, selected complete passages and filenames.
- PASS: question/k CLI arguments, exact run commands, plain-language explanation with line references, actual Q1 output.
- PASS: expected Q1 evidence was recorded before retrieval; manual score check and baseline audit were recorded. No answer was generated during the baseline stage.

### Prompt 2: embeddings

- PASS: specified model on CPU with numpy; encode_document and encode_query with normalization and numpy output; only paragraph text encoded.
- PASS: six document embeddings computed once per experiment-script run and reused across questions.
- PASS: actual versions, shapes, first 12 coordinates to four decimals, vector lengths, use of all 384 coordinates, and no invented coordinate meanings.
- PASS: all six dot-product scores, sorting/tie rule, default k=2, complete top passages, no relevance threshold.
- PASS: Q1 coordinate products, first-12 subtotal, remaining-372 subtotal, full similarity, direct-cosine verification, saved inspection file, explanation.
- NOTE: float32 summation produces an approximately 1.2e-7 difference between displayed matrix-dot and product-sum totals. This is documented and below the stated tolerance; the rankings are unaffected.

### Prompt 3: comparison

- PASS: Q1-Q4 through both methods at k=2, actual saved output, four CSV rows, exact column names, scores in rank order, Q4 required_ids=absent.
- PASS: judgment fields initially left blank, exactly as prompt 3 requests.
- INCOMPLETE FOR FINAL SUBMISSION: the later submission instruction requests results.csv with judgments. Those fields have not yet been completed. Separate Codex observations do not replace the requested completed CSV.
- PASS: Q1 coverage correctly recorded as keyword 2/2, embedding 1/2. Q2/Q3 required chunks retrieved; useful Q3 match and actual score discussed. Q4 missing answer distinguished from similarity.
- PASS: Q1 k=1 and k=3 reruns (also k=2), selected IDs, coverage, and explanation of added conditions/distractions.
- NOT CLAIMED: human partner role swapping or oral explanation. No partner was identified.

### Prompt 4: answers and defense

- PASS: Q1 and Q4 generated in separate fresh projectless chats using only the question, selected embedding passages at k=2, and the supplied answer instruction.
- PASS: no full corpus attached; no project attached; no answering-chat browsing, file reads, or other tool calls recorded. This verifies observed behavior, not an operating-system-level isolation guarantee.
- PASS: citations and missing information audited. Q1 original omission preserved and one prompt revision rerun with unchanged passages. Revised Q1 acknowledges missing access hours; Q4 states wavelength is unspecified.
- PENDING: the student must personally check these Codex-generated audits.

## Did the prompts run literally one by one?

No. The first three prompts were implemented together as one project rather than pasted as three separate user turns. The baseline was run first, followed by embedding inspection/comparison and then fresh answer conversations. Initial model loading did not precede the baseline. The required computations and outputs were produced, but literal prompt-by-prompt interaction and the complete setup order should not be claimed.

## Remaining before submission

1. Add student/partner names to README.md.
2. Verify the recorded evidence and fill results.csv's keyword_evidence_complete, embedding_evidence_complete, and observation columns. For Q4 explicitly indicate absent evidence; do not mark related passages as answer retrieval success.
3. Write each student's own reflection, no more than 150 words, covering workflow, an observed limitation, and a next experiment. REFLECTION.md currently contains instructions only.
4. Ensure the grader can access the private repository and submit its URL through the course sign-up sheet. No course submission was performed.
5. The README points to recorded model/package versions rather than listing the installed package versions directly in its prose. Listing the versions explicitly there would make compliance with the submission wording clearer.

No run evidence, student judgment fields, personal reflection, GitHub state, or code was changed by this recheck. This audit report is the only new file.
