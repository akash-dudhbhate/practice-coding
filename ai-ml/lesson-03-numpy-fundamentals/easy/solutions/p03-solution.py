"""
Lesson 03 - Easy P03
Reshape a 1D array of 24 elements to (2, 3, 4), transpose to (4, 3, 2),
flatten back, and verify the flattened array matches the original.

Solution:
  1. Create a 1D array with 24 elements.
  2. Reshape to (2, 3, 4).
  3. Transpose to (4, 3, 2) using .transpose().
  4. Flatten back to 1D.
  5. Verify the flattened array equals the original.
"""

import numpy as np

# ---------------------------------------------------------------------------
# 1. Create a 1D array with 24 elements
# ---------------------------------------------------------------------------
arr_1d = np.arange(1, 25)  # [1, 2, ..., 24]
print(f"Original 1D array (shape {arr_1d.shape}):")
print(arr_1d)
print()

# ---------------------------------------------------------------------------
# 2. Reshape to (2, 3, 4)
# ---------------------------------------------------------------------------
# Solution: reshape() changes the shape without changing data.
# 2 x 3 x 4 = 24 elements, so the reshape is valid.
arr_3d = arr_1d.reshape(2, 3, 4)
print(f"Reshaped to (2, 3, 4) — shape {arr_3d.shape}:")
print(arr_3d)
print()

# ---------------------------------------------------------------------------
# 3. Transpose to (4, 3, 2)
# ---------------------------------------------------------------------------
# Solution: .transpose() with no args reverses all axes: (2,3,4) -> (4,3,2).
# Alternatively, use .T for the same effect on all axes.
arr_transposed = arr_3d.transpose()  # shape becomes (4, 3, 2)
print(f"Transposed to (4, 3, 2) — shape {arr_transposed.shape}:")
print(arr_transposed)
print()

# ---------------------------------------------------------------------------
# 4. Flatten back to 1D
# ---------------------------------------------------------------------------
# Solution: .flatten() returns a copy of the array collapsed into 1D.
# .ravel() does the same but returns a view when possible.
arr_flat = arr_transposed.flatten()
print(f"Flattened back to 1D — shape {arr_flat.shape}:")
print(arr_flat)
print()

# ---------------------------------------------------------------------------
# 5. Verify the flattened array matches the original
# ---------------------------------------------------------------------------
# Note: transposing changes element order, so the flattened transposed array
# will NOT equal the original. We verify by checking the reshape -> flatten
# round-trip (without transpose) equals the original.
arr_reshaped_back = arr_3d.flatten()
matches_original = np.array_equal(arr_reshaped_back, arr_1d)

print("Verification:")
print(f"  reshape(2,3,4) then flatten == original: {matches_original}")
print(f"  (Transposed flatten differs in order due to axis swap)")

# Demonstrate the correct round-trip: transpose twice returns to original
arr_double_transpose = arr_transposed.transpose().flatten()
matches_double = np.array_equal(arr_double_transpose, arr_1d)
print(f"  transpose twice then flatten == original: {matches_double}")
