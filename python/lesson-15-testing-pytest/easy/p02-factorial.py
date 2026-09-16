"""
LESSON 15 — Testing with pytest
EASY P02 — factorial with parametrize
============================================

CONCEPT:
  `@pytest.mark.parametrize` runs one test function with many input
  rows — each row shows up as its own pass/fail in the report.

PROBLEM:
  Write a function `factorial(n)` that returns n! (raise ValueError
  for negative n). Test it with @pytest.mark.parametrize covering at
  least 0!, 1!, 3!, 5!, plus a test that negative input raises
  ValueError.

TRY THIS INPUT:
  ```python
  print(factorial(5))
  print(factorial(0))
  ```

EXPECTED OUTPUT:
  ```
  120
  1
  ```

RUN TESTS: pytest <this file> -v
CHECK: python3 check.py easy/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
