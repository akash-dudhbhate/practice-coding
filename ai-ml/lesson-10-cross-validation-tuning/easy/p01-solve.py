"""
LESSON — Cross Validation Tuning
EASY P01 — Run 5-fold cross-validation on a random forest with the Iris dataset. Print mean and std of accuracy. Compare with a single train/test split.
==================================================

CONCEPT:
  See concepts.md in this lesson folder for detailed explanations.

PROBLEM:
  Run 5-fold cross-validation on a random forest with the Iris dataset. Print mean and std of accuracy. Compare with a single train/test split


Write a function `solve()` that implements the solution.

# Check your answer: compare with solutions/p01-solution.py
"""

TRY THIS INPUT:
  Add this test code at the bottom of your file:

  ```python
  iris = load_iris()
  X, y = iris.data, iris.target

  # Call your function
  result = solve(...)
  print(result)
  ```

EXPECTED OUTPUT:
  Run the solution file to see expected output:
    python3 easy/solutions/p01-solution.py

  Then compare your output format with theirs.

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
