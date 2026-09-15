# Lesson 14 — Concepts Explained (Async/Await & Concurrency)

> Read this before solving the problems. Each concept explains:
> **What** it is · **Why** it exists · **Where** it's used · **What goes wrong** without it.

---

## Synchronous vs Asynchronous

**What:**
- **Synchronous:** code runs line by line. Each line waits for the previous one to finish. If a line takes 5 seconds (e.g., downloading a file), the entire program blocks for 5 seconds.
- **Asynchronous:** code can start a slow operation, move on to other work, and come back when the operation finishes. Multiple operations can be "in flight" at once.

```python
# Synchronous — total time: 3 seconds (1 + 1 + 1)
import time
def sync_task(n):
    time.sleep(1)
    return f"Task {n} done"
for i in range(3):
    print(sync_task(i))    # takes 3 seconds total

# Asynchronous — total time: ~1 second (all run concurrently)
import asyncio
async def async_task(n):
    await asyncio.sleep(1)
    return f"Task {n} done"
async def main():
    results = await asyncio.gather(async_task(0), async_task(1), async_task(2))
    print(results)    # takes ~1 second total
```

**Why it exists:** Without async, I/O-bound programs (web servers, API clients, scrapers) waste time waiting. A sync web server handling 100 requests each waiting 1 second for a database → 100 seconds. An async server handles all 100 concurrently → 1 second.

**Where it's used:** Web servers (FastAPI, aiohttp), API clients (httpx, aiohttp), web scrapers, chat applications, real-time systems, database drivers (asyncpg).

**What goes wrong without it:**
- Sync code for I/O-bound tasks → slow, can't scale. 1000 concurrent users → 1000 threads → server crashes.
- Using async for CPU-bound tasks → no benefit (async helps with I/O, not computation). Use multiprocessing for CPU-bound work.
- Mixing sync and async incorrectly → blocking the event loop (see below).

---

## async/await Syntax

**What:** `async def` defines a coroutine. `await` pauses the coroutine until the awaited operation completes, yielding control back to the event loop.

```python
async def fetch_data(url):
    response = await aiohttp.get(url)    # pause here, let other tasks run
    data = await response.json()          # pause again
    return data

# await can only be used inside async def
async def main():
    data = await fetch_data("https://api.example.com")
    print(data)

# Run the coroutine
asyncio.run(main())
```

**Why it exists:** Before `async`/`await`, Python used callbacks and yield-based generators for async — hard to read and debug. `async`/`await` makes async code look like sync code — linear, readable, no callback hell.

**Where it's used:** Every async Python program. FastAPI routes are `async def`. aiohttp handlers are `async def`.

**What goes wrong without it:**
- `await` outside `async def` → `SyntaxError`.
- Calling `async def` function without `await` → returns a coroutine object, doesn't execute. `fetch_data("url")` → `<coroutine object>`. Must be `await fetch_data("url")`.
- Forgetting `asyncio.run()` → coroutine never runs. You defined it but never started the event loop.

---

## Event Loop

**What:** The event loop is the engine that runs async code. It manages a queue of tasks, runs each one until it hits an `await`, then switches to another task.

```python
import asyncio

async def task(name, delay):
    await asyncio.sleep(delay)
    return f"{name} done after {delay}s"

async def main():
    # Event loop runs all three concurrently
    results = await asyncio.gather(
        task("A", 1),
        task("B", 2),
        task("C", 1)
    )
    print(results)    # ["A done after 1s", "B done after 2s", "C done after 1s"] after 2s

asyncio.run(main())    # starts the event loop
```

**Why it exists:** Without an event loop, there's nothing to switch between tasks. The loop is what makes concurrency possible — it decides which task to run next when one pauses at `await`.

**Where it's used:** `asyncio.run()` creates and runs the event loop. FastAPI/uvicorn runs the event loop for you. You rarely manage the loop directly in modern Python.

**What goes wrong without it:**
- Calling `asyncio.run()` twice → `RuntimeError: asyncio.run() cannot be called from a running event loop`.
- Blocking the event loop with sync code (e.g., `time.sleep(5)` inside an async function) → ALL other tasks freeze for 5 seconds. Use `await asyncio.sleep(5)` instead.
- Running CPU-intensive code in async → blocks the loop → no concurrency benefit.

---

## asyncio.gather()

**What:** Run multiple coroutines concurrently and collect their results.

```python
async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()

async def main():
    urls = ["url1", "url2", "url3"]
    tasks = [fetch(url) for url in urls]
    results = await asyncio.gather(*tasks)    # all run concurrently
    # results is a list in the same order as tasks
```

**Why it exists:** Without `gather()`, you'd `await` each task one by one — sequential, no concurrency. `gather()` runs them all at once, reducing total time from sum to max.

**Where it's used:** Fetching multiple URLs, parallel database queries, batch processing, any time you have multiple independent async operations.

**What goes wrong without it:**
- `await fetch(url1); await fetch(url2)` → sequential, no concurrency. Takes 2x as long.
- `gather()` without `await` → returns a Future, doesn't actually run. Must `await asyncio.gather(...)`.
- One task raises an exception → `gather()` propagates it, other tasks may be cancelled. Use `return_exceptions=True` to get exceptions as results instead.

---

## asyncio.create_task()

**What:** Schedule a coroutine to run as a task on the event loop, without waiting for it immediately.

```python
async def main():
    task = asyncio.create_task(fetch_data("url"))    # schedule, don't wait
    # do other work here while task runs in background
    result = await task    # now wait for it if not done yet
```

**Why it exists:** `gather()` waits for all tasks. `create_task()` lets you start a task, do other work, and await it later. Useful for fire-and-forget tasks or when you need results at different points.

**Where it's used:** Background tasks, periodic updates, starting multiple tasks at different points in code.

**What goes wrong without it:**
- Creating a task but never awaiting it → task may be cancelled by the garbage collector before it finishes. Always store a reference and await it.
- `create_task()` outside an async function → no running event loop → `RuntimeError`.

---

## aiohttp (Async HTTP Client)

**What:** `aiohttp` is an async HTTP client/server library — like `requests` but for async code.

```python
import aiohttp, asyncio

async def fetch_json(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()

async def main():
    data = await fetch_json("https://api.github.com/users/github")
    print(data["name"])

asyncio.run(main())
```

**Why it exists:** `requests` is synchronous — it blocks the event loop. If you use `requests.get()` inside an async function, ALL other tasks freeze until the request completes. `aiohttp` is async-native — it yields to the event loop during I/O.

**Where it's used:** Async API clients, web scrapers, microservice communication, any async code that makes HTTP requests.

**What goes wrong without it:**
- Using `requests.get()` inside `async def` → blocks the event loop → no concurrency. 100 requests take 100x time, not 1x.
- Forgetting `async with` → session not properly closed → connection leaks.
- Not closing the session → warnings about unclosed connections → resource leaks.

---

## concurrent.futures (Threads & Processes)

**What:** `concurrent.futures` provides thread pools and process pools for parallel execution.

```python
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

# Threads — good for I/O-bound tasks
with ThreadPoolExecutor(max_workers=5) as executor:
    results = list(executor.map(fetch_url, urls))

# Processes — good for CPU-bound tasks
with ProcessPoolExecutor() as executor:
    results = list(executor.map(heavy_computation, data_list))
```

**Why it exists:** Async is for I/O-bound tasks. For CPU-bound tasks (math, image processing), you need actual parallelism — multiple CPU cores. Threads share the GIL (only one thread runs Python at a time), so for CPU-bound work, use processes.

**Where it's used:** ThreadPool for I/O (file operations, network calls without async). ProcessPool for CPU (data processing, image manipulation, ML inference).

**What goes wrong without it:**
- Using threads for CPU-bound work → GIL prevents true parallelism → no speedup. Use processes instead.
- Using processes for I/O-bound work → overhead of creating processes > benefit. Use threads or async.
- Too many workers → resource exhaustion. `max_workers` should match CPU cores for processes, or be reasonable (10-50) for threads.

---

## asyncio.run()

**What:** The entry point for running async code. Creates an event loop, runs the coroutine, and closes the loop.

```python
async def main():
    await some_async_operation()

asyncio.run(main())    # run the async program
```

**Why it exists:** Before `asyncio.run()` (Python 3.7), you had to manually create a loop, run the coroutine, and close the loop — 3 lines of boilerplate. `asyncio.run()` does it all in one call.

**Where it's used:** The top-level entry point of any async script. In web frameworks (FastAPI), the framework calls it for you.

**What goes wrong without it:**
- Calling `asyncio.run()` inside an already-running event loop → `RuntimeError`. You can't nest event loops.
- Calling `asyncio.run()` multiple times → works but creates/destroys a loop each time. Call it once at the top level.
- Jupyter notebooks already have a running event loop → `asyncio.run()` fails. Use `await main()` directly in notebooks.

---

## When to Use What (async vs threads vs processes)

**What:** Decision framework for concurrency:

| Scenario | Use | Why |
|----------|-----|-----|
| Many I/O operations (HTTP, DB, files) | async/await | Non-blocking, scales to 10,000+ concurrent |
| Few I/O operations, sync codebase | ThreadPoolExecutor | Simple, no async rewrite needed |
| CPU-heavy computation | ProcessPoolExecutor | True parallelism, bypasses GIL |
| Mixed I/O + CPU | async + ProcessPool | async for I/O, offload CPU to processes |

**Why it exists:** No single concurrency model is best for all cases. Understanding when to use each prevents performance disasters.

**Where it's used:** Architecture decisions for any performance-sensitive application.

**What goes wrong without it:**
- Using async for CPU-bound work → blocks event loop → worse than sync.
- Using threads for CPU-bound work → GIL → no parallelism → wasted cores.
- Using processes for everything → high overhead, complex (pickling, IPC).
