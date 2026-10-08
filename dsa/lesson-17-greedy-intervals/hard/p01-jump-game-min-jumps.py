"""
LESSON 17 — Greedy & Intervals
HARD P01 — Jump Game II: Minimum Jumps
============================================

CONCEPT:
  Reach tracking with a second variable. `farthest` = the best reach
  achievable from anywhere inside the current jump; `boundary` = where
  the current jump's range ends. When i reaches the boundary you MUST
  spend another jump — boundary = farthest. Counting every reach
  improvement overcounts; only crossings of the boundary are jumps.

PROBLEM:
  Write a function `jump(nums: list[int]) -> int` returning the MINIMUM
  number of jumps to reach the last index from index 0. nums[i] is the
  max jump length from i. The end is always reachable; a single-element
  array needs 0 jumps.

TRY THIS INPUT:
  ```python
  print(jump([2,3,1,1,4]))
  print(jump([2,3,0,1,4]))
  print(jump([1,1,1,1]))
  print(jump([0]))
  print(jump([1,2,3]))
  ```

EXPECTED OUTPUT:
  ```
  2
  2
  3
  0
  2
  ```

CHECK: python3 check.py hard/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
