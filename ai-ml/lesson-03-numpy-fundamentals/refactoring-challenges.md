# Lesson 03 — Refactoring Challenges

## Refactor 01 (Easy): Python Loop for Math
### Before
```python
result = []
for x in arr: result.append(x * 2)
```
### After
```python
result = arr * 2  # numpy vectorized
```

## Refactor 02 (Medium): Nested Lists
### Before
```python
matrix = [[1, 2], [3, 4]]
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        matrix[i][j] *= 2
```
### After
```python
import numpy as np
matrix = np.array([[1, 2], [3, 4]])
matrix *= 2
```

## Refactor 03 (Hard): Manual Matrix Operations
### Before
```python
def dot_product(a, b):
    result = 0
    for i in range(len(a)): result += a[i] * b[i]
    return result
```
### After
```python
result = np.dot(a, b)
```
