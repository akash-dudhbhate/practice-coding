"""
LEVEL 00A — What is AI?
MEDIUM P03 — Similarity (How "Close" Two Texts Are)
====================================================

CONCEPT:
  To compare two pieces of text, count shared words.
  similarity = shared_words / total_unique_words

  "machine learning models" and "machine learning code" share
  2 of 4 unique words → 0.5 similarity. This is called Jaccard
  similarity — the simplest version. Cosine similarity (level-16)
  uses the same idea on vectors instead of word sets.

PROBLEM:
  Write `similarity(text1, text2)`:
    1. Split both into word sets (lowercase)
    2. shared = words in BOTH texts
    3. total = words in EITHER text
    4. return shared / total

TRY THIS INPUT:
  ```python
  print(similarity("machine learning models", "machine learning code"))
  print(similarity("python data science", "cooking pasta recipe"))
  ```

EXPECTED OUTPUT:
  ```
  0.5
  0.0
  ```

WHY THIS MATTERS:
  This IS how search works — find docs most similar to your query.
  RAG (level-12/16) = "find most similar doc, then answer with it."

CHECK: python3 check.py medium/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: implement similarity(text1, text2)


def similarity(text1, text2):
    """Jaccard similarity: shared words / total unique words."""
    pass


# === TEST ===
# print(similarity("machine learning models", "machine learning code"))
# print(similarity("python data science", "cooking pasta recipe"))
