# 33 — What `async def` actually changes

> **Interview question:** "What happens when you put `async` in front of a `def`? What does calling the function return?"
> **What the interviewer is really testing:** Whether you understand that `async def` creates a *coroutine function* — calling it does NOT run the body, it returns a coroutine object that must be awaited — versus thinking `async` means "runs in the background" or "runs in a thread."

## Theory — what it is

`async def` defines a **coroutine function**. The moment you add `async`, calling the function stops executing the body immediately — instead, it returns a **coroutine object**: an inert bundle containing the code and arguments, waiting to be driven. The body runs only when something *awaits* it — either the `await` keyword inside another coroutine, or an event loop like `asyncio.run()`.

`await` means: "run this coroutine now; while it's paused on I/O, let the event loop run something else; when it finishes, give me its return value." Without `await`, you have an object, not a result — like holding a recipe instead of cooking it.

This is the core misconception the question targets: **`async` does not make code run in parallel, in a thread, or "in the background."** It only marks the function as *pausable*. Real concurrency comes from the **event loop** — one thread that juggles many coroutines, switching between them whenever one hits `await` on something slow (network, disk, sleep).

"Jargon" decoded: **event loop** = the scheduler that runs coroutines one at a time and switches at each `await`. **Coroutine object** = the paused, not-yet-running function. **Blocking** = occupying the thread while doing nothing useful (e.g., `time.sleep`).

## Why it was needed

Classical concurrency has costs Python wanted to avoid:

1. **Threads**: the OS decides when to switch — code can be interrupted *between any two bytecode instructions*, so shared state needs locks everywhere. Plus the GIL means threads don't speed up CPU work anyway, and each thread costs ~8MB of stack.
2. **Callbacks** (old-style async): "call this function when the data arrives" — logic scatters across tiny functions, error handling becomes nightmare spaghetti.

Coroutines flip the model: switching happens *only* at `await`, which is visible in the code — you can see exactly where your function might pause, so shared state is safer between awaits. And the code reads top-to-bottom like normal sync code instead of being chopped into callbacks. One thread, thousands of concurrent I/O operations, no locks needed between `await` points.

## Where it's used in a real project

- **Web servers**: FastAPI/Starlette endpoints are `async def` — one worker handles thousands of waiting connections.
- **DB/HTTP clients**: `asyncpg`, `aiohttp`, `httpx.AsyncClient` — fire off many requests, await each as data arrives.
- **Gathering I/O**: `asyncio.gather(fetch_a(), fetch_b(), fetch_c())` runs three requests concurrently in one thread.
- **Anywhere I/O waits**: message queues, websockets, subprocess pipes — anywhere the program would otherwise sit idle.

## Diagram

```
def f():            async def g():
    return 1            return 1

f()          ->  1      g()   ->  <coroutine object>   <- NOTHING ran!
                              |
                        await g()  OR  asyncio.run(g())
                              |
                              v
                             1    <- NOW the body executed

Event loop juggling 3 coroutines (one thread):

time ->  ──────────────────────────────────────────
coro A   [work] await io......[work] await io..[done]
coro B           [work] await io........[work]  [done]
coro C                [work] await io.....[work][done]
         ^ only ONE is running at any instant,
           but none sit idle during I/O waits
```

## Code — explained

```python
import asyncio

async def fetch_user(uid):                          # 1
    print(f"start fetch {uid}")                     # 2
    await asyncio.sleep(1)                          # 3
    return {"id": uid}


coro = fetch_user(7)                                # 4
print(coro)                                         # 5

async def main():
    result = await fetch_user(7)                    # 6
    print("got:", result)

asyncio.run(main())                                 # 7
```

Output:

```
<coroutine object fetch_user at 0x...>
start fetch 7
got: {'id': 7}
```

1. `async def` — defines a coroutine function. The `async` keyword is what changes the call semantics.
2. This print does NOT happen when the function is called — proof the body doesn't run yet.
3. `await asyncio.sleep(1)` — a *non-blocking* sleep: the coroutine pauses here and the event loop may run other coroutines meanwhile. (`time.sleep(1)` would freeze the whole loop — the classic async bug.)
4. `fetch_user(7)` returns a **coroutine object** — the body has not executed. Nothing printed yet.
5. Confirms it: prints `<coroutine object ...>`, not the dict.
6. Inside another coroutine, `await` actually drives it — body runs, prints `start fetch 7`, returns the dict.
7. `asyncio.run` creates the event loop, drives `main()` to completion, closes the loop — the standard entry point for async code.

## Problems

### Easy — the coroutine object trap
**Problem:** A junior dev wrote this and wonders why it prints an object instead of `"done"`. Fix it so it actually runs.
```python
import asyncio

async def job():
    print("done")

result = job()
print(result)
```
**Try this input:** run the script
**Expected output:** `done`
**Solution:**
```python
import asyncio

async def job():
    print("done")

asyncio.run(job())
```
**Logic explained:**
1. `job()` returns a coroutine object — the `print("done")` body never executes.
2. `asyncio.run(job())` hands the coroutine to an event loop, which drives it to completion.
3. Output is `done` — and the useless `result` variable is gone.

### Medium — sequential vs. concurrent
**Problem:** Each `fetch` awaits `asyncio.sleep(1)`. Version A awaits them one by one (~2s total); rewrite as version B using `asyncio.gather` so they run concurrently (~1s total). Print the results list.
**Try this input:** `fetch("a")`, `fetch("b")`
**Expected output:**
```
start a
start b
['a!', 'b!']
```
**Solution:**
```python
import asyncio

async def fetch(name):
    print("start", name)
    await asyncio.sleep(1)
    return name + "!"

async def main():
    results = await asyncio.gather(fetch("a"), fetch("b"))
    print(results)

asyncio.run(main())
```
**Logic explained:**
1. `fetch("a")` and `fetch("b")` each produce coroutine objects — `gather` schedules both on the loop.
2. Both print `start` immediately, then both hit `await asyncio.sleep(1)` and pause — during the pause each lets the other proceed, so the two sleeps *overlap*: ~1s total, not ~2s.
3. `gather` returns the results in argument order: `['a!', 'b!']`.
4. Sequential version `r1 = await fetch("a"); r2 = await fetch("b")` would take ~2s — `await` alone doesn't create concurrency; the loop needs multiple coroutines in flight.

### Hard — blocking the loop
**Problem:** This looks async but takes ~3s and the tasks interleave badly — find the bug and fix it so total time is ~1s and prints interleave.
```python
import asyncio, time

async def tick(name):
    for i in range(3):
        print(name, i)
        time.sleep(1)          # BUG

async def main():
    await asyncio.gather(tick("A"), tick("B"))
```
**Try this input:** run `main()`
**Expected output:**
```
A 0
B 0
A 1
B 1
A 2
B 2
```
**Solution:**
```python
import asyncio

async def tick(name):
    for i in range(3):
        print(name, i)
        await asyncio.sleep(1)      # non-blocking: yields to the loop

async def main():
    await asyncio.gather(tick("A"), tick("B"))

asyncio.run(main())
```
**Logic explained:**
1. `time.sleep(1)` is a **blocking** call — it freezes the whole thread. Coroutine A prints `A 0`, then sleeps a full second *holding the loop hostage*; B can't run. Total ≈ 6 blocking sleeps serialized.
2. `await asyncio.sleep(1)` pauses the coroutine and returns control to the event loop — B gets to run while A "sleeps."
3. With the fix, each iteration both coroutines print then pause together → interleaved output, ~3s total for the loop of 3 (each round overlaps the two 1s sleeps into one).
4. Rule: inside `async def`, only ever call *awaitable* I/O — `asyncio.sleep`, `aiohttp`, `asyncpg`. Any blocking call (`time.sleep`, `requests.get`, `open().read()` on slow disks) stalls every coroutine.

## The 30-second interview answer

"`async def` turns a function into a coroutine function — calling it does NOT run the body, it returns a coroutine object. The body only executes when the coroutine is awaited, either with `await` inside another coroutine or via `asyncio.run` which starts an event loop. `async` doesn't make anything parallel or threaded by itself — it just marks where the function may pause. Real concurrency comes from the event loop juggling many coroutines in one thread, switching at each `await`. The trap to avoid: calling a blocking function like `time.sleep` inside a coroutine freezes the entire loop — you must use awaitable equivalents like `asyncio.sleep`."

## Follow-up trap

**"So `await` makes it concurrent?"** — No. `await a(); await b()` runs them strictly one after another. Concurrency needs multiple coroutines scheduled on the loop at once — `asyncio.gather`, `asyncio.create_task`, or `TaskGroup`. `await` is just "run this and give me the result"; the overlap comes from the loop having other work queued.

**"What happens if you call a coroutine and never await it?"** — You get the object, the body never runs, and at shutdown Python warns `RuntimeWarning: coroutine 'x' was never awaited` — a classic source of "my async code silently did nothing" bugs.
