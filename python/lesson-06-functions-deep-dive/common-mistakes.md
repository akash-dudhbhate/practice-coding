# Lesson 06 — Common Mistakes

## Mistake 01: Mutable default arguments
```python
# WRONG
def func(lst=[]):
    lst.append(1)
    return lst

# CORRECT
def func(lst=None):
    if lst is None:
        lst = []
    lst.append(1)
    return lst
```

## Mistake 02: Default args before required args
```python
# WRONG — SyntaxError
def func(a=1, b):

# CORRECT
def func(b, a=1):
```

## Mistake 03: Using lambda for complex logic
```python
# WRONG — unreadable
func = lambda x: x * 2 if x > 0 else -x if x < 0 else 0

# CORRECT — use def
def func(x):
    if x > 0:
        return x * 2
    elif x < 0:
        return -x
    return 0
```

## Mistake 04: Forgetting return in lambda
```python
# WRONG — lambda doesn't need return, but def does
f = lambda x: return x * 2  # SyntaxError!

# CORRECT
f = lambda x: x * 2
```

## Mistake 05: Not using *args and **kwargs flexibly
```python
# VERBOSE — fixed params
def add(a, b, c, d, e):
    return a + b + c + d + e

# FLEXIBLE
def add(*nums):
    return sum(nums)
```
