"""
LESSON — Evaluation Metrics
HARD P03 — Build a cross-validation evaluation script: use 5-fold CV to evaluate a model with 3 different scoring metrics (accuracy, f1, roc_auc). Print mean ± std for each. Explain why different metrics give different rankings.
==================================================

CONCEPT:
  See concepts.md in this lesson folder for detailed explanations.

PROBLEM:
  Build a cross-validation evaluation script: use 5-fold CV to evaluate a model with 3 different scoring metrics (accuracy, f1, roc_auc). Print mean ± std for each. Explain why different metrics give different rankings


Write a function `solve()` that implements the solution.

# Check your answer: compare with solutions/p03-solution.py
"""

TRY THIS INPUT:
  Add this test code at the bottom of your file:

  ```python
  X, y = make_classification(
  n_samples=1000, n_features=15, n_informative=8,
  n_redundant=3, weights=[0.7], random_state=42

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
