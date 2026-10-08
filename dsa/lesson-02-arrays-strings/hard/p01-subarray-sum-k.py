"""
LESSON 02 — Arrays & Strings
HARD P01 — Subarray Sum Equals K
============================================

CONCEPT:
  Prefix sums + hashmap: if prefix sum P was seen earlier and the
  current prefix is P+k, the subarray between them sums to k. Turn
  "check all subarrays" O(n^2) into "lookup per element" O(n).
  Seed the dict with {0: 1} so subarrays starting at index 0 count.

PROBLEM:
  Write a function `count_subarray_sum(nums: list, k: int) -> int`
  returning the number of CONTIGUOUS subarrays whose sum is exactly k.

TRY THIS INPUT:
  ```python
  print(count_subarray_sum([1, 1, 1], 2))
  print(count_subarray_sum([1, 2, 3], 3))
  print(count_subarray_sum([1, -1, 0], 0))
  ```

EXPECTED OUTPUT:
  ```
  2
  2
  3
  ```

CHECK: python3 check.py hard/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
