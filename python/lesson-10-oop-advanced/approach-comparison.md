# Lesson 10 — Approach Comparison

## Problem: Stack Implementation

### Approach 1: Inheritance (is-a)
```python
class Stack(list):
    def push(self, item): self.append(item)
    def pop(self): return super().pop()
    def peek(self): return self[-1]
```
**Cons:** Exposes ALL list methods (sort, reverse, insert). Users can break the stack.

### Approach 2: Composition (has-a)
```python
class Stack:
    def __init__(self):
        self._data = []
    def push(self, item): self._data.append(item)
    def pop(self): return self._data.pop()
    def peek(self): return self._data[-1]
```
**Pros:** Only exposes stack methods. Internal list is hidden. Can't be broken.

**Winner:** Approach 2 (composition) — "favor composition over inheritance" (Gang of Four).

---

## Problem: Temperature Class

### Approach 1: Methods
```python
class Temperature:
    def __init__(self, c):
        self.c = c
    def to_f(self): return self.c * 9/5 + 32
    def to_k(self): return self.c + 273.15
```
Usage: `t.to_f()` — looks like a function call.

### Approach 2: Properties
```python
class Temperature:
    def __init__(self, c):
        self.c = c
    @property
    def f(self): return self.c * 9/5 + 32
    @property
    def k(self): return self.c + 273.15
```
Usage: `t.f` — looks like an attribute. More natural.

**Winner:** Approach 2 (properties) — computed attributes feel like data, not function calls.
