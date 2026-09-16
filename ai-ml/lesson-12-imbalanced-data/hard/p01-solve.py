"""
LESSON — Imbalanced Data
HARD P01 — Build a complete imbalanced data pipeline: create a 99:1 dataset, compare 4 approaches (baseline, class_weight, SMOTE, SMOTE+undersampling). For each, print F1, PR-AUC, and confusion matrix. Identify the best approach.
==================================================

CONCEPT:
  See concepts.md in this lesson folder for detailed explanations.

PROBLEM:
  Build a complete imbalanced data pipeline: create a 99:1 dataset, compare 4 approaches (baseline, class_weight, SMOTE, SMOTE+undersampling). For each, print F1, PR-AUC, and confusion matrix. Identify the best approach


Write a function `solve()` that implements the solution.

# Check your answer: compare with solutions/p01-solution.py
"""

TRY THIS INPUT:
  Add this test code at the bottom of your file:

  ```python
  X, y = make_classification(
  n_samples=10000,
  n_features=20,
  n_informative=10,
  weights=[0.99, 0.01],
  flip_y=0.0,
  random_state=42,

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
