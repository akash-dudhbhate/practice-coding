"""
LESSON 10 — OOP Advanced
HARD P02 — Stack with Composition
============================================

CONCEPT:
  Prefer composition over inheritance: the Stack HAS a list inside
  (private attribute) rather than IS a list. This hides list methods
  callers shouldn't use.

PROBLEM:
  Write a `Stack` class that keeps a private list internally and
  exposes ONLY: `push(item)`, `pop()` (IndexError if empty),
  `peek()` (IndexError if empty), `is_empty()`, `size()`.

TRY THIS INPUT:
  ```python
  s = Stack()
  s.push(1)
  s.push(2)
  print(s.size(), s.pop(), s.peek())
  ```

EXPECTED OUTPUT:
  ```
  2 2 1
  ```

CHECK: python3 check.py hard/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
