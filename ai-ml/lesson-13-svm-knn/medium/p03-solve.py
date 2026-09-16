"""
LESSON — Svm Knn
MEDIUM P03 — Grid search SVM parameters: C [0.1, 1, 10, 100] and gamma [0.001, 0.01, 0.1, 1]. Use RBF kernel. Print best params and best score. Use scaled data.
==================================================

CONCEPT:
  See concepts.md in this lesson folder for detailed explanations.

PROBLEM:
  Grid search SVM parameters: C [0.1, 1, 10, 100] and gamma [0.001, 0.01, 0.1, 1]. Use RBF kernel. Print best params and best score. Use scaled data


Write a function `solve()` that implements the solution.

# Check your answer: compare with solutions/p03-solution.py
"""

TRY THIS INPUT:
  Add this test code at the bottom of your file:

  ```python
  X, y = make_classification(n_samples=500, n_features=10, n_informative=5, n_redundant=2,
  random_state=42)
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

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
