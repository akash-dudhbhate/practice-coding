"""
LEVEL 16 — Real RAG (Embeddings + Vector DB)
HARD P02 — Evaluate Retrieval (Hit Rate)
========================================

CONCEPT:
  How good is your retriever? The standard quick metric is hit-rate:
  for each test query, does ANY expected keyword show up in the
  top-k retrieved chunks? hits / n_queries.

  This is the RAG version of accuracy — if retrieval fails, the
  generator never had a chance.

PROBLEM:
  Write `eval_rag(queries, expected_keywords, store, vec, k=3)` that:
    1. For each (query, keywords) pair, retrieves top-k chunk texts
    2. Counts a HIT if ANY keyword appears (case-insensitive) in the
       concatenated retrieved texts
    3. Returns the hit rate as a float in [0, 1]
       (return 0.0 for an empty query list)

TRY THIS INPUT:
  ```python
  store = VectorStore(); store.add(DOCS)
  queries  = ["language for data science", "tower in paris"]
  expected = [["python"], ["eiffel"]]
  print(eval_rag(queries, expected, store, store.vec))
  ```

EXPECTED OUTPUT:
  ```
  1.0
  ```

HINT:
  " ".join(retrieved_texts).lower() then `any(kw.lower() in joined ...)`

CHECK: python3 check.py hard/p02
"""

DOCS = [
    "The Eiffel Tower is a wrought-iron lattice tower located in Paris, France.",
    "Python is a popular programming language widely used for data science.",
    "Machine learning models learn patterns from large training datasets.",
    "The Great Wall of China stretches over thirteen thousand miles.",
    "Neural networks are computing systems inspired by biological neurons.",
    "Cooking pasta requires boiling salted water and about ten minutes.",
]

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# store = VectorStore(); store.add(DOCS)
# print(eval_rag(["tower in paris"], [["eiffel"]], store, store.vec))
