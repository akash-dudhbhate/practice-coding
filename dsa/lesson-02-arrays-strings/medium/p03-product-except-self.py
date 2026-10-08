"""
LESSON 02 — Arrays & Strings
MEDIUM P03 — Product Except Self
============================================

CONCEPT:
  Two-pass pattern: pass 1 stores the product of everything LEFT of
  each index, pass 2 multiplies in everything RIGHT of it. No division
  needed — which is why zeros don't break it.

PROBLEM:
  Write a function `product_except_self(nums: list) -> list` returning
  a list where element i is the product of all elements EXCEPT nums[i].
  Do not use division. Must run in O(n).

TRY THIS INPUT:
  ```python
  print(product_except_self([1, 2, 3, 4]))
  print(product_except_self([2, 3, 4]))
  print(product_except_self([-1, 1, 0, -3, 3]))
  ```

EXPECTED OUTPUT:
  ```
  [24, 12, 8, 6]
  [12, 8, 6]
  [0, 0, 9, 0, 0]
  ```

CHECK: python3 check.py medium/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
