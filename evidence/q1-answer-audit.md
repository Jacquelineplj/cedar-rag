# Q1 answer audit - Codex-generated; student verification required

## Method

Original answer: fresh projectless chat `01a15a34-c6fd-7d22-bba5-422bb659c763` (Cedar RAG Q1 answer). Revised answer: fresh projectless chat `01a15a35-3d08-7203-855a-1f5d0bba4cbe` (Cedar RAG Q1 revised answer). Only prompt, question, A2 and T1 were supplied. No project was attached. The recorded conversations show no file reads, browsing, or tool use by the answering chats. Original and revised answers and conversation records are preserved alongside this file. The revised prompt is preserved in the revised conversation JSON.

## Original result: incomplete

- Two trained people are required during operation: directly supported by A2. The conclusion against solo operation at 19:00 follows from "whenever" and does not need an access-hours assumption.
- Training must be renewed every 12 months and a current record is required: directly supported by T1.
- This student's training currency is not established: correctly identifies missing student-specific evidence. The final list awkwardly phrases "This student's training is current" as an unsupported claim even though the prose did not assert it.
- Access hours: the answer did not say whether the selected evidence establishes access at 19:00. This fails the requested missing-evidence check. The retrieved set lacked A1; the answer should acknowledge that gap rather than leave the time condition unaddressed.

## One revision and rerun

Added one instruction: address operation and access hours separately, explicitly check whether 19:00 is within permitted access hours, and distinguish missing information from asserted unsupported facts. Used exactly the same A2 and T1 passages in a new fresh chat; no A1 was added.

## Revised result: passes the selected-evidence audit

| Claim or statement | Support or missing evidence |
| --- | --- |
| Solo operation violates the two-trained-person requirement | A2: two trained people whenever operating |
| The rule also applies during general access hours | A2: explicitly includes those hours |
| A current record is required; renewal every 12 months | T1: both requirements are stated |
| The student's current record is not established | Missing student-specific record; no current status is asserted |
| Whether 19:00 falls within permitted hours is not established | Neither supplied passage contains an access-hours schedule |

The revision helped by explicitly acknowledging the missing access-hours evidence. It did not repair retrieval: Q1's selected set still has coverage 1/2, because A1 is absent. No unsupported access schedule or invented citation appears in the revised answer.
