# Lesson 16 — Debug Exercises

## Debug 01 (Easy): Missing await
```python
async def fetch_data():
    await asyncio.sleep(1)
    return "data"

result = fetch_data()
print(result)
```
<details><summary>Answer</summary>
**Bug:** `fetch_data()` returns a coroutine, not the result. Need to await it.
**Fix:** `result = await fetch_data()` inside an async function, or `asyncio.run(fetch_data())`.
</details>

## Debug 02 (Medium): Blocking in async
```python
async def process():
    time.sleep(5)  # blocks the event loop!
    return "done"
```
<details><summary>Answer</summary>
**Bug:** `time.sleep()` blocks the entire event loop. Other tasks can't run.
**Fix:** `await asyncio.sleep(5)`.
</details>

## Debug 03 (Hard): gather vs wait
```python
async def main():
    results = await asyncio.wait([task1(), task2()])
    print(results)
```
<details><summary>Answer</summary>
**Bug:** `asyncio.wait` returns `(done, pending)` sets, not results. Need to iterate done set.
**Fix:** `results = await asyncio.gather(task1(), task2())` — returns list of results directly.
</details>
