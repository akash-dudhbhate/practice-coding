# Lesson 14 — Debug Exercises

## Debug 01 (Easy): map Returns Iterator
```python
result = map(str, [1, 2, 3])
print(result[0])
```
<details><summary>Answer</summary>
**Bug:** `map` returns an iterator, not a list. Can't index.
**Fix:** `list(map(str, [1, 2, 3]))[0]`.
</details>

## Debug 02 (Medium): filter with None
```python
result = filter(None, [0, 1, 2, "", "a", None])
print(list(result))
```
<details><summary>Answer</summary>
`[1, 2, 'a']` — `filter(None, ...)` removes all falsy values (0, "", None, False, []).
</details>

## Debug 03 (Hard): reduce Missing Import
```python
result = reduce(lambda a, b: a + b, [1, 2, 3])
```
<details><summary>Answer</summary>
**Bug:** `reduce` is not a builtin in Python 3. Need `from functools import reduce`.
</details>
