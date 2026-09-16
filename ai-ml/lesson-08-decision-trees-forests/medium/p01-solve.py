"""
LESSON — Decision Trees Forests
MEDIUM P01 — Train a random forest on `make_classification` (1000 samples, 20 features). Print accuracy. Extract and plot feature importances. Identify the top 5 features.
==================================================

CONCEPT:
  See concepts.md in this lesson folder for detailed explanations.

PROBLEM:
  Train a random forest on `make_classification` (1000 samples, 20 features). Print accuracy. Extract and plot feature importances. Identify the top 5 features


Write a function `solve()` that implements the solution.

# Check your answer: compare with solutions/p01-solution.py
"""

TRY THIS INPUT:
  Add this test code at the bottom of your file:

  ```python
  X, y = make_classification(
  n_samples=1000, n_features=20, n_informative=8,
  n_redundant=4, n_repeated=0, random_state=42

  # Call your function
  result = solve(...)
  print(result)
  ```

EXPECTED OUTPUT:
  Run the solution file to see expected output:
    python3 medium/solutions/p01-solution.py

  Then compare your output format with theirs.

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
