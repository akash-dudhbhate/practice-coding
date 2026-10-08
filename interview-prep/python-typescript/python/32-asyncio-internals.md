# 32 — asyncio internals

> **Interview question:** "How does asyncio work under the hood?"
> **What the interviewer is really testing:** Do you understand the event loop, coroutine suspension at `await`, and that asyncio is *cooperative* — code must voluntarily yield control?

## Theory — what it is

The **event loop** is a single thread running a scheduler. It keeps a queue of "tasks ready to run" and a set of "tasks waiting on something" (a timer, a socket). Each iteration: run every ready task until it pauses, then wait for the next thing to become ready (a timer expiring, network data arriving), wake those tasks, repeat. One thread, many tasks — like a chef juggling dishes: never idle while any dish can be worked on.

A **coroutine** is the object produced by calling an `async def` function — a suspended computation. Under the hood it's built on the same machinery as a **generator**: `await x` compiles to roughly "yield control back to the loop, and when `x` is done, resume me right here with the result." The coroutine object remembers exactly where it paused — local variables and all — so it can continue later.

A **Task** wraps a coroutine and registers it with the event loop so it gets scheduled. `await coroutine` = "pause me until this finishes, then give me its return value." `asyncio.create_task(coro)` = "schedule this to run concurrently, don't wait." `asyncio.gather` = "schedule all of these and wait for all results." The whole system is **cooperative**: nothing preempts a coroutine — it runs until it hits `await` (or returns). That's why a blocking call like `time.sleep()` inside a coroutine freezes *every* task.

## Why it was needed

Threads solve I/O concurrency but cost ~8 MB of stack each and the OS preemptively switches them — thousands of threads thrash the CPU. A server handling 50,000 mostly-idle connections (chat, websockets) can't afford a thread per connection.

Asyncio instead multiplexes everything on one thread: the waits are handled by the OS kernel's notification systems (`epoll`/`kqueue`/`IOCP`) which can watch thousands of sockets at once and report "socket #4123 has data." Coroutines in memory are tiny (~KB). The tradeoff: concurrency only happens at explicit `await` points, and every library you call must be async-aware — a blocking `requests.get()` stalls the whole loop.

## Where it's used in a real project

- **Async web frameworks**: FastAPI, Starlette, aiohttp — one event loop handles thousands of concurrent HTTP requests.
- **High-fan-out clients**: hitting 500 microservice endpoints "at once" with `asyncio.gather`.
- **Websocket/streaming services**: many long-lived, mostly-idle connections.
- **Pipelines with backpressure**: `asyncio.Queue` connecting producer/consumer coroutines; `asyncio.Semaphore` capping concurrency.

## Diagram

```
            +------------------ EVENT LOOP (1 thread) ------------------+
            |                                                          |
 ready -->  |   run A ──> A hits await ──┐                             |
 queue      |   run B ──> B hits await ──┼──> tasks go to "waiting"    |
            |   run C ──> C hits await ──┘    (timer / socket)         |
            |                                                          |
            |   loop waits on epoll: "who's ready?"                    |
            |        ^                                                 |
            +--------|-------------------------------------------------+
                     |
        kernel: "socket 2 has data" / "timer fired"
                     |
            task moves back to READY queue --> runs from its await point
```

## Code — explained

```python
import asyncio

async def worker(name, delay):                   # 1
    print(f"{name} start")
    await asyncio.sleep(delay)                   # 2
    print(f"{name} end")
    return name

async def main():
    t1 = asyncio.create_task(worker("A", 0.02))  # 3
    t2 = asyncio.create_task(worker("B", 0.01))  # 4
    print(await t1)                              # 5
    print(await t2)

asyncio.run(main())                              # 6
```

Output:
```
A start
B start
B end
B
A end
A
```

1. `worker` is a coroutine function; calling it builds a coroutine object — nothing runs yet.
2. `await asyncio.sleep(delay)` — registers a timer with the loop and *suspends* `worker` here. Control returns to the loop, which runs whatever else is ready.
3. `create_task` wraps the coroutine in a Task and schedules it — A starts running immediately (prints `A start`), hits `await`, suspends.
4. Same for B. B's timer (0.01s) fires first.
5. `await t1` — main suspends until task A finishes, then receives its return value `"A"`. B already finished, so `await t2` returns instantly.
6. `asyncio.run` creates the event loop, schedules `main()`, runs until it's done, then closes the loop.

## Problems

### Easy — run one coroutine
**Problem:** Write an async function that prints a greeting and returns 42; run it with `asyncio.run` and print the return value.
**Try this input:** run the script
**Expected output:**
```
hi from coroutine
returned: 42
```
**Solution:**
```python
import asyncio

async def say_hi():
    print("hi from coroutine")
    return 42

result = asyncio.run(say_hi())
print("returned:", result)
```
**Logic explained:**
1. `say_hi()` creates a coroutine object — the body hasn't run yet.
2. `asyncio.run` spins up the event loop, schedules the coroutine, runs it to completion, and returns its result.
3. `print` inside the coroutine happens while the loop drives it; the `42` comes back through `run`.

### Medium — watch tasks interleave
**Problem:** Launch two countdowns concurrently. `X` counts 3→1 with a 0.01s pause between numbers; `Y` counts 2→1 with a 0.03s pause. Show the interleaved output that proves neither blocks the other.
**Try this input:** `countdown("X", 3, 0.01)` and `countdown("Y", 2, 0.03)` via `gather`
**Expected output:**
```
X 3
Y 2
X 2
X 1
Y 1
```
**Solution:**
```python
import asyncio

async def countdown(name, n, delay):
    for i in range(n, 0, -1):
        print(name, i)
        await asyncio.sleep(delay)     # yield control each iteration

async def main():
    await asyncio.gather(countdown("X", 3, 0.01),
                         countdown("Y", 2, 0.03))

asyncio.run(main())
```
**Logic explained:**
1. `gather` schedules both coroutines; X runs first, prints `X 3`, then suspends on `sleep`.
2. The loop immediately starts Y: `Y 2`, then Y suspends for 0.03s.
3. X's 0.01s timer fires first → `X 2`, suspends again; fires again → `X 1`, returns.
4. Y's timer finally fires → `Y 1`. The interleaving proves both made progress during each other's waits — that's the event loop doing its job.

### Hard — cap concurrency with a semaphore
**Problem:** You must run 4 jobs through a resource that allows only 2 at a time (e.g. an API with a connection limit). Use `asyncio.Semaphore(2)` so at most 2 jobs run concurrently.
**Try this input:** `job(i)` for `i in range(4)`
**Expected output:**
```
start 0
start 1
end 0
end 1
start 2
start 3
end 2
end 3
```
**Solution:**
```python
import asyncio

async def job(i, sem):
    async with sem:                    # at most 2 holders at once
        print("start", i)
        await asyncio.sleep(0.01)      # the "work"
        print("end", i)

async def main():
    sem = asyncio.Semaphore(2)
    await asyncio.gather(*(job(i, sem) for i in range(4)))

asyncio.run(main())
```
**Logic explained:**
1. `asyncio.Semaphore(2)` is a counter: `async with` acquires a slot if available, otherwise the coroutine *suspends* until another task releases one.
2. Jobs 0 and 1 acquire the two slots, print `start`, and suspend on `sleep`. Jobs 2 and 3 are stuck inside `async with` — waiting, not running.
3. Jobs 0 and 1's timers fire: `end 0`, `end 1`; each releases its slot.
4. Jobs 2 and 3 wake, print `start`/`end` in turn. Max concurrency was exactly 2 — this is how you rate-limit async work without threads.

## The 30-second interview answer

"Asyncio is single-threaded cooperative multitasking. The event loop keeps a queue of ready tasks and a set of tasks waiting on timers or sockets, watched via the OS's `epoll`/`kqueue`. Each task runs until it hits `await`, which suspends it — the coroutine object remembers where it paused — and the loop runs the next ready task. `create_task` schedules work concurrently; `gather` waits for a group. The catch: nothing preempts a coroutine, so one blocking call like `time.sleep` or `requests.get` freezes every task on the loop."

## Follow-up trap

**"What happens if you call `time.sleep()` inside a coroutine?"** — The whole event loop freezes for that duration. `time.sleep` never yields to the loop — it just blocks the one thread. Every other task's timers and sockets wait. The fix: `await asyncio.sleep()` for delays, `asyncio.to_thread(blocking_fn)` for blocking library calls you can't avoid.

**"`await` vs `create_task` — what's the difference?"** — `await coro` runs it and *pauses you* until it finishes (sequential, you wait). `create_task(coro)` schedules it on the loop and returns immediately with a Task handle (concurrent, it runs while you continue) — then you `await task` later to collect the result. `await` = "do this now, I'll wait"; `create_task` = "start this, I'll check back." Forgetting `create_task` is the #1 reason "async" code runs sequentially.
