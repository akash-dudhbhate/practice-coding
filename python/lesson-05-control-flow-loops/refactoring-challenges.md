# Lesson 05 — Refactoring Challenges

## Refactor 01 (Easy): Find with Flag
### Before
```python
def find_even(nums):
    found = False
    result = None
    for n in nums:
        if n % 2 == 0:
            found = True
            result = n
            break
    if found:
        return result
    return None
```
### After
```python
def find_even(nums):
    for n in nums:
        if n % 2 == 0:
            return n
    return None
```

## Refactor 02 (Medium): Nested If to Early Return
### Before
```python
def classify(n):
    if n > 0:
        if n > 100:
            return "large positive"
        else:
            return "small positive"
    else:
        if n < 0:
            return "negative"
        else:
            return "zero"
```
### After
```python
def classify(n):
    if n > 100: return "large positive"
    if n > 0: return "small positive"
    if n < 0: return "negative"
    return "zero"
```

## Refactor 03 (Hard): Loop with Index
### Before
```python
def print_pairs(lst):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            print(lst[i], lst[j])
```
### After
```python
from itertools import combinations
def print_pairs(lst):
    for a, b in combinations(lst, 2):
        print(a, b)
```
