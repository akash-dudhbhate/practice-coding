# Lesson 03 — Common Mistakes

## Mistake 01: Python loops on numpy
```python
# WRONG — slow
for i in range(len(arr)):
    arr[i] *= 2
# CORRECT — vectorized
arr *= 2
```

## Mistake 02: Copy vs view
```python
# WRONG — modifies original
b = a
b[0] = 99
# CORRECT
b = a.copy()
```

## Mistake 03: Wrong axis
```python
# axis=0 = columns, axis=1 = rows
# Common confusion — always check with small example
```

## Mistake 04: Not checking shapes
```python
# Always verify shapes before operations
print(arr.shape)  # debug
```

## Mistake 05: Mixing dtypes
```python
# WRONG — upcasts silently
np.array([1, 2.5, "a"])  # all strings
# Be explicit about dtype
```
