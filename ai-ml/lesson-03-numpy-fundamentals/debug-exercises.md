# Lesson 03 — Debug Exercises

## Debug 01 (Easy: Shape Mismatch
```python
a = np.array([1, 2, 3])
b = np.array([1, 2])
print(a + b)
```
<details><summary>Answer</summary>
**Bug:** Shapes (3,) and (2,) don't broadcast. ValueError.
**Fix:** Make shapes compatible or use different operation.
</details>

## Debug 02 (Medium: Integer Division in Array
```python
arr = np.array([1, 2, 3], dtype=int)
print(arr / 2)
```
<details><summary>Answer</summary>
In Python 3, `/` returns float even for int arrays: `[0.5, 1., 1.5]`. Use `//` for integer division if needed.
</details>

## Debug 03 (Hard: Copy vs View
```python
a = np.array([1, 2, 3])
b = a
b[0] = 99
print(a)  # [99, 2, 3]
```
<details><summary>Answer</summary>
**Bug:** `b = a` is a reference, not a copy. Modifying b modifies a.
**Fix:** `b = a.copy()`.
</details>
