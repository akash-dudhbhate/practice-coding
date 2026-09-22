"""
LESSON 04 — Dictionaries & Sets
HARD P03 — Char Frequency
============================================

CONCEPT:
  Frequency counting is the classic dict pattern: freq[c] =
  freq.get(c, 0) + 1. To sort by count descending, sorted() with a key
  like lambda x: (-x[1], x[0]) puts highest counts first and breaks
  ties alphabetically.

PROBLEM:
  Write a function `char_frequency(s: str) -> list` that counts
  non-space characters and returns a list of (char, count) tuples
  sorted by frequency descending (ties: alphabetical).
  char_frequency("aab bc") -> [('a',2),('b',2),('c',1)].

TRY THIS INPUT:
  ```python
  print(char_frequency("aab bc"))
  print(char_frequency(""))
  ```

EXPECTED OUTPUT:
  ```
  [('a', 2), ('b', 2), ('c', 1)]
  []
  ```

CHECK: python3 check.py hard/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
