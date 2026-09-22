"""
LEVEL 12 — RAG Systems
EASY P01 — Text Similarity (Embeddings)
========================================

CONCEPT:
  Words → numbers (embeddings) → then math can compare meaning.
  TF-IDF is a simple way: count word frequencies, weight by rarity.
  Cosine similarity between two text vectors: -1 to 1.

  "machine learning" vs "deep learning" → high similarity (shared words)
  "machine learning" vs "cooking recipe" → low similarity

PROBLEM:
  Write `similarity(text1, text2)` that:
    1. TfidfVectorizer on both texts
    2. Cosine similarity between the vectors
    3. Returns the score

TRY THIS INPUT:
  ```python
  s = similarity("machine learning is great", "deep learning uses neural nets")
  print(f"{s:.4f}")
  s2 = similarity("machine learning is great", "cooking recipes and food")
  print(f"{s2:.4f}")
  ```

EXPECTED OUTPUT:
  ```
  0.1274    (similar topics — shared "learning")
  0.0000    (different topics — no shared words)
  ```

HINT:
  from sklearn.feature_extraction.text import TfidfVectorizer
  from sklearn.metrics.pairwise import cosine_similarity

CHECK: python3 check.py easy/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# s = similarity("machine learning is great", "deep learning uses neural nets")
# print(s)
