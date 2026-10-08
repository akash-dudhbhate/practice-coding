"""
LESSON 18 — Advanced Mix
MEDIUM P02 — XOR Two Single Numbers
============================================

CONCEPT:
  Two elements appear once, everything else twice. XOR all → a ^ b
  (the two loners' difference pattern). Any set bit of that XOR is a
  bit where a and b DIFFER — take the lowest one via xor & -xor.
  Partition the array by that bit: the two loners land in different
  groups, every duplicate pair stays together. XOR each group → each
  yields its loner.

PROBLEM:
  Write a function `single_numbers(nums: list[int]) -> list[int]`
  returning the two elements that appear exactly once (order doesn't
  matter). O(n) time, O(1) extra space.

TRY THIS INPUT:
  ```python
  print(sorted(single_numbers([1,2,1,3,2,5])))
  print(sorted(single_numbers([-1,0])))
  print(sorted(single_numbers([1,2,3,4,1,2,3,7])))
  ```

EXPECTED OUTPUT:
  ```
  [3, 5]
  [-1, 0]
  [4, 7]
  ```

CHECK: python3 check.py medium/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
