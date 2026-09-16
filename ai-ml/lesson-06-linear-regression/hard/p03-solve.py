"""
LESSON — Linear Regression
HARD P03 — Build a regression model with assumption checking: fit linear regression, plot residuals, check for linearity (scatter), homoscedasticity (residual plot), and normality (histogram of residuals). Report which assumptions hold.
==================================================

CONCEPT:
  See concepts.md in this lesson folder for detailed explanations.

PROBLEM:
  Build a regression model with assumption checking: fit linear regression, plot residuals, check for linearity (scatter), homoscedasticity (residual plot), and normality (histogram of residuals). Report which assumptions hold


Write a function `solve()` that implements the solution.

# Check your answer: compare with solutions/p03-solution.py
"""

TRY THIS INPUT:
  Add this test code at the bottom of your file:

  ```python
  X, y = make_regression(n_samples=300, n_features=1, noise=10, random_state=42)
  X_train, X_test, y_train, y_test = train_test_split(
  X, y, test_size=0.2, random_state=42

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
