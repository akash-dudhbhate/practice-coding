# Lesson 01 — Approach Comparison

> **Same problem, multiple solutions.** Learn the trade-offs → build judgment.
> There's rarely one "right" way — but there's usually a "best for this situation" way.

---

## Problem: Find the Maximum of Two Numbers

### Approach 1: If/Else (Explicit)

```python
def max_of_two(a, b):
    if a > b:
        return a
    else:
        return b
```

**Pros:** Clear, beginner-friendly, easy to debug.
**Cons:** Verbose. The `else` is unnecessary when `if` returns.
**Best for:** Teaching, when logic is complex.

---

### Approach 2: If without Else (Idiomatic)

```python
def max_of_two(a, b):
    if a >= b:
        return a
    return b
```

**Pros:** Shorter. If the `if` returns, the next line only runs when the condition is false — so `else` is implied.
**Cons:** Slightly less explicit for beginners.
**Best for:** Most production code. This is the Pythonic style.

---

### Approach 3: Ternary (One-liner)

```python
def max_of_two(a, b):
    return a if a >= b else b
```

**Pros:** Most concise. Single expression.
**Cons:** Harder to read for complex conditions. Can become nested and ugly.
**Best for:** Simple conditions. Avoid nesting ternaries.

---

### Approach 4: Built-in `max()`

```python
max_of_two = max  # just use the built-in
# or
result = max(a, b)
```

**Pros:** Zero code. Tested, optimized, handles edge cases.
**Cons:** The exercise says "no built-in max()" — but in real code, ALWAYS use built-ins.
**Best for:** Production code. Never reinvent what Python provides.

---

### Verdict

| Approach | Lines | Readability | Performance | Pythonic? |
|----------|-------|-------------|-------------|-----------|
| If/Else | 4 | ★★★★★ | ★★★★ | ★★★ |
| If no else | 3 | ★★★★ | ★★★★ | ★★★★★ |
| Ternary | 1 | ★★★ | ★★★★ | ★★★★ |
| Built-in | 0 | ★★★★★ | ★★★★★ | ★★★★★ |

**Winner for learning:** Approach 2 (if without else) — idiomatic and clear.
**Winner for production:** Approach 4 (built-in) — always use `max()`.

---

## Problem: Check if a Number is Even

### Approach 1: If/Else returning True/False

```python
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
```

**Pros:** Very explicit.
**Cons:** Redundant — `n % 2 == 0` already IS a boolean. Wrapping it in if/else adds nothing.

---

### Approach 2: Return the condition directly

```python
def is_even(n):
    return n % 2 == 0
```

**Pros:** One line. The expression `n % 2 == 0` evaluates to `True` or `False`, so just return it.
**Cons:** None — this is the best approach.
**Best for:** Always. This is the Pythonic way.

---

### Approach 3: Using bitwise AND

```python
def is_even(n):
    return (n & 1) == 0
```

**Pros:** Faster (bitwise operation).
**Cons:** Less readable. Most people don't know bitwise ops.
**Best for:** Performance-critical code (rare in Python). Avoid in normal code.

---

### Verdict

| Approach | Lines | Readability | Performance | Pythonic? |
|----------|-------|-------------|-------------|-----------|
| If/Else | 4 | ★★★ | ★★★★ | ★★ |
| Return condition | 1 | ★★★★★ | ★★★★ | ★★★★★ |
| Bitwise | 1 | ★★ | ★★★★★ | ★★ |

**Winner:** Approach 2 — return the boolean expression directly. This pattern (return condition instead of if/true/false) is used everywhere in Python.

---

## Problem: Convert Celsius to Fahrenheit

### Approach 1: Intermediate Variable

```python
def celsius_to_fahrenheit(c):
    f = c * 9 / 5 + 32
    return f
```

**Pros:** The variable `f` documents what the value is. Easy to debug (set breakpoint on `f`).
**Cons:** Extra line for a simple calculation.

---

### Approach 2: Direct Return

```python
def celsius_to_fahrenheit(c):
    return c * 9 / 5 + 32
```

**Pros:** Shorter. No unnecessary variable.
**Cons:** Formula is inline — harder to inspect intermediate value.
**Best for:** Simple one-line formulas.

---

### Approach 3: With Rounding

```python
def celsius_to_fahrenheit(c, decimals=1):
    return round(c * 9 / 5 + 32, decimals)
```

**Pros:** Controls output precision. Useful when displaying to users.
**Cons:** Changes the return type behavior (rounded float). Might lose precision for further calculations.
**Best for:** Display purposes. Don't round if the value will be used in further math.

---

### Verdict

| Approach | Lines | Readability | Flexibility | Pythonic? |
|----------|-------|-------------|-------------|-----------|
| Intermediate var | 2 | ★★★★ | ★★★ | ★★★★ |
| Direct return | 1 | ★★★★★ | ★★★ | ★★★★★ |
| With rounding | 1 | ★★★★ | ★★★★★ | ★★★★ |

**Winner:** Approach 2 for simple use. Approach 3 when you need controlled output.

---

## Key Takeaways

1. **Don't wrap booleans in if/else** — `return condition` is always better than `if condition: return True else: return False`.
2. **Use built-in functions** in production — `max()`, `min()`, `sum()`, `len()`. They're tested and optimized.
3. **Direct return** is preferred for simple expressions — no need for an intermediate variable.
4. **Avoid `else` after `return`** — if the `if` block returns, the code after it only runs when the condition is false.
5. **Readability > cleverness** — don't use bitwise tricks unless performance demands it.
