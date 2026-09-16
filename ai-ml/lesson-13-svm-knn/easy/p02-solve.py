"""
LESSON — Svm Knn
EASY P02 — Train SVM with linear kernel on a linearly separable dataset (`make_classification`). Print accuracy and the number of support vectors.
==================================================

CONCEPT:
  See concepts.md in this lesson folder for detailed explanations.

PROBLEM:
  Train SVM with linear kernel on a linearly separable dataset (`make_classification`). Print accuracy and the number of support vectors


Write a function `solve()` that implements the solution.

# Check your answer: compare with solutions/p02-solution.py
"""

TRY THIS INPUT:
  Add this test code at the bottom of your file:

  ```python
  X, y = make_classification(n_samples=500, n_features=10, n_informative=5, random_state=42)
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

  # Call your function
  result = solve(...)
  print(result)
  ```

EXPECTED OUTPUT:
  Run the solution file to see expected output:
    python3 easy/solutions/p02-solution.py

  Then compare your output format with theirs.

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
