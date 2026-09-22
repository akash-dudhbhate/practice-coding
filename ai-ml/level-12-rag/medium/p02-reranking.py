"""
LEVEL 12 — RAG Systems
MEDIUM P02 — Reranking with Cross-Encoder
========================================

CONCEPT:
  First retrieval is fast but imprecise. A reranker takes the
  top results and re-scores them more carefully.

  Simple rerank: boost scores for docs with more query-word overlap.

PROBLEM:
  Write `rerank(query, retrieved_docs)` that:
    1. retrieved_docs = list of (doc, similarity_score)
    2. Re-score: score + 0.1 × (count of query words in doc)
    3. Sort by new score, return reranked list

TRY THIS INPUT:
  ```python
  docs = [("Old doc about AI", 0.6), ("Recent ML advances", 0.5),
          ("Ancient history", 0.4)]
  r = rerank("machine learning advances", docs)
  for d, s in r:
      print(f"({s:.2f}) {d}")
  ```

EXPECTED OUTPUT:
  ```
  (0.60) Recent ML advances   ← boosted by matching "advances"
  (0.60) Old doc about AI     ← tied with Recent, stable sort
  (0.40) Ancient history      ← no query words
  ```

HINT:
  query_words = set(query.lower().split())
  bonus = 0.1 * len(set(doc.lower().split()) & query_words)

CHECK: python3 check.py medium/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# r = rerank("machine learning", [("ML doc", 0.5), ("Other doc", 0.4)])
# print(r)
