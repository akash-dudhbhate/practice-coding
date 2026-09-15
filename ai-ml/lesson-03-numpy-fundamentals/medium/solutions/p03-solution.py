"""
Lesson 03 - Medium P03
Boolean masking: replace negatives with 0, clip values > 100 to 100, count changes.

Solution:
  1. Create an array with values spanning negative to > 100.
  2. Replace negatives with 0 using a boolean mask.
  3. Clip values > 100 to 100.
  4. Count how many elements were modified in each step.
"""

import numpy as np

# ---------------------------------------------------------------------------
# 1. Create a sample array with a wide range of values
# ---------------------------------------------------------------------------
np.random.seed(42)
arr = np.random.randint(-50, 150, size=20)
print("Original array:")
print(arr)
print()

# ---------------------------------------------------------------------------
# 2. Replace negatives with 0
# ---------------------------------------------------------------------------
# Solution: Boolean mask arr < 0 identifies negative positions.
# We count them before modifying, then set those positions to 0.
negative_mask = arr < 0
num_negatives = np.count_nonzero(negative_mask)
arr_clean = arr.copy()
arr_clean[negative_mask] = 0

print(f"Step 1 — Replace negatives with 0:")
print(f"  Negatives found: {num_negatives}")
print(f"  Array after:     {arr_clean}")
print()

# ---------------------------------------------------------------------------
# 3. Clip values > 100 to 100
# ---------------------------------------------------------------------------
# Solution: Boolean mask arr > 100 identifies values above the threshold.
# We count them, then set those positions to 100.
high_mask = arr_clean > 100
num_high = np.count_nonzero(high_mask)
arr_clipped = arr_clean.copy()
arr_clipped[high_mask] = 100

print(f"Step 2 — Clip values > 100 to 100:")
print(f"  Values > 100 found: {num_high}")
print(f"  Array after:        {arr_clipped}")
print()

# ---------------------------------------------------------------------------
# 4. Count total changes
# ---------------------------------------------------------------------------
total_changes = num_negatives + num_high
print(f"Total elements modified: {total_changes} out of {len(arr)}")
print()

# ---------------------------------------------------------------------------
# 5. Alternative: np.clip() does both in one step
# ---------------------------------------------------------------------------
# Solution: np.clip(arr, min, max) clamps values to [min, max] in one call.
arr_clipped_one_step = np.clip(arr, 0, 100)
print(f"One-step np.clip(arr, 0, 100):")
print(f"  {arr_clipped_one_step}")
print(f"  Matches step-by-step result: {np.array_equal(arr_clipped, arr_clipped_one_step)}")
