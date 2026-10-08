"""
LESSON 01 — Time/Space Complexity & Big-O
MEDIUM P03 — Early Exit Comparisons
============================================

CONCEPT:
  Linear search has best case O(1) (target is first) and worst case
  O(n) (target is last or missing). The early `return` is what creates
  the best case — it exits the moment it finds the target.

PROBLEM:
  Write a function `count_comparisons(nums: list, target) -> int` that
  performs a linear search and returns the number of element
  comparisons actually made (stop counting when found!).

TRY THIS INPUT:
  ```python
  print(count_comparisons([5, 9, 2, 7], 5))   # found immediately
  print(count_comparisons([5, 9, 2, 7], 7))   # last element
  print(count_comparisons([5, 9, 2, 7], 99))  # never found
  ```

EXPECTED OUTPUT:
  ```
  1
  4
  4
  ```

CHECK: python3 check.py medium/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
