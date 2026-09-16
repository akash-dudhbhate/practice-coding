"""
LESSON — Linear Regression
MEDIUM P02 — Implement gradient descent for linear regression from scratch. Start with m=0, b=0. Update using gradients. Track MSE over 1000 iterations. Plot the loss curve.
==================================================

CONCEPT:
  See concepts.md in this lesson folder for detailed explanations.

PROBLEM:
  Implement gradient descent for linear regression from scratch. Start with m=0, b=0. Update using gradients. Track MSE over 1000 iterations. Plot the loss curve


Write a function `solve()` that implements the solution.

# Check your answer: compare with solutions/p02-solution.py
"""

TRY THIS INPUT:
  Add this test code at the bottom of your file:

  ```python
  x = np.array([1, 2, 3, 4, 5], dtype=float)
  y = np.array([2, 4, 5, 4, 5], dtype=float)

  # Call your function
  result = solve(...)
  print(result)
  ```

EXPECTED OUTPUT:
  Run the solution file to see expected output:
    python3 medium/solutions/p02-solution.py

  Then compare your output format with theirs.

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
