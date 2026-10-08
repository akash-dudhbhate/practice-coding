# 31 — Concurrency options

> **Interview question:** "When would you use `threading` vs `multiprocessing` vs `asyncio`?"
> **What the interviewer is really testing:** Do you understand the GIL, and can you classify a workload as I/O-bound vs CPU-bound to pick the right tool?

## Theory — what it is

Three tools, three different mechanisms:

- **`threading`** — multiple threads inside one process, sharing memory. Python's **GIL** (Global Interpreter Lock) allows only one thread to run Python bytecode at a time, so threads can't speed up pure-Python CPU work — but while a thread waits on the network or disk, it *releases* the GIL and another thread runs. Threads interleave by preemption (the interpreter switches for you).
- **`multiprocessing`** — multiple separate *processes*, each with its own Python interpreter and its own GIL. Real parallelism across CPU cores: 4 processes on 4 cores genuinely compute at once. Cost: memory is not shared — data must be pickled and sent between processes.
- **`asyncio`** — one thread, one process, many coroutines. Instead of the OS switching threads, your code voluntarily says "I'm waiting now" via `await`, and an event loop switches to the next coroutine. Cheapest overhead of the three, but only helps when the waits are async-aware (e.g. `aiohttp`, `asyncio.sleep`) — a blocking call freezes everything.

The decisive question: is the task **I/O-bound** (spends its time *waiting* — network, disk, database) or **CPU-bound** (spends its time *computing* — math, parsing, compression)? I/O-bound → `threading` or `asyncio`. CPU-bound → `multiprocessing` (the only option that gets true parallelism for Python code).

## Why it was needed

A single thread executes one instruction at a time. If a program spends 95% of its time waiting for network responses, that waiting is wasted CPU time — concurrency tools let other work proceed during the waits. And for genuinely parallel computation, one thread simply cannot use more than one CPU core; you need multiple processes.

Why three tools instead of one? Because the GIL makes threads useless for CPU-bound work, processes are heavy and can't share memory cheaply, and asyncio only works if every library you call cooperates with the event loop. Each tool trades overhead, complexity, and capability differently — matching the tool to the workload is the skill being tested.

## Where it's used in a real project

- **`asyncio`**: high-concurrency I/O services — web servers (FastAPI/Starlette), websocket gateways, a scraper holding 10,000 open connections.
- **`threading` / `ThreadPoolExecutor`**: modest I/O concurrency with sync libraries — downloading 50 files, calling a legacy blocking SDK, running a GUI without freezing.
- **`multiprocessing` / `ProcessPoolExecutor`**: CPU-heavy batch work — image resizing, video encoding, data transforms, numerical crunching.
- **Real hybrid**: a web server (asyncio for requests) that hands heavy parsing to a process pool via `loop.run_in_executor`.

## Diagram

```
I/O-bound task (waiting is the bottleneck):

  sequential   |---wait---|---wait---|---wait---|   3 x wait
  threading    |---wait---|                            \
               |---wait---|   all wait at once          } ~1 x wait
               |---wait---|                            /
  asyncio      same picture — one thread juggling all 3

CPU-bound task (computing is the bottleneck):

  threading    [compute][compute][compute]   still serial! (GIL)
  multiprocess [compute]  on core 1          \
               [compute]  on core 2           } truly parallel
               [compute]  on core 3          /
```

## Code — explained

```python
import asyncio

async def fetch(i):                              # 1
    await asyncio.sleep(0.1)                     # 2
    return i * 10

async def main():
    results = await asyncio.gather(*(fetch(i) for i in range(5)))  # 3
    print(results)

asyncio.run(main())                              # 4
```

1. `async def` defines a coroutine — code that can pause itself.
2. `await asyncio.sleep(0.1)` — "I'm waiting 0.1s; run someone else meanwhile." During this sleep the event loop runs the other 4 coroutines.
3. `asyncio.gather` starts all 5 coroutines concurrently and collects their results **in order**.
4. `asyncio.run` starts the event loop and drives `main()` to completion.

Output: `[0, 10, 20, 30, 40]` in ~0.1s total — sequential would take 0.5s. Same trick with `threading` works too (threads release the GIL while sleeping); `multiprocessing` would also work but is overkill — five processes to do five sleeps wastes RAM and startup time.

## Problems

### Easy — threads for I/O-bound work
**Problem:** You have 4 slow "downloads" (each sleeps 0.05s). Run them concurrently with `ThreadPoolExecutor` and print the results in input order.
**Try this input:** `urls = ["a.com", "b.com", "c.com", "d.com"]`
**Expected output:** `['data-from-a.com', 'data-from-b.com', 'data-from-c.com', 'data-from-d.com']`
**Solution:**
```python
import time
from concurrent.futures import ThreadPoolExecutor

def fetch(url):
    time.sleep(0.05)                 # pretend network call
    return f"data-from-{url}"

urls = ["a.com", "b.com", "c.com", "d.com"]

with ThreadPoolExecutor(max_workers=4) as pool:
    results = list(pool.map(fetch, urls))

print(results)
```
**Logic explained:**
1. `ThreadPoolExecutor(max_workers=4)` creates a pool of 4 worker threads.
2. `pool.map(fetch, urls)` sends each URL to a thread — all four sleeps run *at the same time* because sleeping releases the GIL.
3. `map` preserves input order, so results line up with `urls` — this is why output is deterministic.
4. Total time ≈ 0.05s instead of 0.2s sequential — a 4x win for I/O-bound work with threads.

### Medium — processes for CPU-bound work
**Problem:** Checking primality is pure computation (no waiting). Use a `ProcessPoolExecutor` (or `multiprocessing.Pool`) to check 5 numbers in parallel and print the results.
**Try this input:** `[2, 4, 17, 21, 23]`
**Expected output:** `[True, False, True, False, True]`
**Solution:**
```python
from multiprocessing import Pool

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    with Pool(4) as p:
        results = p.map(is_prime, [2, 4, 17, 21, 23])
    print(results)
```
**Logic explained:**
1. `Pool(4)` spawns 4 worker *processes* — each with its own interpreter and GIL, so the math runs truly in parallel on separate cores.
2. `p.map` pickles each argument, ships it to a worker, and collects results in input order.
3. `if __name__ == "__main__"` is **required** here: on macOS/Windows, workers re-import the main module — without the guard they'd re-run the pool-creation code and spawn workers of their own.
4. Why not threads? The loop in `is_prime` is pure Python bytecode — the GIL forces threads to take turns, so threading would be no faster than sequential (often slower due to switching overhead).

### Hard — mixed workload: I/O + CPU at once
**Problem:** A batch job must fetch 4 URLs (I/O-bound) *and* run 4 heavy computations (CPU-bound) — all concurrently. Route each task type to the correct executor so neither blocks the other.
**Try this input:** `urls = ["a.com", "b.com", "c.com", "d.com"]`, `numbers = [10, 20, 30, 40]`
**Expected output:**
```
['data-from-a.com', 'data-from-b.com', 'data-from-c.com', 'data-from-d.com']
[285, 2470, 8555, 20540]
```
**Solution:**
```python
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

def slow_fetch(url):
    time.sleep(0.05)                  # I/O-bound: waiting
    return f"data-from-{url}"

def heavy(n):
    total = 0
    for i in range(n):                # CPU-bound: computing
        total += i * i
    return total

if __name__ == "__main__":
    urls = ["a.com", "b.com", "c.com", "d.com"]
    numbers = [10, 20, 30, 40]

    with ThreadPoolExecutor() as io_pool, ProcessPoolExecutor() as cpu_pool:
        fetch_futures = [io_pool.submit(slow_fetch, u) for u in urls]
        heavy_futures = [cpu_pool.submit(heavy, n) for n in numbers]
        fetched = [f.result() for f in fetch_futures]
        sums = [f.result() for f in heavy_futures]

    print(fetched)
    print(sums)
```
**Logic explained:**
1. `submit` returns a `Future` immediately — a handle for a result that isn't ready yet; `.result()` blocks until it is.
2. I/O tasks go to threads (cheap, share memory); CPU tasks go to processes (escape the GIL, use all cores). Each executor is sized for its workload.
3. Both pools launch their work *before* we collect results — so fetches and computations overlap.
4. `sum(i*i for i in range(10))` = 285, `range(20)` = 2470, `range(30)` = 8555, `range(40)` = 20540 — computed in parallel across cores.
5. This is the real-world pattern: match each subtask to the executor designed for its bottleneck rather than forcing everything through one tool.

## The 30-second interview answer

"First I classify the workload. I/O-bound — waiting on network or disk — means `asyncio` for very high concurrency (thousands of connections, one thread) or `threading` for moderate concurrency with blocking libraries; both work because the GIL is released during waits. CPU-bound — actual computation in Python — needs `multiprocessing`, because the GIL caps pure-Python threads at one core, while separate processes each get their own interpreter and run truly in parallel. Rule of thumb: asyncio for massive I/O, threads for modest I/O, processes for CPU."

## Follow-up trap

**"What exactly is the GIL?"** — The Global Interpreter Lock: a mutex inside CPython that lets only one thread execute Python bytecode at a time. It exists to make CPython's memory management (reference counting) simple and safe. Consequence: threads give concurrency, not parallelism — fine for waiting, useless for computing. NumPy-style libraries dodge it by releasing the GIL inside C extensions; `multiprocessing` dodges it by using separate interpreters. (Also worth knowing: Python 3.13 added an experimental free-threaded build — GIL removal is in progress, but the standard answer above still applies.)

**"Why not just always use multiprocessing?"** — Cost. Each process is a full interpreter (tens of MB of RAM), startup is slow, and data crossing process boundaries must be pickled (serialized) and copied — you can't share a list by reference. For I/O-bound work you pay that overhead to solve a problem threads solve nearly free. Asyncio is even cheaper: thousands of coroutines in one thread, no serialization — but only if every call you make is async-aware.
