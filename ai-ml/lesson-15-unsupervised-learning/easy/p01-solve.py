"""
LESSON — Unsupervised Learning
EASY P01 — Generate synthetic data with 3 clusters (`make_blobs`). Apply K-Means with K=3. Plot the clusters with different colors. Print the cluster centers.
==================================================

CONCEPT:
  See concepts.md in this lesson folder for detailed explanations.

PROBLEM:
  Generate synthetic data with 3 clusters (`make_blobs`). Apply K-Means with K=3. Plot the clusters with different colors. Print the cluster centers


Write a function `solve()` that implements the solution.

# Check your answer: compare with solutions/p01-solution.py
"""

TRY THIS INPUT:
  Add this test code at the bottom of your file:

  ```python
  X, y_true = make_blobs(n_samples=300, centers=3, cluster_std=1.0, random_state=42)

  # Call your function
  result = solve(...)
  print(result)
  ```

EXPECTED OUTPUT:
  Run the solution file to see expected output:
    python3 easy/solutions/p01-solution.py

  Then compare your output format with theirs.

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
