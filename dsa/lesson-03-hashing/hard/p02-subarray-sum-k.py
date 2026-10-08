"""
LESSON 03 — Hashing (Dict & Set Patterns)
HARD P02 — Count Subarrays Summing to K (prefix-sum hash)
============================================

CONCEPT:
  Keep a running prefix sum and a frequency map of prefix values seen.
  A subarray ending here sums to k exactly when a past prefix equals
  `prefix - k`. Seed the map with {0: 1} so subarrays starting at
  index 0 count. Query BEFORE recording the new prefix. O(n) total
  vs O(n^2) brute force.

PROBLEM:
  Write a function `subarray_sum(nums: list, k: int) -> int` that
  returns the number of contiguous subarrays whose elements sum to k.

TRY THIS INPUT:
  ```python
  print(subarray_sum([1, 1, 1], 2))
  print(subarray_sum([1, 2, 3], 3))
  print(subarray_sum([1, -1, 0], 0))
  ```

EXPECTED OUTPUT:
  ```
  2
  2
  3
  ```

CHECK: python3 check.py hard/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
