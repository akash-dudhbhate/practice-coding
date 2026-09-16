"""
LESSON — Pytorch Fundamentals
HARD P03 — Build a regression pipeline: create a non-linear regression dataset, build a PyTorch MLP, train with MSE loss and Adam optimizer, plot predictions vs actual, and track train/val loss. Add dropout and show it reduces overfitting.
==================================================

CONCEPT:
  See concepts.md in this lesson folder for detailed explanations.

PROBLEM:
  Build a regression pipeline: create a non-linear regression dataset, build a PyTorch MLP, train with MSE loss and Adam optimizer, plot predictions vs actual, and track train/val loss. Add dropout and show it reduces overfitting


Write a function `solve()` that implements the solution.

# Check your answer: compare with solutions/p03-solution.py
"""

TRY THIS INPUT:
  Add this test code at the bottom of your file:

  ```python
  X = np.sort(np.random.rand(300, 1) * 10, axis=0)
  y = np.sin(X).ravel() + np.random.randn(300) * 0.15

  # Call your function
  result = solve(...)
  print(result)
  ```

EXPECTED OUTPUT:
  Run the solution file to see expected output:
    python3 hard/solutions/p03-solution.py

  Then compare your output format with theirs.

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
