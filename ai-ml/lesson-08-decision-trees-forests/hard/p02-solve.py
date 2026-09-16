"""
LESSON — Decision Trees Forests
HARD P02 — Implement a simple decision tree from scratch: implement Gini impurity, find the best split, recursively build the tree. Train on a small 2D dataset. Plot the decision boundary.
==================================================

CONCEPT:
  See concepts.md in this lesson folder for detailed explanations.

PROBLEM:
  Implement a simple decision tree from scratch: implement Gini impurity, find the best split, recursively build the tree. Train on a small 2D dataset. Plot the decision boundary


Write a function `solve()` that implements the solution.

# Check your answer: compare with solutions/p02-solution.py
"""

TRY THIS INPUT:
  Add this test code at the bottom of your file:

  ```python
  X, y = make_classification(
  n_samples=200, n_features=2, n_informative=2, n_redundant=0,
  n_clusters_per_class=1, random_state=42

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
