"""
LESSON 12 — Decorators
HARD P02 — @retry(times=3, delay=1) Decorator
============================================

CONCEPT:
  Retry logic is a classic decorator: loop up to `times`, return on the
  first success, `time.sleep(delay)` between failures, and re-raise the
  last exception if every attempt fails. Keyword arguments with defaults
  make it configurable: `@retry(times=3, delay=0.1)`.

PROBLEM:
  Write `retry(times=3, delay=1)` — a decorator factory. The wrapped
  function is tried up to `times` times; each failure prints
  f"Attempt {n} failed: {e}" and sleeps `delay` seconds (except after
  the last attempt). If all attempts fail, re-raise the last exception.

TRY THIS INPUT:
  ```python
  calls = {"n": 0}

  @retry(times=3, delay=0)
  def flaky():
      calls["n"] += 1
      if calls["n"] < 3:
          raise ValueError("boom")
      return "success"

  print(flaky())
  ```

EXPECTED OUTPUT:
  ```
  Attempt 1 failed: boom
  Attempt 2 failed: boom
  success
  ```

CHECK: python3 check.py hard/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
