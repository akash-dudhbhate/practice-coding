# Lesson 15 — Common Mistakes

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
