"""
LEVEL 07 — Unsupervised Learning
MEDIUM P02 — DBSCAN on Non-Spherical Data
========================================

CONCEPT:
  K-Means assumes round blobs. Real clusters can be crescents,
  rings, or irregular shapes. DBSCAN groups by DENSITY —
  points close together are one cluster, outliers are noise.

  eps = max distance to be "neighbors"; min_samples = min cluster size.

PROBLEM:
  Write `compare_algorithms()` that:
    1. make_moons(300, noise=0.05, seed=42)
    2. KMeans(2) → kmeans_labels
    3. DBSCAN(eps=0.3, min_samples=5) → dbscan_labels
    4. Returns (kmeans_labels, dbscan_labels)

TRY THIS INPUT:
  ```python
  km, db = compare_algorithms()
  print(len(set(km)))  # 2 clusters
  print(len(set(db)))  # 2 clusters (DBSCAN gets them right)
  ```

EXPECTED OUTPUT:
  ```
  2
  2
  ```
  (both find 2 clusters, but DBSCAN's match the moon shapes —
   K-Means slices through them. Visualize to see the difference!)

HINT:
  from sklearn.cluster import DBSCAN
  from sklearn.datasets import make_moons

CHECK: python3 check.py medium/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# km, db = compare_algorithms()
# print(len(set(km)), len(set(db)))
