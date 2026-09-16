"""
LESSON — Linear Regression
HARD P02 — Implement polynomial regression: use `PolynomialFeatures` to add x², x³ terms. Compare linear vs polynomial fit on non-linear data. Plot both fits. Identify when polynomial overfits.
==================================================

CONCEPT:
  See concepts.md in this lesson folder for detailed explanations.

PROBLEM:
  Implement polynomial regression: use `PolynomialFeatures` to add x², x³ terms. Compare linear vs polynomial fit on non-linear data. Plot both fits. Identify when polynomial overfits


Write a function `solve()` that implements the solution.

# Check your answer: compare with solutions/p02-solution.py
"""

TRY THIS INPUT:
  Add this test code at the bottom of your file:

  ```python
  X = np.sort(6 * np.random.rand(100, 1) - 3, axis=0)
  y = 0.5 * X.ravel() ** 2 + X.ravel() + 2 + np.random.randn(100) * 0.5

  # Call your function
  result = solve(...)
  print(result)
  ```

EXPECTED OUTPUT:
  Run the solution file to see expected output:
    python3 hard/solutions/p02-solution.py

  Then compare your output format with theirs.

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
