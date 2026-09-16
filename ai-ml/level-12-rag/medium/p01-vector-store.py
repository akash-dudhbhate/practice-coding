"""
LEVEL 12 — RAG Systems
MEDIUM P01 — Vector Store (In-Memory)
========================================

CONCEPT:
  A vector store = a "database" for embeddings. You store doc +
  its vector, then search by similarity. No external service
  needed — just numpy.

  Steps: embed all docs → store → query → rank by similarity.

PROBLEM:
  Write `vector_store(docs, query, top_k)` that:
    1. TfidfVectorizer on all docs
    2. Store doc + vector pairs
    3. Query: embed query, cosine-similarity rank, return top_k
       as [(doc_text, score), ...]

TRY THIS INPUT:
  ```python
  docs = ["ML is great", "Python is a language", "Deep learning is fun",
          "NLP handles text", "Cooking is an art"]
  r = vector_store(docs, "Tell me about AI", 3)
  for doc, score in r:
      print(f"({score:.4f}) {doc}")
  ```

EXPECTED OUTPUT:
  ```
  (0.0xxx) [doc most similar to query]
  (0.0xxx) [next most similar]
  (0.0xxx) [third]
  ```

HINT:
  Store vectors in a list; query → transform → cosine_similarity
  → argsort descending → top_k

CHECK: python3 check.py medium/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# docs = ["ML is great", "Python is a language", "NLP handles text"]
# r = vector_store(docs, "AI and machine learning", 2)
# print(r)
