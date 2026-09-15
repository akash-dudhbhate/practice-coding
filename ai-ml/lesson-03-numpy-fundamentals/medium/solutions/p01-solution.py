"""
Lesson 03 - Medium P01
Broadcasting: standardize student scores by column (subtract mean, divide by std).

Solution:
  1. Create a matrix of student scores (rows=students, cols=subjects).
  2. Compute column means and stds.
  3. Use broadcasting to standardize: z = (X - mean) / std.
  4. Verify each column has mean ~ 0 and std ~ 1.
"""

import numpy as np

# ---------------------------------------------------------------------------
# 1. Create student scores: 10 students x 4 subjects
# ---------------------------------------------------------------------------
np.random.seed(42)
# Different scales per subject to show why standardization matters
scores = np.array([
    np.random.randint(0, 100, 10),    # Math: 0-100
    np.random.randint(0, 20, 10),     # Quiz: 0-20
    np.random.randint(200, 800, 10),  # SAT: 200-800
    np.random.randint(0, 50, 10),     # Project: 0-50
]).T  # transpose so rows=students, cols=subjects

subjects = ["Math", "Quiz", "SAT", "Project"]
print("Student scores (rows=students, cols=subjects):")
print(scores)
print()

print("Original column means:", scores.mean(axis=0))
print("Original column stds: ", scores.std(axis=0))
print()

# ---------------------------------------------------------------------------
# 2. Standardize using broadcasting
# ---------------------------------------------------------------------------
# Solution: NumPy broadcasting automatically expands the 1D mean/std arrays
# (shape (4,)) to match the 2D scores array (shape (10, 4)).
#   scores (10,4) - mean (4,)   -> broadcast to (10,4)
#   result  (10,4) / std  (4,)  -> broadcast to (10,4)
col_means = scores.mean(axis=0)  # shape (4,)
col_stds = scores.std(axis=0)    # shape (4,)

standardized = (scores - col_means) / col_stds

print("Standardized scores:")
print(standardized)
print()

# ---------------------------------------------------------------------------
# 3. Verify mean ~ 0 and std ~ 1 per column
# ---------------------------------------------------------------------------
print("Verification:")
print(f"  Column means: {standardized.mean(axis=0)}")
print(f"  Column stds:  {standardized.std(axis=0)}")
print()

means_ok = np.allclose(standardized.mean(axis=0), 0, atol=1e-10)
stds_ok = np.allclose(standardized.std(axis=0), 1, atol=1e-10)
print(f"  All means ~ 0: {means_ok}")
print(f"  All stds  ~ 1: {stds_ok}")
