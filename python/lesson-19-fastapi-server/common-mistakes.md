# Lesson 19 — Common Mistakes

## Mistake 01: View vs Copy confusion
```python
# WRONG — modifies original
b = a[:5]
b[0] = 99  # a[0] is now 99!

# CORRECT
b = a[:5].copy()
```

## Mistake 02: Python loops on numpy arrays
```python
# SLOW
total = 0
for x in arr:
    total += x ** 2

# FAST
total = np.sum(arr ** 2)
```

## Mistake 03: Wrong dtype
```python
# WRONG — integer division
arr = np.array([1, 2, 3])
print(arr / 2)  # works in py3, but...
arr_int = np.array([1, 2, 3], dtype=int)
print(arr_int / 2)  # float in py3, but truncates in py2

# BE EXPLICIT
arr = np.array([1, 2, 3], dtype=float)
```

## Mistake 04: Not setting random seed
```python
# NON-REPRODUCIBLE
results = np.random.rand(100)

# REPRODUCIBLE
np.random.seed(42)
results = np.random.rand(100)
```

## Mistake 05: Creating array in loop
```python
# SLOW — grows array each time
arr = np.array([])
for i in range(1000):
    arr = np.append(arr, i)

# FAST — preallocate
arr = np.zeros(1000)
for i in range(1000):
    arr[i] = i
```
