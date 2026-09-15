# Lesson 19 — Debug Exercises

## Debug 01 (Easy): Array Creation
```python
arr = np.array([1, 2, 3], dtype=float)
arr[0] = "hello"
```
<details><summary>Answer</summary>
**Bug:** Can't put a string in a float array — ValueError.
**Fix:** Use object dtype or keep numeric.
</details>

## Debug 02 (Medium): Broadcasting Error
```python
a = np.array([[1, 2], [3, 4]])
b = np.array([1, 2, 3])
print(a + b)
```
<details><summary>Answer</summary>
**Bug:** Shapes (2,2) and (3,) don't broadcast. ValueError.
**Fix:** Reshape b to (2,) or (2,1) depending on intent.
</details>

## Debug 03 (Hard): Copy vs View
```python
a = np.array([1, 2, 3])
b = a[:2]
b[0] = 99
print(a)
```
<details><summary>Answer</summary>
**Bug:** `b = a[:2]` is a VIEW, not a copy. Modifying b modifies a. `a` becomes `[99, 2, 3]`.
**Fix:** `b = a[:2].copy()`.
</details>
