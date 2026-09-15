# Lesson 16 — Common Mistakes

## Mistake 01: Missing await
```python
# WRONG — returns coroutine, not result
data = fetch_data()

# CORRECT
data = await fetch_data()
```

## Mistake 02: Blocking calls in async
```python
# WRONG — blocks event loop
async def process():
    time.sleep(5)
    requests.get(url)

# CORRECT — use async versions
async def process():
    await asyncio.sleep(5)
    await aiohttp.get(url)
```

## Mistake 03: Not using gather
```python
# SLOW — sequential
result1 = await task1()
result2 = await task2()

# FAST — concurrent
result1, result2 = await asyncio.gather(task1(), task2())
```

## Mistake 04: Forgetting asyncio.run
```python
# WRONG — coroutine never runs
async def main(): ...
main()

# CORRECT
asyncio.run(main())
```

## Mistake 05: Mixing sync and async
```python
# WRONG — can't await in sync function
def fetch():
    data = await async_func()  # SyntaxError

# CORRECT
async def fetch():
    data = await async_func()
```
