# Lesson 19 — Intuition Checks

## Check 01: Array vs List
```python
a = np.array([1, 2, 3])
b = [1, 2, 3]
print(a * 2)
print(b * 2)
```
<details><summary>Answer</summary>
```
[2 4 6]
[1, 2, 3, 1, 2, 3]
```
Array does element-wise multiplication. List repeats.
</details>

## Check 02: Shape
```python
a = np.array([[1, 2], [3, 4]])
print(a.shape)
print(a.ndim)
```
<details><summary>Answer</summary>
`(2, 2)`, `2` — shape is dimensions, ndim is number of dimensions.
</details>

## Check 03: Broadcasting
```python
a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([10, 20, 30])
print(a + b)
```
<details><summary>Answer</summary>
```
[[11 22 33]
 [14 25 36]]
```
b is broadcast across rows.
</details>

## Check 04: Random Seed
```python
np.random.seed(42)
a = np.random.rand(3)
np.random.seed(42)
b = np.random.rand(3)
print(np.array_equal(a, b))
```
<details><summary>Answer</summary>
`True` — setting the same seed produces the same "random" numbers. Essential for reproducibility.
</details>

## Check 05: Vectorized vs Loop
```python
# Which is faster for sum of squares?
# A: sum(x**2 for x in arr)
# B: np.sum(arr ** 2)
```
<details><summary>Answer</summary>
**B** — numpy vectorized operations are 100x+ faster than Python loops for large arrays.
</details>
