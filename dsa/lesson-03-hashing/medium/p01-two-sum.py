"""
LESSON 03 — Hashing (Dict & Set Patterns)
MEDIUM P01 — Two Sum (Complement Lookup)
============================================

CONCEPT:
  The complement pattern: store value -> index as you walk. For each
  x, the partner you need is `target - x`. If you've already seen it,
  done — O(n) instead of checking every pair in O(n^2). CHECK first,
  THEN store, so an element never pairs with itself.

PROBLEM:
  Write a function `two_sum(nums: list, target: int) -> list` that
  returns `[i, j]` (i < j) such that nums[i] + nums[j] == target.
  Return [] if no such pair exists. Assume at most one answer.

TRY THIS INPUT:
  ```python
  print(two_sum([2, 7, 11, 15], 9))
  print(two_sum([3, 2, 4], 6))
  print(two_sum([3, 3], 6))
  print(two_sum([1, 5, 9], 20))
  ```

EXPECTED OUTPUT:
  ```
  [0, 1]
  [1, 2]
  [0, 1]
  []
  ```

CHECK: python3 check.py medium/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
