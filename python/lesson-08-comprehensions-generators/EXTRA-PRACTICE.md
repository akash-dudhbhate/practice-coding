# lesson-08-comprehensions-generators — Extra Practice
Everything beyond the core lesson lives here, in order:
mental quizzes → debug drills → mistakes → refactoring → comparisons.

---

## Intuition Checks — predict before you run

## Check 01: Comprehension vs Loop
```python
# Are these equivalent?
a = [x * 2 for x in range(3)]
b = []
for x in range(3):
    b.append(x * 2)
print(a == b)
```
<details><summary>Answer</summary>
`True` — list comprehension is syntactic sugar for a for-loop with append. But comprehension is faster (optimized in CPython).
</details>

## Check 02: Generator Memory
```python
# Which uses less memory for 1M numbers?
a = [x for x in range(1000000)]
b = (x for x in range(1000000))
```
<details><summary>Answer</summary>
`b` (generator) uses almost no memory — it produces values on demand. `a` (list) stores all 1M numbers in memory (~8MB). Use generators for large sequences.
</details>

## Check 03: Nested Comprehension
```python
matrix = [[i * j for j in range(3)] for i in range(3)]
print(matrix)
```
<details><summary>Answer</summary>
`[[0, 0, 0], [0, 1, 2], [0, 2, 4]]` — outer loop (i) creates rows, inner loop (j) creates values in each row.
</details>

## Check 04: Filter in Comprehension
```python
result = [x for x in range(10) if x % 2 == 0 if x % 3 == 0]
print(result)
```
<details><summary>Answer</summary>
`[0, 6]` — multiple `if` clauses are ANDed. Must be even AND divisible by 3.
</details>

## Check 05: Generator vs List Performance
```python
# Which is faster for sum?
sum([x for x in range(1000000)])  # A
sum(x for x in range(1000000))    # B
```
<details><summary>Answer</summary>
**B is faster** — the generator doesn't build a list in memory. `sum()` consumes values one at a time. Less memory allocation = faster.
</details>

---

## Debug Exercises — find and fix the bug

## Debug 01 (Easy): List Comprehension — Wrong Syntax
```python
squares = [for i in range(5): i * i]
```
<details><summary>Answer</summary>
**Bug:** Wrong syntax. Comprehension is `[expression for item in iterable]`, not `[for item in iterable: expression]`.
**Fix:** `squares = [i * i for i in range(5)]`
</details>

## Debug 02 (Medium): Dict Comprehension — Wrong Brackets
```python
lengths = {for word in words: word: len(word)}
```
<details><summary>Answer</summary>
**Bug:** Dict comprehension syntax is `{key: value for item in iterable}`.
**Fix:** `lengths = {word: len(word) for word in words}`
</details>

## Debug 03 (Hard): Generator Exhaustion
```python
gen = (x * 2 for x in range(5))
print(list(gen))
print(list(gen))
```
<details><summary>Answer</summary>
**Bug:** Generators are single-use. The first `list(gen)` exhausts it. The second `list(gen)` returns `[]`.
**Fix:** Store the list if you need to iterate multiple times: `result = list(gen)`.
</details>

---

## Common Mistakes — the traps learners hit

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

---

## Refactoring Challenges — make working code better

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

---

## Approach Comparison — different ways to solve it

## Problem: Squares of Even Numbers

### Approach 1: List comprehension
```python
result = [x * x for x in range(20) if x % 2 == 0]
```

### Approach 2: Generator + list
```python
result = list(x * x for x in range(20) if x % 2 == 0)
```

### Approach 3: Filter + map
```python
result = list(map(lambda x: x * x, filter(lambda x: x % 2 == 0, range(20))))
```

**Winner:** Approach 1 — most readable, most Pythonic. Approach 3 is functional style but harder to read.

---

## Problem: Sum of Squares

### Approach 1: List comprehension
```python
total = sum([x * x for x in range(1000000)])
```
**Cons:** Builds a 1M element list in memory just to sum it.

### Approach 2: Generator expression
```python
total = sum(x * x for x in range(1000000))
```
**Pros:** No list built — values produced on demand. Less memory, faster.

**Winner:** Approach 2 — always use generator expressions with `sum()`, `max()`, `min()`, `any()`, `all()`.
