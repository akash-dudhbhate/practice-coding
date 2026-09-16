"""
LEVEL 16 — Real RAG (Embeddings + Vector DB)
EASY P01 — Embed a Corpus
========================================

CONCEPT:
  "Real" RAG starts with an embedding model: text → vector.
  Production uses sentence-transformers / OpenAI embeddings; here
  TfidfVectorizer plays that role — the pipeline shape is identical.

  Embeddings are stored L2-normalized (each row = a unit vector) so
  that a plain dot product IS a cosine similarity. This is exactly
  what a vector DB stores.

PROBLEM:
  Write `embed(texts)` that:
    1. Fits TfidfVectorizer on `texts` (the corpus)
    2. Returns a DENSE numpy array — one row per text
    3. Every row L2-normalized: np.linalg.norm(row) == 1.0

  (A real pipeline also keeps the fitted vectorizer to embed future
   queries — our VectorStore in medium/p01 owns it, so here you only
   return the matrix.)

TRY THIS INPUT:
  ```python
  import numpy as np
  docs = ["machine learning models learn", "pasta needs boiling water",
          "neural networks mimic neurons"]
  M = embed(docs)
  print(M.shape)
  print(np.linalg.norm(M, axis=1))
  ```

EXPECTED OUTPUT:
  ```
  (3, N)              # N = vocab size
  [1. 1. 1.]          # every row is a unit vector
  ```

HINT:
  X = vec.fit_transform(texts).toarray()
  X / np.linalg.norm(X, axis=1, keepdims=True)
  (guard against a zero norm — empty row would divide by 0)

CHECK: python3 check.py easy/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# import numpy as np
# M = embed(["machine learning models learn", "pasta needs boiling water"])
# print(M.shape, np.linalg.norm(M, axis=1))
