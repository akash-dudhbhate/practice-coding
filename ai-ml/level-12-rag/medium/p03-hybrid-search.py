"""
LEVEL 12 — RAG Systems
MEDIUM P03 — Hybrid Search (Keyword + Semantic)
========================================

CONCEPT:
  Pure keyword search misses synonyms. Pure semantic search
  misses exact matches. Hybrid = combine both:

    final_score = 0.5 × keyword_score + 0.5 × semantic_score

  keyword_score = fraction of query words found in doc
  semantic_score = cosine similarity of TF-IDF vectors

PROBLEM:
  Write `hybrid_search(query, docs, top_k)` that:
    1. Computes both keyword and TF-IDF similarity scores
    2. Combines: 0.5×keyword + 0.5×semantic
    3. Returns top_k [(doc, combined_score), ...]

TRY THIS INPUT:
  ```python
  docs = ["Python is a programming language", "ML models learn patterns",
          "Cooking is an art", "AI and machine learning"]
  r = hybrid_search("machine learning", docs, 2)
  for d, s in r:
      print(f"({s:.4f}) {d}")
  ```

EXPECTED OUTPUT:
  ```
  (0.xxxx) AI and machine learning   ← exact "machine learning" match
  (0.xxxx) ML models learn patterns  ← semantic similarity
  ```

HINT:
  keyword_score = len(set(query_words) & set(doc_words)) / len(query_words)
  semantic_score = cosine_similarity(query_vec, doc_vecs)

CHECK: python3 check.py medium/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# docs = ["Python is a language", "ML models learn", "Cooking is art"]
# r = hybrid_search("machine learning", docs, 2)
# print(r)
