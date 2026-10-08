"""
LESSON 05 — Sliding Window
HARD P03 — Fruit Into Baskets
============================================

CONCEPT:
  Disguise check: you walk a row of trees, each holding one fruit type;
  you carry exactly 2 baskets, each holding ONE type. Stop when you'd
  need a third basket. This is literally "longest subarray with at
  most 2 distinct values" — same skeleton as P02 with k = 2.

PROBLEM:
  Write a function `total_fruit(fruits: list[int]) -> int` that returns
  the maximum number of fruits you can collect — i.e., the length of
  the longest contiguous subarray containing at most 2 distinct values.
  Empty input returns 0.

TRY THIS INPUT:
  ```python
  print(total_fruit([1, 2, 1]))
  print(total_fruit([0, 1, 2, 2]))
  print(total_fruit([1, 2, 3, 2, 2]))
  print(total_fruit([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]))
  print(total_fruit([1, 1, 1, 1]))
  ```

EXPECTED OUTPUT:
  ```
  3
  3
  4
  5
  4
  ```

CHECK: python3 check.py hard/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
