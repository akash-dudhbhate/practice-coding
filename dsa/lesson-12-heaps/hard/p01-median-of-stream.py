"""
LESSON 12 — Heaps
HARD P01 — Median of a Stream
============================================

CONCEPT:
  The median lives at the BOUNDARY between the lower and upper
  halves — you never need the halves sorted, only their extremes.
  Keep TWO heaps: `lo` = max-heap of the lower half (negated) and
  `hi` = min-heap of the upper half. Invariants: every element of
  lo <= every element of hi, and sizes differ by at most 1. Median:
  -lo[0] if lo is bigger, else (-lo[0] + hi[0]) / 2.

PROBLEM:
  Write `running_medians(nums) -> list[float]` — out[i] is the
  median of nums[:i+1]. Empty input -> [].

TRY THIS INPUT:
  ```python
  print(running_medians([1, 2, 3]))
  print(running_medians([5, 1, 4, 2, 3]))
  print(running_medians([]))
  ```

EXPECTED OUTPUT:
  ```
  [1.0, 1.5, 2.0]
  [5.0, 3.0, 4.0, 3.0, 3.0]
  []
  ```

CHECK: python3 check.py hard/p01
"""

import heapq

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
