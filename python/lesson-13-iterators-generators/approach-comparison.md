# Lesson 13 — Approach Comparison

## Problem: Custom Iterator

### Approach 1: Iterator protocol
```python
class Range:
    def __init__(self, n): self.n = n; self.i = 0
    def __iter__(self): return self
    def __next__(self):
        if self.i >= self.n: raise StopIteration
        val = self.i; self.i += 1; return val
```

### Approach 2: Generator
```python
def range_gen(n):
    for i in range(n):
        yield i
```

**Winner:** Approach 2 — generators are simpler for most iterators.

---

## Problem: Queue

### Approach 1: list
```python
q = []
q.append(1); q.append(2)
q.pop(0)  # O(n) — shifts all elements
```

### Approach 2: deque
```python
from collections import deque
q = deque()
q.append(1); q.append(2)
q.popleft()  # O(1)
```

**Winner:** Approach 2 — deque is O(1) for both ends.
