# lesson-16-rest-apis — Extra Practice
Everything beyond the core lesson lives here, in order:
mental quizzes → debug drills → mistakes → refactoring → comparisons.

---

## Intuition Checks — predict before you run

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

---

## Debug Exercises — find and fix the bug

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

---

## Common Mistakes — the traps learners hit

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

---

## Refactoring Challenges — make working code better

## Refactor 01 (Easy): No Status Code Check
### Before
```python
data = requests.get(url).json()
```
### After
```python
res = requests.get(url)
res.raise_for_status()
data = res.json()
```

## Refactor 02 (Medium): Repeated Route Definitions
### Before
```python
@app.get("/users")
def list_users(): return users_db.all()
@app.get("/posts")
def list_posts(): return posts_db.all()
```
### After
```python
def create_crud_routes(app, path, db):
    @app.get(f"/{path}")
    def list_all(): return db.all()

create_crud_routes(app, "users", users_db)
create_crud_routes(app, "posts", posts_db)
```

## Refactor 03 (Hard): No Schema Validation
### Before
```python
@app.post("/users")
def create_user():
    data = request.json
    # no validation — crashes on bad data
    return db.insert(data)
```
### After
```python
from pydantic import BaseModel
class UserCreate(BaseModel):
    name: str
    email: str
    age: int = 0

@app.post("/users")
def create_user():
    user = UserCreate(**request.json)
    return db.insert(user.dict())
```

---

## Approach Comparison — different ways to solve it

## Problem: Fetch Multiple URLs

### Approach 1: Sequential
```python
results = []
for url in urls:
    results.append(await fetch(url))
```
**Cons:** O(n) time — each request waits for the previous.

### Approach 2: gather
```python
results = await asyncio.gather(*[fetch(url) for url in urls])
```
**Pros:** O(1) time (all concurrent). **Cons:** All must complete before any result.

### Approach 3: as_completed
```python
for coro in asyncio.as_completed([fetch(url) for url in urls]):
    result = await coro
    process(result)
```
**Pros:** Process results as they arrive. **Cons:** More complex.

**Winner:** Approach 2 (gather) for most cases. Approach 3 when you need results ASAP.
