"""
LESSON — Decision Trees Forests
EASY P02 — Implement Gini impurity from scratch. Calculate Gini for a node with [3 positive, 2 negative] samples. Verify: 1 - (3/5)² - (2/5)² = 0.48.
==================================================

CONCEPT:
  See concepts.md in this lesson folder for detailed explanations.

PROBLEM:
  Implement Gini impurity from scratch. Calculate Gini for a node with [3 positive, 2 negative] samples. Verify: 1 - (3/5)² - (2/5)² = 0.48


Write a function `solve()` that implements the solution.

# Check your answer: compare with solutions/p02-solution.py
"""

TRY THIS INPUT:
  Add this test code at the bottom of your file:

  ```python
  labels = [1, 1, 1, 0, 0]  # 3 positive, 2 negative
  gini = gini_impurity(labels)
  expected = 1 - (3 / 5) ** 2 - (2 / 5) ** 2

  # Call your function
  result = solve(...)
  print(result)
  ```

EXPECTED OUTPUT:
  Run the solution file to see expected output:
    python3 easy/solutions/p02-solution.py

  Then compare your output format with theirs.

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
