"""
LESSON 04 — Two Pointers
HARD P03 — 4-Sum (fixed two + two pointers)
============================================

CONCEPT:
  Extend 3-sum one level: sort, fix nums[i] AND nums[j], then run the
  sorted two-pointer scan on the rest of the array for
  target - nums[i] - nums[j]. Skip duplicate i and j values and
  duplicate pairs. O(n^3) — still far better than O(n^4) brute force.

PROBLEM:
  Write `four_sum(nums: list, target: int) -> list` returning ALL
  unique quadruplets [a, b, c, d] (sorted ascending) whose sum is
  target. The result list itself sorted; no duplicate quadruplets.

TRY THIS INPUT:
  ```python
  print(four_sum([1, 0, -1, 0, -2, 2], 0))
  print(four_sum([2, 2, 2, 2, 2], 8))
  print(four_sum([], 0))
  ```

EXPECTED OUTPUT:
  ```
  [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
  [[2, 2, 2, 2]]
  []
  ```

CHECK: python3 check.py hard/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
