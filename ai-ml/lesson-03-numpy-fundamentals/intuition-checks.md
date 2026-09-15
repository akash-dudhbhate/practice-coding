# Lesson 03 — Intuition Checks

## Check 01: Why NumPy?
<details><summary>Answer</summary>
NumPy arrays are: faster than lists (C implementation), use less memory (contiguous), support vectorized operations (no Python loops), enable broadcasting.
</details>

## Check 02: Broadcasting
```python
a = np.array([[1, 2], [3, 4]])  # shape (2, 2)
b = np.array([10, 20])          # shape (2,)
print(a + b)  # ?
```
<details><summary>Answer</summary>
`[[11, 22], [13, 24]]` — b is broadcast across rows. Shape (2,) aligns with last dimension of (2,2).
</details>

## Check 03: axis
```python
a = np.array([[1, 2], [3, 4]])
print(a.sum(axis=0))  # ?
print(a.sum(axis=1))  # ?
```
<details><summary>Answer</summary>
axis=0: `[4, 6]` (sum down columns). axis=1: `[3, 7]` (sum across rows). axis=0 collapses rows, axis=1 collapses columns.
</details>

## Check 04: dtype
```python
a = np.array([1, 2, 3], dtype=float)
b = np.array([1, 2, 3], dtype=int)
print(a.dtype, b.dtype)
```
<details><summary>Answer</summary>
`float64 int64` — dtype determines memory and operations. Float for decimals, int for whole numbers. Mixed types upcast to most general.
</details>

## Check 05: reshape
```python
a = np.arange(6)
print(a.reshape(2, 3))
```
<details><summary>Answer</summary>
`[[0, 1, 2], [3, 4, 5]]` — reshapes 1D to 2D. Total elements must match. Use -1 for auto: `reshape(-1, 3)`.
</details>
