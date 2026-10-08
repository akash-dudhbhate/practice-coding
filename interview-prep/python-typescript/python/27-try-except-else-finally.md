# 27 — try / except / else / finally

> **Interview question:** "What do the `else` and `finally` blocks in a `try` statement do, and when does each one run?"
> **What the interviewer is really testing:** Whether you know the exact execution contract — `else` runs only when the `try` *succeeded*, `finally` runs *always* — and whether you understand why `else` exists at all instead of just putting the code inside `try`.

## Theory — what it is

A full `try` statement has four parts, each with a precise trigger condition:

- **`try:`** — the risky code. Python watches this block for exceptions.
- **`except SomeError:`** — runs **only if** an exception was raised in `try` *and* it matches this class. You can have several, checked top to bottom.
- **`else:`** — runs **only if** the `try` block finished *without* any exception. It does NOT run if an `except` fired.
- **`finally:`** — runs **always**: success, caught exception, uncaught exception, even after `return`/`break`/`continue`. It's the last thing that executes before control leaves the statement.

So the full flow is: run `try` → if it raised, find a matching `except`; if it didn't, run `else` → then run `finally` no matter what happened.

Two edge cases worth memorizing:
- If `finally` itself contains `return`, it **overrides** any `return` pending in `try` — a classic gotcha.
- `finally` runs *before* an uncaught exception continues propagating — cleanup happens first, crash second.

## Why it was needed

**Why `else` exists:** anything after `try:` could equally go *inside* the `try` block — so why a separate section? Because the `try` block's contents define what the `except` clauses protect. If you put success-path code inside `try`, an `except ValueError` will also catch a `ValueError` accidentally raised by that success code — a bug you never meant to handle gets silently "handled." `else` draws the line: *only* the risky lines live in `try`; everything the exception handlers shouldn't touch lives in `else`. It keeps the `try` block small, which is exactly what good exception handling wants.

**Why `finally` exists:** some cleanup must happen on *every* path — close a file, release a lock, rollback a transaction — including paths where the exception isn't caught here and is about to propagate. Duplicating cleanup in `try`, every `except`, and before every `return` is fragile; `finally` is the single guaranteed hook.

## Where it's used in a real project

- **Resource cleanup**: `finally: conn.close()` for DB connections, sockets, locks — must run even on exceptions the function doesn't catch.
- **Success-only work**: `try: data = fetch()` / `except NetworkError:` / `else: save_to_db(data)` — `save_to_db`'s own errors must NOT be caught by `except NetworkError`.
- **Transactions**: `try:` commit path, `except:` rollback, `finally:` release the connection back to the pool.
- **Metrics/timing**: `finally: timer.stop()` records the call duration whether it succeeded or blew up.

## Diagram

```
        try:
            risky()              <- the ONLY lines "protected" by except
            |
     exception raised?
       /           \
     YES            NO
      |              |
  matching        else:
  except?           more_work()   <- runs ONLY on success
   /     \           |
 catch   no match    |
  |       |          |
  |     propagate    |
   \      |         /
    \     v        /
     finally:
         cleanup()   <- runs ALWAYS (even before propagating,
                        even after return/break)
              |
        control leaves
```

## Code — explained

```python
def process(text):                                  # 1
    try:
        number = int(text)                          # 2
    except ValueError:
        print("except: not a number")               # 3
    else:
        print("else: doubled =", number * 2)        # 4
    finally:
        print("finally: always runs")               # 5

process("21")
print("---")
process("abc")
```

Output:

```
else: doubled = 42
finally: always runs
---
except: not a number
finally: always runs
```

1. A function so we can also discuss `return` interactions later.
2. `int(text)` is the only risky line — the only line the `except` protects.
3. Runs only when `int()` raises `ValueError`. Note `number` is undefined here — touching it would raise `NameError`.
4. Runs only when `try` succeeded. `number * 2` could itself raise (if `number` were weird), and that error would **not** be caught by the `except` above — which is the entire point of `else`.
5. Runs on both paths — success and failure. This is where `file.close()` / `lock.release()` go.

## Problems

### Easy — predict the output
**Problem:** Predict what this prints for `f(0)` and `f(2)`.
```python
def f(x):
    try:
        r = 10 / x
    except ZeroDivisionError:
        print("caught")
    else:
        print("ok", r)
    finally:
        print("done")
```
**Try this input:** `f(0)`, then `f(2)`
**Expected output:**
```
caught
done
ok 5.0
done
```
**Solution:**
```python
def f(x):
    try:
        r = 10 / x
    except ZeroDivisionError:
        print("caught")
    else:
        print("ok", r)
    finally:
        print("done")

f(0)
f(2)
```
**Logic explained:**
1. `f(0)`: `10 / 0` raises `ZeroDivisionError` → `except` prints `caught` → `else` skipped → `finally` prints `done`.
2. `f(2)`: division succeeds → `except` skipped → `else` prints `ok 5.0` → `finally` prints `done`.
3. `finally` prints in BOTH runs — that's its guarantee.

### Medium — else vs. inside-try
**Problem:** This function has a subtle bug. `report("500")` returns `"bad input"` even though `500` is perfectly valid input — because the `raise ValueError("too big to display")` *inside* the `try` gets caught by its own `except ValueError`. Refactor so the handler only protects `int(text)`, and the internal check surfaces instead.
```python
def report(text):
    try:
        n = int(text)
        if n > 100:
            raise ValueError("too big to display")   # swallowed as "bad input"!
        return f"value is {n}"
    except ValueError:
        return "bad input"
```
**Try this input:** `report("x")`, `report("5")`, `report("500")`
**Expected output:**
```
bad input
value is 5
internal error surfaced: too big to display
```
**Solution:**
```python
def report(text):
    try:
        n = int(text)                     # ONLY the risky parse is protected
    except ValueError:
        return "bad input"
    else:
        if n > 100:
            raise ValueError("too big to display")
        return f"value is {n}"

for t in ["x", "5", "500"]:
    try:
        print(report(t))
    except ValueError as e:
        print("internal error surfaced:", e)
```
**Logic explained:**
1. `int(text)` is the only line that should be covered by `except ValueError` — everything else moved to `else`.
2. `report("x")` → `int` raises `ValueError` → caught → `"bad input"`. Same as before.
3. `report("5")` → parse succeeds → `else` runs → `"value is 5"`.
4. `report("500")` → parse succeeds → `else` runs → the `ValueError("too big to display")` is raised **outside** the `try`, so it propagates to the caller's `except` and prints `internal error surfaced: too big to display` instead of the misleading `"bad input"`.
5. This is the whole reason `else` exists: it shrinks the blast radius of the `except` filter.

### Hard — finally overrides return
**Problem:** Predict and explain the output. Why doesn't it return `"from try"` or `"from except"`?
```python
def weird():
    try:
        return "from try"
    except Exception:
        return "from except"
    finally:
        return "from finally"
```
**Try this input:** `weird()`
**Expected output:** `from finally`
**Solution:**
```python
def weird():
    try:
        return "from try"
    except Exception:
        return "from except"
    finally:
        return "from finally"

print(weird())
```
**Logic explained:**
1. `try` hits `return "from try"` — Python prepares to return that value but must run `finally` first.
2. `finally` contains its own `return` — this **replaces** the pending return value entirely. `"from try"` is discarded.
3. Same rule applies to `except` returns and even to uncaught exceptions: a `return` (or new `raise`) inside `finally` silently swallows whatever was in flight — including exceptions! `finally: return x` will suppress an active exception, which is why returning from `finally` is considered a bug in real code (it's banned by linters like flake8-bugbear).
4. Correct use of `finally`: cleanup statements only — `close()`, `release()`, `print` — never `return`.

## The 30-second interview answer

"`try` runs the risky code; `except` runs only if a matching exception was raised; `else` runs only if `try` completed without any exception; `finally` runs always — success, caught or uncaught exception, even after `return`. I use `else` to keep the `try` block minimal: only the lines that can actually raise the exception I'm catching go inside `try`, so I never accidentally swallow a bug raised by success-path code. `finally` is for cleanup that must happen on every path — closing connections, releasing locks. One trap: a `return` inside `finally` overrides any pending return and can even suppress a propagating exception, so never return from `finally`."

## Follow-up trap

**"If `except` catches the error, does `else` still run?"** — No. `else` runs only when `try` raised *nothing*. It's "the try succeeded" block, not "the statement finished" block — that second job belongs to `finally`.

**"Does `finally` run if the exception is never caught?"** — Yes. `finally` executes while the exception is still propagating, before the frame is torn down. That's exactly why `conn.close()` belongs there: it runs even when this function doesn't handle the error.
