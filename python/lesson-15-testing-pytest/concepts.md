# Lesson 15 — Concepts Explained (Testing with pytest)

> Read this before solving the problems. Each concept explains:
> **What** it is · **Why** it exists · **Where** it's used · **What goes wrong** without it.

---

## Why Testing

**What:** Testing is writing code that verifies your other code works correctly. Instead of manually running your program and checking outputs, you write automated tests that run in seconds.

```python
# The code being tested (in calculator.py)
def add(a, b): return a + b

# The test (in test_calculator.py)
def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
```

**Why it exists:** Without tests, you verify by manually running the program — slow, error-prone, and you forget to check edge cases. Automated tests run in seconds, catch regressions (bugs introduced by changes), and document expected behavior.

**Where it's used:** Every professional codebase. CI/CD pipelines run tests on every commit. Open-source projects require tests for pull requests.

**What goes wrong without it:**
- You change one function → break another → don't notice until a user reports it.
- "It worked yesterday" → you changed something but don't know what broke.
- Fear of refactoring → you can't improve code because you might break it silently.
- Manual testing takes hours → you skip it → bugs reach production.

---

## pytest Basics

**What:** pytest is the most popular Python testing framework. It finds functions named `test_*`, runs them, and reports pass/fail.

```python
# test_math.py
def test_addition():
    assert 1 + 1 == 2

def test_string_concat():
    assert "hello" + " " + "world" == "hello world"
```

Run tests: `pytest` (auto-discovers `test_*.py` files and `test_*` functions)

**Why it exists:** Before pytest, Python had `unittest` — verbose, class-based, lots of boilerplate. pytest uses plain `assert` statements and auto-discovery. Less code, more readable.

**Where it's used:** Every Python project that tests (which should be all of them). Django, Flask, FastAPI all use pytest.

**What goes wrong without it:**
- No tests → bugs in production → user complaints, data loss, security issues.
- Using `print()` to verify → you have to read the output manually → not automated → you'll skip it.
- Tests that test nothing: `def test_something(): assert True` → always passes → false confidence.

---

## assert Statement

**What:** `assert` checks that a condition is True. If it's False, it raises `AssertionError` and the test fails.

```python
assert 2 + 2 == 4          # passes
assert 2 + 2 == 5          # fails: AssertionError
assert "hello".upper() == "HELLO"    # passes
assert len([1, 2, 3]) == 3           # passes

# With a message (shown on failure):
assert x > 0, f"x should be positive, got {x}"
```

**Why it exists:** `assert` is the simplest possible test — one line, no framework. pytest enhances assert with rich comparison output (shows exactly what differed).

**Where it's used:** In every test function. Also in production code for debugging (but assertions can be disabled with `-O` flag, so don't use them for validation in production).

**What goes wrong without it:**
- `assert x is True` vs `assert x == True` → `is` checks identity, `==` checks equality. For booleans, use `assert x` (cleanest).
- `assert` in production code with `-O` flag → assertions are stripped → validation disappears → security bugs.
- Comparing floats: `assert 0.1 + 0.2 == 0.3` → FAILS (floating point error). Use `pytest.approx(0.3)`.

---

## Test Discovery

**What:** pytest automatically finds your tests by following naming conventions:
- Files: `test_*.py` or `*_test.py`
- Functions: `test_*`
- Classes: `Test*` (with `test_*` methods)

```
project/
├── calculator.py
└── tests/
    ├── test_calculator.py    # pytest finds this
    │   ├── test_add()        # pytest runs this
    │   └── test_subtract()   # and this
    └── test_strings.py
        └── test_upper()
```

Run: `pytest` (from project root) — finds and runs all tests.

**Why it exists:** Without auto-discovery, you'd have to manually register every test. pytest's convention-over-configuration means you just name things correctly and they're found.

**Where it's used:** Every pytest project. CI pipelines run `pytest` and it finds everything.

**What goes wrong without it:**
- Naming a test `add_test()` instead of `test_add()` → pytest doesn't find it → test silently doesn't run.
- File named `calculator_test.py` works but `calculator_tests.py` doesn't → must match `test_*.py` or `*_test.py`.
- Tests outside `test_*.py` files → not discovered. Keep tests in properly named files.

---

## Fixtures

**What:** Fixtures provide setup data/objects for tests. They're reusable across multiple tests.

```python
import pytest

@pytest.fixture
def sample_list():
    return [1, 2, 3, 4, 5]

@pytest.fixture
def empty_list():
    return []

def test_sum(sample_list):
    assert sum(sample_list) == 15

def test_length(sample_list):
    assert len(sample_list) == 5

def test_empty(empty_list):
    assert len(empty_list) == 0
```

**Why it exists:** Without fixtures, you'd set up the same data in every test — duplication. Fixtures let you define setup once and inject it into any test by name (parameter name matches fixture name).

**Where it's used:** Database connections, temporary files, mock objects, sample data, test clients (Flask/Django test client).

**What goes wrong without it:**
- Parameter name doesn't match fixture name → `fixture not found` error. `def test_x(my_data)` needs a fixture named `my_data`.
- Fixtures with side effects (creating files, DB entries) → tests affect each other. Use `yield` fixtures with cleanup.
- Overusing fixtures for simple data → `@pytest.fixture def two(): return 2` is overkill. Just use `2` directly in the test.

---

## Fixture with yield (setup/teardown)

**What:** A fixture that uses `yield` can do cleanup after the test finishes.

```python
import pytest, tempfile, os

@pytest.fixture
def temp_file():
    # SETUP — runs before the test
    f = tempfile.NamedTemporaryFile(mode='w', delete=False)
    f.write("test data")
    f.close()
    yield f.name    # test runs here, gets the file path
    # TEARDOWN — runs after the test
    os.unlink(f.name)    # clean up the file

def test_read_file(temp_file):
    with open(temp_file) as f:
        assert f.read() == "test data"
```

**Why it exists:** Without teardown, test files, databases, and connections accumulate. `yield` fixtures ensure cleanup happens even if the test fails.

**Where it's used:** Database transactions (rollback after test), temporary files, network connections, mock patches that need restoring.

**What goes wrong without it:**
- Forgetting cleanup → temp files pile up → disk fills up.
- Test fails before cleanup → resource leaked. `yield` fixtures always run teardown, even on failure.
- Setup fails before `yield` → teardown doesn't run → partial setup leaked. Handle setup errors carefully.

---

## parametrize

**What:** Run the same test with multiple inputs — one test function, many test cases.

```python
@pytest.mark.parametrize("input, expected", [
    (1, 1),
    (2, 4),
    (3, 9),
    (4, 16),
    (-1, 1),
    (0, 0),
])
def test_square(input, expected):
    assert input ** 2 == expected
```

This runs 6 separate test cases. If one fails, pytest tells you which input failed.

**Why it exists:** Without parametrize, you'd write 6 separate test functions or loop inside one test (which stops at the first failure). Parametrize gives individual pass/fail per case.

**Where it's used:** Testing functions with many input combinations, edge cases, boundary values.

**What goes wrong without it:**
- Looping inside a test: `for x in cases: assert f(x) == expected` → first failure stops all → you don't know if later cases pass.
- Too many parameters → test becomes hard to read. Group related cases.
- Parameter names must match: `@parametrize("a,b", ...)` with `def test_x(a, b)` — mismatch → error.

---

## Testing Exceptions

**What:** Test that your code raises the expected exception when it should.

```python
import pytest

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        1 / 0

def test_invalid_input():
    with pytest.raises(ValueError, match="must be positive"):
        validate_age(-5)
```

**Why it exists:** Without exception testing, you only test the happy path. Error handling code goes untested → bugs in error handling → confusing errors for users.

**Where it's used:** Testing validation, error handling, edge cases, permission checks.

**What goes wrong without it:**
- Not testing exceptions → error handling code has bugs → users get wrong error messages.
- `pytest.raises(WrongException)` → test fails because the right exception was raised, not the one you expected.
- Forgetting `with` → `pytest.raises()` without context manager → doesn't catch anything → test always fails.

---

## Mocking

**What:** Replace real objects with fake ones to isolate the code being tested.

```python
from unittest.mock import Mock, patch

def test_fetch_data():
    # Replace requests.get with a mock
    with patch('requests.get') as mock_get:
        mock_get.return_value.json.return_value = {"name": "test"}
        result = fetch_data("http://example.com")
        assert result["name"] == "test"
        mock_get.assert_called_once_with("http://example.com")
```

**Why it exists:** Without mocking, tests that call APIs hit real servers → slow, flaky, rate-limited, costs money. Mocking replaces external dependencies with controlled fakes.

**Where it's used:** API calls, database queries, file I/O, any external dependency in tests.

**What goes wrong without it:**
- Tests that hit real APIs → slow (network), flaky (server down), expensive (API limits).
- Over-mocking → you're testing the mock, not the code. If you mock everything, you're not testing real behavior.
- Mock not matching real interface → test passes but real code fails → false confidence.

---

## Test Coverage

**What:** Coverage measures what percentage of your code is executed by tests.

```bash
pip install pytest-cov
pytest --cov=myapp --cov-report=term-missing
```

Output shows:
```
Name              Stmts   Miss  Cover   Missing
---------------------------------------------
myapp/utils.py       20      3    85%   15, 22-23
```

**Why it exists:** Without coverage, you don't know which code paths are untested. 100 tests might all test the same function while 80% of your code has zero tests. Coverage reveals the gaps.

**Where it's used:** CI pipelines (enforce minimum coverage), code review (identify untested new code), refactoring (ensure you don't drop coverage).

**What goes wrong without it:**
- 100% coverage doesn't mean 100% correct — tests might run the code but not assert anything meaningful.
- Chasing 100% coverage → writing useless tests for trivial code (getters, setters) → wasted time.
- Ignoring coverage → large untested areas → bugs hide in the dark.

---

## Test Organization

**What:** How to structure tests in a project.

```
project/
├── src/
│   └── myapp/
│       ├── utils.py
│       └── models.py
└── tests/
    ├── conftest.py          # shared fixtures
    ├── test_utils.py        # tests for utils.py
    ├── test_models.py       # tests for models.py
    └── integration/         # slower integration tests
        └── test_api.py
```

**Why it exists:** Without organization, tests are scattered, hard to find, and hard to run selectively. A clear structure lets you run specific tests: `pytest tests/test_utils.py` or `pytest -k "add"`.

**Where it's used:** Every project with more than a few tests.

**What goes wrong without it:**
- All tests in one file → 1000-line test file → can't find anything.
- `conftest.py` missing → fixtures duplicated across files. `conftest.py` fixtures are available to all tests in that directory.
- No separation of unit/integration tests → running all tests is slow because integration tests hit real services.
