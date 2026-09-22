"""
LESSON 14 — Async & Concurrency
EASY P02 — Async Start/End
============================================

CONCEPT:
  `await asyncio.sleep(t)` suspends the coroutine for t seconds —
  the event loop can run other work meanwhile. This prints before
  and after the pause.

PROBLEM:
  Write an async function `start_end()` that prints "Start", awaits
  `asyncio.sleep(0.5)`, then prints "End".

TRY THIS INPUT:
  ```python
  import asyncio, time
  start = time.time()
  asyncio.run(start_end())
  print(f"Took {time.time() - start:.2f}s")
  ```

EXPECTED OUTPUT:
  ```
  Start
  End
  Took 0.50s
  ```

CHECK: python3 check.py easy/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
