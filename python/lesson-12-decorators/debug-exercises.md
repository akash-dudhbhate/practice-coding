# Lesson 12 — Debug Exercises

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
