"""
LESSON 04 — Dictionaries & Sets
HARD P02 — Set Difference
============================================

CONCEPT:
  Set subtraction (set_a - set_b) gives items in a but not b. Doing it
  both directions splits the symmetric difference — everything unique
  to either side — into two labelled buckets in a dict.

PROBLEM:
  Write a function `set_difference(a: list, b: list) -> dict` that
  returns {"only_a": sorted list of items in a but not b,
           "only_b": sorted list of items in b but not a}.

TRY THIS INPUT:
  ```python
  print(set_difference([1, 2, 3], [2, 3, 4]))
  print(set_difference([1, 2], [1, 2]))
  ```

EXPECTED OUTPUT:
  ```
  {'only_a': [1], 'only_b': [4]}
  {'only_a': [], 'only_b': []}
  ```

CHECK: python3 check.py hard/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
