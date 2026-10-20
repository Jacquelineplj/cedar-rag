# Keyword audit (Codex-generated; student should verify)

Exactly six chunks are loaded, with the source ID and filename stored separately. Search uses only paragraph text. The original six source paragraphs are preserved in docs/.

Manual Q1 score check: the query's distinct remaining tokens are {trained, graduate, student, operate, laser, alone, 19, 00}. A1 shares {00, graduate, trained}, so its score is 3. A2 shares {laser, trained}, so its score is 2. Repeated occurrences of "laser" in A2 do not increase its score. "student" and "students" do not match, nor do "operate" and "operating". No stemming is applied.

Q1 selects A1 and A2, so the keyword baseline contains both required passages (coverage 2/2). These are retrieval observations; no answer was generated during Task 1.
