# Lesson 12 — Concepts Explained (Decorators)

> Read this before solving the problems. Each concept explains:
> **What** it is · **Why** it exists · **Where** it's used · **What goes wrong** without it.

---

## Functions as First-Class Objects

**What:** In Python, functions are objects. You can assign them to variables, pass them as arguments, and return them from other functions.

```python
def greet(name): return f"Hello, {name}"

say_hello = greet          # assign function to variable
say_hello("Akash")         # "Hello, Akash"

def call_func(func, arg):  # pass function as argument
    return func(arg)

call_func(greet, "Bob")    # "Hello, Bob"

def get_greeter():         # return a function
    return greet

get_greeter()("Carol")     # "Hello, Carol"
```

**Why it exists:** This is the foundation of decorators, callbacks, and higher-order functions. Without first-class functions, you can't write decorators, can't pass callbacks, and can't build flexible APIs.

**Where it's used:** Decorators (this lesson), event handlers, callbacks, `map()`/`filter()` (they take functions as arguments), sorting with `key=`.

**What goes wrong without it:**
- Calling instead of passing: `call_func(greet("Bob"), arg)` → passes the RESULT, not the function → TypeError.
- Forgetting parentheses: `say_hello` is the function, `say_hello("Akash")` is the call. Mixing these up is a common beginner mistake.

---

## Higher-Order Functions

**What:** A higher-order function is a function that takes another function as an argument OR returns a function.

```python
# Takes a function as argument
def apply_twice(func, value):
    return func(func(value))

apply_twice(lambda x: x + 3, 5)   # 11  (5+3=8, 8+3=11)

# Returns a function
def make_multiplier(n):
    def multiply(x):
        return x * n
    return multiply

double = make_multiplier(2)
double(5)    # 10
triple = make_multiplier(3)
triple(5)    # 15
```

**Why it exists:** Higher-order functions let you write code that is more flexible — you can customize behavior by passing different functions. `sorted(list, key=...)` works with any key function because it's higher-order.

**Where it's used:** `map()`, `filter()`, `sorted(key=)`, `functools.reduce()`, decorators, event systems, middleware (Django/Flask).

**What goes wrong without it:**
- Without higher-order functions, you'd write separate functions for each case: `sort_by_name()`, `sort_by_age()`, `sort_by_date()` instead of one `sorted(key=...)`.
- Returning a function instead of calling it: `make_multiplier(2)` returns a function, `make_multiplier(2)(5)` calls it. Forgetting the second call → you get a function object, not the result.

---

## Closure

**What:** A closure is a function that "remembers" variables from the scope where it was created, even after that scope is gone.

```python
def make_counter():
    count = 0                    # variable in make_counter's scope
    def increment():
        nonlocal count            # access the outer variable
        count += 1
        return count
    return increment              # return the inner function

counter = make_counter()          # count = 0 is "captured"
counter()    # 1 — count is now 1
counter()    # 2 — count is now 2
counter()    # 3 — count is now 3
```

**Why it exists:** Without closures, the inner function couldn't access `count` after `make_counter` returns. Closures let you create functions with private state — like a mini-object with just one method.

**Where it's used:** Decorators (the wrapper function is a closure that captures the original function), factory functions, callbacks with state, memoization.

**What goes wrong without it:**
- Forgetting `nonlocal` → `UnboundLocalError` when trying to modify the outer variable. Python treats `count += 1` as a local variable assignment, shadowing the outer one.
- Late binding in loops: closures capture the VARIABLE, not the VALUE. All closures in a loop share the same variable → they all return the last value.
- Memory leaks: closures keep references to the outer scope → garbage collector can't free it.

---

## Basic Decorator

**What:** A decorator is a function that takes another function and extends its behavior without modifying it. You apply it with `@decorator_name`.

```python
def uppercase_result(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)    # call the original function
        return result.upper()              # modify the result
    return wrapper

@uppercase_result
def greet(name):
    return f"hello, {name}"

greet("akash")    # "HELLO, AKASH" — wrapper uppercased the result
```

`@uppercase_result` above `def greet` is shorthand for: `greet = uppercase_result(greet)`

**Why it exists:** Without decorators, you'd have to modify the function itself to add behavior. Decorators let you add logging, timing, caching, authentication, etc. WITHOUT touching the original function's code.

**Where it's used:** Everywhere in Python — `@property`, `@staticmethod`, `@classmethod` are built-in decorators. Web frameworks: `@app.route` (Flask), `@router.get` (FastAPI). `@dataclass`, `@functools.lru_cache`.

**What goes wrong without it:**
- Forgetting `return wrapper` → the decorator returns `None` → calling the decorated function → `TypeError: 'NoneType' is not callable`.
- Forgetting `*args, **kwargs` in wrapper → decorator only works with functions that have no arguments → breaks for any real function.
- Not calling `func()` inside wrapper → the original function never runs → only the decorator's behavior executes.

---

## Decorator with Arguments

**What:** A decorator that itself takes arguments. Requires three levels of nesting.

```python
def repeat(times):                    # decorator factory
    def decorator(func):              # the actual decorator
        def wrapper(*args, **kwargs):  # the wrapper
            result = None
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)                            # call the factory, get the decorator
def say_hi(name):
    print(f"Hi, {name}")

say_hi("Akash")    # prints "Hi, Akash" three times
```

**Why it exists:** Without decorator arguments, you can't customize the decorator's behavior. `@repeat(3)` vs `@repeat(5)` — the argument controls how many times to repeat.

**Where it's used:** `@app.route("/path")` (Flask — the path is an argument), `@lru_cache(maxsize=128)` (functools — cache size is an argument), `@retry(times=3)` (custom retry logic).

**What goes wrong without it:**
- Forgetting the extra nesting → decorator receives the function instead of the argument → `TypeError`.
- `@repeat` without parentheses → `times` gets the function object → `range(function)` → `TypeError`.
- Confusion about which level receives what: level 1 gets the argument, level 2 gets the function, level 3 is the wrapper.

---

## functools.wraps

**What:** `@functools.wraps(func)` preserves the original function's metadata (name, docstring) when it's wrapped by a decorator.

```python
from functools import wraps

def my_decorator(func):
    @wraps(func)                    # preserve original metadata
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def greet(name):
    """Say hello to someone."""
    return f"Hello, {name}"

greet.__name__    # "greet" (preserved by @wraps)
greet.__doc__     # "Say hello to someone." (preserved)
# Without @wraps: greet.__name__ would be "wrapper" — the wrapper's name
```

**Why it exists:** Without `@wraps`, the decorated function's `__name__` becomes `"wrapper"` and its docstring is lost. This breaks debugging, documentation generation (Sphinx), and tools that inspect function names.

**Where it's used:** EVERY custom decorator should use `@wraps`. It's not optional — it's a best practice that prevents real problems.

**What goes wrong without it:**
- `greet.__name__` → `"wrapper"` → debugging shows "wrapper" instead of "greet" → confusing stack traces.
- `help(greet)` → shows wrapper's docstring (usually empty) instead of the original function's documentation.
- Testing frameworks can't find the original function by name → test discovery fails.
- Always use `@wraps(func)` — there's no reason not to.

---

## Stacking Decorators

**What:** You can apply multiple decorators to one function. They apply bottom-up (closest to the function first).

```python
@decorator_a     # applied second (outermost)
@decorator_b     # applied first (innermost)
def my_func():
    pass

# Equivalent to: my_func = decorator_a(decorator_b(my_func))
```

**Why it exists:** You often need multiple behaviors — logging AND timing AND caching. Stacking lets you compose behaviors without writing one giant decorator.

**Where it's used:** Web routes (`@app.route` + `@login_required`), API endpoints (`@router.get` + `@validate_input` + `@rate_limit`).

**What goes wrong without it:**
- Order matters: `@log @validate` validates first, then logs. `@validate @log` logs first, then validates. Wrong order → logs invalid calls or validates before logging.
- Forgetting that order is bottom-up → decorators apply in unexpected order → subtle bugs.
- Each decorator must use `@wraps` or the chain breaks (metadata lost at each level).

---

## Class Decorator

**What:** A decorator can also be a class (with `__call__` and `__init__`) instead of a function.

```python
class CountCalls:
    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"Call {self.count} of {self.func.__name__}")
        return self.func(*args, **kwargs)

@CountCalls
def say_hi():
    print("Hi!")

say_hi()    # Call 1 of say_hi / Hi!
say_hi()    # Call 2 of say_hi / Hi!
say_hi.count  # 2 — state is stored in the decorator instance
```

**Why it exists:** Class decorators can maintain STATE (like a call counter) more naturally than function decorators. The class instance persists between calls.

**Where it's used:** Stateful decorators (call counting, rate limiting, caching with stats), `@dataclass` (transforms a class), `@property` (technically a class).

**What goes wrong without it:**
- Forgetting `__call__` → the class instance isn't callable → `TypeError: 'CountCalls' object is not callable`.
- `self.func` not called in `__call__` → original function never runs.
- State is shared across all calls to the decorated function → if you don't want this, use a function decorator instead.

---

## Practical Decorator Patterns

**What:** Common decorator patterns used in real code:

```python
# 1. Timing decorator
import time
def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took {time.time() - start:.4f}s")
        return result
    return wrapper

# 2. Logging decorator
def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}({args}, {kwargs})")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

# 3. Caching decorator (simplified lru_cache)
def cache(func):
    stored = {}
    @wraps(func)
    def wrapper(*args):
        if args not in stored:
            stored[args] = func(*args)
        return stored[args]
    return wrapper
```

**Why it exists:** These patterns are so common that wrapping them in decorators avoids repeating the same boilerplate in every function. One `@timer` decorator works for ANY function.

**Where it's used:** Production code everywhere — timing for performance analysis, logging for debugging, caching for expensive computations, authentication for protected routes.

**What goes wrong without it:**
- Copy-pasting timing/logging code into every function → 50 functions with the same 5 lines of timing code → change the timing format, edit 50 places.
- Caching without a decorator → manual dict management in every function → error-prone, inconsistent.
- Always use `@wraps` in these patterns → debugging shows the real function name.
