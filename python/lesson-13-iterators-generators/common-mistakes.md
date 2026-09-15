# Lesson 13 — Common Mistakes

## Mistake 01: Not implementing __iter__
```python
# WRONG — only __next__, can't use in for loop
class MyIter:
    def __next__(self): ...

# CORRECT
class MyIter:
    def __iter__(self): return self
    def __next__(self): ...
```

## Mistake 02: Infinite generator without exit
```python
# DANGEROUS — hangs
def gen():
    while True:
        yield 1
list(gen())  # infinite!

# FIX — add a limit
def gen(n):
    for _ in range(n):
        yield 1
```

## Mistake 03: Using list when deque is needed
```python
# SLOW — O(n) for front operations
queue = [1, 2, 3]
queue.insert(0, 0)  # O(n)

# FAST — O(1)
from collections import deque
queue = deque([1, 2, 3])
queue.appendleft(0)  # O(1)
```

## Mistake 04: Modifying namedtuple
```python
# WRONG
p.x = 10  # AttributeError

# CORRECT
p = p._replace(x=10)
```

## Mistake 05: Not using Counter
```python
# VERBOSE
counts = {}
for item in items:
    counts[item] = counts.get(item, 0) + 1

# BETTER
from collections import Counter
counts = Counter(items)
```
