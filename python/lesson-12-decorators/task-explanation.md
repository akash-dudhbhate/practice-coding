# Lesson 12 — Decorators

## What you'll learn
- Functions as first-class objects
- Higher-order functions
- Closures
- Writing basic decorators
- Decorators with arguments
- functools.wraps
- Stacking decorators
- Class decorators
- Practical patterns (timing, logging, caching)

## Lesson

### Basic decorator
```python
def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@log
def greet(name): return f"Hi {name}"
```

### Decorator with arguments
```python
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def say_hi(): print("Hi!")
```

---

## Your Tasks

### Easy
1. `easy/p01-solve.py` — Write a decorator `@shout` that converts the function's string return value to UPPERCASE.
2. `easy/p02-solve.py` — Write a decorator `@timer` that measures and prints how long a function takes to execute (use `time.time()`).
3. `easy/p03-solve.py` — Write a decorator `@log_call` that prints the function name before calling it and the return value after.

### Medium
4. `medium/p01-solve.py` — Write a decorator `@repeat(n)` that calls the decorated function n times and returns the last result.
5. `medium/p02-solve.py` — Write a decorator `@cache` that stores results in a dict keyed by arguments. If the same arguments are called again, return the cached result instead of re-computing.
6. `medium/p03-solve.py` — Write a decorator `@validate_positive` that checks all numeric arguments are positive (> 0). If any are not, raise ValueError.

### Hard
7. `hard/p01-solve.py` — Write a class decorator `@CountCalls` that counts how many times a function is called. Store the count as an attribute accessible via `func.count`.
8. `hard/p02-solve.py` — Write a decorator `@retry(times=3, delay=1)` that retries a function up to `times` times if it raises an exception, waiting `delay` seconds between retries. Use `time.sleep()`.
9. `hard/p03-solve.py` — Stack two decorators: `@log` (prints function name and args) and `@timer` (prints execution time). Apply both to a function and verify the output shows both logging and timing.

### How to work
- Write your complete solution from scratch below the TODO marker.
- Remove the TODO line when done.
