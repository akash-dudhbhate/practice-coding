# Lesson 01 — Debug Exercises

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
