"""
LESSON — Pytorch Fundamentals
MEDIUM P03 — Compare optimizers: train the same network with SGD, SGD+momentum, and Adam. Plot the loss curves for all three on the same graph. Identify the fastest converging optimizer.
==================================================

CONCEPT:
  See concepts.md in this lesson folder for detailed explanations.

PROBLEM:
  Compare optimizers: train the same network with SGD, SGD+momentum, and Adam. Plot the loss curves for all three on the same graph. Identify the fastest converging optimizer


Write a function `solve()` that implements the solution.

# Check your answer: compare with solutions/p03-solution.py
"""

TRY THIS INPUT:
  Add this test code at the bottom of your file:

  ```python
  X, y = make_classification(
  n_samples=500, n_features=10, n_informative=5,
  n_classes=2, random_state=42
  X_train, X_test, y_train, y_test = train_test_split(
  X, y, test_size=0.2, random_state=42
  scaler = StandardScaler()

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
