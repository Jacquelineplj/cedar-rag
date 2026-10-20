# Submission completion record

Author: Jacqueline Pan. Completed with Codex assistance on October 20, 2026, following the user's explicit request to complete the outstanding materials.

## Final deliverables

| Rubric criterion | Weight | Evidence |
| --- | --- | --- |
| Visible embedding process | 3 | embedding-inspection.txt: real CPU model; (6,384) and (384,) shapes; first 12 coordinates; vector lengths; all six similarities; coordinate products/subtotals; direct cosine verification. |
| Retrieval comparison | 3 | retrieval-runs.txt, results.csv, retrieval-audit.md, k-experiment.txt. All four final CSV rows now contain judgments and observations. Q4 is absent evidence, with both completeness fields false and no coverage ratio. |
| Grounded answer audit | 2 | q1-answer-audit.md, q4-answer-audit.md and final-pass/ transcripts. Q1's original failed the missing-hours check; one revision with unchanged evidence passed. Q4 correctly abstained. Both earlier and final original answers are preserved. |
| Reproducibility and explanation | 2 | README.md, requirements-lock.txt, code explanations, explicit model/package versions, author's name, and 104-word REFLECTION.md covering workflow, observed failure, and a next experiment. The reflection explicitly identifies Codex assistance. |

These materials address the rubric's substantive deliverables; no instructor grade is guaranteed. The individual reflection was drafted by Codex at the user's explicit request, so independent personal authorship is not claimed.

## Sequential execution

1. Confirmed the real model loads on CPU before rerunning Task 1. Versions and confirmation are saved in setup-confirmation.txt.
2. Reran the exact keyword Q1 baseline and verified six chunks and the score calculation. No answer was generated at this stage.
3. Reran the real embedding Q1 inspection and verified shapes, unit vector lengths, six scores, and cosine agreement.
4. Ran all four questions through both retrievers and the k experiment; preserved blank initial judgments in results-template.csv, then completed final judgments in results.csv.
5. Started fresh projectless Q1 and Q4 answer chats after retrieval, containing only the supplied instruction, question and selected passages. Saved all output. Audited each factual claim. Preserved Q1's failure and reran once with the revised instruction and identical passages.

The original code was authored as one project rather than three separate pasted prompt turns. The new execution follows setup and tasks in order; it does not rewrite that history. Human partner role swapping is not claimed because no partner was listed.

## Verification

- Original six paragraph texts were rechecked against the PDF.
- Original numerical retrieval results reproduced in the real CPU model at absolute tolerance 1e-6.
- A full model rerun after filling judgments preserved results.csv exactly and kept results-template.csv blank.
- Final fresh-chat transcripts match their saved answers and contain no answer-side tool calls.
- All required CSV judgment and observation fields are populated.
- Reflection body is 104 words, below the 150-word limit.

## External setup and submission status

The GitHub repository is https://github.com/Jacquelineplj/cedar-rag, private. The grader must have access. No invitation or repository visibility change is made without knowing the intended grader or visibility.

The current registered Codex Project is ps5 and includes the cedar-rag subfolder. The available app tools do not register an additional project; the code, local repository, virtual environment and run commands all work in the current project. A separate cedar-rag project is a remaining app setup step if literal compliance is required.

The course sign-up sheet URL was extracted from the original PDF. It was not accessible through the available web tool. Google Drive was found as an available Sheets integration, but it is not installed/connected; its installation was suggested. No course-sheet row was written and no submission success is claimed.

Course sheet: https://docs.google.com/spreadsheets/d/1ZewIG5udWWpk3Kdrab5yDbsWDV4gnH3liKobIAp7HG4/edit?usp=sharing
