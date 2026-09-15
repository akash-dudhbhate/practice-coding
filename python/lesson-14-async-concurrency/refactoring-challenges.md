# Lesson 14 — Refactoring Challenges

## Refactor 01 (Easy): Sequential Async
### Before
```python
async def main():
    a = await fetch("a")
    b = await fetch("b")
    return a + b
```
### After
```python
async def main():
    a, b = await asyncio.gather(fetch("a"), fetch("b"))
    return a + b
```

## Refactor 02 (Medium): Blocking in Async
### Before
```python
async def process():
    time.sleep(5)  # blocks event loop
```
### After
```python
async def process():
    await asyncio.sleep(5)
```

## Refactor 03 (Hard): Callback Hell to Async/Await
### Before
```python
def fetch_all(callback):
    fetch("a", lambda a: fetch("b", lambda b: callback(a + b)))
```
### After
```python
async def fetch_all():
    a = await fetch("a")
    b = await fetch("b")
    return a + b
```
