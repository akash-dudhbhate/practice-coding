# lesson-01-variables-types-functions — Extra Practice
Everything beyond the core lesson lives here, in order:
mental quizzes → debug drills → mistakes → refactoring → comparisons.

---

## Intuition Checks — predict before you run

> **Don't run the code.** Answer mentally first, then check.
> These build your mental model of how Python works — the #1 predictor of coding speed.

---

## Check 01: Variable Assignment

```python
a = 5
b = a
a = 10
print(b)
```

**What prints?**
- (A) 10
- (B) 5
- (C) Error

<details>
<summary>Answer</summary>

**(B) 5**

`b = a` copies the VALUE (5) into b. When `a` changes to 10, `b` still holds 5. Variables are labels for values, not references to each other.
</details>

---

## Check 02: Integer Division

```python
print(7 / 2)
print(7 // 2)
print(7 % 2)
```

**What prints (3 lines)?**

<details>
<summary>Answer</summary>

```
3.5
3
1
```

- `/` always returns a float (even for whole numbers: `6 / 2` → `3.0`)
- `//` is floor division (truncates toward negative infinity)
- `%` is the remainder
</details>

---

## Check 03: Function Return

```python
def greet(name):
    print(f"Hello, {name}!")

result = greet("Akash")
print(result)
```

**What prints (2 lines)?**

<details>
<summary>Answer</summary>

```
Hello, Akash!
None
```

The function PRINTS the greeting but doesn't RETURN anything. Functions without `return` return `None`. `print(result)` prints `None`.
</details>

---

## Check 04: Type of Result

```python
x = 10 / 2
print(type(x).__name__)
```

**What prints?**
- (A) int
- (B) float
- (C) str

<details>
<summary>Answer</summary>

**(B) float**

`/` ALWAYS returns a float, even when the result is a whole number. `10 / 2` → `5.0` (float), not `5` (int). Use `//` if you want integer division.
</details>

---

## Check 05: Default Arguments

```python
def add_to(item, lst=[]):
    lst.append(item)
    return lst

print(add_to(1))
print(add_to(2))
```

**What prints (2 lines)?**

<details>
<summary>Answer</summary>

```
[1]
[1, 2]
```

Default mutable arguments (lists, dicts) are created ONCE when the function is defined, not each call. Both calls share the same list. This is the #1 Python gotcha. Fix: use `lst=None` and create inside.
</details>

---

## Scoring

- **5/5:** Excellent — you have strong Python intuition
- **3-4/5:** Good — review the ones you missed
- **1-2/5:** Re-read concepts.md before continuing
- **0/5:** Go back and study the lesson again — don't rush

---

## Debug Exercises — find and fix the bug

> **Fix the broken code.** Each snippet has 1-3 bugs. Find them, explain why they're wrong, and write the fix.
> Don't run the code until you've identified the bug mentally — this trains your debugging intuition.

---

## Debug 01 (Easy): Max of Two — Syntax Error

```python
def max_of_two(a, b)
    if a > b:
        return a
    else
        return b
```

**Hint:** Python uses colons to start blocks.

<details>
<summary>Click to reveal the bugs</summary>

**Bugs:**
1. Missing colon `:` after `def max_of_two(a, b)` — line 1
2. Missing colon `:` after `else` — line 4

**Why:** Python requires `:` at the end of `def`, `if`, `else`, `for`, `while`, `class` statements to indicate a block follows.

**Fix:**
```python
def max_of_two(a, b):
    if a > b:
        return a
    else:
        return b
```
</details>

---

## Debug 02 (Medium): Even Check — Logic Error

```python
def is_even(n):
    if n % 2 == 1:
        return True
    return False
```

**Hint:** What does "even" mean? Check the condition.

<details>
<summary>Click to reveal the bug</summary>

**Bug:** The condition checks for ODD (`n % 2 == 1`), not even. It returns `True` for odd numbers and `False` for even numbers — the opposite of what the function name says.

**Why:** `n % 2 == 1` is true for odd numbers (1, 3, 5...). For even numbers, `n % 2 == 0`. The function name says `is_even` but the logic checks for odd.

**Fix:**
```python
def is_even(n):
    if n % 2 == 0:
        return True
    return False
```

**Even better (idiomatic):**
```python
def is_even(n):
    return n % 2 == 0
```
</details>

---

## Debug 03 (Hard): Temperature Conversion — Multiple Bugs

```python
def celsius_to_fahrenheit(c):
    f = c * 9 / 5
    return f

def fahrenheit_to_celsius(f):
    c = (f - 32) * 5 / 9
    return f

# Test
print(celsius_to_fahrenheit(100))  # Should print 212.0
print(fahrenheit_to_celsius(212))  # Should print 100.0
```

**Hint:** Check the formula AND the return statements. There are 2 bugs.

<details>
<summary>Click to reveal the bugs</summary>

**Bug 1:** `celsius_to_fahrenheit` is missing `+ 32`. The formula is `F = C * 9/5 + 32`, not just `C * 9/5`. So `celsius_to_fahrenheit(100)` returns `180.0` instead of `212.0`.

**Bug 2:** `fahrenheit_to_celsius` returns `f` (the input) instead of `c` (the calculated value). The calculation is correct but the wrong variable is returned.

**Why:** Bug 1 is a formula error — forgetting the offset. Bug 2 is a variable name error — returning the input instead of the result. Both are extremely common in real code.

**Fix:**
```python
def celsius_to_fahrenheit(c):
    return c * 9 / 5 + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9
```
</details>

---

## How to use these exercises

1. **Read the code** and try to spot the bug WITHOUT running it.
2. **Write down** what you think is wrong and why.
3. **Check** by revealing the answer.
4. **Fix it** in your editor and run to verify.
5. **Reflect:** Could you have prevented this bug? What habit would help?

> **The goal:** Train your eyes to see bugs before they happen. After 100 debug exercises, you'll catch 80% of bugs mentally before running code.

---

## Common Mistakes — the traps learners hit

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

---

## Refactoring Challenges — make working code better

> **Take working but ugly code and make it better.** Same output, cleaner code.
> This trains your eye for code quality — the skill that separates juniors from seniors.

---

## Refactor 01 (Easy): Verbose If/Else

### Before
```python
def check_number(n):
    if n > 0:
        return True
    else:
        return False
```

### Problems
1. `if/else` returning True/False is redundant — the condition IS a boolean
2. `else` is unnecessary when `if` returns

### After
```python
def check_number(n):
    return n > 0
```

### What you learned
**Return the condition directly.** `n > 0` already evaluates to `True` or `False`. Wrapping it in if/else adds 3 lines for nothing.

---

## Refactor 02 (Medium): Repeated Logic

### Before
```python
def process_data(data):
    result = []
    for item in data:
        if item > 0:
            result.append(item * 2)
    return result
```

### Problems
1. Manual loop + append is verbose
2. Filter and transform in one step is less readable

### After
```python
def process_data(data):
    return [item * 2 for item in data if item > 0]
```

### What you learned
**List comprehensions replace filter+transform loops.** One line, faster, more Pythonic. The pattern: `[transform for item in iterable if condition]`.

---

## Refactor 03 (Hard): Nested Conditionals

### Before
```python
def calculate_price(quantity, price, discount):
    if quantity > 0:
        if price > 0:
            if discount > 0:
                total = quantity * price
                total = total - (total * discount / 100)
                return total
            else:
                return quantity * price
        else:
            return 0
    else:
        return 0
```

### Problems
1. Deep nesting (3 levels) — hard to read
2. Repeated `return 0` for error cases
3. `total = total - ...` should use `-=` 
4. Discount logic mixed with validation

### After
```python
def calculate_price(quantity, price, discount):
    if quantity <= 0 or price <= 0:
        return 0
    total = quantity * price
    if discount > 0:
        total -= total * discount / 100
    return total
```

### What you learned
1. **Guard clauses first** — handle error cases early, return immediately. Flattens nesting.
2. **Combine conditions** — `quantity <= 0 or price <= 0` replaces two nested ifs.
3. **Use `-=`** — compound assignment is cleaner than `x = x - y`.

---

## Refactoring Checklist

When reviewing code, ask:
- [ ] Can an if/else returning True/False be just `return condition`?
- [ ] Can a loop with append be a list comprehension?
- [ ] Can nested ifs be flattened with guard clauses (early return)?
- [ ] Can repeated code be extracted to a function?
- [ ] Can `x = x + y` be `x += y`?
- [ ] Can verbose conditions be combined with `and`/`or`?
- [ ] Is the function doing ONE thing? (Single Responsibility)
- [ ] Are variable names descriptive? (`data` vs `user_emails`)

> **The goal:** After 100 refactoring challenges, you'll write clean code the first time — because your eyes have seen the difference 100 times.

---

## Approach Comparison — different ways to solve it

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
