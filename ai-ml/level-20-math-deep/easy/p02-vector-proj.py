"""
LEVEL 20 — Deep Math for ML
EASY P02 — Vector Projection
========================================

CONCEPT:
  The projection of v onto u is the "shadow" v casts on the line
  through u. Formula:

      proj_u(v) = (v·u / u·u) * u

  The result is parallel to u, with length |v|·cos(θ).
  This is the atom of: cosine similarity, Gram-Schmidt
  orthogonalization, least squares, and attention mechanisms
  (how much does the query "align" with each key?).

PROBLEM:
  Write `project(v, u)` that returns the projection of v onto u.

TRY THIS INPUT:
  ```python
  v = np.array([3.0, 4.0])
  u = np.array([1.0, 0.0])
  print(project(v, u))   # [3. 0.] — the x-component of v
  ```

EXPECTED OUTPUT:
  ```
  [3. 0.]
  ```
  (v's shadow on the x-axis drops the y-component)

HINT:
  return (np.dot(v, u) / np.dot(u, u)) * u
  The ratio (v·u)/(u·u) is a scalar — it scales u.

CHECK: python3 check.py easy/p02
"""

import numpy as np


# === WRITE YOUR CODE BELOW ===
def project(v, u):
    # TODO: return (v·u / u·u) * u
    pass


# === TEST ===
# v = np.array([3.0, 4.0])
# u = np.array([1.0, 0.0])
# print(project(v, u))
