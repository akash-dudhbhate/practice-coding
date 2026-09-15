# Lesson 06 — Functions Deep Dive

## What you'll learn
- Default parameters and the mutable-default trap.
- `*args` and `**kwargs` for flexible signatures.
- Lambda functions for short one-off operations.
- Scope (LEGB) and closures.
- Higher-order functions and type hints.

## Lesson

Functions can be far more flexible than simple `def f(a, b): return ...`.

### Defaults & flexible args
```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}"

def sum_all(*nums):           # tuple of positional args
    return sum(nums)

def build(**opts):            # dict of keyword args
    return opts
```

### Lambda
```python
sorted(nums, key=lambda n: -n)   # inline one-expression function
```

### Scope & closures
```python
def make_multiplier(factor):
    return lambda n: n * factor   # remembers 'factor'
double = make_multiplier(2)
```

### Key rules
- Never use a mutable default (`def f(x=[]):`). Use `x=None`.
- `*args` → tuple; `**kwargs` → dict.
- Lambdas are single-expression only; use `def` for anything complex.
- Avoid `global`; pass values as arguments.

---

## Your Tasks

This lesson has **9 practice problems** across three difficulty levels. Start with `easy/` and work your way up. Each problem file has the description at the top — **write your complete solution from scratch below** (function signature + body) to practice remembering syntax.

### Easy (start here)
1. `easy/p01-solve.py` — `greet(name, greeting="Hello")`: return `"{greeting}, {name}!"`. `greet("Akash")` → `"Hello, Akash!"`.
2. `easy/p02-solve.py` — `sum_all(*nums)`: return the sum of any number of arguments. `sum_all(1,2,3)` → `6`; `sum_all()` → `0`.
3. `easy/p03-solve.py` — `square(n)`: return `n * n` using a lambda assigned to a variable (demonstrate lambda usage).

### Medium
4. `medium/p01-solve.py` — `make_tag(tag, text, **attrs)`: return an HTML string `"<tag k=\"v\" ...>text</tag>"`. `make_tag("a", "link", href="x.com")` → `'<a href="x.com">link</a>'`.
5. `medium/p02-solve.py` — `safe_append(item, lst=None)`: append `item` to `lst` and return the list, avoiding the mutable-default bug (create a new list when `lst is None`).
6. `medium/p03-solve.py` — `apply_func(func, items)`: return a new list with `func` applied to each item (use a loop; mimic `map`).

### Hard
7. `hard/p01-solve.py` — `make_counter(start=0)`: return a closure function that increments and returns the current count each call. `c = make_counter(); c(); c()` → `1` then `2`.
8. `hard/p02-solve.py` — `compose(f, g)`: return a new function that computes `f(g(x))`. `h = compose(lambda x: x+1, lambda x: x*2); h(3)` → `7`.
9. `hard/p03-solve.py` — `build_profile(name, **info)`: return a dict with `name` plus all keyword info, then a function `format_profile(profile)` that returns `"name (key1=val1, key2=val2)"`. Write both; test together.

### How to work
- Open a problem file, read the description in the header comment.
- Write your **complete solution from scratch** below the TODO marker.
- Remove the TODO line when done.
- Run `python <filename>` to test with your own inputs.
- When done, tell me and I'll review. Say **"give me next task"** to advance to the next lesson.
