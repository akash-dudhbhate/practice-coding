# Lesson 19 — Approach Comparison

## Problem: Sum of Squares

### Approach 1: Loop
```python
total = sum(x ** 2 for x in arr)
```
**Cons:** O(n) Python overhead.

### Approach 2: Vectorized
```python
total = np.sum(arr ** 2)
```
**Pros:** 100x faster for large arrays.

### Approach 3: Dot product
```python
total = arr @ arr  # or np.dot(arr, arr)
```
**Pros:** Even faster, mathematically elegant.

**Winner:** Approach 3 for sum of squares. Approach 2 for general operations.

---

## Problem: Matrix Operations

### Approach 1: Nested loops
```python
result = np.zeros((n, m))
for i in range(n):
    for j in range(m):
        result[i, j] = a[i] * b[j]
```

### Approach 2: Outer product
```python
result = np.outer(a, b)
```

**Winner:** Approach 2 — one line, 1000x faster.
