"""
LESSON — Cross Validation Tuning
EASY P02 — Use `StratifiedKFold` with 5 folds on an imbalanced dataset (90% class 0). Verify each fold has the same class ratio. Print fold sizes and class counts.
==================================================

CONCEPT:
  See concepts.md in this lesson folder for detailed explanations.

PROBLEM:
  Use `StratifiedKFold` with 5 folds on an imbalanced dataset (90% class 0). Verify each fold has the same class ratio. Print fold sizes and class counts


Write a function `solve()` that implements the solution.

# Check your answer: compare with solutions/p02-solution.py
"""

TRY THIS INPUT:
  Add this test code at the bottom of your file:

  ```python
  X, y = make_classification(
  n_samples=1000, n_features=5, n_informative=3,
  weights=[0.9], random_state=42

  # Call your function
  result = solve(...)
  print(result)
  ```

EXPECTED OUTPUT:
  Run the solution file to see expected output:
    python3 easy/solutions/p02-solution.py

  Then compare your output format with theirs.

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
