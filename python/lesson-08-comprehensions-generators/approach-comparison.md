# Lesson 08 — Approach Comparison

## Problem: Squares of Even Numbers

### Approach 1: List comprehension
```python
result = [x * x for x in range(20) if x % 2 == 0]
```

### Approach 2: Generator + list
```python
result = list(x * x for x in range(20) if x % 2 == 0)
```

### Approach 3: Filter + map
```python
result = list(map(lambda x: x * x, filter(lambda x: x % 2 == 0, range(20))))
```

**Winner:** Approach 1 — most readable, most Pythonic. Approach 3 is functional style but harder to read.

---

## Problem: Sum of Squares

### Approach 1: List comprehension
```python
total = sum([x * x for x in range(1000000)])
```
**Cons:** Builds a 1M element list in memory just to sum it.

### Approach 2: Generator expression
```python
total = sum(x * x for x in range(1000000))
```
**Pros:** No list built — values produced on demand. Less memory, faster.

**Winner:** Approach 2 — always use generator expressions with `sum()`, `max()`, `min()`, `any()`, `all()`.
