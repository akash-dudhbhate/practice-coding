# Lesson 05 — Common Mistakes

## Mistake 01: Using while when for is better
```python
# WRONG — manual counter
i = 0
while i < 10:
    print(i)
    i += 1

# CORRECT
for i in range(10):
    print(i)
```

## Mistake 02: Off-by-one in range
```python
# WRONG — misses the last element
for i in range(1, len(items)):  # skips index 0
# CORRECT
for i in range(len(items)):
```

## Mistake 03: Forgetting break/else pattern
```python
# VERBOSE
found = False
for item in items:
    if item == target:
        found = True
        break
if not found:
    print("not found")

# PYTHONIC — for/else
for item in items:
    if item == target:
        print("found")
        break
else:
    print("not found")
```

## Mistake 04: Modifying list during iteration
```python
# WRONG — skips elements after removal
for item in items:
    if item < 0:
        items.remove(item)

# CORRECT — list comprehension
items = [item for item in items if item >= 0]
```

## Mistake 05: Infinite while loop
```python
# WRONG — no exit condition update
while True:
    user_input = input("Enter q to quit: ")
    if user_input == "q":
        break
    # if user never types q, infinite loop!
```
