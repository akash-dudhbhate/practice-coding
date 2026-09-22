"""
LESSON 03 — Lists & Tuples
EASY P02 — Reverse List
============================================

CONCEPT:
  Slicing works on lists just like strings — items[::-1] produces a
  reversed COPY. The key detail: return a new list and leave the
  original untouched, because callers often still need their data.

PROBLEM:
  Write a function `reverse_list(items: list) -> list` that returns a
  NEW list with the elements in reverse order. Do NOT mutate the
  input list.

TRY THIS INPUT:
  ```python
  print(reverse_list([1, 2, 3]))
  original = [1, 2, 3]
  reverse_list(original)
  print(original)
  ```

EXPECTED OUTPUT:
  ```
  [3, 2, 1]
  [1, 2, 3]
  ```

CHECK: python3 check.py easy/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
