# Lesson 14 — Approach Comparison

## Problem: Double Positive Numbers

### Approach 1: map + filter
```python
result = list(map(lambda x: x * 2, filter(lambda x: x > 0, nums)))
```

### Approach 2: List comprehension
```python
result = [x * 2 for x in nums if x > 0]
```

### Approach 3: Generator + list
```python
result = list(x * 2 for x in nums if x > 0)
```

**Winner:** Approach 2 — most readable, most Pythonic.

---

## Problem: Product of List

### Approach 1: reduce
```python
from functools import reduce
product = reduce(lambda a, b: a * b, nums)
```

### Approach 2: Loop
```python
product = 1
for n in nums:
    product *= n
```

### Approach 3: math.prod (Python 3.8+)
```python
import math
product = math.prod(nums)
```

**Winner:** Approach 3 — built-in, tested, clear.
