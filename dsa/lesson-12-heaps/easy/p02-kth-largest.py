"""
LESSON 12 — Heaps
EASY P02 — Kth Largest
============================================

CONCEPT:
  The top-K pattern: keep a MIN-heap of size k holding "the best k
  seen so far." Its root h[0] is the WORST of the kept k — the bar
  every newcomer must beat. If x > h[0], heapreplace evicts the
  worst and keeps the new one. O(n log k) and O(k) space instead of
  sorting's O(n log n). Duplicates count (kth largest of
  [7,7,7], k=2 is 7).

PROBLEM:
  Write `kth_largest(nums, k) -> int`. You may assume
  1 <= k <= len(nums).

TRY THIS INPUT:
  ```python
  print(kth_largest([3, 2, 1, 5, 6, 4], 2))
  print(kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
  print(kth_largest([1], 1))
  print(kth_largest([7, 7, 7], 2))
  ```

EXPECTED OUTPUT:
  ```
  5
  4
  1
  7
  ```

CHECK: python3 check.py easy/p02
"""

import heapq

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
