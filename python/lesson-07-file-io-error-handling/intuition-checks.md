# Lesson 07 — Intuition Checks

## Check 01: With Statement
```python
with open("test.txt", "w") as f:
    f.write("hello")
print(f.closed)
```
What prints?

<details><summary>Answer</summary>
`True` — `with` automatically closes the file when the block exits, even if an exception occurs.
</details>

## Check 02: Exception Order
```python
try:
    result = 10 / 0
except ZeroDivisionError:
    result = "zero"
except Exception:
    result = "other"
print(result)
```
What prints?

<details><summary>Answer</summary>
`zero` — Specific exceptions must come BEFORE general ones. `ZeroDivisionError` is caught first.
</details>

## Check 03: Finally Always Runs
```python
try:
    return "try"
finally:
    print("finally")
```
What happens?

<details><summary>Answer</summary>
Prints "finally" THEN returns "try". `finally` ALWAYS runs, even if the function returns or an exception occurs.
</details>

## Check 04: Raise vs Return
```python
def divide(a, b):
    if b == 0:
        raise ValueError("zero!")
    return a / b

try:
    divide(1, 0)
except ValueError as e:
    print(e)
```
What prints?

<details><summary>Answer</summary>
`zero!` — `raise` throws an exception. The `except` catches it and `as e` binds the exception to `e`.
</details>

## Check 05: File Modes
```python
# What does each mode do?
# "r" → ?
# "w" → ?
# "a" → ?
# "r+" → ?
```
<details><summary>Answer</summary>
- `"r"` — read (file must exist)
- `"w"` — write (creates or OVERWRITES)
- `"a"` — append (creates or appends to end)
- `"r+"` — read and write (file must exist, doesn't truncate)
</details>
