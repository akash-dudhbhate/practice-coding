"""
LESSON 03 — Lists & Tuples
MEDIUM P02 — Sort By Length
============================================

CONCEPT:
  sorted() accepts a `key` function that maps each element to the value
  used for comparison. Passing key=len sorts strings by their length
  instead of alphabetically, and it's a stable sort — equal-length
  items keep their original order.

PROBLEM:
  Write a function `sort_by_length(words: list) -> list` that returns a
  new list of strings sorted by length, shortest first, using sorted()
  with a key.

TRY THIS INPUT:
  ```python
  print(sort_by_length(["apple", "hi", "cat"]))
  print(sort_by_length(["same", "four"]))
  print(sort_by_length([]))
  ```

EXPECTED OUTPUT:
  ```
  ['hi', 'cat', 'apple']
  ['same', 'four']
  []
  ```

CHECK: python3 check.py medium/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
