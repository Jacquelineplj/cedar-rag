# Individual reflection

Author: Jacqueline Pan. Prepared with Codex assistance at the author's request.

A question becomes a cited answer through document preparation, retrieval, and generation. Each paragraph keeps its ID and filename, while its text is encoded into a normalized vector. Similarity ranks candidate passages; a separate answer conversation uses only the selected evidence and cites supporting IDs. The Q1 result shows a limitation: embeddings retrieved the operating and training rules but missed the access-hours rule. Increasing k from two to three still did not retrieve that missing rule. Retrieval similarity therefore cannot guarantee complete evidence. The next experiment would combine keyword and embedding candidates and measure whether Q1's evidence coverage improves without adding unsupported answer claims.
