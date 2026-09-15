# Lesson 04 — Common Mistakes

## Mistake 01: Using `in` on dict checks values instead of keys
```python
d = {"a": 1, "b": 2}
# WRONG — checks values, not keys
if 1 in d:  # False! checks keys
# CORRECT
if "a" in d:  # True
if 1 in d.values():  # True — but slower
```

## Mistake 02: Modifying dict while iterating
```python
# WRONG — RuntimeError
d = {"a": 1, "b": 2}
for key in d:
    if d[key] == 1:
        del d[key]

# CORRECT — iterate over a copy
for key in list(d.keys()):
    if d[key] == 1:
        del d[key]
```

## Mistake 03: Using dict when you need a list of pairs
```python
# WRONG — keys must be hashable, loses duplicates
d = {["a", 1], ["b", 2]}  # TypeError — list not hashable

# CORRECT — use list of tuples
pairs = [("a", 1), ("b", 2)]
```

## Mistake 04: Not using defaultdict
```python
# VERBOSE
counts = {}
for word in words:
    if word not in counts:
        counts[word] = 0
    counts[word] += 1

# BETTER — defaultdict
from collections import defaultdict
counts = defaultdict(int)
for word in words:
    counts[word] += 1
```

## Mistake 05: Using set for ordered data
```python
# WRONG — sets are unordered
unique_ordered = set([3, 1, 2])  # {1, 2, 3} — order lost!

# CORRECT — use dict.fromkeys (preserves order)
unique_ordered = list(dict.fromkeys([3, 1, 2]))  # [3, 1, 2]
```
