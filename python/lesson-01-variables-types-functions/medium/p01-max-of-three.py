"""
LESSON 01 — Variables, Types & Functions
MEDIUM P01 — Max of Three Numbers
============================================

CONCEPT:
  Functions can call other functions — that's how big programs are
  built from small pieces. If you already have max_of_two(a, b), the
  max of three numbers is just max_of_two(max_of_two(a, b), c):
  first find the bigger of a and b, then compare that with c.

PROBLEM:
  Write a function `max_of_three(a: int, b: int, c: int) -> int` that
  returns the largest of the three integers. Write your own max_of_two
  helper in this file and reuse it — do NOT use the built-in max().

TRY THIS INPUT:
  ```python
  print(max_of_three(1, 5, 3))
  print(max_of_three(9, 2, 7))
  print(max_of_three(4, 4, 4))
  ```

EXPECTED OUTPUT:
  ```
  5
  9
  4
  ```

CHECK: python3 check.py medium/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
