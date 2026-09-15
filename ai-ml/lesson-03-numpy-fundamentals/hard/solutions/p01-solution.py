"""
Lesson 03 - Hard P01
Linear regression using the normal equation:
  w = (X^T X)^{-1} X^T y

Solution:
  1. Generate synthetic data from a known linear relationship.
  2. Add a bias (intercept) column of ones to X.
  3. Solve for weights using the normal equation.
  4. Compare with sklearn's LinearRegression.
  5. Make predictions and compute R^2.
"""

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# ---------------------------------------------------------------------------
# 1. Generate synthetic data: y = 3*x1 + 5*x2 - 2*x3 + 10 + noise
# ---------------------------------------------------------------------------
np.random.seed(42)
n_samples = 200
X = np.random.randn(n_samples, 3)
true_weights = np.array([3.0, 5.0, -2.0])
true_bias = 10.0
noise = np.random.randn(n_samples) * 0.5
y = X @ true_weights + true_bias + noise

print(f"True weights: {true_weights}, True bias: {true_bias}")
print(f"Data shape: X={X.shape}, y={y.shape}")
print()

# ---------------------------------------------------------------------------
# 2. Add bias column (column of ones) to X
# ---------------------------------------------------------------------------
# Solution: To include an intercept term in the normal equation, we prepend
# (or append) a column of ones to the feature matrix.
X_bias = np.hstack([np.ones((n_samples, 1)), X])  # shape (200, 4)
print(f"X with bias column: {X_bias.shape}")
print()

# ---------------------------------------------------------------------------
# 3. Solve using the normal equation: w = (X^T X)^{-1} X^T y
# ---------------------------------------------------------------------------
# Solution: The normal equation gives the closed-form solution for OLS linear
# regression. w[0] is the bias, w[1:] are the feature weights.
XtX = X_bias.T @ X_bias
Xty = X_bias.T @ y
w_normal = np.linalg.inv(XtX) @ Xty

print("Normal equation results:")
print(f"  Estimated bias:    {w_normal[0]:.4f}  (true: {true_bias})")
print(f"  Estimated weights: {w_normal[1:]}  (true: {true_weights})")
print()

# More numerically stable alternative: np.linalg.solve instead of inv
w_solve = np.linalg.solve(XtX, Xty)
print(f"  Using np.linalg.solve: {w_solve}")
print(f"  Matches inv approach:  {np.allclose(w_normal, w_solve)}")
print()

# ---------------------------------------------------------------------------
# 4. Make predictions and compute R^2
# ---------------------------------------------------------------------------
y_pred_normal = X_bias @ w_normal
r2_normal = r2_score(y, y_pred_normal)
print(f"R^2 (normal equation): {r2_normal:.6f}")
print()

# ---------------------------------------------------------------------------
# 5. Compare with sklearn LinearRegression
# ---------------------------------------------------------------------------
sklearn_model = LinearRegression()
sklearn_model.fit(X, y)
y_pred_sklearn = sklearn_model.predict(X)
r2_sklearn = r2_score(y, y_pred_sklearn)

print("sklearn LinearRegression results:")
print(f"  Estimated bias:    {sklearn_model.intercept_:.4f}")
print(f"  Estimated weights: {sklearn_model.coef_}")
print(f"  R^2 (sklearn):     {r2_sklearn:.6f}")
print()

print("Comparison:")
print(f"  Weights match: {np.allclose(w_normal[1:], sklearn_model.coef_, atol=1e-6)}")
print(f"  Bias match:    {np.allclose(w_normal[0], sklearn_model.intercept_, atol=1e-6)}")
print(f"  R^2 match:     {np.isclose(r2_normal, r2_sklearn)}")
