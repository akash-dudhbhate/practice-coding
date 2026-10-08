"""
LESSON 17 — Greedy & Intervals
MEDIUM P01 — Erase Minimum Overlapping Intervals
============================================

CONCEPT:
  Activity selection in disguise: "remove the fewest" = "keep the most
  non-overlapping". The greedy that works is sort by END — always keep
  the interval that finishes earliest; it frees the most room for what
  follows. Sorting by start is THE bug here (a long early interval
  blocks everything).

PROBLEM:
  Write a function `erase_overlap_intervals(intervals: list[list[int]]) -> int`
  that returns the MINIMUM number of intervals to remove so the rest are
  pairwise non-overlapping. Touching endpoints ([1,2] then [2,3]) do NOT
  overlap — a meeting can start exactly when another ends.

TRY THIS INPUT:
  ```python
  print(erase_overlap_intervals([[1,2],[2,3],[3,4],[1,3]]))
  print(erase_overlap_intervals([[1,2],[1,2],[1,2]]))
  print(erase_overlap_intervals([[1,2],[2,3]]))
  print(erase_overlap_intervals([[0,2],[1,3],[2,4],[3,5],[4,6]]))
  ```

EXPECTED OUTPUT:
  ```
  1
  2
  0
  2
  ```

CHECK: python3 check.py medium/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
