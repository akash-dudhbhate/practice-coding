# lesson-19-fastapi-server — Extra Practice
Everything beyond the core lesson lives here, in order:
mental quizzes → debug drills → mistakes → refactoring → comparisons.

---

## Intuition Checks — predict before you run

## Check 01: Array vs List
```python
a = np.array([1, 2, 3])
b = [1, 2, 3]
print(a * 2)
print(b * 2)
```
<details><summary>Answer</summary>
```
[2 4 6]
[1, 2, 3, 1, 2, 3]
```
Array does element-wise multiplication. List repeats.
</details>

## Check 02: Shape
```python
a = np.array([[1, 2], [3, 4]])
print(a.shape)
print(a.ndim)
```
<details><summary>Answer</summary>
`(2, 2)`, `2` — shape is dimensions, ndim is number of dimensions.
</details>

## Check 03: Broadcasting
```python
a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([10, 20, 30])
print(a + b)
```
<details><summary>Answer</summary>
```
[[11 22 33]
 [14 25 36]]
```
b is broadcast across rows.
</details>

## Check 04: Random Seed
```python
np.random.seed(42)
a = np.random.rand(3)
np.random.seed(42)
b = np.random.rand(3)
print(np.array_equal(a, b))
```
<details><summary>Answer</summary>
`True` — setting the same seed produces the same "random" numbers. Essential for reproducibility.
</details>

## Check 05: Vectorized vs Loop
```python
# Which is faster for sum of squares?
# A: sum(x**2 for x in arr)
# B: np.sum(arr ** 2)
```
<details><summary>Answer</summary>
**B** — numpy vectorized operations are 100x+ faster than Python loops for large arrays.
</details>

---

## Debug Exercises — find and fix the bug

## Debug 01 (Easy): Array Creation
```python
arr = np.array([1, 2, 3], dtype=float)
arr[0] = "hello"
```
<details><summary>Answer</summary>
**Bug:** Can't put a string in a float array — ValueError.
**Fix:** Use object dtype or keep numeric.
</details>

## Debug 02 (Medium): Broadcasting Error
```python
a = np.array([[1, 2], [3, 4]])
b = np.array([1, 2, 3])
print(a + b)
```
<details><summary>Answer</summary>
**Bug:** Shapes (2,2) and (3,) don't broadcast. ValueError.
**Fix:** Reshape b to (2,) or (2,1) depending on intent.
</details>

## Debug 03 (Hard): Copy vs View
```python
a = np.array([1, 2, 3])
b = a[:2]
b[0] = 99
print(a)
```
<details><summary>Answer</summary>
**Bug:** `b = a[:2]` is a VIEW, not a copy. Modifying b modifies a. `a` becomes `[99, 2, 3]`.
**Fix:** `b = a[:2].copy()`.
</details>

---

## Common Mistakes — the traps learners hit

## Mistake 01: View vs Copy confusion
```python
# WRONG — modifies original
b = a[:5]
b[0] = 99  # a[0] is now 99!

# CORRECT
b = a[:5].copy()
```

## Mistake 02: Python loops on numpy arrays
```python
# SLOW
total = 0
for x in arr:
    total += x ** 2

# FAST
total = np.sum(arr ** 2)
```

## Mistake 03: Wrong dtype
```python
# WRONG — integer division
arr = np.array([1, 2, 3])
print(arr / 2)  # works in py3, but...
arr_int = np.array([1, 2, 3], dtype=int)
print(arr_int / 2)  # float in py3, but truncates in py2

# BE EXPLICIT
arr = np.array([1, 2, 3], dtype=float)
```

## Mistake 04: Not setting random seed
```python
# NON-REPRODUCIBLE
results = np.random.rand(100)

# REPRODUCIBLE
np.random.seed(42)
results = np.random.rand(100)
```

## Mistake 05: Creating array in loop
```python
# SLOW — grows array each time
arr = np.array([])
for i in range(1000):
    arr = np.append(arr, i)

# FAST — preallocate
arr = np.zeros(1000)
for i in range(1000):
    arr[i] = i
```

---

## Refactoring Challenges — make working code better

## Refactor 01 (Easy): No Type Hints
### Before
```python
@app.get("/users/{id}")
def get_user(id):
    user = db.get(id)
    return user
```
### After
```python
@app.get("/users/{id}")
def get_user(id: int) -> dict:
    user = db.get(id)
    return user
```

## Refactor 02 (Medium): No Pydantic Model
### Before
```python
@app.post("/users")
def create_user(user: dict):
    db.insert(user)
```
### After
```python
class UserCreate(BaseModel):
    name: str
    email: str

@app.post("/users")
def create_user(user: UserCreate):
    db.insert(user.dict())
```

## Refactor 03 (Hard): Sync in Async Route
### Before
```python
@app.get("/data")
async def get_data():
    data = requests.get(url).json()  # blocking!
    return data
```
### After
```python
import httpx
@app.get("/data")
async def get_data():
    async with httpx.AsyncClient() as client:
        data = (await client.get(url)).json()
    return data
```

---

## Approach Comparison — different ways to solve it

## Problem: Sum of Squares

### Approach 1: Loop
```python
total = sum(x ** 2 for x in arr)
```
**Cons:** O(n) Python overhead.

### Approach 2: Vectorized
```python
total = np.sum(arr ** 2)
```
**Pros:** 100x faster for large arrays.

### Approach 3: Dot product
```python
total = arr @ arr  # or np.dot(arr, arr)
```
**Pros:** Even faster, mathematically elegant.

**Winner:** Approach 3 for sum of squares. Approach 2 for general operations.

---

## Problem: Matrix Operations

### Approach 1: Nested loops
```python
result = np.zeros((n, m))
for i in range(n):
    for j in range(m):
        result[i, j] = a[i] * b[j]
```

### Approach 2: Outer product
```python
result = np.outer(a, b)
```

**Winner:** Approach 2 — one line, 1000x faster.
