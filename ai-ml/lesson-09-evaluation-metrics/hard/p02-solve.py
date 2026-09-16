"""
LESSON — Evaluation Metrics
HARD P02 — Implement a custom threshold optimizer: get prediction probabilities, sweep thresholds 0.1 to 0.9, calculate F1 for each. Plot F1 vs threshold. Find and print the optimal threshold.
==================================================

CONCEPT:
  See concepts.md in this lesson folder for detailed explanations.

PROBLEM:
  Implement a custom threshold optimizer: get prediction probabilities, sweep thresholds 0.1 to 0.9, calculate F1 for each. Plot F1 vs threshold. Find and print the optimal threshold


Write a function `solve()` that implements the solution.

# Check your answer: compare with solutions/p02-solution.py
"""

TRY THIS INPUT:
  Add this test code at the bottom of your file:

  ```python
  X, y = make_classification(
  n_samples=1000, n_features=10, n_informative=5,
  n_redundant=2, weights=[0.7], random_state=42

  # Call your function
  result = solve(...)
  print(result)
  ```

EXPECTED OUTPUT:
  Run the solution file to see expected output:
    python3 hard/solutions/p02-solution.py

  Then compare your output format with theirs.

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
