# Lesson 14 — Async/Await & Concurrency

## What you'll learn
- Sync vs async execution
- async/await syntax
- Event loop
- asyncio.gather() for concurrent tasks
- asyncio.create_task()
- aiohttp for async HTTP
- concurrent.futures (threads & processes)
- asyncio.run()
- When to use async vs threads vs processes

## Lesson

### Basic async
```python
import asyncio
async def greet(name):
    await asyncio.sleep(1)
    return f"Hello, {name}"

async def main():
    result = await greet("Akash")
    print(result)

asyncio.run(main())
```

### Concurrent tasks
```python
async def main():
    results = await asyncio.gather(
        fetch("url1"),
        fetch("url2"),
        fetch("url3")
    )  # all run at once
```

---

## Your Tasks

### Easy
1. `easy/p01-solve.py` — Write an async function `async_greet(name)` that awaits `asyncio.sleep(1)` then returns a greeting. Run it with `asyncio.run()`.
2. `easy/p02-solve.py` — Write an async function that prints "Start", awaits `asyncio.sleep(0.5)`, then prints "End". Measure total time.
3. `easy/p03-solve.py` — Write two async functions with different sleep durations. Run both concurrently with `asyncio.gather()` and print total time (should be max, not sum).

### Medium
4. `medium/p01-solve.py` — Write an async function `fetch_all(urls)` that fetches multiple URLs concurrently using `asyncio.gather()`. Use `asyncio.sleep()` to simulate network delay.
5. `medium/p02-solve.py` — Write a script that uses `ThreadPoolExecutor` to download (simulate) 5 files concurrently. Each "download" is a `time.sleep()` call.
6. `medium/p03-solve.py` — Write a script that uses `ProcessPoolExecutor` to compute squares of numbers 1-20 in parallel across multiple processes.

### Hard
7. `hard/p01-solve.py` — Write an async rate limiter: a function that processes 10 tasks but only allows 3 to run concurrently at any time (use `asyncio.Semaphore`).
8. `hard/p02-solve.py` — Write an async web scraper that fetches 5 URLs concurrently, handles timeouts (5 second limit per request), and collects all successful results. Use `asyncio.wait_for()` for timeout.
9. `hard/p03-solve.py` — Write a producer-consumer pattern: one async producer generates 10 items, two async consumers process them concurrently using `asyncio.Queue`.

### How to work
- Write your complete solution from scratch below the TODO marker.
- Remove the TODO line when done.
