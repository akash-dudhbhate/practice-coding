"""
LESSON 04 — Dictionaries & Sets
MEDIUM P01 — Merge Dicts
============================================

CONCEPT:
  The {**d1, **d2} unpacking syntax builds a new dict from two others —
  keys from the second dict overwrite the first on conflict. It leaves
  both inputs untouched, unlike d1.update(d2) which mutates d1.

PROBLEM:
  Write a function `merge_dicts(d1: dict, d2: dict) -> dict` that
  returns a NEW dict merging d1 and d2. On conflicting keys, d2's
  value wins. Do NOT mutate either input dict.

TRY THIS INPUT:
  ```python
  print(merge_dicts({"a": 1, "b": 2}, {"b": 3, "c": 4}))
  print(merge_dicts({}, {"a": 1}))
  ```

EXPECTED OUTPUT:
  ```
  {'a': 1, 'b': 3, 'c': 4}
  {'a': 1}
  ```

CHECK: python3 check.py medium/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
