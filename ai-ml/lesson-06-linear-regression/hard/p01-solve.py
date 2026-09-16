"""
LESSON — Linear Regression
HARD P01 — Build a complete regression pipeline: load a real dataset (e.g., California Housing from sklearn), preprocess (scale features), train, evaluate with MSE/R², and plot actual vs predicted values.
==================================================

CONCEPT:
  See concepts.md in this lesson folder for detailed explanations.

PROBLEM:
  Build a complete regression pipeline: load a real dataset (e.g., California Housing from sklearn), preprocess (scale features), train, evaluate with MSE/R², and plot actual vs predicted values


Write a function `solve()` that implements the solution.

# Check your answer: compare with solutions/p01-solution.py
"""

TRY THIS INPUT:
  Add this test code at the bottom of your file:

  ```python
  data = fetch_california_housing()
  X, y = data.data, data.target
  feature_names = data.feature_names

  # Call your function
  result = solve(...)
  print(result)
  ```

EXPECTED OUTPUT:
  Run the solution file to see expected output:
    python3 hard/solutions/p01-solution.py

  Then compare your output format with theirs.

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
