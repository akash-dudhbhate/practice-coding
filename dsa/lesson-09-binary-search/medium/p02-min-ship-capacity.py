"""
LESSON 09 — Binary Search
MEDIUM P02 — Minimum Capacity to Ship Packages in D Days
============================================

CONCEPT:
  "Search the answer": the ship's capacity C must be at least
  max(weights) (or the heaviest package never fits) and at most
  sum(weights) (one giant trip). For any C you can SIMULATE the
  loading in one pass and count days — bigger C → fewer days.
  Monotone → binary search on C.

PROBLEM:
  Write `min_ship_capacity(weights: list, days: int) -> int`:
  the smallest conveyor capacity that ships every package (in the
  given order, no reordering) within `days` days.

TRY THIS INPUT:
  ```python
  print(min_ship_capacity([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))
  print(min_ship_capacity([3, 2, 2, 4, 1, 4], 3))
  print(min_ship_capacity([1, 2, 3, 1, 1], 4))
  ```

EXPECTED OUTPUT:
  ```
  15
  6
  3
  ```

CHECK: python3 check.py medium/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
