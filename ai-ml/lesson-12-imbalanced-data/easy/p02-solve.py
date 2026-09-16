"""
LESSON — Imbalanced Data
EASY P02 — Use `class_weight='balanced'` on the same dataset. Compare recall for class 1 with and without class weights. Print both classification reports.
==================================================

CONCEPT:
  See concepts.md in this lesson folder for detailed explanations.

PROBLEM:
  Use `class_weight='balanced'` on the same dataset. Compare recall for class 1 with and without class weights. Print both classification reports


Write a function `solve()` that implements the solution.

# Check your answer: compare with solutions/p02-solution.py
"""

TRY THIS INPUT:
  Add this test code at the bottom of your file:

  ```python
  X, y = make_classification(
  n_samples=1000,
  n_features=10,
  n_informative=5,
  n_redundant=2,
  weights=[0.95, 0.05],
  flip_y=0.0,
  random_state=42,

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
