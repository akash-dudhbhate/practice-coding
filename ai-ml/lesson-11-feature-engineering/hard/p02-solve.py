"""
LESSON — Feature Engineering
HARD P02 — Build a feature engineering comparison: take a dataset, train a model with (a) raw features, (b) scaled features, (c) scaled + encoded, (d) scaled + encoded + interactions. Compare accuracy for each stage. Show the improvement at each step.
==================================================

CONCEPT:
  See concepts.md in this lesson folder for detailed explanations.

PROBLEM:
  Build a feature engineering comparison: take a dataset, train a model with (a) raw features, (b) scaled features, (c) scaled + encoded, (d) scaled + encoded + interactions. Compare accuracy for each stage. Show the improvement at each step


Write a function `solve()` that implements the solution.

# Check your answer: compare with solutions/p02-solution.py
"""

TRY THIS INPUT:
  Add this test code at the bottom of your file:

  ```python
  n = 500
  age = np.random.randint(18, 70, n)
  income = np.random.randint(20000, 150000, n)
  education = np.random.choice(["highschool", "bachelor", "master", "phd"], n)
  city = np.random.choice(["NYC", "LA", "Chicago", "Houston"], n)
  prob = 1 / (1 + np.exp(-(0.00003 * income + 0.02 * age - 3)))
  y = (np.random.rand(n) < prob).astype(int)

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
