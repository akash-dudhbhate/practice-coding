# 26 — Exception best practices

> **Interview question:** "Why is a bare `except:` considered a bug? How do you decide which exceptions to catch?"
> **What the interviewer is really testing:** Do you understand that `except` is a *filter*, that the filter works by class inheritance, and that catching too broadly hides real bugs — or have you just been told "bare except is bad" without knowing why.

## Theory — what it is

When code fails, Python creates an **exception object** and unwinds the call stack until it finds an `except` block whose class matches. "Matches" means: the raised exception is an instance of the `except` class **or a subclass of it**. So `except ValueError` catches `ValueError` and anything inheriting from it, but not `TypeError` or `KeyError` — those are siblings in the tree, not children.

A **bare `except:`** (no class at all) is the widest possible filter: it catches *everything*, including `KeyboardInterrupt` (Ctrl+C), `SystemExit` (`sys.exit()`), and `GeneratorExit`. Those live under `BaseException`, a level *above* `Exception`, precisely so normal error handling doesn't touch them. Bare `except:` reaches up and grabs them anyway.

The practical rule: **catch the most specific exception you can actually handle.** If you can't do anything useful with the error — retry, fall back, translate it — let it propagate. A bug that crashes loudly is easier to find than a bug that gets swallowed and corrupts data quietly.

"Jargon" decoded: **unwinding the stack** = abandoning each running function until an `except` is found. **Propagate** = letting the exception keep traveling up to the caller.

## Why it was needed

Bare `except:` causes three concrete disasters:

1. **It hides bugs.** A `TypeError` from a typo inside your `try` gets caught and treated as "the expected failure." You debug for hours because the real traceback never surfaces.
2. **It breaks program control.** `except:` catches `KeyboardInterrupt`, so Ctrl+C stops working — the user literally cannot kill your script. `SystemExit` from `sys.exit()` is also swallowed, so the program refuses to exit.
3. **It destroys information.** `except:` gives you no `as e` object, no message, no type — you learn nothing about what went wrong.

Python's designers put `KeyboardInterrupt` and `SystemExit` under `BaseException` — *outside* `Exception` — specifically so that `except Exception` ("catch everything reasonable") is safe, while bare `except:` remains a footgun.

## Where it's used in a real project

- **API calls**: `except requests.Timeout:` retries; `except requests.HTTPError:` logs and returns 502 — different failures, different reactions.
- **Parsing user input**: `except ValueError:` around `int(text)` catches bad input without masking a `NameError` in the same block.
- **Cleanup boundaries**: `except Exception:` at a top-level worker loop logs the crash and continues to the next job — broad catch is OK *only* at a boundary where you log and re-raise or record.
- **Libraries**: SDKs raise specific error trees (`botocore.exceptions.ClientError` subclasses) so users can filter precisely.

## Diagram

```
BaseException                     <- bare "except:" catches ALL of this
   |
   +-- KeyboardInterrupt          <- Ctrl+C   (must NOT be swallowed)
   +-- SystemExit                 <- sys.exit()
   +-- GeneratorExit
   |
   +-- Exception                  <- "except Exception" catches this subtree
         |
         +-- ArithmeticError
         |      +-- ZeroDivisionError
         +-- LookupError
         |      +-- KeyError
         |      +-- IndexError
         +-- TypeError
         +-- ValueError           <- except ValueError catches ONLY this box
                                    (+ its subclasses)

except:                  -> the whole tree  (BUG)
except BaseException:    -> the whole tree  (equally bad)
except Exception:        -> Exception subtree (OK at top-level only)
except ValueError:       -> one branch      (what you usually want)
```

## Code — explained

```python
def parse_age(text):                        # 1
    return int(text)


# BAD — bare except swallows everything
def bad_parse(text):
    try:
        return parse_age(text)              # 2
    except:                                 # 3
        return -1                           # 4


# GOOD — catch only what you can handle
def good_parse(text):
    try:
        return parse_age(text)
    except ValueError as e:                 # 5
        print(f"not a number: {e}")
        return -1


print(good_parse("abc"))                    # 6
```

1. `int("abc")` raises `ValueError` — a specific, documented failure.
2. Suppose `parse_age` were renamed but this call site wasn't updated — that's a `NameError` bug.
3. `except:` catches the `NameError` *and* the `ValueError` — the typo is invisible.
4. Returning `-1` on *any* failure means a code bug silently produces a wrong value.
5. `except ValueError as e` — the filter matches only `ValueError` (and its subclasses). A `NameError` or `TypeError` would still crash loudly, which is what you want while developing.
6. Output: `not a number: invalid literal for int() with base 10: 'abc'` then `-1`.

## Problems

### Easy — replace the bare except
**Problem:** This function hides bugs. Fix it to catch only the real failure, so `int()` errors return `0` but other bugs still crash.
```python
def to_int(text):
    try:
        return int(text)
    except:
        return 0
```
**Try this input:** `to_int("42")`, `to_int("oops")`
**Expected output:**
```
42
0
```
**Solution:**
```python
def to_int(text):
    try:
        return int(text)
    except ValueError:
        return 0

print(to_int("42"))
print(to_int("oops"))
```
**Logic explained:**
1. `int()` raises `ValueError` for bad strings — that's the one expected failure.
2. `except ValueError` catches exactly that; a typo elsewhere (`itn(text)`) now raises `NameError` and crashes visibly instead of returning `0`.
3. `to_int("42")` succeeds → `42`. `to_int("oops")` → `ValueError` → `0`.

### Medium — order the except blocks
**Problem:** Given the hierarchy `ZeroDivisionError` is a child of `ArithmeticError`, fix this code so the specific message wins (right now the general handler shadows it).
```python
def divide(a, b):
    try:
        return a / b
    except ArithmeticError:
        return "math error"
    except ZeroDivisionError:
        return "cannot divide by zero"
```
**Try this input:** `divide(10, 0)`, `divide(10, 2)`
**Expected output:**
```
cannot divide by zero
5.0
```
**Solution:**
```python
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:       # most specific FIRST
        return "cannot divide by zero"
    except ArithmeticError:         # general LAST
        return "math error"

print(divide(10, 0))
print(divide(10, 2))
```
**Logic explained:**
1. Python checks `except` blocks top to bottom and uses the **first** match.
2. `ZeroDivisionError` IS an `ArithmeticError`, so `except ArithmeticError` placed first would match it and the specific block would be dead code.
3. Reordered: `divide(10, 0)` hits `ZeroDivisionError` first → `"cannot divide by zero"`. `divide(10, 2)` returns `5.0`.
4. Rule of thumb: children before parents, always.

### Hard — catch a tuple, but re-raise the rest
**Problem:** Write `load_config(text)` that parses `key=value` lines. On `ValueError` *or* `IndexError` return `{}` (bad config is expected); any other exception must propagate. Demonstrate with a line missing `=` and a line that triggers a bug you should NOT catch.
**Try this input:** `load_config("a=1\nbroken")` and `load_config(None)`
**Expected output:**
```
{}
AttributeError escaped: 'NoneType' object has no attribute 'splitlines'
```
**Solution:**
```python
def load_config(text):
    try:
        config = {}
        for line in text.splitlines():
            key, value = line.split("=")        # ValueError: no "="
            config[key.strip()] = value.strip()
        return config
    except (ValueError, IndexError):            # expected parse failures only
        return {}
    # anything else (e.g. TypeError from None.splitlines()) propagates

print(load_config("a=1\nbroken"))               # -> {}
try:
    load_config(None)
except AttributeError as e:
    print("AttributeError escaped:", e)
```
**Logic explained:**
1. `"broken"` has no `"="`, so `line.split("=")` returns one element and unpacking into `key, value` raises `ValueError` → caught → `{}`.
2. `except (ValueError, IndexError)` is a **tuple catch** — one block handling several unrelated exception types.
3. `None.splitlines()` raises `AttributeError` — NOT in the tuple — so it escapes the function.
4. The caller's `except AttributeError` catches it and prints `AttributeError escaped: ...`. The narrow filter did its job: expected failures handled, unexpected bugs visible.

## The 30-second interview answer

"`except` is a filter matched by class inheritance — `except SomeError` catches that class and all its subclasses. A bare `except:` catches *everything*, including `KeyboardInterrupt` and `SystemExit`, which live under `BaseException` specifically to avoid normal handlers — so bare except can make Ctrl+C stop working and can swallow a `TypeError` typo as if it were an expected failure. My rule: catch the most specific exception I can actually do something about, order handlers from specific to general, and if I truly need a broad catch — like at the top of a worker loop — I use `except Exception`, log the full traceback, and usually re-raise."

## Follow-up trap

**"So `except Exception:` is always safe?"** — No. It's *safer* (it skips `KeyboardInterrupt`/`SystemExit`) but still swallows every bug in the `try` block. It's only appropriate at a top-level boundary where you log and record the failure, never around two lines where you could name the real error.

**"What about `except:` with a `raise` after it — is that fine?"** — Mostly yes: `except: ... cleanup ...; raise` re-raises the same exception, so nothing is swallowed. But `finally:` usually expresses that intent better — cleanup that runs whether or not an exception occurred.
