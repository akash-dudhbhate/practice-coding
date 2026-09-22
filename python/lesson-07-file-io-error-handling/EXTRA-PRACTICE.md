# lesson-07-file-io-error-handling — Extra Practice
Everything beyond the core lesson lives here, in order:
mental quizzes → debug drills → mistakes → refactoring → comparisons.

---

## Intuition Checks — predict before you run

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

---

## Debug Exercises — find and fix the bug

## Debug 01 (Easy): Read File — Not Using `with`
```python
def read_file(path):
    f = open(path, "r")
    return f.read()
```
**Hint:** What happens to the file handle?

<details><summary>Answer</summary>
**Bug:** File is never closed. `f.close()` is missing. If called many times, file handles leak.
**Fix:** Use `with open(path) as f:` — auto-closes even on errors.
</details>

## Debug 02 (Medium): Write File — Wrong Mode
```python
def append_log(path, message):
    with open(path, "w") as f:
        f.write(message + "\n")
```
**Hint:** What happens to existing content?

<details><summary>Answer</summary>
**Bug:** `"w"` mode OVERWRITES the file. Each call erases previous logs.
**Fix:** Use `"a"` (append) mode.
</details>

## Debug 03 (Hard): Bare Except
```python
def safe_int(s):
    try:
        return int(s)
    except:
        return None
```
**Hint:** What if the user presses Ctrl+C?

<details><summary>Answer</summary>
**Bug:** Bare `except:` catches EVERYTHING including KeyboardInterrupt and SystemExit. The user can't Ctrl+C.
**Fix:** `except ValueError:` — catch only the expected exception.
</details>

---

## Common Mistakes — the traps learners hit

## Mistake 01: Not using `with`
```python
# WRONG — file never closed
f = open("file.txt")
data = f.read()

# CORRECT
with open("file.txt") as f:
    data = f.read()
```

## Mistake 02: Bare except
```python
# WRONG — catches everything
try:
    ...
except:
    pass

# CORRECT — catch specific exceptions
try:
    ...
except (ValueError, TypeError) as e:
    print(f"Error: {e}")
```

## Mistake 03: Using "w" when you mean "a"
```python
# WRONG — overwrites existing content
with open("log.txt", "w") as f:
    f.write("new log\n")

# CORRECT — appends
with open("log.txt", "a") as f:
    f.write("new log\n")
```

## Mistake 04: Not handling file-not-found
```python
# WRONG — crashes if file missing
with open("config.json") as f:
    config = json.load(f)

# CORRECT
try:
    with open("config.json") as f:
        config = json.load(f)
except FileNotFoundError:
    config = {}
```

## Mistake 05: Swallowing exceptions
```python
# WRONG — hides bugs
try:
    do_something()
except:
    pass  # silently ignores ALL errors

# CORRECT — log or handle
try:
    do_something()
except Exception as e:
    logging.error(f"Failed: {e}")
    raise  # re-raise if you can't handle it
```

---

## Refactoring Challenges — make working code better

## Refactor 01 (Easy): Manual File Close
### Before
```python
f = open("data.txt", "r")
content = f.read()
f.close()
return content
```
### After
```python
with open("data.txt") as f:
    return f.read()
```

## Refactor 02 (Medium): Bare Except
### Before
```python
try:
    result = int(user_input)
except:
    result = 0
```
### After
```python
try:
    result = int(user_input)
except ValueError:
    result = 0
```

## Refactor 03 (Hard): Repeated Try/Except
### Before
```python
def safe_int(s):
    try: return int(s)
    except: return None
def safe_float(s):
    try: return float(s)
    except: return None
def safe_bool(s):
    try: return bool(s)
    except: return None
```
### After
```python
def safe_convert(value, converter):
    try: return converter(value)
    except (ValueError, TypeError): return None

safe_int = lambda s: safe_convert(s, int)
safe_float = lambda s: safe_convert(s, float)
```

---

## Approach Comparison — different ways to solve it

## Problem: Read a File Safely

### Approach 1: try/except
```python
def read_file(path):
    try:
        with open(path) as f:
            return f.read()
    except FileNotFoundError:
        return None
```

### Approach 2: Check then open (TOCTOU)
```python
import os
def read_file(path):
    if os.path.exists(path):
        with open(path) as f:
            return f.read()
    return None
```
**Bug!** Race condition — file could be deleted between `exists()` and `open()`. "Time of Check to Time of Use" (TOCTOU).

**Winner:** Approach 1 (try/except) — "Easier to Ask Forgiveness than Permission" (EAFP). Pythonic.

---

## Problem: Safe Integer Conversion

### Approach 1: try/except
```python
def safe_int(s):
    try:
        return int(s)
    except ValueError:
        return None
```

### Approach 2: isdigit check
```python
def safe_int(s):
    if s.isdigit():
        return int(s)
    return None
```
**Bug!** `"-5".isdigit()` is False — doesn't handle negative numbers.

**Winner:** Approach 1 — handles all valid int formats including negatives.
