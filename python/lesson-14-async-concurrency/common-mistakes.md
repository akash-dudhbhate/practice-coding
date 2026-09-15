# Lesson 14 — Common Mistakes

## Mistake 01: Using map/filter when comprehension is clearer
```python
# LESS READABLE
list(map(lambda x: x * 2, filter(lambda x: x > 0, nums)))

# MORE READABLE
[x * 2 for x in nums if x > 0]
```

## Mistake 02: Forgetting reduce import
```python
# WRONG
reduce(...)  # NameError

# CORRECT
from functools import reduce
```

## Mistake 03: Not using partial for configuration
```python
# VERBOSE
def make_greeter(greeting, name):
    return f"{greeting}, {name}!"
hello = lambda name: make_greeter("Hello", name)

# BETTER
from functools import partial
hello = partial(make_greeter, "Hello")
```

## Mistake 04: Side effects in map
```python
# WRONG — map is for transformation, not side effects
list(map(print, [1, 2, 3]))  # prints AND returns [None, None, None]

# CORRECT
for x in [1, 2, 3]:
    print(x)
```

## Mistake 05: Confusing any/all with OR/AND
```python
# WRONG
if any(x for x in items):  # works but redundant
# SIMPLER
if items:  # truthy if non-empty
```
