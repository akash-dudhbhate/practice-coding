"""
LESSON — Cross Validation Tuning
EASY P03 — Use `GridSearchCV` to tune `max_depth` (try 1, 3, 5, 10, 20) for a decision tree on `make_classification`. Print the best depth and best score.
==================================================

CONCEPT:
  See concepts.md in this lesson folder for detailed explanations.

PROBLEM:
  Use `GridSearchCV` to tune `max_depth` (try 1, 3, 5, 10, 20) for a decision tree on `make_classification`. Print the best depth and best score


Write a function `solve()` that implements the solution.

# Check your answer: compare with solutions/p03-solution.py
"""

TRY THIS INPUT:
  Add this test code at the bottom of your file:

  ```python
  X, y = make_classification(
  n_samples=800, n_features=15, n_informative=8,
  n_redundant=3, random_state=42

  # Call your function
  result = solve(...)
  print(result)
  ```

EXPECTED OUTPUT:
  Run the solution file to see expected output:
    python3 easy/solutions/p03-solution.py

  Then compare your output format with theirs.

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
