"""
LESSON — Decision Trees Forests
EASY P03 — Train a decision tree with and without `max_depth` limit. Compare training and test accuracy. Show that unlimited depth overfits (100% train, lower test).
==================================================

CONCEPT:
  See concepts.md in this lesson folder for detailed explanations.

PROBLEM:
  Train a decision tree with and without `max_depth` limit. Compare training and test accuracy. Show that unlimited depth overfits (100% train, lower test)


Write a function `solve()` that implements the solution.

# Check your answer: compare with solutions/p03-solution.py
"""

TRY THIS INPUT:
  Add this test code at the bottom of your file:

  ```python
  X, y = make_classification(
  n_samples=500, n_features=10, n_informative=5,
  n_redundant=2, n_repeated=1, random_state=42

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
