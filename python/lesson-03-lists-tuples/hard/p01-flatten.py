"""
LESSON 03 — Lists & Tuples
HARD P01 — Flatten
============================================

CONCEPT:
  isinstance(item, list) tells you whether an element is itself a list.
  .extend() adds all of a sub-list's elements at once, while .append()
  adds a single item — picking the right one is the whole trick.

PROBLEM:
  Write a function `flatten(nested: list) -> list` that takes a list
  which may contain sub-lists (one level deep) and returns a single
  flat list. [[1,2],[3],[4,5]] -> [1,2,3,4,5].

TRY THIS INPUT:
  ```python
  print(flatten([[1, 2], [3], [4, 5]]))
  print(flatten([1, [2], 3]))
  print(flatten([]))
  ```

EXPECTED OUTPUT:
  ```
  [1, 2, 3, 4, 5]
  [1, 2, 3]
  []
  ```

CHECK: python3 check.py hard/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
