"""
LESSON — Decision Trees Forests
HARD P03 — Build a feature importance analysis: train a random forest, get feature importances, select top 5 features, retrain with only those features. Compare accuracy before and after feature selection. Document whether reducing features hurt.
==================================================

CONCEPT:
  See concepts.md in this lesson folder for detailed explanations.

PROBLEM:
  Build a feature importance analysis: train a random forest, get feature importances, select top 5 features, retrain with only those features. Compare accuracy before and after feature selection. Document whether reducing features hurt


Write a function `solve()` that implements the solution.

# Check your answer: compare with solutions/p03-solution.py
"""

TRY THIS INPUT:
  Add this test code at the bottom of your file:

  ```python
  X, y = make_classification(
  n_samples=1000, n_features=20, n_informative=8,
  n_redundant=4, random_state=42

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
