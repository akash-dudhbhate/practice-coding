"""
LESSON — Svm Knn
MEDIUM P02 — Compare SVM kernels (linear, RBF, poly) on a non-linear dataset (`make_circles` or `make_moons`). Print accuracy for each. Plot decision boundaries for all three.
==================================================

CONCEPT:
  See concepts.md in this lesson folder for detailed explanations.

PROBLEM:
  Compare SVM kernels (linear, RBF, poly) on a non-linear dataset (`make_circles` or `make_moons`). Print accuracy for each. Plot decision boundaries for all three


Write a function `solve()` that implements the solution.

# Check your answer: compare with solutions/p02-solution.py
"""

TRY THIS INPUT:
  Add this test code at the bottom of your file:

  ```python
  X, y = make_moons(n_samples=300, noise=0.15, random_state=42)
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

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
