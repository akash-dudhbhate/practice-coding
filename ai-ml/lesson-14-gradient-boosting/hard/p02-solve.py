"""
LESSON — Gradient Boosting
HARD P02 — Implement gradient boosting from scratch: implement the sequential tree training, residual calculation, and prediction (sum of trees * learning_rate). Use sklearn's DecisionTreeRegressor as the base. Train on a regression dataset. Plot the loss curve.
==================================================

CONCEPT:
  See concepts.md in this lesson folder for detailed explanations.

PROBLEM:
  Implement gradient boosting from scratch: implement the sequential tree training, residual calculation, and prediction (sum of trees * learning_rate). Use sklearn's DecisionTreeRegressor as the base. Train on a regression dataset. Plot the loss curve


Write a function `solve()` that implements the solution.

# Check your answer: compare with solutions/p02-solution.py
"""

TRY THIS INPUT:
  Add this test code at the bottom of your file:

  ```python
  X, y = make_regression(n_samples=500, n_features=10, n_informative=5, noise=10, random_state=42)
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

  # Call your function
  result = solve(...)
  print(result)
  ```

EXPECTED OUTPUT:
  Run the solution file to see expected output:
    python3 hard/solutions/p02-solution.py

  Then compare your output format with theirs.

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
