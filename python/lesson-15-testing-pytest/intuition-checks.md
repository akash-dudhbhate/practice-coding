# Lesson 15 — Intuition Checks

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
