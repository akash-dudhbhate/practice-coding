"""
LEVEL 16 — Real RAG (Embeddings + Vector DB)
EASY P02 — Cosine Similarity vs All Docs
========================================

CONCEPT:
  With normalized vectors, cosine similarity = dot product.
  One matrix-vector product scores a query against EVERY doc at
  once — this is the inner loop of every vector DB.

PROBLEM:
  Write `cosine_all(query_vec, doc_matrix)` that:
    1. Accepts a query vector (1-D array, one-row 2-D, or sparse row)
    2. Accepts a doc matrix (one row per doc; dense or sparse)
    3. Returns a 1-D numpy array of cosine similarities,
       length == number of doc rows
    4. Normalizes BOTH sides — do NOT assume inputs are unit vectors

TRY THIS INPUT:
  ```python
  import numpy as np
  D = np.array([[1., 0.], [0., 1.], [1., 1.]])
  q = np.array([1., 0.])
  print(cosine_all(q, D))
  ```

EXPECTED OUTPUT:
  ```
  [1.     0.     0.7071]   # identical → 1, orthogonal → 0, diagonal → ~0.71
  ```

HINT:
  q / ||q||, each row D[i] / ||D[i]||, then D_norm @ q_norm.
  Handle sparse inputs with `.toarray()` if the arg has that attr.

CHECK: python3 check.py easy/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# import numpy as np
# print(cosine_all(np.array([1., 0.]), np.array([[1., 0.], [0., 1.]])))
