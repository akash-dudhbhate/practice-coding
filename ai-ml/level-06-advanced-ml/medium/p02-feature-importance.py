"""
LEVEL 06 — Advanced ML
MEDIUM P02 — Feature Importance Filtering
========================================

CONCEPT:
  Not all features help. Noise features hurt — they add variance
  without signal. Use feature importance to keep only the top ones.

  Compare: all features vs top-5 → top-5 often scores HIGHER.

PROBLEM:
  Write `select_top()` that:
    1. make_classification(200, 10 features, n_informative=5, seed=42)
    2. Split 80/20 (seed=42)
    3. Train RF on all → all_acc
    4. Get importances, pick top-5 indices, retrain on those → top5_acc
    5. Returns (all_acc, top5_acc, top5_indices)

TRY THIS INPUT:
  ```python
  a, b, idx = select_top()
  print(f"All: {a:.4f}  Top5: {b:.4f}")
  print(idx)
  ```

EXPECTED OUTPUT:
  ```
  All: 0.9000  Top5: 0.9500
  [3, 4, 5, 6, 8]
  ```

HINT:
  np.argsort(importances)[-5:] → top-5 indices (or sort descending)

CHECK: python3 check.py medium/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# a, b, idx = select_top()
# print(a, b, idx)
