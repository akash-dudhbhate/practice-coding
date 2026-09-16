"""
LESSON — Svm Knn
EASY P03 — Compare KNN with K=1, K=5, K=20 on the same dataset. Print train and test accuracy for each. Show that K=1 overfits (100% train, lower test).
==================================================

CONCEPT:
  See concepts.md in this lesson folder for detailed explanations.

PROBLEM:
  Compare KNN with K=1, K=5, K=20 on the same dataset. Print train and test accuracy for each. Show that K=1 overfits (100% train, lower test)


Write a function `solve()` that implements the solution.

# Check your answer: compare with solutions/p03-solution.py
"""

TRY THIS INPUT:
  Add this test code at the bottom of your file:

  ```python
  X, y = make_classification(n_samples=500, n_features=10, n_informative=5, n_redundant=2,
  n_clusters_per_class=2, random_state=42)
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)

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
