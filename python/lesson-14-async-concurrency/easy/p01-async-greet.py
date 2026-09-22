"""
LESSON 14 — Async & Concurrency
EASY P01 — Async Greet
============================================

CONCEPT:
  `async def` defines a coroutine — calling it doesn't run it.
  `await` pauses without blocking, and `asyncio.run()` drives the
  coroutine to completion.

PROBLEM:
  Write an async function `async_greet(name)` that awaits
  `asyncio.sleep(1)` then returns "Hello, {name}!".

TRY THIS INPUT:
  ```python
  import asyncio
  print(asyncio.run(async_greet("Akash")))
  ```

EXPECTED OUTPUT:
  ```
  Hello, Akash!
  ```

CHECK: python3 check.py easy/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
