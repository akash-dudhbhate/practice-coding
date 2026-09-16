"""
LESSON — Svm Knn
HARD P01 — Build a model comparison: KNN, SVM (linear), SVM (RBF), Random Forest on the same dataset. For each: tune the key hyperparameter with CV, print best score, and create a comparison table. Identify the best model.
==================================================

CONCEPT:
  See concepts.md in this lesson folder for detailed explanations.

PROBLEM:
  Build a model comparison: KNN, SVM (linear), SVM (RBF), Random Forest on the same dataset. For each: tune the key hyperparameter with CV, print best score, and create a comparison table. Identify the best model


Write a function `solve()` that implements the solution.

# Check your answer: compare with solutions/p01-solution.py
"""

TRY THIS INPUT:
  Add this test code at the bottom of your file:

  ```python
  X, y = make_classification(n_samples=800, n_features=15, n_informative=8, n_redundant=3,
  n_clusters_per_class=2, random_state=42)
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

  # Call your function
  result = solve(...)
  print(result)
  ```

EXPECTED OUTPUT:
  Run the solution file to see expected output:
    python3 hard/solutions/p01-solution.py

  Then compare your output format with theirs.

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
