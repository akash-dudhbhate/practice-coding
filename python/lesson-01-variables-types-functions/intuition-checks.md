# Lesson 01 — Intuition Checks

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
