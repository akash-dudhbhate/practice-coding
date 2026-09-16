"""
LESSON — Gradient Boosting
EASY P03 — Train gradient boosting with `n_iter_no_change=10` (early stopping). Print the actual number of trees used (`n_estimators_`). Show that it stops before the max.
==================================================

CONCEPT:
  See concepts.md in this lesson folder for detailed explanations.

PROBLEM:
  Train gradient boosting with `n_iter_no_change=10` (early stopping). Print the actual number of trees used (`n_estimators_`). Show that it stops before the max


Write a function `solve()` that implements the solution.

# Check your answer: compare with solutions/p03-solution.py
"""

TRY THIS INPUT:
  Add this test code at the bottom of your file:

  ```python
  X, y = make_classification(n_samples=1000, n_features=20, n_informative=10, n_redundant=5,
  random_state=42)
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

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
