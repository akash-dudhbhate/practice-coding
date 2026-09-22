"""
LEVEL 16 — Real RAG (Embeddings + Vector DB)
MEDIUM P03 — Retrieve
========================================

CONCEPT:
  Retrieval is the online half: embed the query with the SAME
  vectorizer that embedded the docs (a different vector space would
  be meaningless), ask the store for top-k, map indices back to
  raw texts.

PROBLEM:
  Write `retrieve(store, query, vec, k=3)` that:
    1. Embeds `query` with vec.transform([query])
       (vec = the fitted vectorizer — e.g. store.vec)
    2. Calls store.query(q_vec, k) → [(idx, score), ...]
    3. Returns a list of the top-k chunk TEXTS (strings), best first

TRY THIS INPUT:
  ```python
  store = VectorStore(); store.add(DOCS)
  r = retrieve(store, "which programming language for data science?",
               store.vec, k=2)
  print(r)
  ```

EXPECTED OUTPUT:
  ```
  ['Python is a popular programming language widely used for data science.',
   '<2nd best doc>']
  ```

HINT:
  hits = store.query(vec.transform([query]), k)
  return [store.texts[i] for i, _ in hits]

CHECK: python3 check.py medium/p03
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
# print(retrieve(store, "how long to cook pasta?", store.vec, k=1))
