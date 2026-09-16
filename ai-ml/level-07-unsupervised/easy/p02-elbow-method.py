"""
LEVEL 07 — Unsupervised Learning
EASY P02 — Elbow Method
========================================

CONCEPT:
  How to pick K? Try K=1..10, plot inertia (sum of distances to
  nearest center). The "elbow" — where adding more K barely helps —
  is the sweet spot.

  model.inertia_ = total within-cluster distance.

PROBLEM:
  Write `elbow()` that:
    1. make_blobs(300, centers=3, seed=42)
    2. For K=1..10: KMeans → inertia
    3. Returns list of 10 inertias

TRY THIS INPUT:
  ```python
  inertias = elbow()
  print(len(inertias))          # 10
  print(f"{inertias[0]:.0f}")   # ~13142 (K=1, worst)
  print(f"{inertias[2]:.0f}")   # ~364  (K=3, elbow!)
  ```

EXPECTED OUTPUT:
  ```
  10
  20402
  567
  ```
  (massive drop at K=3 → 3 is the right number of clusters)

HINT:
  inertias.append(KMeans(n_clusters=k, n_init=10).fit(X).inertia_)

CHECK: python3 check.py easy/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# ins = elbow()
# print(ins[0], ins[2])
