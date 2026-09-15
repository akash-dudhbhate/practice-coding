# Lesson 12 — Approach Comparison

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
