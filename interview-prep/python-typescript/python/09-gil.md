# 09 — The GIL: what it is and which workloads it actually blocks

> **Interview question:** "What is the GIL, and when does `threading` actually speed up a Python program?"
> **What the interviewer is really testing:** Whether you know the GIL only blocks **CPU-bound** threads — I/O-bound threads release it while waiting — plus the real workarounds (multiprocessing, C extensions, free-threaded builds).

## Theory — what it is

The **GIL (Global Interpreter Lock)** is a single mutex inside CPython that allows **only one thread to execute Python bytecode at a time** — per process, even on a 32-core machine. Two Python threads literally take turns holding the lock; the interpreter forces a switch roughly every 5 ms (`sys.getswitchinterval`).

Why it exists: CPython's memory model is **reference counting** — every object op mutates a refcount, and doing that safely across threads without a global lock would need fine-grained locking on *every object* — slow, complex, deadlock-prone. The GIL makes refcounting thread-safe for free and massively simplifies the C extension API.

**When the GIL is released:**

- **Blocking I/O** — `socket.recv`, `file.read`, `time.sleep`, DB calls: a thread drops the GIL while it waits, so other threads run. *This is the key to everything below.*
- **C extensions that opt out** — NumPy releases the GIL during heavy array math; `hashlib`, `re`, compression libs too.
- **Periodically** — every ~5 ms so threads take turns (prevents one thread from starving others).

**The consequence:**

- **CPU-bound pure Python** (`sum(range(N))`, JSON crunching, loops) — threads give **no speedup**; bytecode still runs one-at-a-time. Often slightly *slower* from switching overhead.
- **I/O-bound work** (HTTP calls, DB queries, file reads, sleeps) — threads **do help**: while one waits on the network holding no lock, others execute. Waiting overlaps → real speedup.
- One process can never use multiple cores for Python bytecode.

**Workarounds for CPU-bound:** `multiprocessing` / `ProcessPoolExecutor` — each process has its own interpreter *and its own GIL* → true parallelism. Or push work into GIL-releasing native code (NumPy, Cython). `asyncio` is for I/O-bound — one thread, no GIL contention at all. Python **3.13+** ships an experimental **free-threaded build** (PEP 703, `python3.13t`) that runs without the GIL — the beginning of the end for it. PyPy/Jython/IronPython have no GIL either.

## Why it was needed

In 1992, when CPython added threads, the GIL was the pragmatic choice: single-core machines were the norm, thread-safe refcounting via fine-grained locks would have been far slower for the common single-threaded case, and C extensions could assume a simple lock model. The cost — no multi-core CPU parallelism in threads — only became painful as cores multiplied. Removing it is hard precisely because the entire C ecosystem was built assuming it; the 3.13 free-threaded build is the first real attempt at a no-GIL CPython.

## Where it's used in a real project

- **Web servers:** Gunicorn/uWSGI worker *threads* work fine — request handlers spend their lives waiting on DB/network I/O, which releases the GIL.
- **Parallel API calls / scraping:** `ThreadPoolExecutor` over `requests.get` — the canonical I/O-bound win; 10 concurrent calls ≈ 1 call's latency.
- **Data science:** NumPy/pandas release the GIL for vectorized ops — BLAS routines genuinely multithread; but your *pure-Python* loop over rows doesn't.
- **CPU-heavy pipelines:** image/video transforms, compression, ML preprocessing → `ProcessPoolExecutor` or Celery *process* workers — never threads.
- **Mixing badly:** CPU-bound code in threads "parallelizes" nothing — the classic interview gotcha and a real prod bug ("we added threads, it got slower").

## Diagram

```
CPU-bound, 2 threads, 2 cores — GIL serializes:

  GIL:  [==T1==][==T2==][==T1==][==T2==]     only ONE thread runs at a time
  total ≈ same as sequential (sometimes worse: switch overhead)

I/O-bound, 2 threads — waits overlap:

  T1:  [py]==waiting for network==[py]
  T2:        [py]==waiting for net==[py]
  total ≈ HALF of sequential — while T1 waits (GIL released), T2 runs

CPU-bound done right — 2 PROCESSES = 2 GILs = real parallelism:

  proc1: [=========== burn ===========]
  proc2: [=========== burn ===========]     both cores busy
```

## Code — explained

```python
import threading, time

def cpu_burn(n):                 # pure-Python CPU work: holds the GIL
    while n:
        n -= 1

def io_wait():                   # I/O work: releases the GIL while sleeping
    time.sleep(0.3)

N = 30_000_000

# --- CPU-bound ---
t = time.time(); cpu_burn(N); cpu_burn(N)
print("cpu sequential:", round(time.time() - t, 2))   # ~0.6s (machine-dependent)

t = time.time()
ts = [threading.Thread(target=cpu_burn, args=(N,)) for _ in range(2)]
[t.start() for t in ts]; [t.join() for t in ts]
print("cpu threaded:  ", round(time.time() - t, 2))   # ~0.6s — NO speedup!

# --- I/O-bound ---
t = time.time(); io_wait(); io_wait()
print("io sequential: ", round(time.time() - t, 2))   # ~0.6s

t = time.time()
ts = [threading.Thread(target=io_wait) for _ in range(2)]
[t.start() for t in ts]; [t.join() for t in ts]
print("io threaded:   ", round(time.time() - t, 2))   # ~0.3s — waits overlapped
```

1. `cpu_burn` never does I/O — it holds the GIL the whole time except forced ~5 ms handoffs. Two threads take turns; total time ≈ sequential. The GIL is *why* "more threads" can't help here.
2. `io_wait` calls `time.sleep`, which releases the GIL for the entire sleep — both threads' waits run concurrently, halving elapsed time.
3. The asymmetry is the whole lesson: **threading speedup ≈ fraction of time spent in I/O waits**, not CPU work.
4. To truly parallelize `cpu_burn` you need processes — each `multiprocessing` worker gets its own interpreter and its own GIL (see Hard).

## Problems

### Easy — which one threads help?
**Problem:** Two workloads — which gets faster with 4 threads, and why? (a) four `requests.get(url)` calls, (b) four `sum(range(10**7))` computations.
**Try this input:** reason it out, then confirm the rule with a sleep-vs-burn check.
**Expected output:** `io-bound: True` / `cpu-bound: False`
**Solution:**
```python
def speeds_up_with_threads(kind):
    return kind == "io"      # I/O waits release the GIL; CPU work doesn't

print("io-bound:", speeds_up_with_threads("io"))    # True
print("cpu-bound:", speeds_up_with_threads("cpu"))  # False
```
**Logic explained:**
1. `requests.get` spends ~99% of its time blocked on the network — the GIL is released during the wait, so the four calls overlap: ~1× latency total instead of 4×.
2. `sum(range(10**7))` is pure bytecode on the CPU — threads take turns holding the GIL; four of them finish in ~the same 4× time.
3. Rule of thumb: if the work is *waiting*, thread it; if it's *computing*, you need processes.

### Medium — parallel fetch with `ThreadPoolExecutor`
**Problem:** Fetch 4 URLs concurrently with threads. Simulate each fetch with `time.sleep(0.2)` and prove the wall-clock time is ~0.2s, not ~0.8s.
**Try this input:** `urls = ["a", "b", "c", "d"]`
**Expected output:** `['data:a', 'data:b', 'data:c', 'data:d']` and `0.2` elapsed.
**Solution:**
```python
import time
from concurrent.futures import ThreadPoolExecutor

def fetch(url):
    time.sleep(0.2)            # fake network latency — GIL released here
    return f"data:{url}"

urls = ["a", "b", "c", "d"]
t = time.time()
with ThreadPoolExecutor(max_workers=4) as ex:
    results = list(ex.map(fetch, urls))
print(results)                      # ['data:a', 'data:b', 'data:c', 'data:d']
print(round(time.time() - t, 1))    # 0.2 — sequential would be 0.8
```
**Logic explained:**
1. Each `fetch` spends its life inside `time.sleep` — I/O wait → GIL released → all four sleeps run concurrently.
2. `ex.map(fetch, urls)` farms the calls across 4 worker threads; `list(...)` collects in order.
3. Elapsed ≈ one fetch's latency (`0.2`) instead of four (`0.8`) — the signature of I/O-bound threading wins.
4. Swap `time.sleep` for a real `requests.get` and the same speedup holds — that's why threaded HTTP fans out so well.

### Hard — CPU-bound done right: `ProcessPoolExecutor`
**Problem:** `burn(n)` is pure CPU. Show that `ProcessPoolExecutor` — not threads — achieves real parallelism, and return correct results.
**Try this input:** `burn` over `[3, 4]` — `burn(n)` sums `i*i` for `i in range(n)`.
**Expected output:** `[5, 14]` — computed in two separate processes, each with its own GIL.
**Solution:**
```python
from concurrent.futures import ProcessPoolExecutor

def burn(n):
    s = 0
    for i in range(n):
        s += i * i
    return s

if __name__ == "__main__":               # REQUIRED for multiprocessing
    with ProcessPoolExecutor(max_workers=2) as ex:
        print(list(ex.map(burn, [3, 4])))   # [5, 14] — truly parallel
```
**Logic explained:**
1. `burn(3)` = 0+1+4 = `5`; `burn(4)` = 0+1+4+9 = `14` — deterministic results.
2. Each worker is a separate **process** with its own interpreter and its own GIL — two `burn`s genuinely execute on two cores at once.
3. `if __name__ == "__main__"` is mandatory: on `spawn` platforms (macOS/Windows) workers re-import the module — without the guard they'd re-run the pool creation and recurse forever. Always include it.
4. The trade-offs: arguments/results are **pickled** across process boundaries (overhead; must be picklable), processes cost more memory than threads, and shared state needs explicit IPC — processes buy parallelism at the price of isolation.

## The 30-second interview answer

"The GIL is a single lock in CPython that lets only one thread execute Python bytecode at a time per process. It exists to keep reference-counted memory management thread-safe without locking every object. The practical rule: **threads can't speed up CPU-bound Python** — bytecode still serializes — but they **do speed up I/O-bound work**, because threads release the GIL while blocked on network, disk, or sleep, so waits overlap. C extensions like NumPy can also release it. For real CPU parallelism I use `ProcessPoolExecutor` — separate processes, separate GILs — or `asyncio` for massive I/O concurrency in one thread. Python 3.13 added an experimental free-threaded build that removes the GIL entirely."

## Follow-up trap

**"So threads are useless in Python?"** — no, that's the trap answer. Threads are the *right* tool for I/O-bound concurrency: the GIL is dropped during every blocking call, so 50 threads hitting APIs run ~50× faster than sequentially. Also expect: *"Does NumPy multithread?"* — yes, its C kernels release the GIL (and BLAS uses native threads), which is why `numpy` ops scale while `for` loops over rows don't. *"Does asyncio dodge the GIL?"* — it's single-threaded, so the GIL is never contended; it wins on connection count, not CPU. *"Will removing the GIL break anything?"* — the 3.13 free-threaded build trades some single-thread performance (~few % slower) and requires C extensions to opt in — that's the real cost discussion.
