"""
LEVEL 07 — Unsupervised Learning
EASY P01 — K-Means Clustering
========================================

CONCEPT:
  K-Means groups unlabeled data into K clusters:
    1. Place K random centers
    2. Assign each point to nearest center
    3. Move centers to the mean of their points
    4. Repeat until stable

  cluster_centers_ → the learned centers
  labels_ → which cluster each point belongs to

PROBLEM:
  Write `cluster()` that:
    1. make_blobs(300, centers=3, seed=42)
    2. KMeans(n_clusters=3, random_state=42, n_init=10)
    3. Returns (labels, centers)

TRY THIS INPUT:
  ```python
  labels, centers = cluster()
  print(len(labels))      # 300
  print(len(centers))     # 3
  print(set(labels))      # {0, 1, 2}
  ```

EXPECTED OUTPUT:
  ```
  300
  3
  {0, 1, 2}
  ```

HINT:
  from sklearn.cluster import KMeans
  km.fit(X) then km.labels_ and km.cluster_centers_

CHECK: python3 check.py easy/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# labels, centers = cluster()
# print(len(labels), len(centers))
