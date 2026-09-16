"""
LESSON — Cross Validation Tuning
MEDIUM P02 — Use `RandomizedSearchCV` with 20 iterations on the same parameter space (expanded with more values). Compare the best score and time taken with grid search.
==================================================

CONCEPT:
  See concepts.md in this lesson folder for detailed explanations.

PROBLEM:
  Use `RandomizedSearchCV` with 20 iterations on the same parameter space (expanded with more values). Compare the best score and time taken with grid search


Write a function `solve()` that implements the solution.

# Check your answer: compare with solutions/p02-solution.py
"""

TRY THIS INPUT:
  Add this test code at the bottom of your file:

  ```python
  X, y = make_classification(
  n_samples=800, n_features=15, n_informative=8,
  n_redundant=3, random_state=42

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
