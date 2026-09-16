"""
LESSON 14 — Async & Concurrency
HARD P01 — Async Rate Limiter
============================================

CONCEPT:
  `asyncio.Semaphore(n)` allows at most n coroutines to hold it at
  once — `async with sem:` blocks extra tasks until a slot frees.

PROBLEM:
  Write an async `limited_task(sem, task_id)` that acquires the
  semaphore, sleeps 0.1s, and returns task_id. Then an async
  `main()` that runs 10 tasks through a Semaphore(3) via gather and
  returns the results.

TRY THIS INPUT:
  ```python
  import asyncio
  results = asyncio.run(main())
  print(sorted(results))
  ```

EXPECTED OUTPUT:
  ```
  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
  ```

CHECK: python3 check.py hard/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
