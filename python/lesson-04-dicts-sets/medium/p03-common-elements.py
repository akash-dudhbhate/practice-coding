"""
LESSON 04 — Dictionaries & Sets
MEDIUM P03 — Common Elements
============================================

CONCEPT:
  Set intersection (set(a) & set(b)) gives elements present in both
  collections in one step — much faster than nested loops. sorted()
  then turns the result into a predictable, ordered list.

PROBLEM:
  Write a function `common_elements(a: list, b: list) -> list` that
  returns a sorted list of elements present in BOTH lists, using set
  intersection. common_elements([1,2,3],[2,3,4]) -> [2, 3].

TRY THIS INPUT:
  ```python
  print(common_elements([1, 2, 3], [2, 3, 4]))
  print(common_elements([1], [2]))
  print(common_elements([], []))
  ```

EXPECTED OUTPUT:
  ```
  [2, 3]
  []
  []
  ```

CHECK: python3 check.py medium/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
