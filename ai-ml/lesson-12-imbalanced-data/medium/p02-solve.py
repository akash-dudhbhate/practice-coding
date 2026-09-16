"""
LESSON — Imbalanced Data
MEDIUM P02 — Apply SMOTE to the imbalanced dataset. Train a model. Compare F1 with random oversampling. Use `imblearn.pipeline.Pipeline` to ensure SMOTE is applied inside CV (no leakage).
==================================================

CONCEPT:
  See concepts.md in this lesson folder for detailed explanations.

PROBLEM:
  Apply SMOTE to the imbalanced dataset. Train a model. Compare F1 with random oversampling. Use `imblearn.pipeline.Pipeline` to ensure SMOTE is applied inside CV (no leakage)


Write a function `solve()` that implements the solution.

# Check your answer: compare with solutions/p02-solution.py
"""

TRY THIS INPUT:
  Add this test code at the bottom of your file:

  ```python
  X, y = make_classification(
  n_samples=2000,
  n_features=15,
  n_informative=8,
  weights=[0.95, 0.05],
  flip_y=0.0,
  random_state=42,

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
