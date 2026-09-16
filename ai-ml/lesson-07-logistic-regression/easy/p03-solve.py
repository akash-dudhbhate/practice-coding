"""
LESSON — Logistic Regression
EASY P03 — Implement a confusion matrix from scratch (2x2). Calculate TP, TN, FP, FN. Verify against `sklearn.metrics.confusion_matrix`.
==================================================

CONCEPT:
  See concepts.md in this lesson folder for detailed explanations.

PROBLEM:
  Implement a confusion matrix from scratch (2x2). Calculate TP, TN, FP, FN. Verify against `sklearn.metrics.confusion_matrix`


Write a function `solve()` that implements the solution.

# Check your answer: compare with solutions/p03-solution.py
"""

TRY THIS INPUT:
  Add this test code at the bottom of your file:

  ```python
  y_true = [0, 0, 1, 1, 1, 0, 1, 0, 1, 0]
  y_pred = [0, 1, 1, 1, 0, 0, 1, 0, 1, 1]

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
