# Lesson 07 — File I/O & Error Handling

## What you'll learn
- Reading and writing files with `open()` and `with`.
- Handling errors with `try`/`except`/`finally`.
- Raising and defining custom exceptions.
- Reading and writing JSON.

## Lesson

Files persist data; error handling keeps your program alive when things go wrong.

### File I/O
```python
with open("data.txt") as f:      # auto-closes
    content = f.read()

with open("out.txt", "w") as f:
    f.write("hello\n")
```

### Error handling
```python
try:
    value = int(input())
except ValueError:
    print("Not a number")
finally:
    print("always runs")
```

### Custom exceptions
```python
class MyError(Exception):
    pass
raise MyError("something went wrong")
```

### Key rules
- Always use `with` for files — it guarantees closing.
- `"w"` overwrites; `"a"` appends; `write()` adds no newline.
- Catch SPECIFIC exceptions, never bare `except:`.
- Subclass `Exception`, not `BaseException`.

---

## Your Tasks

This lesson has **9 practice problems** across three difficulty levels. Start with `easy/` and work your way up. Each problem file has the description at the top — **write your complete solution from scratch below** (function signature + body) to practice remembering syntax.

### Easy (start here)
1. `easy/p01-solve.py` — `read_file(path)`: return the full contents of a file as a string using `with`. Raise `FileNotFoundError` handling: return `None` if the file doesn't exist.
2. `easy/p02-solve.py` — `write_file(path, text)`: write `text` to `path` using `with` (overwrite mode). Return `True` on success.
3. `easy/p03-solve.py` — `safe_int(s)`: try to convert `s` to int; return the int, or `None` if it fails (catch `ValueError`).

### Medium
4. `medium/p01-solve.py` — `count_lines(path)`: return the number of lines in a file. Return `0` if the file doesn't exist (handle `FileNotFoundError`).
5. `medium/p02-solve.py` — `append_log(path, message)`: append `message` + newline to `path` (create if missing). Use `"a"` mode.
6. `medium/p03-solve.py` — `read_json(path)`: read a JSON file and return the parsed object. Return `None` on `FileNotFoundError` or `json.JSONDecodeError`.

### Hard
7. `hard/p01-solve.py` — `safe_divide(a, b)`: return `a / b`; raise a custom `DivideByZeroError(Exception)` if `b == 0`; raise `TypeError` if inputs aren't numeric.
8. `hard/p02-solve.py` — `process_file(path)`: read a file of one-number-per-line, return the sum. Skip blank lines. Handle missing file by raising `FileNotFoundError` with a clear message; handle non-numeric lines by skipping them with a warning print.
9. `hard/p03-solve.py` — `config_loader(path)`: read a JSON config file; validate it has a `"host"` key (raise custom `ConfigError(Exception)` if missing); return the config dict. Handle file-not-found and bad-JSON by raising `ConfigError` with a helpful message.

### How to work
- Open a problem file, read the description in the header comment.
- Write your **complete solution from scratch** below the TODO marker.
- Remove the TODO line when done.
- Run `python <filename>` to test with your own inputs.
- When done, tell me and I'll review. Say **"give me next task"** to advance to the next lesson.
