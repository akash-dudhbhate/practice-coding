"""
LESSON 03 — Lists & Tuples
MEDIUM P01 — Remove Duplicates
============================================

CONCEPT:
  A set gives O(1) "have I seen this before?" lookups. Tracking seen
  items while building a result list removes duplicates while keeping
  the original order — unlike set(items), which scrambles order.

PROBLEM:
  Write a function `remove_duplicates(items: list) -> list` that
  returns a new list with duplicates removed, preserving the original
  order of first appearance.

TRY THIS INPUT:
  ```python
  print(remove_duplicates([1, 2, 2, 3, 3, 3]))
  print(remove_duplicates(["a", "b", "a"]))
  print(remove_duplicates([]))
  ```

EXPECTED OUTPUT:
  ```
  [1, 2, 3]
  ['a', 'b']
  []
  ```

CHECK: python3 check.py medium/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
