"""
LESSON — Neural Networks
HARD P02 — Build an MLP regression pipeline: create a non-linear regression dataset, train MLPRegressor with different hidden layer sizes, plot the predictions vs actual for each, and identify the best architecture. Show overfitting with too many neurons.
==================================================

CONCEPT:
  See concepts.md in this lesson folder for detailed explanations.

PROBLEM:
  Build an MLP regression pipeline: create a non-linear regression dataset, train MLPRegressor with different hidden layer sizes, plot the predictions vs actual for each, and identify the best architecture. Show overfitting with too many neurons


Write a function `solve()` that implements the solution.

# Check your answer: compare with solutions/p02-solution.py
"""

TRY THIS INPUT:
  Add this test code at the bottom of your file:

  ```python
  X = np.sort(np.random.rand(300, 1) * 10, axis=0)
  y = np.sin(X).ravel() + np.random.randn(300) * 0.1

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
