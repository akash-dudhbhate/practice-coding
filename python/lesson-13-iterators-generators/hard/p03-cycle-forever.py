"""
LESSON 13 — Iterators & Generators
HARD P03 — cycle_forever (Round-Robin Generator)
============================================

CONCEPT:
  `itertools.cycle` repeats an iterable forever — useful for round-robin
  assignment. Implementing it yourself means saving the items to a list
  once (the input might be a one-shot generator), then looping forever.

PROBLEM:
  Write a generator `cycle_forever(iterable)` that yields the items in
  order, repeating forever. An empty iterable should yield nothing.
  Bonus in `__main__`: use it to round-robin assign 7 tasks to
  3 workers.

TRY THIS INPUT:
  ```python
  from itertools import islice
  print(list(islice(cycle_forever(["a", "b", "c"]), 7)))
  ```

EXPECTED OUTPUT:
  ```
  ['a', 'b', 'c', 'a', 'b', 'c', 'a']
  ```

CHECK: python3 check.py hard/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
