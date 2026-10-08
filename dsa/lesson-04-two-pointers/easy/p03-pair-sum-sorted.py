"""
LESSON 04 — Two Pointers
EASY P03 — Pair Sum on a Sorted Array
============================================

CONCEPT:
  Sorted input gives a direction to blame: if nums[L] + nums[R] is
  too small, nums[L] can never pair with anything remaining -> L += 1.
  Too big -> R -= 1. Each step discards one candidate for good: O(n)
  time, O(1) space (vs hashing's O(n) space).

PROBLEM:
  Write a function `pair_sum_sorted(nums: list, target: int) -> list`.
  `nums` is sorted ascending. Return `[i, j]` with i < j such that
  nums[i] + nums[j] == target, or [] if none. Assume at most one
  answer.

TRY THIS INPUT:
  ```python
  print(pair_sum_sorted([2, 7, 11, 15], 9))
  print(pair_sum_sorted([1, 2, 4, 7, 11], 9))
  print(pair_sum_sorted([1, 3, 5], 10))
  ```

EXPECTED OUTPUT:
  ```
  [0, 1]
  [1, 3]
  []
  ```

CHECK: python3 check.py easy/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
