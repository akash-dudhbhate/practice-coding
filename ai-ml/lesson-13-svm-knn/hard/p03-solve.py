"""
LESSON — Svm Knn
HARD P03 — Build an SVM from scratch using gradient descent (linear SVM with hinge loss). Implement the loss function and gradient. Train on a 2D dataset. Plot the decision boundary and margin. Compare with sklearn's SVC.
==================================================

CONCEPT:
  See concepts.md in this lesson folder for detailed explanations.

PROBLEM:
  Build an SVM from scratch using gradient descent (linear SVM with hinge loss). Implement the loss function and gradient. Train on a 2D dataset. Plot the decision boundary and margin. Compare with sklearn's SVC


Write a function `solve()` that implements the solution.

# Check your answer: compare with solutions/p03-solution.py
"""

TRY THIS INPUT:
  Add this test code at the bottom of your file:

  ```python
  X, y = make_blobs(n_samples=200, centers=2, n_features=2, random_state=42, cluster_std=1.0)

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
