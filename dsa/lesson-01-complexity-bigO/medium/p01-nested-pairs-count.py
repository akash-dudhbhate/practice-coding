"""
LESSON 01 — Time/Space Complexity & Big-O
MEDIUM P01 — Nested Pairs Count
============================================

CONCEPT:
  Nested loops don't always run n×n times. For
  `for i in range(n): for j in range(i+1, n)`, the inner loop runs
  (n-1) + (n-2) + ... + 1 + 0 = n*(n-1)/2 times — still O(n²).

PROBLEM:
  Write a function `count_pair_ops(n: int) -> int` returning the total
  number of inner-loop iterations for the nested loop above.

TRY THIS INPUT:
  ```python
  print(count_pair_ops(5))   # 4+3+2+1+0
  print(count_pair_ops(4))   # 3+2+1+0
  print(count_pair_ops(1))   # no pairs
  print(count_pair_ops(10))
  ```

EXPECTED OUTPUT:
  ```
  10
  6
  0
  45
  ```

CHECK: python3 check.py medium/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
