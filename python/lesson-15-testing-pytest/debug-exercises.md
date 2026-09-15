# Lesson 15 — Debug Exercises

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
