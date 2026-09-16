"""
LEVEL 20 — Deep Math for ML
MEDIUM P01 — PCA From Scratch
========================================

CONCEPT:
  PCA finds the directions of maximum variance in your data and
  projects onto the top-k of them. The recipe:

    1. Center:        Xc = X - X.mean(axis=0)
    2. Covariance:    C  = Xc.T @ Xc / (n - 1)      # (d, d), symmetric
    3. Eigendecompose C — eigenvectors = principal axes,
       eigenvalues = variance along each axis
    4. Keep top-k eigenvectors as columns of W      # (d, k)
    5. Project:       Z = Xc @ W                    # (n, k)

  sklearn.decomposition.PCA does exactly this. Now you'll know
  what papers mean by "we projected onto the first principal
  components."

PROBLEM:
  Write `pca_scratch(X, k)` that returns the data projected onto
  its top-k principal components. Shape: (n_samples, k).

TRY THIS INPUT:
  ```python
  np.random.seed(42)
  X = np.random.randn(100, 3) @ np.array([[2,0,0],[0,1,0],[0,0,0.1]])
  Z = pca_scratch(X, 2)
  print(Z.shape)        # (100, 2)
  print(Z.var(axis=0))  # big variance in col 0, small in col 1
  ```

EXPECTED OUTPUT:
  ```
  (100, 2)
  [~4. ~1.]  (descending — first component captures the most variance)
  ```

HINT:
  np.linalg.eig returns unordered eigenvalues — argsort descending,
  take the first k columns as W, then Xc @ W.

CHECK: python3 check.py medium/p01
"""

import numpy as np


# === WRITE YOUR CODE BELOW ===
def pca_scratch(X, k):
    # TODO: center → covariance → top-k eigenvectors → project
    pass


# === TEST ===
# np.random.seed(42)
# X = np.random.randn(100, 3)
# Z = pca_scratch(X, 2)
# print(Z.shape)
