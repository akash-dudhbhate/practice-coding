"""
LESSON 17 — Greedy & Intervals
EASY P01 — Merge Overlapping Intervals
============================================

CONCEPT:
  THE interval pattern: sort by start, sweep once, track the "current"
  interval being built. After sorting, an interval that overlaps the
  current one simply EXTENDS it (take max of ends); a disjoint one
  commits the current and starts a new one.

PROBLEM:
  Write a function `merge(intervals: list[list[int]]) -> list[list[int]]`
  that merges all overlapping intervals and returns the minimal set of
  non-overlapping intervals covering the same ranges. Touching intervals
  (end == next start) DO merge: [1,4] + [4,5] → [1,5]. Input may be
  unsorted. Return them sorted by start.

TRY THIS INPUT:
  ```python
  print(merge([[1,3],[2,6],[8,10],[15,18]]))
  print(merge([[1,4],[4,5]]))
  print(merge([[2,6],[1,3]]))
  ```

EXPECTED OUTPUT:
  ```
  [[1, 6], [8, 10], [15, 18]]
  [[1, 5]]
  [[1, 6]]
  ```

CHECK: python3 check.py easy/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
