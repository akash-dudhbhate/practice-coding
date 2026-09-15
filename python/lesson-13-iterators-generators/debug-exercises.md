# Lesson 13 — Debug Exercises

## Debug 01 (Easy): Iterator Missing __iter__
```python
class Counter:
    def __init__(self, n): self.n = n
    def __next__(self):
        if self.n <= 0: raise StopIteration
        self.n -= 1
        return self.n + 1
```
<details><summary>Answer</summary>
**Bug:** No `__iter__` method — can't be used in for loops.
**Fix:** Add `def __iter__(self): return self`.
</details>

## Debug 02 (Medium): Generator Not Resumable
```python
def counter():
    n = 0
    while True:
        yield n
        n += 1

gen = counter()
list(gen)  # [0, 1, 2, ...] infinite!
```
<details><summary>Answer</summary>
**Bug:** Infinite generator — `list()` tries to collect all values, hangs forever.
**Fix:** Add a limit parameter or use `itertools.islice(gen, 10)`.
</details>

## Debug 03 (Hard): namedtuple Immutability
```python
from collections import namedtuple
Point = namedtuple("Point", ["x", "y"])
p = Point(1, 2)
p.x = 10
```
<details><summary>Answer</summary>
**Bug:** namedtuples are immutable — can't assign to fields.
**Fix:** Use `p._replace(x=10)` which returns a NEW namedtuple.
</details>
