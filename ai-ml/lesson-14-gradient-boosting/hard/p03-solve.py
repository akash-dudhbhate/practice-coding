"""
LESSON — Gradient Boosting
HARD P03 — Build a boosting library comparison: compare sklearn GradientBoosting, XGBoost, LightGBM (if installed) on the same dataset. For each: training time, accuracy, F1, and memory usage. Create a comparison table. Identify the best for speed and the best for accuracy.
==================================================

CONCEPT:
  See concepts.md in this lesson folder for detailed explanations.

PROBLEM:
  Build a boosting library comparison: compare sklearn GradientBoosting, XGBoost, LightGBM (if installed) on the same dataset. For each: training time, accuracy, F1, and memory usage. Create a comparison table. Identify the best for speed and the best for accuracy


Write a function `solve()` that implements the solution.

# Check your answer: compare with solutions/p03-solution.py
"""

TRY THIS INPUT:
  Add this test code at the bottom of your file:

  ```python
  X, y = make_classification(n_samples=5000, n_features=30, n_informative=15, n_redundant=5,
  random_state=42)
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

  # Call your function
  result = solve(...)
  print(result)
  ```

EXPECTED OUTPUT:
  Run the solution file to see expected output:
    python3 hard/solutions/p03-solution.py

  Then compare your output format with theirs.

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
