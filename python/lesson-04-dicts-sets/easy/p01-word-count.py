"""
LESSON 04 — Dictionaries & Sets
EASY P01 — Word Count
============================================

CONCEPT:
  A dict maps keys to values — perfect for counting things. The pattern
  counts[word] = counts.get(word, 0) + 1 means "get the current count
  or 0, then add one", which avoids KeyError on first sight of a word.

PROBLEM:
  Write a function `word_count(text: str) -> dict` that returns a dict
  mapping each word (lowercased) to how many times it appears.
  word_count("the cat the dog") -> {"the": 2, "cat": 1, "dog": 1}.

TRY THIS INPUT:
  ```python
  print(word_count("the cat the dog"))
  print(word_count(""))
  ```

EXPECTED OUTPUT:
  ```
  {'the': 2, 'cat': 1, 'dog': 1}
  {}
  ```

CHECK: python3 check.py easy/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
