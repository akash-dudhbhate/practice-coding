"""
LESSON 17 — Greedy & Intervals
MEDIUM P02 — Insert Interval
============================================

CONCEPT:
  Merge's cousin: the input is ALREADY sorted and disjoint, plus one new
  interval to slot in. Three clean phases: (1) output every interval
  ending before the new one starts, (2) absorb every interval it
  overlaps — growing it with min/max — (3) output the rest. No need to
  merge the whole list again.

PROBLEM:
  Write a function
  `insert(intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]`
  where `intervals` is sorted by start and non-overlapping. Insert
  `newInterval`, merge it with anything it touches (touching counts as
  overlap), and return the sorted non-overlapping result.

TRY THIS INPUT:
  ```python
  print(insert([[1,3],[6,9]], [2,5]))
  print(insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))
  print(insert([], [5,7]))
  print(insert([[5,8]], [1,3]))
  ```

EXPECTED OUTPUT:
  ```
  [[1, 5], [6, 9]]
  [[1, 2], [3, 10], [12, 16]]
  [[5, 7]]
  [[1, 3], [5, 8]]
  ```

CHECK: python3 check.py medium/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
