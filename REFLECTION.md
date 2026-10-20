# Individual reflection

Author: Jacqueline Pan

The main lesson from this task is that a high similarity score does not mean the evidence is complete. For Q1, embedding retrieval found the operating and training rules but missed the access hours rule. Increasing k from 2 to 3 did not solve this problem.

The workflow starts by keeping each paragraph as a chunk with its ID and filename. The question and passages are converted into vectors. Similarity scores select the passages, and a separate conversation uses them to write an answer with citations. Each claim still needs to be checked against its source.

Next, I would test combining keyword and embedding results to see whether this improves evidence coverage without adding unsupported claims.
