"""
LESSON — Logistic Regression
HARD P01 — Build a complete binary classification pipeline: load Breast Cancer dataset, preprocess (scale), train logistic regression with different C values (0.01, 1, 100), compare precision/recall/F1 for each. Plot the effect of C.
==================================================

CONCEPT:
  See concepts.md in this lesson folder for detailed explanations.

PROBLEM:
  Build a complete binary classification pipeline: load Breast Cancer dataset, preprocess (scale), train logistic regression with different C values (0.01, 1, 100), compare precision/recall/F1 for each. Plot the effect of C


Write a function `solve()` that implements the solution.

# Check your answer: compare with solutions/p01-solution.py
"""

TRY THIS INPUT:
  Add this test code at the bottom of your file:

  ```python
  data = load_breast_cancer()
  X, y = data.data, data.target

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
