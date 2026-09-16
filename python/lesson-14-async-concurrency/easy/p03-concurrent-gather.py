"""
LESSON 14 — Async & Concurrency
EASY P03 — Concurrent with gather
============================================

CONCEPT:
  `asyncio.gather()` runs coroutines concurrently — total time is
  the SLOWEST task, not the sum of all tasks.

PROBLEM:
  Write async functions `task1()` (sleep 0.3, return "task1 done")
  and `task2()` (sleep 0.5, return "task2 done"), plus an async
  `main()` that runs both with `asyncio.gather` and returns the
  results list.

TRY THIS INPUT:
  ```python
  import asyncio, time
  start = time.time()
  results = asyncio.run(main())
  print(results)
  print(f"{time.time() - start:.2f}s  # ~0.5 not 0.8")
  ```

EXPECTED OUTPUT:
  ```
  ['task1 done', 'task2 done']
  0.50s  # ~0.5 not 0.8
  ```

CHECK: python3 check.py easy/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
