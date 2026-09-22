"""
LEVEL 16 — Real RAG (Embeddings + Vector DB)
HARD P03 — Hybrid Retrieval (Dense + Keyword Fusion)
========================================

CONCEPT:
  Dense vectors capture meaning but can miss exact rare terms;
  keyword search nails exact terms but ignores meaning. Production
  RAG fuses both:  fused = alpha·dense + (1-alpha)·keyword.

  BM25-ish keyword score per doc:
      sum over query terms t of
          idf(t) * f * (k1 + 1) / (f + k1 * (1 - b + b * dl / avgdl))
      where f = count of t in doc, dl = doc length, avgdl = mean dl,
      idf(t) = log((N - df + 0.5) / (df + 0.5) + 1),
      k1 = 1.5, b = 0.75, N = number of docs, df = docs containing t.

PROBLEM:
  Write `hybrid(store, vec, query, docs, k=3, alpha=0.5)` that:
    1. dense[i] = cosine score of doc i — get it from
       store.query(q_vec, k=len(docs))  (assume store holds `docs`
       in the same order)
    2. kw[i] = BM25-ish keyword score of doc i (lowercased .split())
    3. Max-normalize each score vector, fuse with alpha, re-rank
    4. Return [(idx, fused_score), ...] for top-k, sorted desc —
       same shape as store.query

TRY THIS INPUT:
  ```python
  store = VectorStore(); store.add(DOCS)
  print(hybrid(store, store.vec, "great wall thousand miles", DOCS, k=2))
  ```

EXPECTED OUTPUT:
  ```
  [(3, 0.9...), (x, 0....)]    # the Great Wall doc first
  ```

HINT:
  def _norm(a): m = a.max(); return a / m if m > 0 else a
  fused = alpha * _norm(dense) + (1 - alpha) * _norm(kw)

CHECK: python3 check.py hard/p03
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
# print(hybrid(store, store.vec, "eiffel tower paris", DOCS, k=2))
