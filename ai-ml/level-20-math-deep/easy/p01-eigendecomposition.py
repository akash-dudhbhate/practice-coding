"""
LEVEL 20 — Deep Math for ML
EASY P01 — Eigendecomposition
========================================

CONCEPT:
  For a square matrix A, an eigenvector v satisfies: A·v = λ·v
  The matrix just rescales v by λ — it doesn't rotate it.
  Eigenvalues tell you the "natural axes" of a linear transform.
  This is THE math behind PCA, spectral clustering, and PageRank.

  For a SYMMETRIC matrix (A = A.T): eigenvalues are real and
  eigenvectors are orthonormal (perpendicular, unit length).

PROBLEM:
  Write `eigendecompose(A)` that returns (eigenvalues, eigenvectors)
  sorted by eigenvalue DESCENDING. eigenvectors is a matrix whose
  COLUMNS are the eigenvectors.

TRY THIS INPUT:
  ```python
  A = np.array([[2.0, 1.0], [1.0, 2.0]])   # symmetric
  vals, vecs = eigendecompose(A)
  print(vals)          # [3. 1.] — sorted descending
  print(vecs.shape)    # (2, 2)
  print(A @ vecs[:,0]) # 3.0 * vecs[:,0] (up to float noise)
  ```

EXPECTED OUTPUT:
  ```
  [3. 1.]
  (2, 2)
  [2.12 2.12]  ≈ 3 * [0.707, 0.707]
  ```

HINT:
  vals, vecs = np.linalg.eig(A)
  idx = np.argsort(vals)[::-1]   # descending order
  return vals[idx], vecs[:, idx] # reorder columns too!

CHECK: python3 check.py easy/p01
"""

import numpy as np


# === WRITE YOUR CODE BELOW ===
def eigendecompose(A):
    # TODO: np.linalg.eig, then sort eigenpairs descending by eigenvalue
    pass


# === TEST ===
# A = np.array([[2.0, 1.0], [1.0, 2.0]])
# vals, vecs = eigendecompose(A)
# print(vals)
# print(vecs)
