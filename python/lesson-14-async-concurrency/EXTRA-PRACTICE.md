# lesson-14-async-concurrency — Extra Practice
Everything beyond the core lesson lives here, in order:
mental quizzes → debug drills → mistakes → refactoring → comparisons.

---

## Intuition Checks — predict before you run

## Check 01: map vs comprehension
```python
# Which is more Pythonic?
list(map(str, [1, 2, 3]))           # A
[str(x) for x in [1, 2, 3]]        # B
```
<details><summary>Answer</summary>
**B** — list comprehensions are generally preferred in Python. More readable.
</details>

## Check 02: filter
```python
result = filter(lambda x: x > 2, [1, 2, 3, 4])
print(list(result))
```
<details><summary>Answer</summary>
`[3, 4]` — keeps elements where the function returns True.
</details>

## Check 03: reduce
```python
from functools import reduce
result = reduce(lambda a, b: a * b, [1, 2, 3, 4])
print(result)
```
<details><summary>Answer</summary>
`24` — `((1 * 2) * 3) * 4`. reduce applies function cumulatively.
</details>

## Check 04: partial
```python
from functools import partial
double = partial(lambda x, y: x * y, 2)
print(double(5))
```
<details><summary>Answer</summary>
`10` — `partial` fixes the first argument. `double(5)` = `lambda(2, 5)` = 10.
</details>

## Check 05: any/all
```python
print(any([False, 0, "", None]))
print(all([True, 1, "a"]))
```
<details><summary>Answer</summary>
`False`, `True` — `any` returns True if ANY element is truthy. `all` returns True if ALL elements are truthy.
</details>

---

## Debug Exercises — find and fix the bug

## Debug 01 (Easy): map Returns Iterator
```python
result = map(str, [1, 2, 3])
print(result[0])
```
<details><summary>Answer</summary>
**Bug:** `map` returns an iterator, not a list. Can't index.
**Fix:** `list(map(str, [1, 2, 3]))[0]`.
</details>

## Debug 02 (Medium): filter with None
```python
result = filter(None, [0, 1, 2, "", "a", None])
print(list(result))
```
<details><summary>Answer</summary>
`[1, 2, 'a']` — `filter(None, ...)` removes all falsy values (0, "", None, False, []).
</details>

## Debug 03 (Hard): reduce Missing Import
```python
result = reduce(lambda a, b: a + b, [1, 2, 3])
```
<details><summary>Answer</summary>
**Bug:** `reduce` is not a builtin in Python 3. Need `from functools import reduce`.
</details>

---

## Common Mistakes — the traps learners hit

## Mistake 01: Using map/filter when comprehension is clearer
```python
# LESS READABLE
list(map(lambda x: x * 2, filter(lambda x: x > 0, nums)))

# MORE READABLE
[x * 2 for x in nums if x > 0]
```

## Mistake 02: Forgetting reduce import
```python
# WRONG
reduce(...)  # NameError

# CORRECT
from functools import reduce
```

## Mistake 03: Not using partial for configuration
```python
# VERBOSE
def make_greeter(greeting, name):
    return f"{greeting}, {name}!"
hello = lambda name: make_greeter("Hello", name)

# BETTER
from functools import partial
hello = partial(make_greeter, "Hello")
```

## Mistake 04: Side effects in map
```python
# WRONG — map is for transformation, not side effects
list(map(print, [1, 2, 3]))  # prints AND returns [None, None, None]

# CORRECT
for x in [1, 2, 3]:
    print(x)
```

## Mistake 05: Confusing any/all with OR/AND
```python
# WRONG
if any(x for x in items):  # works but redundant
# SIMPLER
if items:  # truthy if non-empty
```

---

## Refactoring Challenges — make working code better

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

---

## Approach Comparison — different ways to solve it

## Problem: Double Positive Numbers

### Approach 1: map + filter
```python
result = list(map(lambda x: x * 2, filter(lambda x: x > 0, nums)))
```

### Approach 2: List comprehension
```python
result = [x * 2 for x in nums if x > 0]
```

### Approach 3: Generator + list
```python
result = list(x * 2 for x in nums if x > 0)
```

**Winner:** Approach 2 — most readable, most Pythonic.

---

## Problem: Product of List

### Approach 1: reduce
```python
from functools import reduce
product = reduce(lambda a, b: a * b, nums)
```

### Approach 2: Loop
```python
product = 1
for n in nums:
    product *= n
```

### Approach 3: math.prod (Python 3.8+)
```python
import math
product = math.prod(nums)
```

**Winner:** Approach 3 — built-in, tested, clear.
