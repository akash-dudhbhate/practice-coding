# Lesson 07 — Concepts Explained (File I/O & Error Handling)

> Read this before solving the problems. Each concept explains:
> **What** it is · **Why** it exists · **Where** it's used · **What goes wrong** without it.

---

## Opening & Reading Files

**What:** `open(path, mode)` opens a file and returns a file object. `mode` is `"r"` (read), `"w"` (write/overwrite), `"a"` (append), `"rb"`/`"wb"` (binary).

```python
f = open("data.txt", "r")   # open for reading
content = f.read()          # whole file as one string
f.close()                   # MUST close to release resources

# Read line by line:
f = open("data.txt")
for line in f:
    print(line.strip())     # strip the trailing newline
f.close()

lines = open("data.txt").readlines()  # list of lines (with newlines)
```

**Why it exists:** Programs need to persist and load data — config, logs, user data, exports. Files are the most basic persistent storage.

**Where it's used:** Reading config, processing logs, loading datasets, saving output, CSV/JSON files.

**What goes wrong without it:**
- Forgetting `f.close()` → file stays open, locks held, data may not flush to disk, resource leaks. On Windows you can't delete a file that's still open.
- `FileNotFoundError` if the path doesn't exist (in read mode).
- `read()` on a huge file loads it all into memory → program crashes. Stream line-by-line instead.

---

## The `with` Statement (Context Manager)

**What:** `with` automatically closes the file (or releases the resource) when the block exits — even if an error occurs.

```python
with open("data.txt", "r") as f:
    content = f.read()
# f is automatically closed here, no matter what happened inside

with open("out.txt", "w") as f:
    f.write("hello\n")
# file flushed and closed automatically
```

**Why it exists:** Manually closing files is error-prone — you forget, or an exception skips the `close()`. `with` guarantees cleanup, making resource management safe and automatic.

**Where it's used:** Every file operation in modern Python. Also used for locks, database connections, network sockets — anything that needs cleanup.

**What goes wrong without it:**
- Without `with`, an exception between `open()` and `close()` leaves the file open.
- Forgetting to close many files in a loop → "Too many open files" error.
- Using `f` outside the `with` block → file is closed; operations fail with `ValueError: I/O operation on closed file`.

---

## Writing to Files

**What:** `write(string)` writes text; `writelines(list)` writes each item. `"w"` overwrites; `"a"` appends.

```python
with open("out.txt", "w") as f:
    f.write("first line\n")
    f.write("second line\n")

with open("out.txt", "a") as f:
    f.write("appended line\n")

with open("lines.txt", "w") as f:
    f.writelines(["a\n", "b\n", "c\n"])
```

**Why it exists:** Programs must produce output — reports, logs, generated code, exports. Writing to files persists results beyond the program's run.

**Where it's used:** Logging, generating reports, saving processed data, writing config, exporting CSV/JSON.

**What goes wrong without it:**
- `"w"` mode TRUNCATES (erases) the file immediately on open. Using `"w"` when you meant `"a"` destroys existing data.
- `write()` does NOT add a newline — you must add `\n` yourself. Forgetting this puts everything on one line.
- `writelines()` does NOT add newlines either (despite the name) — add them in your data.
- Writing text to a file opened in binary mode (`"wb"`) → `TypeError: a bytes-like object is required`.

---

## try / except / finally

**What:** `try` runs code that might fail; `except` handles the error; `finally` always runs (cleanup).

```python
try:
    value = int(input("Enter a number: "))
    result = 10 / value
except ValueError:
    print("That's not a number")
except ZeroDivisionError:
    print("Can't divide by zero")
except Exception as e:        # catch-all (use sparingly)
    print(f"Unexpected error: {e}")
finally:
    print("This always runs")  # cleanup, close files, etc.
```

**Why it exists:** Programs run in an unpredictable world — bad input, missing files, network failures. Without error handling, one error crashes the whole program. `try/except` lets you recover gracefully.

**Where it's used:** Input validation, file/network operations, parsing, anywhere external input could be malformed.

**What goes wrong without it:**
- Bare `except:` (no exception type) catches EVERYTHING including `KeyboardInterrupt` and `SystemExit` — hides bugs and makes Ctrl-C not work. Always catch specific exceptions.
- Catching too broadly and silently passing → errors are swallowed, bugs hide forever. At least log the error.
- Forgetting `finally` for cleanup → resources leak when an exception occurs.
- Putting too much code in `try` → you catch errors from the wrong line. Keep `try` blocks small.

---

## Raising Exceptions

**What:** `raise` throws an exception intentionally, stopping normal flow until something catches it.

```python
def set_age(age):
    if age < 0:
        raise ValueError("age cannot be negative")
    if not isinstance(age, int):
        raise TypeError("age must be an integer")
    return age

# Re-raising:
try:
    do_something()
except ValueError:
    log_error()
    raise     # re-raise the same exception
```

**Why it exists:** When your function detects an invalid state, it should fail loudly and clearly rather than return garbage. Raising forces the caller to deal with the problem.

**Where it's used:** Input validation, precondition checks, signaling unsupported operations, enforcing invariants.

**What goes wrong without it:**
- Returning `None` or `-1` on error instead of raising → caller doesn't know an error happened, uses the bad value, bugs propagate silently.
- `raise ValueError("msg")` vs `raise ValueError` (no parens) — both work, but the message version is far more helpful for debugging.
- Raising in a `finally` block masks the original exception — avoid it.

---

## Custom Exceptions

**What:** You define your own exception classes by subclassing `Exception`. This lets callers catch your specific errors.

```python
class InsufficientFundsError(Exception):
    """Raised when a withdrawal exceeds the balance."""
    pass

class Account:
    def __init__(self, balance):
        self.balance = balance
    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(
                f"Need {amount}, have {self.balance}"
            )
        self.balance -= amount

try:
    Account(100).withdraw(150)
except InsufficientFundsError as e:
    print(e)   # "Need 150, have 100"
```

**Why it exists:** Built-in exceptions (`ValueError`, etc.) are generic. Custom exceptions let callers handle YOUR errors specifically without catching unrelated ones. They also carry domain meaning.

**Where it's used:** Libraries and apps with specific error conditions — payment failures, auth errors, validation rules, API errors.

**What goes wrong without it:**
- Using generic `Exception` or `ValueError` for everything → callers can't distinguish your errors from others; `except ValueError` catches too much.
- Subclassing `BaseException` directly instead of `Exception` → `except Exception:` won't catch it (e.g., `KeyboardInterrupt` inherits `BaseException`). Always subclass `Exception`.
- Not adding a docstring/message → debugging is harder.

---

## Common File/IO Exceptions

**What:** The exceptions you'll meet most when doing I/O.

```python
FileNotFoundError     # file doesn't exist (read mode)
PermissionError       # no read/write permission
IsADirectoryError     # path is a directory, not a file
FileExistsError       # file exists (with 'x' exclusive mode)
ValueError            # I/O on closed file, bad mode
UnicodeDecodeError    # reading bytes as text with wrong encoding
```

**Why it exists:** Different failure modes need different handling — "file missing" might prompt the user, "permission denied" might log and skip. Distinct exceptions let you respond appropriately.

**Where it's used:** Robust file processing, batch jobs that should continue past bad files, user-facing apps with friendly error messages.

**What goes wrong without it:**
- Catching only `Exception` hides WHICH error occurred → you can't give a useful message.
- `UnicodeDecodeError` when reading a non-UTF-8 file as text → specify `encoding="utf-8"` or open in binary mode.
- Not handling `PermissionError` → one unreadable file crashes a batch job processing thousands.

---

## Reading & Writing JSON

**What:** `json` module converts between Python objects and JSON text.

```python
import json

data = {"name": "Akash", "scores": [90, 85, 88]}

# Write
with open("data.json", "w") as f:
    json.dump(data, f, indent=2)

# Read
with open("data.json") as f:
    loaded = json.load(f)
# loaded == data

# Strings
json.dumps(data)        # '{"name": "Akash", ...}'  (to string)
json.loads('{"a": 1}')  # {"a": 1}  (from string)
```

**Why it exists:** JSON is the lingua franca of APIs and config. It's human-readable and language-agnostic. The `json` module handles conversion so you work with Python dicts/lists, not raw text.

**Where it's used:** API responses, config files, data exchange between languages, storing structured data.

**What goes wrong without it:**
- `json.load` on malformed JSON → `json.JSONDecodeError`. Wrap in try/except for user-provided files.
- `dump` of non-serializable objects (datetime, custom classes) → `TypeError: Object of type ... is not JSON serializable`. Convert first or use a `default=` handler.
- `load` vs `loads`: `load(file)`, `loads(string)`. Mixing them up causes errors.
