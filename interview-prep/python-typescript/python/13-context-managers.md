# 13 — Context Managers

> **Interview question:** "What is a context manager? Write one using `contextlib` and one as a class."
> **What the interviewer is really testing:** Whether you understand the `with` statement as guaranteed setup/teardown — not just "it's how you open files."

## Theory — what it is

A **context manager** is an object that wraps a block of code with a *before* step and an *after* step. You use it with the `with` statement:

```python
with something() as x:
    ...  # the "body"
```

Under the hood, `with` calls two dunder methods:

- `__enter__()` — runs when the block starts; its return value is bound to the `as` variable.
- `__exit__(exc_type, exc_value, traceback)` — runs when the block ends, **even if it raised an exception**. If it returns a truthy value, the exception is swallowed; otherwise it propagates.

`contextlib.contextmanager` is a decorator that lets you write the same thing as a **generator**: everything before `yield` is `__enter__`, the yielded value becomes the `as` variable, and everything after `yield` (inside `finally`) is `__exit__`.

## Why it was needed

The classic bug context managers fix:

```python
f = open("data.txt")
data = f.read()
process(data)     # if THIS raises, f.close() never runs -> leaked handle
f.close()
```

The `try/finally` fix works but is noisy and easy to forget. `with open(...) as f:` makes cleanup *structural* — you literally cannot reach the end of the block without `__exit__` running, exception or not. It converts "remember to clean up" into "cleanup is automatic."

## Where it's used in a real project

- **Files**: `with open(path) as f:` — closes the handle no matter what.
- **Database transactions**: `with conn:` — commit on success, rollback on exception.
- **Locks**: `with lock:` — release the lock even if the critical section crashes.
- **Temporary state**: `contextlib` helpers like `redirect_stdout`, `suppress`, `chdir`-style swappers for tests.
- **Timing/benchmarking**: `with timer():` around a block you want to measure.

## Diagram

```
with CM() as x:
     |
     v
+----------------------------+
|  __enter__()  ->  x        |   (setup: open file, acquire lock)
+----------------------------+
     |   <body runs here>
     v
+----------------------------+
|  __exit__(exc_type, ...)   |   (cleanup: close, release — ALWAYS runs)
|  return False: propagate   |
|  return True:  swallow     |
+----------------------------+

Generator version:
   code before yield  ==  __enter__
   yield value        ==  `as x`
   code in finally    ==  __exit__
```

## Code — explained

**Class version** — a lock-style manager:

```python
class FakeLock:
    def __enter__(self):
        print("acquired")
        return self                       # bound to `as` target

    def __exit__(self, exc_type, exc, tb):
        print("released")
        return False                      # False -> don't hide exceptions

with FakeLock() as lock:
    print("critical section")
# Output:
# acquired
# critical section
# released
```

**`contextlib` version** — same behavior, generator style:

```python
from contextlib import contextmanager

@contextmanager
def fake_lock():
    print("acquired")          # setup  == __enter__
    try:
        yield                  # hands control to the with-block
    finally:
        print("released")      # cleanup == __exit__ (finally => always runs)

with fake_lock():
    print("critical section")
# identical output
```

Line-by-line:

1. `__enter__`/`yield`-before: runs at `with` — do setup, optionally return/yield the resource.
2. The `try/finally` in the generator version matters: if the body raises, the exception is thrown **into** the generator at the `yield` line — `finally` guarantees cleanup still runs.
3. `__exit__` returning `False` lets exceptions propagate; returning `True` suppresses them (sparingly!).
4. In the generator version, to suppress an exception you'd `except` around `yield` and *not* re-raise.

## Problems

### Easy — Banner with `contextlib`
**Problem:** Write `banner(name)` — a contextmanager printing `--- name ---` before the block and `--- end ---` after.
**Try this input:**
```python
with banner("setup"):
    print("working")
```
**Expected output:**
```
--- setup ---
working
--- end ---
```
**Solution:**
```python
from contextlib import contextmanager

@contextmanager
def banner(name):
    print(f"--- {name} ---")
    try:
        yield
    finally:
        print("--- end ---")

with banner("setup"):
    print("working")
```
**Logic explained:**
1. Code before `yield` = `__enter__`: prints the header.
2. `yield` (no value → `as` would get `None`) hands off to the block.
3. `finally` = `__exit__`: prints the footer even if `working` had raised.

### Medium — Class-based resource
**Problem:** Write `Resource` as a **class** context manager that prints `open`, runs the body, prints `close`, and reports via `__exit__` whether the block ended cleanly.
**Try this input:**
```python
with Resource() as r:
    print("using", r)
```
**Expected output:**
```
open
using <__main__.Resource object at 0x...>
close (clean exit)
```
(the address varies)
**Solution:**
```python
class Resource:
    def __enter__(self):
        print("open")
        return self

    def __exit__(self, exc_type, exc, tb):
        if exc_type is None:
            print("close (clean exit)")
        else:
            print(f"close (after {exc_type.__name__})")
        return False                       # never suppress here

with Resource() as r:
    print("using", r)
```
**Logic explained:**
1. `__enter__` returns `self`, so `r` *is* the Resource — hence `using <Resource object>`.
2. `__exit__` inspects `exc_type`: `None` means the block finished normally.
3. `return False` — if the block had raised, we log it and let it propagate.

### Hard — Selective suppression
**Problem:** Write `IgnoreValueError` — a class context manager that swallows `ValueError` raised in the block but lets everything else propagate.
**Try this input:**
```python
with IgnoreValueError():
    raise ValueError("boom")
print("survived")
```
**Expected output:** `survived`
**Solution:**
```python
class IgnoreValueError:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        # True -> suppress; must ONLY be true for ValueError
        return exc_type is not None and issubclass(exc_type, ValueError)

with IgnoreValueError():
    raise ValueError("boom")     # swallowed by __exit__'s True
print("survived")                # still runs

# A KeyError in the block would propagate normally (return -> False).
```
**Logic explained:**
1. When the block raises `ValueError`, `__exit__` is called with `exc_type=ValueError`.
2. `issubclass(exc_type, ValueError)` is `True` → `__exit__` returns `True` → Python swallows the exception and continues after the `with`.
3. For `KeyError`, the expression is `False` → exception propagates. This is exactly what `contextlib.suppress(ValueError)` does for real.

## The 30-second interview answer

"A context manager wraps a block with guaranteed setup and teardown: `__enter__` runs at the top, `__exit__` runs at the bottom even on exceptions, and returning truthy from `__exit__` suppresses the exception. As a class you write those two methods; with `contextlib.contextmanager` you write a generator where code before `yield` is enter, the yielded value is the `as` target, and a `finally` after `yield` is exit. Files, locks, and DB transactions use this everywhere so cleanup can't be skipped."

## Follow-up trap

**"What's the bug in this?"**

```python
@contextmanager
def bad():
    print("start")
    yield                       # no try/finally!
    print("end")
```

If the `with` body raises, the exception is thrown into the generator at `yield` — since nothing catches it, `"end"` never prints. **Cleanup after `yield` must live in `finally`** (or you must `except` and re-raise). A related trap: returning `True` from `__exit__` by accident (e.g., returning a logged message) silently swallows *all* exceptions — always return `False`/`None` unless suppression is the goal.
