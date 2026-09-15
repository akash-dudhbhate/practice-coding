# Lesson 12 — Common Mistakes

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
