# Lesson 13 — Refactoring Challenges

## Refactor 01 (Easy): Iterator Class for Simple Sequence
### Before
```python
class Range:
    def __init__(self, n): self.n = n; self.i = 0
    def __iter__(self): return self
    def __next__(self):
        if self.i >= self.n: raise StopIteration
        v = self.i; self.i += 1; return v
```
### After
```python
def range_gen(n):
    for i in range(n):
        yield i
```

## Refactor 02 (Medium): Building List for Sum
### Before
```python
total = sum([x * 2 for x in data])
```
### After
```python
total = sum(x * 2 for x in data)
```

## Refactor 03 (Hard): Manual Counter
### Before
```python
class Counter:
    def __init__(self): self.n = 0
    def __next__(self):
        self.n += 1
        return self.n
    def __iter__(self): return self
```
### After
```python
from itertools import count
# count() is infinite counter
```
