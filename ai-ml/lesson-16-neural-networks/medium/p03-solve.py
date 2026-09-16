"""
LESSON — Neural Networks
MEDIUM P03 — Demonstrate overfitting: train a large MLP (100, 100, 100) on a small dataset. Show training accuracy = 100% but test accuracy is low. Then add `alpha=0.1` (L2 regularization) and show improvement.
==================================================

CONCEPT:
  See concepts.md in this lesson folder for detailed explanations.

PROBLEM:
  Demonstrate overfitting: train a large MLP (100, 100, 100) on a small dataset. Show training accuracy = 100% but test accuracy is low. Then add `alpha=0.1` (L2 regularization) and show improvement


Write a function `solve()` that implements the solution.

# Check your answer: compare with solutions/p03-solution.py
"""

TRY THIS INPUT:
  Add this test code at the bottom of your file:

  ```python
  X, y = make_classification(
  n_samples=200, n_features=20, n_informative=5, n_redundant=5,
  n_classes=2, random_state=42
  X_train, X_test, y_train, y_test = train_test_split(
  X, y, test_size=0.3, random_state=42
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
