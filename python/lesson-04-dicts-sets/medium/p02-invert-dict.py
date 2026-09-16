"""
LESSON 04 — Dictionaries & Sets
MEDIUM P02 — Invert Dict
============================================

CONCEPT:
  d.items() yields (key, value) pairs you can loop over. A dict
  comprehension {v: k for k, v in d.items()} swaps them in one line —
  and if two keys shared a value, the last one wins naturally.

PROBLEM:
  Write a function `invert_dict(d: dict) -> dict` that returns a new
  dict with keys and values swapped. If values aren't unique, keep the
  LAST key seen for each value.

TRY THIS INPUT:
  ```python
  print(invert_dict({"a": 1, "b": 2}))
  print(invert_dict({}))
  ```

EXPECTED OUTPUT:
  ```
  {1: 'a', 2: 'b'}
  {}
  ```

CHECK: python3 check.py medium/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
