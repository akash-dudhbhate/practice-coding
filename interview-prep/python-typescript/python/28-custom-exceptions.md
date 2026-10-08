# 28 — Custom exceptions

> **Interview question:** "When would you define your own exception classes, and how would you design the hierarchy?"
> **What the interviewer is really testing:** Do you understand that exceptions are ordinary classes, and that `except` matching is based on inheritance — a parent class catches all its children.

## Theory — what it is

An **exception** is an object that represents "something went wrong." When code calls `raise SomeError("message")`, Python stops normal execution and unwinds the call stack until it finds a matching `except` block. If none is found, the program crashes with a traceback.

A **custom exception** is simply a class you write that inherits from `Exception` (or from a more specific built-in like `ValueError`). You define one when you want callers to be able to distinguish *your* failure from all the other ways code can fail. `except KeyError` and `except MyAppError` are different filters — custom exceptions give you a filter that only matches your own bugs/failures.

A **hierarchy** means organizing your exceptions as a family tree: one base class for "anything my library can throw," and children for specific failures. Because `except ParentClass` catches `ParentClass` *and every subclass of it*, callers can choose to handle failures broadly (`except PaymentError`) or narrowly (`except CardDeclinedError`).

"Jargon" decoded: **unwinding the stack** = abandoning each running function, one by one, until an `except` is found. **Subclass/child class** = a class that inherits behavior from a parent.

## Why it was needed

Without custom exceptions you have three bad options:

1. **Return special values** like `None` or `-1` to signal failure. Callers forget to check, and the error silently turns into a wrong result far away from the cause.
2. **Raise generic built-ins** like `raise Exception("bad")`. Callers can only catch it with `except Exception`, which also catches *every other bug in the program* — including typos and null derefs you never intended to handle.
3. **Reuse a built-in** like `ValueError` for your domain error. Now callers can't tell "the user typed a bad number" from "the payment gateway rejected the card" — both look identical.

Custom exceptions let the error *name* carry meaning and let the *class tree* control how broadly callers catch.

## Where it's used in a real project

- **Web APIs / SDKs**: `requests` raises `requests.HTTPError`, `requests.ConnectionError`, `requests.Timeout` — all children of `requests.RequestException`, so users can catch them all at once or one by one.
- **Database layers**: an ORM raises `ObjectDoesNotExist`, `DuplicateKey`, `DeadlockDetected` so app code can react differently (404 vs retry).
- **Domain validation**: `InsufficientFundsError` in a banking app — business logic failures that must never be confused with a code bug.
- **Retry/circuit-breaker logic**: catching a specific `RateLimitError` (with a `retry_after` attribute) to decide whether retrying is even allowed.

## Diagram

```
                 BaseException            (system-exiting things)
                      |
                 Exception                (catch this if you must catch "everything")
                      |
               +------+-------+-------- ...
               |              |
          ValueError      AppError  <── your base class
                              |
                        PaymentError  <── domain-level base
                              |
                    +---------+---------+
                    |                   |
          InsufficientFundsError  CardDeclinedError

except PaymentError   → catches BOTH boxes at the bottom (inheritance!)
except CardDeclinedError → catches only that one
except Exception      → catches EVERYTHING in this tree (dangerous)
```

## Code — explained

```python
class AppError(Exception):
    """Base class for every error this app raises."""          # 1

class PaymentError(AppError):
    """Any failure while charging the customer."""             # 2

class InsufficientFundsError(PaymentError):
    """The account doesn't have enough money."""               # 3


def charge_card(balance: float, amount: float) -> float:
    if amount > balance:
        raise InsufficientFundsError(                          # 4
            f"need {amount}, have {balance}"
        )
    return balance - amount


try:
    charge_card(50, 100)                                       # 5
except InsufficientFundsError as e:                            # 6
    print("please add funds:", e)
except PaymentError as e:                                      # 7
    print("payment failed:", e)
```

1. `class AppError(Exception)` — our root. Inheriting from `Exception` makes it a normal, catchable error. The docstring is the only body needed; `pass` also works.
2. `PaymentError` is a *child* of `AppError` — it IS an `AppError`.
3. `InsufficientFundsError` is a *grandchild* — it is an `AppError`, a `PaymentError`, and an `Exception` all at once.
4. `raise` creates the object and starts stack unwinding. The string goes to `Exception.__init__` and is what `print(e)` shows.
5. Calling with `amount=100 > balance=50` triggers the raise.
6. `except InsufficientFundsError` matches — this block runs. Output: `please add funds: need 100, have 50`.
7. This line would also have matched (parent catches children), but Python checks `except` blocks **top to bottom** and uses the **first** match — so order matters: specific first, general last.

## Problems

### Easy — raise your own error
**Problem:** Define `NegativeAgeError` and raise it from `set_age(age)` when `age < 0`. Catch it and print the message.
**Try this input:** `set_age(-5)`
**Expected output:** `Caught: age cannot be negative: -5`
**Solution:**
```python
class NegativeAgeError(Exception):
    pass

def set_age(age):
    if age < 0:
        raise NegativeAgeError(f"age cannot be negative: {age}")
    return age

try:
    set_age(-5)
except NegativeAgeError as e:
    print("Caught:", e)
```
**Logic explained:**
1. `NegativeAgeError(Exception)` — an empty subclass is a complete, valid custom exception.
2. `set_age(-5)` hits the guard, builds the message, and raises.
3. `except NegativeAgeError` matches exactly; `e` holds the exception object, and printing it shows the message passed to `raise`.

### Medium — catch the parent, get the children
**Problem:** Build a hierarchy `FileError` → `FileMissingError`, `FilePermissionError`. Write `read_file(name)` that raises the right child, then catch *just the parent* to handle both failures in one `except`.
**Try this input:** `"report.csv"`, `"missing.txt"`, `"secret.txt"`
**Expected output:**
```
report.csv -> a,b,c
missing.txt -> failed: missing.txt does not exist
secret.txt -> failed: no access to secret.txt
```
**Solution:**
```python
class FileError(Exception):
    """Base for all file problems."""

class FileMissingError(FileError):
    pass

class FilePermissionError(FileError):
    pass

FAKE_FS = {"report.csv": "a,b,c", "secret.txt": "classified"}

def read_file(name):
    if name not in FAKE_FS:
        raise FileMissingError(f"{name} does not exist")
    if name.startswith("secret"):
        raise FilePermissionError(f"no access to {name}")
    return FAKE_FS[name]

for name in ["report.csv", "missing.txt", "secret.txt"]:
    try:
        print(name, "->", read_file(name))
    except FileError as e:          # one except catches BOTH children
        print(name, "-> failed:", e)
```
**Logic explained:**
1. Both specific errors inherit from `FileError`, so `except FileError` matches either one.
2. `"report.csv"` exists and doesn't start with `"secret"` → returns its contents.
3. `"missing.txt"` isn't in `FAKE_FS` → `FileMissingError`, caught by the parent `except`.
4. `"secret.txt"` exists but fails the permission check → `FilePermissionError`, also caught.
5. This is the payoff of a hierarchy: callers pick their granularity. `except FileError` = "any file problem"; `except FileMissingError` = "just that one."

### Hard — exceptions that carry data
**Problem:** Design `APIError` storing a `status_code` and `retry_after`, plus a `RateLimitError` child. Catch the child specifically to read `retry_after`, and show the parent catch still works for other API errors.
**Try this input:** `call_api(fail_with="rate_limit")`
**Expected output:** `rate limited — wait 30s (HTTP 429)`
**Solution:**
```python
class APIError(Exception):
    def __init__(self, message, status_code, retry_after=0):
        super().__init__(message)      # keep normal Exception behavior
        self.status_code = status_code
        self.retry_after = retry_after

class RateLimitError(APIError):
    def __init__(self, retry_after):
        super().__init__("too many requests", 429, retry_after)

def call_api(fail_with=None):
    if fail_with == "rate_limit":
        raise RateLimitError(retry_after=30)
    if fail_with == "server":
        raise APIError("internal error", 500)
    return {"ok": True}

try:
    call_api(fail_with="rate_limit")
except RateLimitError as e:
    print(f"rate limited — wait {e.retry_after}s (HTTP {e.status_code})")
except APIError as e:
    print(f"API failed with HTTP {e.status_code}: {e}")
```
**Logic explained:**
1. `APIError.__init__` accepts extra fields, stores them as attributes, then calls `super().__init__(message)` so `str(e)` still works normally.
2. `RateLimitError` hard-codes the message and status, so raising it is a one-liner — the child *specializes* the parent.
3. `except RateLimitError` runs first (most specific), and `e.retry_after` / `e.status_code` are read off the exception object — exceptions are data carriers, not just messages.
4. If `fail_with="server"` were passed, the second `except APIError` would catch it — the hierarchy still works.
5. This is exactly how real SDKs work (`requests.HTTPError` has `.response`, `boto3` errors carry `.response["Error"]["Code"]`).

## The 30-second interview answer

"Define a custom exception when callers need to react to your failure differently than to generic errors. I always create one base class for the module — like `PaymentError` — and subclass it for each specific failure, like `CardDeclinedError`. Because `except` matches by inheritance, callers can catch the whole family or just one member. I order `except` blocks from most specific to most general, and if callers need details like an HTTP status or retry delay, I store them as attributes on the exception and call `super().__init__` with the message."

## Follow-up trap

**"Why not just raise `Exception('payment failed')` directly?"** — Two reasons: (1) the caller can only catch it with `except Exception`, which also swallows every unrelated bug in the `try` block — a `TypeError` typo would look like "payment failed" and be silently handled; (2) the name carries no meaning. A named class is self-documenting and gives callers a precise filter.

**"What's `raise ... from` (exception chaining)?"** — When you catch a low-level error and re-raise your own (`raise PaymentError(...) from original`), Python records the original as `__cause__` and prints "The above exception was the direct cause..." in the traceback. Use it so the root cause isn't lost when you translate errors across layer boundaries.
