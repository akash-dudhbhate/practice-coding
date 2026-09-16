"""
LESSON 03 — Lists & Tuples
MEDIUM P03 — Swap Pairs
============================================

CONCEPT:
  Python can swap two values in one line with tuple unpacking: a, b =
  b, a. Stepping through a list by 2 (range(0, n, 2)) lets you swap
  each adjacent pair in place.

PROBLEM:
  Write a function `swap_pairs(items: list) -> list` that swaps every
  pair of adjacent elements. For [1,2,3,4,5] return [2,1,4,3,5] —
  the last element stays put if the length is odd. Don't mutate input.

TRY THIS INPUT:
  ```python
  print(swap_pairs([1, 2, 3, 4, 5]))
  print(swap_pairs([1, 2]))
  print(swap_pairs([1]))
  ```

EXPECTED OUTPUT:
  ```
  [2, 1, 4, 3, 5]
  [2, 1]
  [1]
  ```

CHECK: python3 check.py medium/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
