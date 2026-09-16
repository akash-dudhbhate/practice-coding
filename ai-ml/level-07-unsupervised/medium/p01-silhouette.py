"""
LEVEL 07 — Unsupervised Learning
MEDIUM P01 — Silhouette Score for Best K
========================================

CONCEPT:
  Elbow is visual; silhouette is a NUMBER. For each point:
    a = mean distance to own cluster, b = mean distance to
    nearest other cluster.  s = (b - a) / max(a, b)  ∈ [-1, 1]

  Higher = better separated clusters. Try K=2..7, pick max.

PROBLEM:
  Write `best_k()` that:
    1. make_blobs(300, centers=3, seed=42)
    2. For K=2..7: KMeans → silhouette_score
    3. Returns (best_K, best_score, all_scores_dict)

TRY THIS INPUT:
  ```python
  k, s, all_s = best_k()
  print(k, f"{s:.4f}")
  ```

EXPECTED OUTPUT:
  ```
  3 0.8467
  ```

HINT:
  from sklearn.metrics import silhouette_score
  silhouette_score(X, labels)

CHECK: python3 check.py medium/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# k, s, d = best_k()
# print(k, s)
