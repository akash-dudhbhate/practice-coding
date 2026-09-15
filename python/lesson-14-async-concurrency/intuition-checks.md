# Lesson 14 — Intuition Checks

## Check 01: map vs comprehension
```python
# Which is more Pythonic?
list(map(str, [1, 2, 3]))           # A
[str(x) for x in [1, 2, 3]]        # B
```
<details><summary>Answer</summary>
**B** — list comprehensions are generally preferred in Python. More readable.
</details>

## Check 02: filter
```python
result = filter(lambda x: x > 2, [1, 2, 3, 4])
print(list(result))
```
<details><summary>Answer</summary>
`[3, 4]` — keeps elements where the function returns True.
</details>

## Check 03: reduce
```python
from functools import reduce
result = reduce(lambda a, b: a * b, [1, 2, 3, 4])
print(result)
```
<details><summary>Answer</summary>
`24` — `((1 * 2) * 3) * 4`. reduce applies function cumulatively.
</details>

## Check 04: partial
```python
from functools import partial
double = partial(lambda x, y: x * y, 2)
print(double(5))
```
<details><summary>Answer</summary>
`10` — `partial` fixes the first argument. `double(5)` = `lambda(2, 5)` = 10.
</details>

## Check 05: any/all
```python
print(any([False, 0, "", None]))
print(all([True, 1, "a"]))
```
<details><summary>Answer</summary>
`False`, `True` — `any` returns True if ANY element is truthy. `all` returns True if ALL elements are truthy.
</details>
