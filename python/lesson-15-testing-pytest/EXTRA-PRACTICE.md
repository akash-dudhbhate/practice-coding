# lesson-15-testing-pytest — Extra Practice
Everything beyond the core lesson lives here, in order:
mental quizzes → debug drills → mistakes → refactoring → comparisons.

---

## Intuition Checks — predict before you run

## Check 01: assert
```python
assert 1 + 1 == 2
assert 1 + 1 == 3
```
What happens?
<details><summary>Answer</summary>
First assert passes. Second raises `AssertionError`. Assert is for debugging — disabled with `python -O`.
</details>

## Check 02: pytest fixture
```python
@pytest.fixture
def sample():
    return [1, 2, 3]

def test_len(sample):
    assert len(sample) == 3
```
How does `sample` get its value?
<details><summary>Answer</summary>
pytest sees the parameter name `sample`, finds the fixture with that name, calls it, and passes the return value. Dependency injection.
</details>

## Check 03: parametrize
```python
@pytest.mark.parametrize("x,y,expected", [
    (1, 2, 3),
    (4, 5, 9),
])
def test_add(x, y, expected):
    assert x + y == expected
```
How many tests run?
<details><summary>Answer</summary>
2 — one for each parameter set. pytest generates separate test cases.
</details>

## Check 04: patch
```python
from unittest.mock import patch
with patch("module.func", return_value=42):
    assert module.func() == 42
print(module.func())
```
<details><summary>Answer</summary>
After the `with` block, `module.func` is restored. The last print calls the real function.
</details>

## Check 05: TDD Order
What's the TDD cycle?
<details><summary>Answer</summary>
1. **Red** — write a failing test
2. **Green** — write minimal code to pass
3. **Refactor** — improve code while keeping tests green
</details>

---

## Debug Exercises — find and fix the bug

## Debug 01 (Easy): Test Not Asserting
```python
def test_add():
    result = add(1, 2)
    result == 3  # no assert!
```
<details><summary>Answer</summary>
**Bug:** `result == 3` is an expression that evaluates to True/False but doesn't ASSERT anything. Test always passes.
**Fix:** `assert result == 3`.
</details>

## Debug 02 (Medium): Wrong Test Order
```python
def test_shared_state():
    global data
    data = [1, 2, 3]
    assert len(data) == 3

def test_modifies_state():
    global data
    data.append(4)
    assert len(data) == 4
```
<details><summary>Answer</summary>
**Bug:** Tests share global state. If `test_modifies_state` runs first, `test_shared_state` fails.
**Fix:** Use fixtures or setup/teardown to reset state between tests.
</details>

## Debug 03 (Hard): Mock Not Restored
```python
def test_with_mock():
    original = module.function
    module.function = lambda: "mocked"
    assert module.function() == "mocked"
    # function never restored!
```
<details><summary>Answer</summary>
**Bug:** `module.function` is never restored to `original`. Other tests use the mock.
**Fix:** Use `try/finally` or `unittest.mock.patch` which auto-restores.
</details>

---

## Common Mistakes — the traps learners hit

## Mistake 01: No assert in test
```python
# WRONG — test always passes
def test_add():
    add(1, 2)  # no assertion

# CORRECT
def test_add():
    assert add(1, 2) == 3
```

## Mistake 02: Testing implementation, not behavior
```python
# WRONG — tests internal details
def test_sort():
    assert sort([3, 1, 2]).__class__ == list
    assert sort([3, 1, 2])[0] < sort([3, 1, 2])[1]

# CORRECT — tests observable behavior
def test_sort():
    assert sort([3, 1, 2]) == [1, 2, 3]
```

## Mistake 03: Shared state between tests
```python
# WRONG — order-dependent
data = []
def test_1():
    data.append(1)
    assert len(data) == 1
def test_2():
    data.append(2)
    assert len(data) == 2  # fails if test_1 didn't run

# CORRECT — use fixtures
@pytest.fixture
def data():
    return []
```

## Mistake 04: Not testing edge cases
```python
# WRONG — only tests happy path
def test_divide():
    assert divide(10, 2) == 5

# CORRECT — test edge cases too
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)
def test_divide_negative():
    assert divide(-10, 2) == -5
```

## Mistake 05: Using print instead of assert
```python
# WRONG — doesn't fail the test
def test_add():
    print(add(1, 2))  # just prints, never fails

# CORRECT
def test_add():
    assert add(1, 2) == 3
```

---

## Refactoring Challenges — make working code better

## Refactor 01 (Easy): No Assert
### Before
```python
def test_add():
    result = add(1, 2)
    if result == 3:
        print("pass")
```
### After
```python
def test_add():
    assert add(1, 2) == 3
```

## Refactor 02 (Medium): Repeated Setup
### Before
```python
def test_a():
    db = create_db()
    db.add("x")
    assert db.count() == 1
def test_b():
    db = create_db()
    db.add("y")
    assert db.count() == 1
```
### After
```python
@pytest.fixture
def db():
    return create_db()
def test_a(db):
    db.add("x")
    assert db.count() == 1
```

## Refactor 03 (Hard): Multiple Asserts in One Test
### Before
```python
def test_user():
    u = create_user("A")
    assert u.name == "A"
    assert u.age == 0
    assert u.email is None
    assert u.is_active
```
### After
```python
def test_user_name():
    assert create_user("A").name == "A"
def test_user_defaults():
    u = create_user("A")
    assert u.age == 0
    assert u.email is None
    assert u.is_active
```

---

## Approach Comparison — different ways to solve it

## Problem: Test a Function

### Approach 1: unittest
```python
import unittest
class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)
```

### Approach 2: pytest
```python
def test_add():
    assert add(1, 2) == 3
```

**Winner:** Approach 2 (pytest) — less boilerplate, better assertions, fixtures.

---

## Problem: Mock External API

### Approach 1: Manual mock
```python
def test_fetch():
    original = requests.get
    requests.get = lambda *a, **k: Mock(text="data")
    try:
        assert fetch() == "data"
    finally:
        requests.get = original
```

### Approach 2: patch
```python
from unittest.mock import patch
@patch("requests.get")
def test_fetch(mock_get):
    mock_get.return_value.text = "data"
    assert fetch() == "data"
```

**Winner:** Approach 2 — auto-restores, cleaner.
