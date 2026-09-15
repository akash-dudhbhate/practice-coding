# Lesson 08 — Refactoring Challenges

## Refactor 01 (Easy): Map + Lambda
### Before
```python
result = list(map(lambda x: x ** 2, numbers))
```
### After
```python
result = [x ** 2 for x in numbers]
```

## Refactor 02 (Medium): Nested Loops to Comprehension
### Before
```python
result = []
for row in matrix:
    for val in row:
        if val > 0:
            result.append(val)
```
### After
```python
result = [val for row in matrix for val in row if val > 0]
```

## Refactor 03 (Hard): List When Generator Suffices
### Before
```python
total = sum([x * 2 for x in range(1000000)])
```
### After
```python
total = sum(x * 2 for x in range(1000000))
```
