"""
LESSON 12 — Heaps
MEDIUM P01 — K Closest Points
============================================

CONCEPT:
  Top-K on a computed key (distance to origin). Compare distance^2 —
  sqrt is monotone, skipping it saves work and keeps everything int.
  For "k smallest by key" the heap-of-size-k trick flips: keep a
  MAX-heap (negated distances) so the FARTHEST of the kept k sits
  on top, ready to be evicted by anything closer.

PROBLEM:
  Write `k_closest(points, k) -> list[list[int]]` — the k points
  closest to (0,0). To keep the answer deterministic, both
  SELECTION and the returned list follow (distance^2, x, y)
  ascending — a distance tie prefers smaller x, then smaller y.
  Assume 1 <= k <= len(points).

TRY THIS INPUT:
  ```python
  print(k_closest([[1, 3], [-2, 2]], 1))
  print(k_closest([[3, 3], [5, -1], [-2, 4]], 2))
  print(k_closest([[0, 0], [1, 0], [0, 1]], 2))
  ```

EXPECTED OUTPUT:
  ```
  [[-2, 2]]
  [[3, 3], [-2, 4]]
  [[0, 0], [0, 1]]
  ```

CHECK: python3 check.py medium/p01
"""

import heapq

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
