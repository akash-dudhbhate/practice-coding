"""
LESSON — Logistic Regression
MEDIUM P03 — Train multiclass logistic regression on the Iris dataset (3 classes). Print accuracy, confusion matrix, and per-class precision/recall using `classification_report`.
==================================================

CONCEPT:
  See concepts.md in this lesson folder for detailed explanations.

PROBLEM:
  Train multiclass logistic regression on the Iris dataset (3 classes). Print accuracy, confusion matrix, and per-class precision/recall using `classification_report`


Write a function `solve()` that implements the solution.

# Check your answer: compare with solutions/p03-solution.py
"""

TRY THIS INPUT:
  Add this test code at the bottom of your file:

  ```python
  iris = load_iris()
  X, y = iris.data, iris.target
  class_names = iris.target_names

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
