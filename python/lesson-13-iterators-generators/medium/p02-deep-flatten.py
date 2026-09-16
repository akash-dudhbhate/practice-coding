"""
LESSON 13 — Iterators & Generators
MEDIUM P02 — Recursive flatten with yield from
============================================

CONCEPT:
  `yield from sub_generator` forwards all values from a nested generator,
  which makes recursive generators clean: when you hit a list inside a
  list, just `yield from flatten(item)` to recurse.

PROBLEM:
  Write a generator `flatten(nested_list)` that yields every non-list
  item from an arbitrarily nested list, in order. Items that are lists
  get flattened recursively; everything else is yielded as-is.

TRY THIS INPUT:
  ```python
  print(list(flatten([1, [2, [3, [4]]], 5])))
  print(list(flatten([])))
  ```

EXPECTED OUTPUT:
  ```
  [1, 2, 3, 4, 5]
  []
  ```

CHECK: python3 check.py medium/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
