"""
LESSON — Evaluation Metrics
MEDIUM P01 — Create an imbalanced dataset (95% class 0, 5% class 1). Train a model. Show that accuracy is high (95%) but recall for class 1 is low. Print the classification report.
==================================================

CONCEPT:
  See concepts.md in this lesson folder for detailed explanations.

PROBLEM:
  Create an imbalanced dataset (95% class 0, 5% class 1). Train a model. Show that accuracy is high (95%) but recall for class 1 is low. Print the classification report


Write a function `solve()` that implements the solution.

# Check your answer: compare with solutions/p01-solution.py
"""

TRY THIS INPUT:
  Add this test code at the bottom of your file:

  ```python
  X, y = make_classification(
  n_samples=2000, n_features=10, n_informative=5,
  n_redundant=2, weights=[0.95], flip_y=0.01,
  random_state=42

  # Call your function
  result = solve(...)
  print(result)
  ```

EXPECTED OUTPUT:
  Run the solution file to see expected output:
    python3 medium/solutions/p01-solution.py

  Then compare your output format with theirs.

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
