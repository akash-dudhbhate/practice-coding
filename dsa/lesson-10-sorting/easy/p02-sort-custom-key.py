"""
LESSON 10 — Sorting
EASY P02 — Sort With a Custom Key
============================================

CONCEPT:
  Python's sorted() takes key= — a function extracting the value
  to sort by. Return a TUPLE from the key and Python compares
  element-wise: primary criterion first, ties broken by the next.
  This is the real-world sort skill — nobody hand-rolls sorts for
  ordering data.

PROBLEM:
  Write `sort_by_length(words: list) -> list` returning a NEW list
  of the strings sorted by length ascending; strings of equal
  length must be ordered alphabetically.

TRY THIS INPUT:
  ```python
  print(sort_by_length(["banana", "kiwi", "apple", "fig", "cherry"]))
  print(sort_by_length(["bb", "aa", "c"]))
  print(sort_by_length([]))
  ```

EXPECTED OUTPUT:
  ```
  ['fig', 'kiwi', 'apple', 'banana', 'cherry']
  ['c', 'aa', 'bb']
  []
  ```

CHECK: python3 check.py easy/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
