# Lesson 03 — Refactoring Challenges

## Refactor 01 (Easy): Manual Sum
### Before
```python
def total(numbers):
    result = 0
    for n in numbers:
        result = result + n
    return result
```
### After
```python
def total(numbers):
    return sum(numbers)
```

## Refactor 02 (Medium): Manual Filter
### Before
```python
def get_positives(nums):
    result = []
    for n in nums:
        if n > 0:
            result.append(n)
    return result
```
### After
```python
def get_positives(nums):
    return [n for n in nums if n > 0]
```

## Refactor 03 (Hard): Multiple Passes
### Before
```python
def process(items):
    filtered = []
    for x in items:
        if x is not None:
            filtered.append(x)
    transformed = []
    for x in filtered:
        transformed.append(x * 2)
    result = []
    for x in transformed:
        if x > 0:
            result.append(x)
    return result
```
### After
```python
def process(items):
    return [x * 2 for x in items if x is not None and x * 2 > 0]
```
