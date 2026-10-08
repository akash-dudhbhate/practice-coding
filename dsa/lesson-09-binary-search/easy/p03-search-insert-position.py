"""
LESSON 09 — Binary Search
EASY P03 — Search Insert Position
============================================

CONCEPT:
  Lower bound returns the first index where nums[i] >= target —
  which is exactly where target would be inserted to keep the
  array sorted. No "found / not found" branch: the loop always
  returns a position in [0, len(nums)].

PROBLEM:
  Write a function `search_insert(nums: list, target: int) -> int`
  that returns the index where `target` is found in sorted `nums`,
  or the index where it WOULD be inserted to keep the order.

TRY THIS INPUT:
  ```python
  print(search_insert([1, 3, 5, 6], 5))
  print(search_insert([1, 3, 5, 6], 2))
  print(search_insert([1, 3, 5, 6], 7))
  print(search_insert([1, 3, 5, 6], 0))
  ```

EXPECTED OUTPUT:
  ```
  2
  1
  4
  0
  ```

CHECK: python3 check.py easy/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
