# Lesson 08 — Debug Exercises

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
