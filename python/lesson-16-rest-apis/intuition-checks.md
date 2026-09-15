# Lesson 16 — Intuition Checks

## Check 01: async/await
```python
async def foo():
    return 42

print(type(foo()))
```
<details><summary>Answer</summary>
`<class 'coroutine'>` — calling an async function returns a coroutine, not the result. Must await it.
</details>

## Check 02: asyncio.run
```python
async def main():
    return "hello"

print(asyncio.run(main()))
```
<details><summary>Answer</summary>
`hello` — `asyncio.run` executes the coroutine and returns the result. This is the entry point for async code.
</details>

## Check 03: Concurrent vs Sequential
```python
async def task(n):
    await asyncio.sleep(1)
    return n

# A:
await task(1); await task(2)  # 2 seconds total

# B:
await asyncio.gather(task(1), task(2))  # 1 second total
```
<details><summary>Answer</summary>
A takes 2 seconds (sequential). B takes 1 second (concurrent). `gather` runs tasks in parallel.
</details>

## Check 04: create_task
```python
async def main():
    t = asyncio.create_task(asyncio.sleep(1))
    # do other work
    await t
```
<details><summary>Answer</summary>
`create_task` schedules the coroutine to run concurrently. You can do other work while it runs, then await it when you need the result.
</details>

## Check 05: Cancellation
```python
async def main():
    task = asyncio.create_task(asyncio.sleep(10))
    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        print("cancelled")
```
<details><summary>Answer</summary>
Prints "cancelled" — `cancel()` raises `CancelledError` in the task.
</details>
