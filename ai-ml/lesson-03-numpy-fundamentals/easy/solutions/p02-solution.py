"""
Lesson 03 - Easy P02
Indexing and slicing on a 5x5 matrix:
  - Extract the center 3x3 submatrix.
  - Extract the last row.
  - Extract the first column.
  - Extract all elements greater than 10.

Solution:
  Use NumPy slicing [row_start:row_end, col_start:col_end] and boolean masking.
"""

import numpy as np

# ---------------------------------------------------------------------------
# 1. Create a 5x5 matrix
# ---------------------------------------------------------------------------
np.random.seed(42)
matrix = np.random.randint(0, 50, size=(5, 5))
print("Original 5x5 matrix:")
print(matrix)
print()

# ---------------------------------------------------------------------------
# 2. Extract the center 3x3 submatrix
# ---------------------------------------------------------------------------
# Solution: rows 1:4 and cols 1:4 give the center 3x3 block (indices 1,2,3).
center_3x3 = matrix[1:4, 1:4]
print("Center 3x3 submatrix (matrix[1:4, 1:4]):")
print(center_3x3)
print()

# ---------------------------------------------------------------------------
# 3. Extract the last row
# ---------------------------------------------------------------------------
# Solution: index -1 selects the last row.
last_row = matrix[-1]
print("Last row (matrix[-1]):")
print(last_row)
print()

# ---------------------------------------------------------------------------
# 4. Extract the first column
# ---------------------------------------------------------------------------
# Solution: [:, 0] selects all rows of column 0.
first_col = matrix[:, 0]
print("First column (matrix[:, 0]):")
print(first_col)
print()

# ---------------------------------------------------------------------------
# 5. Extract all elements greater than 10
# ---------------------------------------------------------------------------
# Solution: Boolean masking selects elements that satisfy a condition.
# This returns a 1D array of all matching elements (flattened).
elements_gt_10 = matrix[matrix > 10]
print("Elements > 10 (matrix[matrix > 10]):")
print(elements_gt_10)
print(f"Count: {len(elements_gt_10)}")
print()

# Bonus: Boolean mask showing which positions are > 10
print("Boolean mask (matrix > 10):")
print(matrix > 10)
