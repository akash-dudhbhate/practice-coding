# lesson-12-decorators — Extra Practice
Everything beyond the core lesson lives here, in order:
mental quizzes → debug drills → mistakes → refactoring → comparisons.

---

## Intuition Checks — predict before you run

## Check 01: Decorator Execution
```python
def deco(func):
    print("decorating")
    def wrapper():
        print("calling")
        func()
    return wrapper

@deco
def hello(): print("hello")

print("defined")
hello()
```
<details><summary>Answer</summary>
```
decorating
defined
calling
hello
```
"decorating" runs at definition time (when @deco is applied). "calling" and "hello" run when called.
</details>

## Check 02: Context Manager
```python
class CM:
    def __enter__(self):
        print("enter")
        return self
    def __exit__(self, *args):
        print("exit")

with CM() as cm:
    print("body")
```
<details><summary>Answer</summary>
```
enter
body
exit
```
</details>

## Check 03: Exception in Context Manager
```python
class CM:
    def __enter__(self): return self
    def __exit__(self, *args):
        print("exit")
        return True

with CM():
    raise ValueError("oops")
print("after")
```
<details><summary>Answer</summary>
```
exit
after
```
`__exit__` returning True SUPPRESSES the exception. If it returns False/None, the exception propagates.
</details>

## Check 04: contextlib
```python
from contextlib import contextmanager
@contextmanager
def cm():
    print("setup")
    yield
    print("teardown")

with cm():
    print("body")
```
<details><summary>Answer</summary>
```
setup
body
teardown
```
</details>

## Check 05: Stacked Decorators
```python
@decorator_a
@decorator_b
def func(): pass
```
Which applies first?
<details><summary>Answer</summary>
`decorator_b` applies first (closest to function), then `decorator_a`. Equivalent to `func = decorator_a(decorator_b(func))`.
</details>

---

## Debug Exercises — find and fix the bug

## Debug 01 (Easy): Decorator Missing @wraps
```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def greet(name):
    "Greets someone"
    return f"Hello, {name}"

print(greet.__name__)
```
<details><summary>Answer</summary>
**Bug:** `greet.__name__` is `"wrapper"`, not `"greet"`. Metadata is lost.
**Fix:** `from functools import wraps` and add `@wraps(func)` to wrapper.
</details>

## Debug 02 (Medium): Context Manager Missing Exit
```python
class FileManager:
    def __init__(self, path):
        self.path = path
    def __enter__(self):
        self.f = open(self.path)
        return self.f
```
<details><summary>Answer</summary>
**Bug:** No `__exit__` method — file never closes when used with `with`.
**Fix:** Add `def __exit__(self, *args): self.f.close()`.
</details>

## Debug 03 (Hard): Decorator with Wrong Args
```python
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat
def greet():
    print("Hi")
```
<details><summary>Answer</summary>
**Bug:** `@repeat` (no parentheses) passes the FUNCTION as `times`. Need `@repeat(3)`.
**Fix:** Either always use `@repeat(3)`, or handle the case where `times` is a function.
</details>

---

## Common Mistakes — the traps learners hit

## Mistake 01: Missing @wraps
```python
# WRONG — loses metadata
def deco(func):
    def wrapper(*a, **k): return func(*a, **k)
    return wrapper

# CORRECT
from functools import wraps
def deco(func):
    @wraps(func)
    def wrapper(*a, **k): return func(*a, **k)
    return wrapper
```

## Mistake 02: Forgetting __exit__ in context manager
```python
# WRONG — resource leak
class CM:
    def __enter__(self): self.f = open(...); return self.f
    # no __exit__!

# CORRECT
class CM:
    def __enter__(self): self.f = open(...); return self.f
    def __exit__(self, *a): self.f.close()
```

## Mistake 03: Decorator without parentheses
```python
# If decorator takes args, must use parentheses
@repeat(3)  # correct
@repeat     # wrong — passes function as first arg
```

## Mistake 04: Not handling exceptions in __exit__
```python
# Check the exc_type argument
def __exit__(self, exc_type, exc_val, exc_tb):
    if exc_type is not None:
        # exception occurred
        log.error(exc_val)
    self.cleanup()
```

## Mistake 05: Yielding without try/finally in contextmanager
```python
# WRONG — cleanup doesn't run on exception
@contextmanager
def cm():
    setup()
    yield
    cleanup()

# CORRECT
@contextmanager
def cm():
    setup()
    try:
        yield
    finally:
        cleanup()
```

---

## Refactoring Challenges — make working code better

## Refactor 01 (Easy): No @wraps
### Before
```python
def timer(func):
    def wrapper(*a, **k):
        return func(*a, **k)
    return wrapper
```
### After
```python
from functools import wraps
def timer(func):
    @wraps(func)
    def wrapper(*a, **k):
        return func(*a, **k)
    return wrapper
```

## Refactor 02 (Medium): Manual Timing
### Before
```python
def fetch_data():
    start = time.time()
    result = api.get()
    print(f"Took {time.time() - start}s")
    return result
```
### After
```python
@timer
def fetch_data():
    return api.get()
```

## Refactor 03 (Hard): Repeated Try/Except Pattern
### Before
```python
def fetch_user():
    try: return api.get_user()
    except: return None
def fetch_post():
    try: return api.get_post()
    except: return None
```
### After
```python
def safe_api(func):
    @wraps(func)
    def wrapper(*a, **k):
        try: return func(*a, **k)
        except: return None
    return wrapper

fetch_user = safe_api(api.get_user)
fetch_post = safe_api(api.get_post)
```

---

## Approach Comparison — different ways to solve it

## Problem: Timing Decorator

### Approach 1: Class-based
```python
class Timer:
    def __init__(self, func):
        self.func = func
    def __call__(self, *args, **kwargs):
        start = time.time()
        result = self.func(*args, **kwargs)
        print(f"{time.time() - start}s")
        return result
```

### Approach 2: Function-based
```python
def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"{time.time() - start}s")
        return result
    return wrapper
```

**Winner:** Approach 2 — simpler, more common for decorators.

---

## Problem: File Resource Manager

### Approach 1: Class with __enter__/__exit__
```python
class FileOpener:
    def __init__(self, path): self.path = path
    def __enter__(self): self.f = open(self.path); return self.f
    def __exit__(self, *a): self.f.close()
```

### Approach 2: contextlib
```python
from contextlib import contextmanager
@contextmanager
def open_file(path):
    f = open(path)
    try:
        yield f
    finally:
        f.close()
```

**Winner:** Approach 2 — less boilerplate, more Pythonic for simple cases.
