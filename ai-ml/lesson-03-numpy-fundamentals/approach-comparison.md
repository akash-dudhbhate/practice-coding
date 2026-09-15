# Lesson 03 — Approach Comparison

## Problem: Element-wise Operation

### Approach 1: Loop
```python
result = np.zeros(len(arr))
for i in range(len(arr)):
    result[i] = arr[i] ** 2
```

### Approach 2: Vectorized
```python
result = arr ** 2
```

**Winner:** Approach 2 — 100x faster, cleaner.

---

## Problem: Matrix Multiply

### Approach 1: Nested loops
```python
for i in range(n):
    for j in range(m):
        for k in range(p):
            result[i][j] += a[i][k] * b[k][j]
```

### Approach 2: np.dot
```python
result = np.dot(a, b)  # or a @ b
```

**Winner:** Approach 2 — 1000x faster, one line.
