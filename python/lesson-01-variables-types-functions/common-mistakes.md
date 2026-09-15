# Lesson 01 — Common Mistakes (What NOT to Do)

> Anti-patterns that beginners make. Learn these early → save hours of debugging later.

---

## Mistake 01: Using `==` for comparison in `if` instead of `=`

```python
# WRONG — assignment, not comparison (SyntaxError in if)
if x = 5:
    print("x is 5")

# CORRECT
if x == 5:
    print("x is 5")
```

**Why it's wrong:** `=` assigns, `==` compares. Python catches this as a SyntaxError, but in other languages (C, JS) it silently assigns and the `if` is always true.

---

## Mistake 02: Forgetting `return` in a function

```python
# WRONG — prints but returns None
def square(n):
    print(n * n)

result = square(5)  # result is None, not 25

# CORRECT — returns the value
def square(n):
    return n * n
```

**Why it's wrong:** `print` shows output on screen but doesn't give the value back. `return` gives the value to the caller. If you need the result later, you must `return` it.

**Rule:** If the function computes a value → `return` it. If it just displays → `print` is fine.

---

## Mistake 03: Confusing `/` and `//`

```python
# WRONG — expects int, gets float
average = 10 / 2  # 5.0, not 5
if average == 5:  # False! 5.0 != 5 in some contexts
    print("perfect")

# CORRECT — use // for integer division
average = 10 // 2  # 5 (int)
```

**Why it's wrong:** `/` always returns a float. `//` returns an int (when both operands are ints). Use `//` when you need integer results.

---

## Mistake 04: Mutable default arguments

```python
# WRONG — the list is shared across all calls
def add_item(item, lst=[]):
    lst.append(item)
    return lst

add_item(1)  # [1]
add_item(2)  # [1, 2] — NOT [2]!

# CORRECT — use None and create inside
def add_item(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst
```

**Why it's wrong:** Default argument values are evaluated ONCE when the function is defined, not each call. Mutable defaults (list, dict, set) are shared. This is the #1 Python gotcha.

---

## Mistake 05: Not using type hints on function signatures

```python
# NOT IDEAL — unclear what types are expected
def calculate(a, b):
    return a + b

# BETTER — type hints document the contract
def calculate(a: int, b: int) -> int:
    return a + b
```

**Why it matters:** Type hints don't enforce types at runtime, but they:
1. Document what the function expects and returns
2. Enable IDE autocomplete and type checking (mypy)
3. Help other developers (and future you) understand the code

**Rule:** Always add type hints to function parameters and return types.

---

## Mistake 06: Comparing floats with `==`

```python
# WRONG — float precision issues
if 0.1 + 0.2 == 0.3:
    print("equal")  # NEVER prints!

print(0.1 + 0.2)  # 0.30000000000000004

# CORRECT — use a tolerance
if abs(0.1 + 0.2 - 0.3) < 1e-9:
    print("equal")  # prints
```

**Why it's wrong:** Floating-point numbers can't represent most decimals exactly. `0.1 + 0.2` is `0.30000000000000004`, not `0.3`. Always compare floats with a tolerance (epsilon), not `==`.

---

## Mistake 07: Using `is` instead of `==` for value comparison

```python
# WRONG — `is` checks identity, not equality
a = [1, 2, 3]
b = [1, 2, 3]
if a is b:  # False! different objects
    print("same")

# CORRECT — `==` checks value equality
if a == b:  # True! same values
    print("same")
```

**Why it's wrong:** `is` checks if two variables point to the SAME object in memory. `==` checks if the VALUES are equal. Use `==` for comparing values. Use `is` only for `None`, `True`, `False`.

---

## Summary Table

| Mistake | Wrong | Right | Rule |
|---------|-------|-------|------|
| Assignment vs comparison | `if x = 5:` | `if x == 5:` | `=` assigns, `==` compares |
| Missing return | `print(n*n)` | `return n*n` | Return if you need the value |
| `/` vs `//` | `10 / 2` → `5.0` | `10 // 2` → `5` | Use `//` for integers |
| Mutable defaults | `def f(lst=[])` | `def f(lst=None)` | Never use mutable defaults |
| No type hints | `def f(a, b):` | `def f(a: int, b: int) -> int:` | Always add type hints |
| Float comparison | `0.1 + 0.2 == 0.3` | `abs(a - b) < 1e-9` | Never compare floats with `==` |
| `is` vs `==` | `a is b` | `a == b` | `is` for None/True/False, `==` for values |
