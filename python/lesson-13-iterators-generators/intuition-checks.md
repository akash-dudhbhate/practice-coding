# Lesson 13 — Intuition Checks

## Check 01: Iterator Protocol
```python
class Range3:
    def __iter__(self):
        yield 0; yield 1; yield 2

for x in Range3():
    print(x)
```
<details><summary>Answer</summary>
```
0
1
2
```
`__iter__` can be a generator — each `yield` produces a value.
</details>

## Check 02: namedtuple vs tuple
```python
from collections import namedtuple
P = namedtuple("P", "x y")
p = P(1, 2)
print(p[0], p.x)
```
<details><summary>Answer</summary>
`1 1` — namedtuples support BOTH index access (like tuples) AND attribute access.
</details>

## Check 03: deque vs list
```python
from collections import deque
d = deque([1, 2, 3])
d.appendleft(0)
print(d)
```
<details><summary>Answer</summary>
`deque([0, 1, 2, 3])` — deque supports O(1) append/pop at both ends. List is O(n) at the front.
</details>

## Check 04: Chain
```python
from itertools import chain
for x in chain([1, 2], [3, 4]):
    print(x)
```
<details><summary>Answer</summary>
```
1
2
3
4
```
`chain` combines iterables without creating a new list.
</details>

## Check 05: zip_longest
```python
from itertools import zip_longest
for a, b in zip_longest([1, 2], [3, 4, 5]):
    print(a, b)
```
<details><summary>Answer</summary>
```
1 3
2 4
None 5
```
`zip_longest` fills missing values with None (or a specified fillvalue). Regular `zip` stops at the shortest.
</details>
