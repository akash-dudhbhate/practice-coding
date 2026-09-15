# Lesson 07 — Common Mistakes

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
