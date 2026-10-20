# Retrieval comparison and interpretation

These observations explain the actual local runs and the completed judgments in results.csv.

| Question | Keyword selected | Embedding selected | Required evidence coverage |
| --- | --- | --- | --- |
| Q1 | A1 (3), A2 (2) | A2 (0.68644559), T1 (0.58195281) | Keyword 2/2; embedding 1/2 |
| Q2 | A2 (2), B1 (1) | A2 (0.58519334), T1 (0.43476063) | Both 1/1 |
| Q3 | T1 (2), A2 (1) | T1 (0.74202740), B1 (0.47119522) | Both 1/1 |
| Q4 | A2 (1), B1 (1) | T1 (0.34772122), A2 (0.32082716) | Not applicable: no source states a wavelength |

Q1's embedding result is partial evidence, even though A2 establishes the restriction on operating alone. A1, which supplies the hours and written approval rule, ranks fourth at 0.37424892. The baseline happens to retrieve the complete target set. Its match on "00" illustrates a limitation of literal token overlap, despite this successful result.

For Q3, T1 is a useful paraphrase match: the embedding similarity is 0.74202740 for "refresh my laser qualification" versus "training must be renewed." The keyword baseline also succeeds here because it shares "must" and "laser" with T1; this experiment does not demonstrate an embedding-only success.

Q4 returns top passages because embedding retrieval sorts and selects k regardless of answerability. Positive similarities reflect related text and do not establish that wavelength is specified. Keyword retrieval likewise matches the word "laser" without finding wavelength information.

## k experiment

For Q1, k=1 selects A2; k=2 selects A2,T1; k=3 selects A2,T1,B1. Each has required coverage 1/2. T1 adds a current training condition and 12-month renewal interval. B1 adds booking duration and calendar procedure. Neither adds the missing access-hours rule. Increasing k can add relevant conditions or distractions without completing the evidence target.

## Visible vectors

The actual document matrix shape is (6,384); Q1's question shape is (384,). The first 12 displayed coordinates have maximum 0.1357 (T1 coordinate 12) and minimum -0.1167 (T1 coordinate 5). Neither coordinate alone says what T1 means. Representation is distributed across the vector; retrieval uses all 384 coordinates.

The first 12 Q1/A2 coordinate products sum to 0.01611150; the other 372 sum to 0.67033422. Their full sum is 0.68644571. Matrix multiplication reports 0.68644559: this approximately 1.2e-7 difference is floating-point summation order, within the 1e-6 tolerance, rather than a change in ranking or rounded-input calculation. All vector lengths are approximately 1, and direct cosine agrees with dot products within tolerance.
