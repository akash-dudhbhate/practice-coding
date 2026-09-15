# Lesson 07 — Approach Comparison

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
