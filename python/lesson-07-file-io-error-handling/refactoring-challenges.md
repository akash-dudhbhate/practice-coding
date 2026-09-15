# Lesson 07 — Refactoring Challenges

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
