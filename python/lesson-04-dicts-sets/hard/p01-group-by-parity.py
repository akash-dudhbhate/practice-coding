"""
LESSON 04 — Dictionaries & Sets
HARD P01 — Group By Parity
============================================

CONCEPT:
  Grouping means building a dict where each key holds a list of matching
  items. The modulo operator n % 2 tells you parity: 0 means even,
  1 means odd — that decides which bucket gets the number.

PROBLEM:
  Write a function `group_by_parity(nums: list) -> dict` that returns
  {"even": [...], "odd": [...]} grouping numbers by parity. Both keys
  must always be present, even for empty input.

TRY THIS INPUT:
  ```python
  print(group_by_parity([1, 2, 3, 4]))
  print(group_by_parity([]))
  ```

EXPECTED OUTPUT:
  ```
  {'even': [2, 4], 'odd': [1, 3]}
  {'even': [], 'odd': []}
  ```

CHECK: python3 check.py hard/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
