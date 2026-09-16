"""
LESSON — Imbalanced Data
EASY P03 — Use `stratify=y` in `train_test_split` on the imbalanced dataset. Verify both train and test have the same class ratio. Print class counts for each.
==================================================

CONCEPT:
  See concepts.md in this lesson folder for detailed explanations.

PROBLEM:
  Use `stratify=y` in `train_test_split` on the imbalanced dataset. Verify both train and test have the same class ratio. Print class counts for each


Write a function `solve()` that implements the solution.

# Check your answer: compare with solutions/p03-solution.py
"""

TRY THIS INPUT:
  Add this test code at the bottom of your file:

  ```python
  X, y = make_classification(
  n_samples=1000,
  n_features=5,
  n_informative=3,
  weights=[0.90, 0.10],
  flip_y=0.0,
  random_state=42,

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
