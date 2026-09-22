"""
LEVEL 06 — Advanced ML
EASY P01 — Polynomial Features Rescue a Bad Fit
========================================

CONCEPT:
  A straight line can't fit a curve. But if you add x² as a new
  feature, a LINEAR model can fit parabolas — it's still linear
  in the features, the features are just nonlinear now.

  PolynomialFeatures(degree=2): [x] → [x, x²]

PROBLEM:
  Write `compare_linear_poly()` that:
    1. make_regression(200 samples, 1 feature, noise=30, seed=42)
    2. Makes it nonlinear: y = y**2 / 100
    3. Splits 80/20 (seed=42)
    4. Trains LinearRegression on raw X → R²
    5. Trains on PolynomialFeatures(degree=2, include_bias=False) → R²
    6. Returns (linear_r2, poly_r2)

TRY THIS INPUT:
  ```python
  l, p = compare_linear_poly()
  print(f"{l:.4f} {p:.4f}")
  ```

EXPECTED OUTPUT:
  ```
  -0.0669 0.7929
  ```
  (Linear R² is NEGATIVE — worse than guessing the mean!
   Poly recovers to 0.79. Feature engineering = power.)

HINT:
  poly.fit_transform(X_train) / poly.transform(X_test)
  Never fit_transform on test data.

CHECK: python3 check.py easy/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# l, p = compare_linear_poly()
# print(l, p)
