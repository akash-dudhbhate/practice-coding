"""
Lesson 03 - Easy P01
Create a 4x5 array of random integers (0-100) with a fixed seed.
Print shape, dtype, ndim, size, and column means.

Solution:
  1. Set a random seed for reproducibility.
  2. Create a 4x5 array of random integers in [0, 100].
  3. Print array attributes and column-wise means.
"""

import numpy as np

# ---------------------------------------------------------------------------
# 1. Set seed and create the array
# ---------------------------------------------------------------------------
# Solution: np.random.seed() ensures the same random numbers are generated
# every run, making results reproducible.
np.random.seed(42)
arr = np.random.randint(0, 101, size=(4, 5))

# ---------------------------------------------------------------------------
# 2. Print the array and its attributes
# ---------------------------------------------------------------------------
print("Array:")
print(arr)
print()

print(f"shape : {arr.shape}   # (rows, cols) = (4, 5)")
print(f"dtype : {arr.dtype}   # data type of elements")
print(f"ndim  : {arr.ndim}    # number of dimensions")
print(f"size  : {arr.size}    # total number of elements")
print()

# ---------------------------------------------------------------------------
# 3. Compute and print column means
# ---------------------------------------------------------------------------
# Solution: axis=0 computes the mean along rows (i.e., per column).
col_means = arr.mean(axis=0)
print("Column means (axis=0):")
for i, m in enumerate(col_means):
    print(f"  Column {i}: {m:.2f}")
print()

# Bonus: row means (axis=1)
row_means = arr.mean(axis=1)
print("Row means (axis=1):")
for i, m in enumerate(row_means):
    print(f"  Row {i}: {m:.2f}")
