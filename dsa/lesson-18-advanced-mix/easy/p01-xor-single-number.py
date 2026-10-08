"""
LESSON 18 — Advanced Mix
EASY P01 — XOR Single Number
============================================

CONCEPT:
  XOR cancels pairs: a ^ a = 0, a ^ 0 = a, and XOR is commutative.
  Fold every element into one accumulator — duplicates annihilate and
  the lone element survives. O(n) time, O(1) space — no dict, no set.

PROBLEM:
  Write a function `single_number(nums: list[int]) -> int`. Every element
  appears exactly twice except ONE — return it. Must run in O(1) extra
  space (a Counter or set technically works but misses the point).
  Negative numbers are fine — XOR handles them.

TRY THIS INPUT:
  ```python
  print(single_number([2,2,1]))
  print(single_number([4,1,2,1,2]))
  print(single_number([1]))
  print(single_number([-1,-1,-2]))
  ```

EXPECTED OUTPUT:
  ```
  1
  4
  1
  -2
  ```

CHECK: python3 check.py easy/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
