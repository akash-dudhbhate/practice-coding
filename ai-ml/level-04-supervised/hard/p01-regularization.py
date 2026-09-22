"""
LEVEL 04 — Supervised Learning
HARD P01 — L1 vs L2 Regularization
========================================

CONCEPT:
  Regularization penalizes large coefficients → simpler models.
    L1 (Lasso): adds |w| penalty → pushes weak coefs to EXACTLY 0
    L2 (Ridge): adds w² penalty → shrinks all coefs, keeps them nonzero

  L1 = feature selection (kills features). L2 = gentle shrinkage.

PROBLEM:
  Write `compare_regularization()` that:
    1. make_regression(100, 10 features, noise=10, seed=42)
    2. Fits LinearRegression, Lasso(alpha=1.0), Ridge(alpha=1.0)
    3. Returns (linear_coefs, lasso_coefs, ridge_coefs)

TRY THIS INPUT:
  ```python
  lr, la, ri = compare_regularization()
  print(f"{lr[0]:.4f} {la[0]:.4f} {ri[0]:.4f}")
  print(f"{la[2]:.4f}")   # Lasso shrinks weak features harder
  ```

EXPECTED OUTPUT:
  ```
  18.4465 17.3065 18.4271
  2.2856
  ```
  (Feature 2: linear=3.91, lasso=2.29 — L1 shrunk it most)

HINT:
  from sklearn.linear_model import Lasso, Ridge
  coef_ attribute holds the learned weights.

CHECK: python3 check.py hard/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# lr, la, ri = compare_regularization()
# print(la)
