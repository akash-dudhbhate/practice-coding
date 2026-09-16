"""
LESSON — Neural Networks
HARD P03 — Build a neural network hyperparameter study: fix a dataset, vary (a) learning rate [0.001, 0.01, 0.1], (b) batch size [16, 32, 64], (c) architecture [(32,), (64, 32), (128, 64, 32)]. For each combination, record final loss and accuracy. Create a heatmap or table of results.
==================================================

CONCEPT:
  See concepts.md in this lesson folder for detailed explanations.

PROBLEM:
  Build a neural network hyperparameter study: fix a dataset, vary (a) learning rate [0.001, 0.01, 0.1], (b) batch size [16, 32, 64], (c) architecture [(32,), (64, 32), (128, 64, 32)]. For each combination, record final loss and accuracy. Create a heatmap or table of results


Write a function `solve()` that implements the solution.

# Check your answer: compare with solutions/p03-solution.py
"""

TRY THIS INPUT:
  Add this test code at the bottom of your file:

  ```python
  X, y = make_classification(
  n_samples=1000, n_features=20, n_informative=10,
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
    python3 hard/solutions/p03-solution.py

  Then compare your output format with theirs.

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
