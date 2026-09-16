"""
LEVEL 07 — Unsupervised Learning
EASY P03 — PCA for Visualization
========================================

CONCEPT:
  High-dimensional data can't be plotted directly. PCA projects
  it to 2D while keeping as much variance as possible.
  explained_variance_ratio_ tells you how much info you kept.

PROBLEM:
  Write `pca_2d()` that:
    1. Loads iris (4 features)
    2. StandardScaler → PCA(n_components=2)
    3. Returns (X_2d, explained_variance_ratio)

TRY THIS INPUT:
  ```python
  X2, ev = pca_2d()
  print(X2.shape)       # (150, 2)
  print(f"{ev[0]:.4f}") # first component variance share
  print(f"{ev.sum():.4f}")  # total captured
  ```

EXPECTED OUTPUT:
  ```
  (150, 2)
  0.7296
  0.9581
  ```
  (2 components capture 96% of the 4D data's variance!)

HINT:
  from sklearn.decomposition import PCA
  Always scale first: StandardScaler().fit_transform(X)

CHECK: python3 check.py easy/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# X2, ev = pca_2d()
# print(X2.shape, ev.sum())
