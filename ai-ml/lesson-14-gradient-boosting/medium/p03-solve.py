"""
LESSON — Gradient Boosting
MEDIUM P03 — Compare random forest vs gradient boosting on the same dataset. For both: tune key hyperparameters, print best accuracy, training time, and prediction time. Create a comparison table.
==================================================

CONCEPT:
  See concepts.md in this lesson folder for detailed explanations.

PROBLEM:
  Compare random forest vs gradient boosting on the same dataset. For both: tune key hyperparameters, print best accuracy, training time, and prediction time. Create a comparison table


Write a function `solve()` that implements the solution.

# Check your answer: compare with solutions/p03-solution.py
"""

TRY THIS INPUT:
  Add this test code at the bottom of your file:

  ```python
  X, y = make_classification(n_samples=2000, n_features=25, n_informative=12, n_redundant=5,
  random_state=42)
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

  # Call your function
  result = solve(...)
  print(result)
  ```

EXPECTED OUTPUT:
  Run the solution file to see expected output:
    python3 medium/solutions/p03-solution.py

  Then compare your output format with theirs.

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
