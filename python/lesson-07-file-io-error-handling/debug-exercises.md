# Lesson 07 — Debug Exercises

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
