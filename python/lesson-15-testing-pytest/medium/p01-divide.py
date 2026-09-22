"""
LESSON 15 — Testing with pytest
MEDIUM P01 — divide with pytest.raises
============================================

CONCEPT:
  `with pytest.raises(ErrorType):` asserts that the block raises —
  the test fails if no exception (or the wrong one) happens.

PROBLEM:
  Write a function `divide(a, b)` that returns a/b and raises
  ZeroDivisionError when b is 0. Write tests for normal division
  AND for the exception using pytest.raises.

TRY THIS INPUT:
  ```python
  print(divide(10, 2))
  try:
      divide(1, 0)
  except ZeroDivisionError:
      print("caught")
  ```

EXPECTED OUTPUT:
  ```
  5.0
  caught
  ```

RUN TESTS: pytest <this file> -v
CHECK: python3 check.py medium/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
