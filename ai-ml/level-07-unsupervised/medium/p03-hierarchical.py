"""
LEVEL 07 — Unsupervised Learning
MEDIUM P03 — Hierarchical Clustering (Agglomerative)
========================================

CONCEPT:
  AgglomerativeClustering builds clusters bottom-up:
    start with every point as its own cluster,
    merge the two closest, repeat until K remain.
  Produces a dendrogram (tree of merges).

  n_clusters=K; linkage='ward' minimizes merge variance.

PROBLEM:
  Write `hierarchical()` that:
    1. make_blobs(50, centers=3, seed=42)
    2. AgglomerativeClustering(n_clusters=3)
    3. Returns labels array

TRY THIS INPUT:
  ```python
  labels = hierarchical()
  print(len(labels))     # 50
  print(set(labels))     # {0, 1, 2}
  ```

EXPECTED OUTPUT:
  ```
  50
  {0, 1, 2}
  ```

HINT:
  from sklearn.cluster import AgglomerativeClustering
  .fit_predict(X) returns labels directly.

CHECK: python3 check.py medium/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# labels = hierarchical()
# print(set(labels))
