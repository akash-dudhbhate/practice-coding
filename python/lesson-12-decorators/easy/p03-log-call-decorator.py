"""
LESSON 12 — Decorators
EASY P03 — @log_call Decorator
============================================

CONCEPT:
  Inside a decorator's wrapper you can run code BEFORE the call (log the
  function name) and AFTER it (log the return value). `func.__name__`
  gives you the wrapped function's name for readable logs.

PROBLEM:
  Write a decorator `log_call(func)` that prints f"Calling {func.__name__}"
  before calling the function and f"Returned: {result}" after. Apply it
  to `add(a, b)` returning a + b.

TRY THIS INPUT:
  ```python
  print(add(2, 3))
  ```

EXPECTED OUTPUT:
  ```
  Calling add
  Returned: 5
  5
  ```

CHECK: python3 check.py easy/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
