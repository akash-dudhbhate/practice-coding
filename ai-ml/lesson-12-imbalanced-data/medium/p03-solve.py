"""
LESSON — Imbalanced Data
MEDIUM P03 — Adjust the decision threshold: train a model, get probabilities, try thresholds 0.3, 0.5, 0.7. For each, print precision, recall, F1. Find the threshold that maximizes F1.
==================================================

CONCEPT:
  See concepts.md in this lesson folder for detailed explanations.

PROBLEM:
  Adjust the decision threshold: train a model, get probabilities, try thresholds 0.3, 0.5, 0.7. For each, print precision, recall, F1. Find the threshold that maximizes F1


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
  weights=[0.90, 0.10],
  flip_y=0.0,
  random_state=42,

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
