# Lesson 04 — Intuition Checks

## Check 01: Dict vs List Lookup
```python
d = {i: i for i in range(10000)}
l = list(range(10000))

# Which is faster?
# A: `9999 in d`
# B: `9999 in l`
```
Which is faster?

<details><summary>Answer</summary>
**A is much faster.** Dict lookup is O(1) (hash table). List lookup is O(n) (scans each element). For 10000 items, dict is ~10000× faster for worst case.
</details>

## Check 02: Dict Ordering
```python
d = {"c": 1, "a": 2, "b": 3}
print(list(d.keys()))
```
What prints? (Python 3.7+)

<details><summary>Answer</summary>
```
['c', 'a', 'b']
```
Since Python 3.7, dicts maintain insertion order. Before 3.7, order was arbitrary.
</details>

## Check 03: Set Operations
```python
a = {1, 2, 3}
b = {2, 3, 4}
print(a & b)
print(a | b)
print(a - b)
```
What prints (3 lines)?

<details><summary>Answer</summary>
```
{2, 3}
{1, 2, 3, 4}
{1}
```
`&` = intersection, `|` = union, `-` = difference.
</details>

## Check 04: Dict Get with Default
```python
d = {"a": 1}
print(d.get("b", 0))
print(d.get("a", 0))
print(d["b"])
```
What happens (3 lines)?

<details><summary>Answer</summary>
```
0
1
KeyError
```
`.get(key, default)` returns default if key missing. `d[key]` raises KeyError if missing.
</details>

## Check 05: Set from String
```python
s = set("hello")
print(s)
print(len(s))
```
What prints (2 lines)?

<details><summary>Answer</summary>
```
{'h', 'e', 'l', 'o'}
4
```
`set("hello")` creates a set of UNIQUE characters. 'l' appears twice in "hello" but once in the set.
</details>
