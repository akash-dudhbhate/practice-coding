"""
LESSON 04 — Dictionaries & Sets
EASY P02 — Has Key
============================================

CONCEPT:
  d.get(key) returns the value for a key, or None if the key is
  missing — a safe lookup that never raises KeyError. (Edge case: a
  key stored with value None needs a fallback, e.g. `or key in d`.)

PROBLEM:
  Write a function `has_key(d: dict, key) -> bool` that returns True
  if `key` exists in dict `d`, False otherwise. Use .get() for the
  lookup (not just the `in` operator alone).

TRY THIS INPUT:
  ```python
  print(has_key({"a": 1}, "a"))
  print(has_key({"a": 1}, "b"))
  print(has_key({}, "a"))
  ```

EXPECTED OUTPUT:
  ```
  True
  False
  False
  ```

CHECK: python3 check.py easy/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
