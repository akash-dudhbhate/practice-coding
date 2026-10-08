"""
LESSON 03 — Hashing (Dict & Set Patterns)
EASY P01 — Count Frequencies
============================================

CONCEPT:
  A dict maps item -> count. Walking the list once and doing
  `counts[x] = counts.get(x, 0) + 1` builds a full frequency table
  in O(n) — no sorting, no nested loops.

PROBLEM:
  Write a function `count_frequencies(items: list) -> dict` that
  returns a dict mapping each distinct item to how many times it
  appears. Items may be strings or numbers.

TRY THIS INPUT:
  ```python
  print(count_frequencies(["a", "b", "a", "c", "b", "a"]))
  print(count_frequencies([7, 7, 7]))
  print(count_frequencies([]))
  ```

EXPECTED OUTPUT:
  ```
  {'a': 3, 'b': 2, 'c': 1}
  {7: 3}
  {}
  ```

CHECK: python3 check.py easy/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
