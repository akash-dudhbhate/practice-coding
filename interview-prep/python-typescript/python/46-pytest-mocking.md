# 46 — pytest fixtures, `parametrize`, and `unittest.mock` patching

> **Interview question:** "What testing tools have you used? Explain pytest fixtures, parametrize, and mocking."
> **What the interviewer is really testing:** That you write real tests — not `assert True` — and can isolate code from the network/DB without hitting either.

## Theory — what it is

**pytest** is Python's standard test framework. Any function named `test_*` in a file named `test_*.py` is a test; a plain `assert` is the assertion (no `self.assertEqual` ceremony like `unittest`).

A **fixture** is setup/teardown code pytest injects into tests by name. You mark a function `@pytest.fixture`; any test that lists it as a parameter gets its return value. Fixtures solve "every test needs a fresh DB connection/temp file/sample object."

**`@pytest.mark.parametrize`** runs one test function many times with different inputs — a table of cases without copy-pasting.

**Mocking** (`unittest.mock`) replaces a real object — an HTTP client, a DB, `requests.get` — with a fake you control. `patch` swaps the object *where it's looked up*; `Mock`/`MagicMock` record calls so you can assert "was it called once with these args?"

## Why it was needed

Without fixtures, setup code duplicates across every test and teardown leaks files/connections. Without parametrize, people write 12 near-identical tests and stop adding cases. Without mocks, your "unit tests" actually call Stripe's API or your Postgres — they're slow, flaky, fail offline, and can mutate real data.

Together they let you test the *edges*: timeouts, 500 responses, empty inputs — cases you can't reliably reproduce against real services.

## Where it's used in a real project

- **DB fixture**: `conftest.py` provides a fresh in-memory DB or rolled-back transaction per test.
- **API tests**: `parametrize` over `(payload, expected_status)` tables for an endpoint.
- **External calls**: patch `requests.get` / `boto3` / `stripe` so tests run offline in CI.
- **Time-dependent code**: patch `datetime.now` / `time.time` to test "token expires after 1h" deterministically.

## Diagram

```
test file                         pytest machinery
------------------          ---------------------------------
@pytest.fixture             runs once per test that asks for it
def db():        --------->  creates fresh DB -> yields to test
    yield conn               then runs teardown after the test

@pytest.mark.parametrize    one function, N test cases:
("n, expected", [...])  -->  test_x(1, ...)  test_x(2, ...)  ...

@patch("app.payment.charge")  swaps the NAME 'charge' in the
def test_pay(m):              module under test with a MagicMock
    ... m.return_value        for the duration of the test only
```

## Code — explained

```python
# app.py
import requests                                           # 1

def get_username(user_id: int) -> str:
    r = requests.get(f"https://api.example.com/users/{user_id}")  # 2
    r.raise_for_status()
    return r.json()["name"]                               # 3

# test_app.py
import pytest
from unittest.mock import patch, Mock
from app import get_username                              # 4

@pytest.fixture                                           # 5
def sample_user():
    return {"id": 7, "name": "ada"}                       # 6

@pytest.mark.parametrize("n,expected",                    # 7
                         [(0, 1), (1, 1), (5, 120)])
def test_factorial(n, expected):
    import math
    assert math.factorial(n) == expected                  # 8

@patch("app.requests.get")                                # 9
def test_get_username(mock_get, sample_user):
    mock_get.return_value.json.return_value = {"name": "ada"}  # 10
    assert get_username(7) == "ada"                       # 11
    mock_get.assert_called_once_with(
        "https://api.example.com/users/7")                # 12
```

1. The code under test imports `requests` at module level — important for *where* we patch.
2. `get_username` makes a real network call — untestable offline unless we replace it.
3. Returns the `name` field of the JSON body.
4. Import the function to test. Fixtures and mocks only work on what tests can see.
5. `@pytest.fixture` registers `sample_user` — pytest calls it fresh for each test that names it.
6. Returning a dict; `yield` instead of `return` would add teardown code after the yield.
7. `parametrize` declares `(n, expected)` triples — pytest generates 3 separate tests, each reported individually.
8. One `assert` covers all cases; a failure on `5 -> 120` reports `test_factorial[5-120]` so you know which case broke.
9. **Patch the name where it's used** — `app.requests.get`, not `requests.get` globally. Inside `app`, `requests` is the same module object, so patching `app.requests.get` intercepts the call this module makes. (`patch("requests.get")` also works here since it's the same object, but for `from x import f` style imports you MUST patch where it's imported into.)
10. Configure the mock: `mock_get(...)` returns a Mock whose `.json()` returns our dict — simulating a 200 response.
11. Call the real function; inside it, `requests.get` is now our mock — zero network.
12. Assert on the *interaction*: called exactly once, with the exact URL. This catches bugs like wrong URL construction.

## Problems

### Easy — first parametrize
**Problem:** Write `is_palindrome(s)` (ignore case) and a parametrized test over `["Level", "noon", "abc"]` with expected `[True, True, False]`. Then just show the function + a print-based check.
**Try this input:** `["Level", "noon", "abc"]`
**Expected output:** `True True False`
**Solution:**
```python
def is_palindrome(s: str) -> bool:
    s = s.lower()
    return s == s[::-1]

cases = [("Level", True), ("noon", True), ("abc", False)]
print(*[is_palindrome(s) for s, _ in cases])            # True True False

# --- pytest version ---
# @pytest.mark.parametrize("s,expected", cases)
# def test_pal(s, expected):
#     assert is_palindrome(s) == expected
```
**Logic explained:**
1. `s[::-1]` reverses the string; compare after `.lower()` so case doesn't matter.
2. The `cases` list IS the parametrize table — same data shape as the decorator takes.
3. In pytest, each tuple becomes an independent test case: one failure doesn't hide the rest.

### Medium — fixture + teardown
**Problem:** Write a fixture that creates a temp file with 3 lines, yields its path, and deletes it after the test. Show it works by reading the file inside a "test" function (plain function call simulating pytest's injection).
**Try this input:** run the simulated test
**Expected output:** `3` lines read, then `file deleted: True`
**Solution:**
```python
import os, tempfile
from contextlib import contextmanager

@contextmanager                                  # what @pytest.fixture(yield) does
def log_file():
    fd, path = tempfile.mkstemp(suffix=".log")
    with os.fdopen(fd, "w") as f:
        f.write("a\nb\nc\n")
    yield path                                   # <- test runs here
    os.remove(path)                              # <- teardown always runs

with log_file() as path:
    n = sum(1 for _ in open(path))
    print("lines:", n)
print("file deleted:", not os.path.exists(path))
# lines: 3
# file deleted: True

# --- pytest equivalent ---
# @pytest.fixture
# def log_file():
#     fd, path = tempfile.mkstemp(suffix=".log")
#     ...
#     yield path
#     os.remove(path)
#
# def test_count(log_file):
#     assert sum(1 for _ in open(log_file)) == 3
```
**Logic explained:**
1. Everything before `yield` = setup; after `yield` = teardown that runs even if the test fails.
2. The test receives `path` — whatever was yielded.
3. `mkstemp` gives a real file safely; `os.remove` cleans up so 1,000 test runs don't litter `/tmp`.

### Hard — mock a flaky dependency
**Problem:** `send_welcome_email(user)` calls `mailer.send(to, subject)` and returns `True`; if `mailer.send` raises `SMTPError` it returns `False`. Write the function, then test BOTH paths with `unittest.mock` — no real SMTP. Prove `send` was called with the right recipient.
**Try this input:** `{"email": "a@b.com"}` — once healthy, once with `side_effect=SMTPError`
**Expected output:** `True` then `False`, and mock recorded the call to `a@b.com`
**Solution:**
```python
from unittest.mock import Mock

class SMTPError(Exception):
    pass

def send_welcome_email(user, mailer) -> bool:    # mailer injected = easy to mock
    try:
        mailer.send(user["email"], "Welcome!")
        return True
    except SMTPError:
        return False

user = {"email": "a@b.com"}

# path 1: success
mailer = Mock()
mailer.send.return_value = None
print(send_welcome_email(user, mailer))          # True
mailer.send.assert_called_once_with("a@b.com", "Welcome!")

# path 2: SMTP failure -> returns False instead of crashing
mailer2 = Mock()
mailer2.send.side_effect = SMTPError("connection refused")
print(send_welcome_email(user, mailer2))         # False
```
**Logic explained:**
1. `mailer` is passed in (dependency injection) — in pytest you'd often `patch("app.mailer")` instead, same idea.
2. `Mock()` auto-creates any attribute/method accessed; `return_value` controls what calls return.
3. `side_effect = SomeException` makes the call *raise* — how you test failure paths that are impossible to trigger on demand with real services.
4. `assert_called_once_with(...)` verifies not just *that* it was called but with exact args — catches "sent email to wrong address" bugs.

## The 30-second interview answer

"I use pytest for everything. Fixtures give each test fresh setup — a DB connection, a temp dir — via `@pytest.fixture` and `yield` for teardown. `parametrize` turns a table of inputs and expected outputs into separate test cases, so edge cases are cheap to add. For anything that leaves the process — HTTP, SMTP, AWS — I patch it with `unittest.mock`, patching the name where the code-under-test looks it up, and use `side_effect` to simulate failures plus `assert_called_with` to verify interactions. Rule of thumb: unit tests mock boundaries, a few integration tests hit the real thing."

## Follow-up trap

**"Why did your patch not work — you patched `requests.get` but the real call still fired?"** Classic answer: because the module under test did `from requests import get` — that binds the name `get` *inside* `app`'s namespace at import time. Patching `requests.get` changes `requests`, but `app.get` still points at the original function. Fix: `patch("app.get")` — always patch where the name is *looked up*, not where it's defined. Second trap: **fixture scope** — `@pytest.fixture(scope="module")` creates the object once per file; mutable state then leaks between tests. Know `function` (default) vs `class`/`module`/`session`, and why `session`-scoped DB fixtures need careful reset.
