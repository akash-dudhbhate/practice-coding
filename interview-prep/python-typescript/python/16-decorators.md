# 16 — Decorators: `@timer` and `@retry(times=3)`

> **Interview question:** "Write a decorator that times a function. Now write one that takes arguments — `@retry(times=3)`."
> **What the interviewer is really testing:** Whether you truly get that `@deco` is just `f = deco(f)` — and can handle the extra layer a decorator-with-arguments needs.

## Theory — what it is

A **decorator** is a function that takes a function and returns a (usually new) function that wraps it — adding behavior before/after the call. The `@` syntax is pure sugar:

```python
@timer
def f(): ...
# is IDENTICAL to:
def f(): ...
f = timer(f)
```

So `timer` receives the original `f` and returns a `wrapper`; the name `f` now points to `wrapper`. When `wrapper` runs, it does its extra work, calls the real `f`, and (importantly) returns `f`'s result.

A **decorator with arguments** adds one more layer. `@retry(times=3)` means `retry(3)` is called *first* and must return the actual decorator:

```python
@retry(times=3)
def f(): ...
# is IDENTICAL to:
f = retry(times=3)(f)      # retry(3) -> decorator; decorator(f) -> wrapper
```

Three nested functions: `retry` (takes config) → `deco` (takes the function) → `wrapper` (takes the call args).

## Why it was needed

Cross-cutting concerns — timing, logging, retries, auth checks, caching — would otherwise be copy-pasted into every function:

```python
def handler():
    start = time.time()      # noise repeated in EVERY function
    ...
    log("took", time.time()-start)
```

A decorator keeps each function focused on its job while the wrapper handles the boilerplate once. Decorators exist because "wrap every function in this file with X" is a real, recurring need — Flask routes, pytest fixtures, `functools.lru_cache`, `@staticmethod` are all this pattern.

## Where it's used in a real project

- **Web frameworks**: `@app.route("/users")` registers the view function.
- **Caching**: `@functools.lru_cache(maxsize=128)` memoizes calls.
- **Auth**: `@requires_login` / `@permission("admin")` on views.
- **Resilience**: `@retry(times=3)`, `@timeout(5)`, `@rate_limit` around flaky network calls.

## Diagram

```
WITHOUT ARGS (2 layers)              WITH ARGS (3 layers)

@timer                                @retry(times=3)
def f():  ==  f = timer(f)            def f(): == f = retry(3)(f)

timer(f) -> wrapper                   retry(3) -> deco -> deco(f) -> wrapper

call f(4):                            call f(4):
  wrapper(4)                            wrapper(4)
    |--> f(4)  wrapped work               |--> try f(4); on fail, retry (knows times=3)
```

## Code — explained

**Part 1 — the timer:**

```python
import functools
import time

def timer(f):
    @functools.wraps(f)                    # keep f's name/docstring (file 17!)
    def wrapper(*args, **kwargs):          # accept ANY signature
        start = time.time()
        result = f(*args, **kwargs)        # call the real function
        print(f"{f.__name__} took {time.time() - start:.3f}s")
        return result                      # DON'T forget to return!
    return wrapper

@timer
def slow_add(a, b):
    time.sleep(0.01)
    return a + b

print(slow_add(2, 3))
# slow_add took 0.010s
# 5
```

**Part 2 — `retry` with an argument:**

```python
import functools

def retry(times):                          # layer 1: receives decorator ARGS
    def deco(f):                           # layer 2: receives the FUNCTION
        @functools.wraps(f)
        def wrapper(*args, **kwargs):      # layer 3: receives CALL args
            for attempt in range(1, times + 1):
                try:
                    return f(*args, **kwargs)
                except Exception:
                    if attempt == times:
                        raise              # last attempt failed -> give up
        return wrapper
    return deco
```

Line-by-line:

1. `wrapper(*args, **kwargs)` — the decorated function keeps its real signature at call sites; we forward everything.
2. `return f(...)` / `return result` — if you don't return, callers silently get `None`.
3. `retry(times=3)` — `times` is captured by `wrapper` via **closure** (file 15!) — that's how the wrapper "remembers" the config.
4. `range(1, times + 1)` — attempts 1..3; on the last failure, `raise` re-raises the original exception instead of looping forever.

## Problems

### Easy — `@shout`
**Problem:** Write `@shout` — uppercases the string a function returns.
**Try this input:**
```python
@shout
def greet(name):
    return f"hello {name}"

print(greet("sam"))
```
**Expected output:** `HELLO SAM`
**Solution:**
```python
import functools

def shout(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        return f(*args, **kwargs).upper()   # transform the RESULT
    return wrapper

@shout
def greet(name):
    return f"hello {name}"

print(greet("sam"))          # HELLO SAM
```
**Logic explained:**
1. `greet = shout(greet)` — `greet` now points at `wrapper`.
2. `wrapper` calls the real `greet`, gets `"hello sam"`, uppercases it.
3. `*args/**kwargs` forwarding means it works for any arity.

### Medium — `@log_calls`
**Problem:** Write `@log_calls` printing `calling <name>(<args>)` before each call.
**Try this input:**
```python
@log_calls
def add(a, b):
    return a + b

add(2, 3)
```
**Expected output:** `calling add(2, 3)`
**Solution:**
```python
import functools

def log_calls(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        print(f"calling {f.__name__}{args}")
        return f(*args, **kwargs)
    return wrapper

@log_calls
def add(a, b):
    return a + b

add(2, 3)        # calling add(2, 3)
```
**Logic explained:**
1. `args` is a tuple — `f"{args}"` prints `(2, 3)`.
2. `f.__name__` reads the *original* function's name — thanks to `@functools.wraps`, `add.__name__` stays `"add"` too.
3. The `return` forwards `5` to the caller even though we don't print it.

### Hard — `@retry(times=3)` proven
**Problem:** Implement `retry(times)` and prove it retries exactly `times` times using a flaky function that fails twice then succeeds.
**Try this input:**
```python
calls = {"n": 0}

@retry(times=3)
def flaky():
    calls["n"] += 1
    if calls["n"] < 3:
        raise ValueError("nope")
    return "ok"

print(flaky(), calls["n"])
```
**Expected output:** `ok 3`
**Solution:**
```python
import functools

def retry(times):
    def deco(f):
        @functools.wraps(f)
        def wrapper(*args, **kwargs):
            for attempt in range(1, times + 1):
                try:
                    return f(*args, **kwargs)
                except Exception:
                    if attempt == times:
                        raise
        return wrapper
    return deco

calls = {"n": 0}

@retry(times=3)
def flaky():
    calls["n"] += 1
    if calls["n"] < 3:
        raise ValueError("nope")
    return "ok"

print(flaky(), calls["n"])     # ok 3
```
**Logic explained:**
1. Call 1: `n=1` → `ValueError` → attempt 1 ≠ 3 → loop continues.
2. Call 2: `n=2` → `ValueError` → attempt 2 ≠ 3 → continue.
3. Call 3: `n=3` → returns `"ok"` → `wrapper` returns it. `calls["n"]` is `3`.
4. If attempt 3 had raised, `attempt == times` → `raise` propagates the real exception. Optional polish: sleep between attempts, or catch only specific exception types passed as `exceptions=(ValueError,)`.

## The 30-second interview answer

"A decorator is a function that takes a function and returns a wrapper — `@timer def f` literally means `f = timer(f)`. The wrapper uses `*args/**kwargs` to forward arguments, calls the original, and returns its result. A decorator with arguments needs a third layer: `@retry(times=3)` means `f = retry(3)(f)` — `retry(3)` returns the decorator, which returns the wrapper; the config lives in the closure. I always add `@functools.wraps(f)` so the wrapper keeps the original's name and docstring."

## Follow-up trap

**"What order do stacked decorators apply in?"**

```python
@a
@b
def f(): ...
# == f = a(b(f))  — bottom-up: b wraps f first, then a wraps that.
```

So at *call* time, `a`'s code runs first (outermost). Also expect: **"What happens if the wrapped function takes arguments or returns a value?"** — that's exactly why `*args/**kwargs` and `return f(...)` exist; forgetting `return` is the #1 decorator bug (callers get `None`). Bonus probe: **decorating a method** — `self` arrives inside `*args`, so a generic wrapper handles it fine.
