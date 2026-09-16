"""
LESSON — Logistic Regression
EASY P02 — Use sklearn to train logistic regression on `make_classification` (binary). Print accuracy, precision, recall, and F1-score.
==================================================

CONCEPT:
  See concepts.md in this lesson folder for detailed explanations.

PROBLEM:
  Use sklearn to train logistic regression on `make_classification` (binary). Print accuracy, precision, recall, and F1-score


Write a function `solve()` that implements the solution.

# Check your answer: compare with solutions/p02-solution.py
"""

TRY THIS INPUT:
  Add this test code at the bottom of your file:

  ```python
  X, y = make_classification(
  n_samples=500, n_features=10, n_informative=5,
  n_redundant=2, n_classes=2, random_state=42

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
