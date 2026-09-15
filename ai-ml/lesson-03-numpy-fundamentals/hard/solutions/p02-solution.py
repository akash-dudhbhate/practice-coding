"""
Lesson 03 - Hard P02
Compute a pairwise distance matrix N x N using broadcasting only (no loops).

Solution:
  1. Generate N random points in D-dimensional space.
  2. Use broadcasting to compute all pairwise Euclidean distances at once.
  3. Verify against scipy/scikit-learn pairwise distances.
  4. Check the diagonal is zero and the matrix is symmetric.
"""

import numpy as np
from sklearn.metrics.pairwise import euclidean_distances

# ---------------------------------------------------------------------------
# 1. Generate N points in D-dimensional space
# ---------------------------------------------------------------------------
np.random.seed(42)
N = 100  # number of points
D = 3    # dimensions
points = np.random.randn(N, D)

print(f"Points shape: {points.shape} ({N} points in {D}D)")
print()

# ---------------------------------------------------------------------------
# 2. Compute pairwise distance matrix using broadcasting
# ---------------------------------------------------------------------------
# Solution:
#   Step 1: Expand points to shape (N, 1, D) and (1, N, D).
#   Step 2: Subtract -> difference array of shape (N, N, D).
#   Step 3: Square, sum over last axis, take sqrt -> (N, N) distance matrix.
# Broadcasting handles the expansion automatically without creating copies.
diff = points[:, np.newaxis, :] - points[np.newaxis, :, :]  # shape (N, N, D)
dist_matrix = np.sqrt(np.sum(diff ** 2, axis=-1))            # shape (N, N)

print(f"Distance matrix shape: {dist_matrix.shape}")
print(f"First 5x5 block:")
print(np.round(dist_matrix[:5, :5], 4))
print()

# ---------------------------------------------------------------------------
# 3. Verify properties
# ---------------------------------------------------------------------------
# Diagonal should be zero (distance from a point to itself)
diag_ok = np.allclose(np.diag(dist_matrix), 0)
# Matrix should be symmetric (dist(a,b) == dist(b,a))
symmetric_ok = np.allclose(dist_matrix, dist_matrix.T)

print(f"Diagonal is all zeros: {diag_ok}")
print(f"Matrix is symmetric:   {symmetric_ok}")
print()

# ---------------------------------------------------------------------------
# 4. Verify against sklearn's euclidean_distances
# ---------------------------------------------------------------------------
sklearn_dist = euclidean_distances(points)
matches_sklearn = np.allclose(dist_matrix, sklearn_dist)
print(f"Matches sklearn euclidean_distances: {matches_sklearn}")
print()

# ---------------------------------------------------------------------------
# 5. Memory-efficient alternative (for large N)
# ---------------------------------------------------------------------------
# Solution: For very large N, the (N, N, D) intermediate array may be too big.
# We can use the identity: ||a - b||^2 = ||a||^2 + ||b||^2 - 2*a.b
# This avoids the 3D intermediate and works with only (N, N) arrays.
sq_norms = np.sum(points ** 2, axis=1)  # shape (N,)
dist_sq_eff = sq_norms[:, np.newaxis] + sq_norms[np.newaxis, :] - 2 * (points @ points.T)
dist_eff = np.sqrt(np.maximum(dist_sq_eff, 0))  # clip negatives from float errors

matches_efficient = np.allclose(dist_eff, dist_matrix, atol=1e-8)
print(f"Efficient method matches broadcasting method: {matches_efficient}")
