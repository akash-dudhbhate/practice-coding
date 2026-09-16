"""
LESSON — Evaluation Metrics
MEDIUM P02 — Plot the ROC curve for a logistic regression model. Calculate AUC. Add a random baseline line (diagonal). Interpret: AUC=0.9 means what?
==================================================

CONCEPT:
  See concepts.md in this lesson folder for detailed explanations.

PROBLEM:
  Plot the ROC curve for a logistic regression model. Calculate AUC. Add a random baseline line (diagonal). Interpret: AUC=0.9 means what?


Write a function `solve()` that implements the solution.

# Check your answer: compare with solutions/p02-solution.py
"""

TRY THIS INPUT:
  Add this test code at the bottom of your file:

  ```python
  X, y = make_classification(
  n_samples=1000, n_features=10, n_informative=5,
  n_redundant=2, random_state=42

  # Call your function
  result = solve(...)
  print(result)
  ```

EXPECTED OUTPUT:
  Run the solution file to see expected output:
    python3 medium/solutions/p02-solution.py

  Then compare your output format with theirs.

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
