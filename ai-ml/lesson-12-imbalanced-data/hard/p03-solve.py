"""
LESSON — Imbalanced Data
HARD P03 — Build a comparison of evaluation metrics: train a model on imbalanced data. Calculate accuracy, F1, ROC-AUC, PR-AUC. Show that accuracy and ROC-AUC look good but F1 and PR-AUC reveal the truth. Plot both ROC and PR curves. Explain which is more honest.
==================================================

CONCEPT:
  See concepts.md in this lesson folder for detailed explanations.

PROBLEM:
  Build a comparison of evaluation metrics: train a model on imbalanced data. Calculate accuracy, F1, ROC-AUC, PR-AUC. Show that accuracy and ROC-AUC look good but F1 and PR-AUC reveal the truth. Plot both ROC and PR curves. Explain which is more honest


Write a function `solve()` that implements the solution.

# Check your answer: compare with solutions/p03-solution.py
"""

TRY THIS INPUT:
  Add this test code at the bottom of your file:

  ```python
  X, y = make_classification(
  n_samples=2000,
  n_features=10,
  n_informative=5,
  weights=[0.95, 0.05],
  flip_y=0.0,
  random_state=42,

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
