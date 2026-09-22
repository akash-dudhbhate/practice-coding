"""
LEVEL 06 — Advanced ML
MEDIUM P03 — PCA Dimensionality Reduction
========================================

CONCEPT:
  PCA finds the axes of maximum variance and projects data onto
  fewer dimensions. 10 features → 3 components that still capture
  most of the information.

  explained_variance_ratio_ = how much info each component keeps.

PROBLEM:
  Write `reduce_pca()` that:
    1. make_classification(200, 10 features, n_informative=5, seed=42)
    2. StandardScaler → PCA(n_components=3)
    3. Returns (X_reduced, explained_variance_ratio_array)

TRY THIS INPUT:
  ```python
  Xr, ev = reduce_pca()
  print(Xr.shape)     # (200, 3)
  print(f"{ev.sum():.4f}")  # total variance captured
  ```

EXPECTED OUTPUT:
  ```
  (200, 3)
  0.5334  (top 3 components capture ~53% of the variance)
  ```

HINT:
  PCA needs scaled data first — always StandardScaler before PCA.
  pca.explained_variance_ratio_

CHECK: python3 check.py medium/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# Xr, ev = reduce_pca()
# print(Xr.shape, ev.sum())
