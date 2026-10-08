"""
LESSON 12 — Heaps
MEDIUM P02 — Merge K Sorted Lists
============================================

CONCEPT:
  k sorted lists = k sorted streams. A heap of size k holds the
  FRONTIER — the current head of each list. Pop the smallest
  frontier element, output it, push that list's NEXT element.
  Entries are (value, list_idx, elem_idx): the indices make every
  tuple unique (no payload comparisons) and tell you where to fetch
  the successor. O(N log k) total.

PROBLEM:
  Write `merge_k_sorted(lists) -> list[int]` — merge k sorted lists
  of ints into one sorted list. Empty lists and empty input are
  legal.

TRY THIS INPUT:
  ```python
  print(merge_k_sorted([[1, 4, 5], [1, 3, 4], [2, 6]]))
  print(merge_k_sorted([]))
  print(merge_k_sorted([[], [], [1]]))
  print(merge_k_sorted([[-2, -1, 0], [1], [0, 2]]))
  ```

EXPECTED OUTPUT:
  ```
  [1, 1, 2, 3, 4, 4, 5, 6]
  []
  [1]
  [-2, -1, 0, 0, 1, 2]
  ```

CHECK: python3 check.py medium/p02
"""

import heapq

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
