"""
LESSON — Evaluation Metrics
HARD P01 — Build a metric comparison script: train 3 models (logistic regression, decision tree, random forest) on the same dataset. For each, print accuracy, precision, recall, F1, and AUC. Create a comparison table (pandas DataFrame).
==================================================

CONCEPT:
  See concepts.md in this lesson folder for detailed explanations.

PROBLEM:
  Build a metric comparison script: train 3 models (logistic regression, decision tree, random forest) on the same dataset. For each, print accuracy, precision, recall, F1, and AUC. Create a comparison table (pandas DataFrame)


Write a function `solve()` that implements the solution.

# Check your answer: compare with solutions/p01-solution.py
"""

TRY THIS INPUT:
  Add this test code at the bottom of your file:

  ```python
  X, y = make_classification(
  n_samples=1000, n_features=15, n_informative=8,
  n_redundant=3, random_state=42

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
