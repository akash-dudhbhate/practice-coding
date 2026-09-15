# Lesson 08 — Common Mistakes

## Mistake 01: Overusing comprehensions
```python
# UNREADABLE
result = [transform(x) for x in data if validate(x) for y in process(x) if filter(y)]

# BETTER — use a loop
result = []
for x in data:
    if validate(x):
        for y in process(x):
            if filter(y):
                result.append(transform(y))
```

## Mistake 02: Reusing exhausted generators
```python
gen = (x for x in range(5))
list(gen)  # [0, 1, 2, 3, 4]
list(gen)  # [] — already exhausted!
```

## Mistake 03: Using list when generator suffices
```python
# WASTES MEMORY
total = sum([x * 2 for x in range(1000000)])

# BETTER
total = sum(x * 2 for x in range(1000000))
```

## Mistake 04: Side effects in comprehension
```python
# WRONG — comprehension is for creating data, not side effects
[print(x) for x in range(5)]

# CORRECT
for x in range(5):
    print(x)
```

## Mistake 05: Confusing generator expression with list comprehension
```python
a = (x for x in range(5))  # generator — lazy
b = [x for x in range(5)]  # list — eager
print(type(a))  # <class 'generator'>
print(type(b))  # <class 'list'>
```
