"""
LESSON 15 — Testing with pytest
HARD P02 — Stack with Parametrized Tests
============================================

CONCEPT:
  Parametrize can drive whole scenarios: feed each row a list of
  items to push and the expected pop result — one test function,
  many cases.

PROBLEM:
  Write a `Stack` class (push, pop, peek, is_empty — pop/peek raise
  IndexError when empty). Write parametrized tests for push/pop
  sequences and a test that popping from an empty stack raises.

TRY THIS INPUT:
  ```python
  s = Stack()
  s.push(1); s.push(2)
  print(s.pop(), s.peek())
  ```

EXPECTED OUTPUT:
  ```
  2 1
  ```

RUN TESTS: pytest <this file> -v
CHECK: python3 check.py hard/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
