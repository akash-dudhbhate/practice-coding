"""
LEVEL 16 — Real RAG (Embeddings + Vector DB)
MEDIUM P01 — VectorStore Class
========================================

CONCEPT:
  A vector DB has two operations: add(texts) and query(vector, k).
  FAISS, Chroma, Pinecone — same shape. We build a mini one with
  numpy: store normalized vectors, query = matmul + argsort.

  The embedding model is fixed at ingest time: fit the vectorizer on
  the FIRST .add(), then only .transform() on later adds (re-fitting
  would change the vector space and invalidate stored vectors).

PROBLEM:
  Write a `VectorStore` class:
    __init__()           → self.vec (TfidfVectorizer),
                           self.texts (list of raw strings),
                           self.matrix (None until first add)
    .add(texts)          → fit_transform on FIRST add, transform on
                           later adds; L2-normalize rows; append to
                           self.matrix (dense np.array) and self.texts;
                           return number of texts added (int)
    .query(q_vec, k=3)   → q_vec is an EMBEDDED query (sparse row or
                           dense array); cosine-score it against all
                           stored vectors; return a list of
                           [(idx, score), ...] for the top-k,
                           sorted by score descending

  IMPORTANT: check.py uses store.vec to embed queries and reads
  store.texts — keep those exact attribute names.

TRY THIS INPUT:
  ```python
  store = VectorStore()
  store.add(["machine learning models learn", "pasta needs boiling water",
             "neural networks mimic neurons"])
  q = store.vec.transform(["neural networks brain neurons"])
  print(store.query(q, k=2))
  ```

EXPECTED OUTPUT:
  ```
  [(2, 0.6...), (0, 0.0...)]    # (doc index, cosine score), sorted desc
  ```

HINT:
  normalize q inside query(), then scores = self.matrix @ q_vec
  → np.argsort(-scores)[:k]

CHECK: python3 check.py medium/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# store = VectorStore()
# store.add(["machine learning models learn", "pasta needs boiling water",
#            "neural networks mimic neurons"])
# print(store.query(store.vec.transform(["neural nets"]), k=2))
