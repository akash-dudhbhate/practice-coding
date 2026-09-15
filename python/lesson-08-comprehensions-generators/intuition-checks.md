# Lesson 08 — Intuition Checks

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
