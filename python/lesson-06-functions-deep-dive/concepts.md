# Lesson 06 — Concepts Explained (Functions Deep Dive)

> Read this before solving the problems. Each concept explains:
> **What** it is · **Why** it exists · **Where** it's used · **What goes wrong** without it.

---

## Default Parameters

**What:** A parameter with a default value, used when the caller doesn't supply one.

```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

greet("Akash")           # "Hello, Akash!"  (greeting defaults)
greet("Akash", "Hi")     # "Hi, Akash!"
greet("Sam", greeting="Yo")  # keyword arg
```

**Why it exists:** Many functions have common-case values. Defaults let callers omit them for the common case while still allowing override. This keeps calls short without losing flexibility.

**Where it's used:** Configuration (`timeout=30`), formatting (`sep=" "`), optional flags (`verbose=False`), API wrappers.

**What goes wrong without it:**
- **Mutable default argument bug**: `def f(items=[]):` — the SAME list is shared across ALL calls. `items.append(x)` persists between calls, causing bizarre accumulating behavior. Fix: `def f(items=None): if items is None: items = []`.
- Defaults must come AFTER non-default params: `def f(a, b=2)` is valid; `def f(a=1, b)` is a `SyntaxError`.
- Default evaluated once at definition time, not each call — this is why the mutable-default bug happens.

---

## *args (Variable Positional Arguments)

**What:** `*args` collects any extra positional arguments into a tuple.

```python
def add_all(*numbers):
    return sum(numbers)

add_all(1, 2, 3)       # 6  -> numbers = (1, 2, 3)
add_all()              # 0  -> numbers = ()
add_all(10, 20)        # 30

def show(name, *hobbies):
    print(f"{name}: {hobbies}")
show("Akash", "coding", "music")  # Akash: ('coding', 'music')
```

**Why it exists:** Sometimes you don't know how many arguments will be passed — a sum of any count, a logger with any number of fields, `print()` accepting any number of items. `*args` lets a function accept a flexible number of positional arguments.

**Where it's used:** `print(*objs)`, `max(*nums)`, aggregators, forwarding arguments to another function, building flexible APIs.

**What goes wrong without it:**
- You'd have to pass a list explicitly: `add_all([1,2,3])` — less natural than `add_all(1,2,3)`.
- Forgetting the `*`: `def f(args):` receives a single tuple argument, not unpacked values. `f(1,2,3)` then fails with "takes 1 positional argument but 3 were given."
- `*args` is a tuple (immutable) — you can't append to it. If you need to modify, convert: `items = list(args)`.

---

## **kwargs (Variable Keyword Arguments)

**What:** `**kwargs` collects any extra keyword arguments into a dict.

```python
def create_user(name, **details):
    user = {"name": name}
    user.update(details)
    return user

create_user("Akash", age=25, city="LA", admin=True)
# {"name": "Akash", "age": 25, "city": "LA", "admin": True}
# details = {"age": 25, "city": "LA", "admin": True}
```

**Why it exists:** Functions often accept optional named settings you don't want to enumerate explicitly — config passthrough, optional metadata, flexible constructors. `**kwargs` captures them as a dict.

**Where it's used:** Wrapper functions that forward options (`requests.get(url, **options)`), plugin systems, decorators, building objects from dynamic data.

**What goes wrong without it:**
- `TypeError: got an unexpected keyword argument 'x'` when the caller passes a keyword the function didn't declare. `**kwargs` absorbs extras instead.
- Forgetting `**`: `def f(kwargs):` receives a single dict argument. `f(a=1)` fails. You need `def f(**kwargs)`.
- Keys are strings — `kwargs["age"]`, not `kwargs[age]`. Using a variable as key looks up that variable's value.

---

## Keyword-Only & Position-Only Parameters

**What:** Parameters after a `*` are keyword-only (must be passed by name). Parameters before a `/` are position-only (can't be passed by name).

```python
# keyword-only (after *)
def fetch(url, *, timeout=30, retries=3):
    ...
fetch("http://x.com", timeout=10)   # OK
# fetch("http://x.com", 10)         # TypeError — timeout must be by name

# position-only (before /)
def power(base, exp, /):
    return base ** exp
power(2, 3)        # OK
# power(2, exp=3)  # TypeError — exp is position-only
```

**Why it exists:** Keyword-only params make APIs clearer and let you reorder parameters later without breaking callers (they use names). Position-only lets you rename internal params without breaking callers who happened to use the same keyword name.

**Where it's used:** Library APIs (e.g., `sorted(iterable, *, key, reverse)`), functions with many options, avoiding name clashes.

**What goes wrong without it:**
- Without keyword-only, callers pass positional args in the wrong order silently → subtle bugs.
- Renaming a parameter breaks callers using it as a keyword (unless it's position-only).

---

## Lambda Functions

**What:** A lambda is a small anonymous function defined in one expression. It's limited to a single expression (no statements).

```python
square = lambda x: x * x
square(5)          # 25

# Common as a callback:
nums = [1, 2, 3, 4]
sorted(nums, key=lambda n: -n)        # [4, 3, 2, 1]  (descending)
sorted(["bbb", "a", "cc"], key=lambda s: len(s))  # ["a", "cc", "bbb"]

# With map/filter:
list(map(lambda x: x * 2, [1, 2, 3]))  # [2, 4, 6]
```

**Why it exists:** For tiny one-off functions, defining a full `def` is overkill. Lambdas let you inline a small function right where it's used, especially as `key`/`callback` arguments.

**Where it's used:** `sort(key=...)`, `map()`, `filter()`, `reduce()`, GUI callbacks, short transformations.

**What goes wrong without it:**
- Overusing lambdas for complex logic → unreadable, can't have docstrings, can't be debugged easily. Use `def` for anything non-trivial.
- Lambda closure capture bug: `[lambda: i for i in range(3)]` — all return the final `i` (2), because they capture the variable, not the value. Fix: `lambda i=i: i`.
- Assigning a lambda to a variable (`f = lambda x: x`) when a `def` would be clearer — lambdas have no name in tracebacks, making errors harder to read.

---

## Scope (Local, Enclosing, Global, Built-in)

**What:** Scope determines where a name is visible. Python uses LEGB order: Local → Enclosing → Global → Built-in.

```python
x = "global"            # global

def outer():
    x = "enclosing"     # enclosing (for inner)
    def inner():
        x = "local"     # local
        print(x)
    inner()
    print(x)
outer()
print(x)
# local / enclosing / global

count = 0
def increment():
    global count        # modify global
    count += 1
```

**Why it exists:** Scope prevents name collisions. Without it, every variable in a 10,000-line program would share one namespace — chaos. Scope keeps functions self-contained and predictable.

**Where it's used:** Every program. Functions define local scope; modules define global scope.

**What goes wrong without it:**
- `UnboundLocalError`: assigning to a global inside a function without `global` — Python treats it as local, but you read it before assigning.
- Overusing `global` → functions have hidden dependencies, hard to test and reason about. Avoid globals; pass values as arguments.
- Modifying a mutable global (list) works without `global` (you mutate, not rebind), which surprises people and causes bugs.

---

## Closures

**What:** A closure is a function that "remembers" variables from the enclosing scope where it was defined, even after that scope finished.

```python
def make_multiplier(factor):
    def multiply(n):
        return n * factor    # 'factor' is remembered from make_multiplier
    return multiply

double = make_multiplier(2)
triple = make_multiplier(3)
double(5)    # 10
triple(5)    # 15
# make_multiplier already returned, but 'factor' is captured
```

**Why it exists:** Closures let you create customized functions at runtime — a function with bundled state. This is the foundation of decorators, partial application, and many functional patterns.

**Where it's used:** Decorators, `functools.partial`, callbacks with state, configuration functions, hiding data (private state without classes).

**What goes wrong without it:**
- Late-binding loop bug: `funcs = [lambda: i for i in range(3)]`; calling each returns `2`. The variable `i` is looked up at call time, not capture time. Fix: `lambda i=i: i`.
- Forgetting that closures capture variables by reference, not value — the captured variable can change before the closure runs.
- Overusing closures for state that a class would express more clearly.

---

## Returning Functions & Higher-Order Functions

**What:** Functions are first-class objects — you can pass them as arguments and return them from other functions. A function that takes/returns a function is "higher-order."

```python
def apply_twice(func, x):
    return func(func(x))

apply_twice(lambda n: n + 3, 5)   # 11  ((5+3)+3)

def make_greeter(greeting):
    def greet(name):
        return f"{greeting}, {name}"
    return greet

hi = make_greeter("Hi")
hi("Akash")   # "Hi, Akash"
```

**Why it exists:** Treating functions as data lets you build flexible, reusable abstractions — `map`, `filter`, `sorted(key=...)`, decorators, strategies. You customize behavior by passing a different function.

**Where it's used:** `sorted(key=...)`, `map`/`filter`, event handlers, decorators, strategy patterns, dispatch tables.

**What goes wrong without it:**
- Passing a function CALL instead of the function: `sorted(nums, key=abs())` — calls `abs()` immediately with no args → error. Pass `key=abs` (no parens).
- Forgetting to actually call the returned function: `result = make_greeter("Hi")` gives a function, not a string. You need `make_greeter("Hi")("Akash")`.

---

## Type Hints & Docstrings

**What:** Type hints annotate expected types; docstrings document behavior. Both are optional but valuable.

```python
def add(a: int, b: int) -> int:
    """Return the sum of a and b.

    Args:
        a: first integer
        b: second integer
    Returns:
        their sum
    """
    return a + b
```

**Why it exists:** Type hints let tools (mypy, IDEs) catch type errors before runtime. Docstrings let `help()` and readers understand a function without reading its body.

**Where it's used:** Every well-maintained codebase. Libraries document public APIs with docstrings; larger projects use type hints for safety.

**What goes wrong without it:**
- No docstring → users must read the source to understand behavior.
- No type hints → passing wrong types fails at runtime with confusing errors instead of being caught by tooling.
- Hints are NOT enforced at runtime — `add("x", 1)` still runs (and may crash inside). They're documentation + tooling, not guards.
