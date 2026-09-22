"""
LESSON 04 — Dictionaries & Sets
EASY P03 — Unique Items
============================================

CONCEPT:
  Sets store unique values and answer "have I seen this?" in constant
  time. Tracking a `seen` set while appending to a result list keeps
  the first-seen order — something set(items) alone can't do.

PROBLEM:
  Write a function `unique_items(items: list) -> list` that returns a
  list of unique items preserving first-seen order, using a set for
  tracking. [1,2,2,3,3,3] -> [1,2,3].

TRY THIS INPUT:
  ```python
  print(unique_items([1, 2, 2, 3, 3, 3]))
  print(unique_items([]))
  ```

EXPECTED OUTPUT:
  ```
  [1, 2, 3]
  []
  ```

CHECK: python3 check.py easy/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
