"""
Polynomial Regression vs Linear Regression
==========================================
Compare linear regression with polynomial regression on non-linear data.
Use PolynomialFeatures to create polynomial terms and plot both fits.
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error, r2_score


if __name__ == "__main__":
    # Generate non-linear data: y = 0.5*x^2 + x + 2 + noise
    np.random.seed(42)
    X = np.sort(6 * np.random.rand(100, 1) - 3, axis=0)
    y = 0.5 * X.ravel() ** 2 + X.ravel() + 2 + np.random.randn(100) * 0.5

    # --- Linear regression ---
    lin_model = LinearRegression()
    lin_model.fit(X, y)
    y_pred_lin = lin_model.predict(X)

    mse_lin = mean_squared_error(y, y_pred_lin)
    r2_lin = r2_score(y, y_pred_lin)

    # --- Polynomial regression (degree 2) ---
    poly_features = PolynomialFeatures(degree=2, include_bias=False)
    X_poly = poly_features.fit_transform(X)

    poly_model = LinearRegression()
    poly_model.fit(X_poly, y)
    y_pred_poly = poly_model.predict(X_poly)

    mse_poly = mean_squared_error(y, y_pred_poly)
    r2_poly = r2_score(y, y_pred_poly)

    print("=== Linear vs Polynomial Regression ===\n")
    print(f"{'Metric':<10} {'Linear':<15} {'Polynomial (deg 2)':<20}")
    print("-" * 45)
    print(f"{'MSE':<10} {mse_lin:<15.4f} {mse_poly:<20.4f}")
    print(f"{'R^2':<10} {r2_lin:<15.4f} {r2_poly:<20.4f}")

    # Plot both
    plt.figure(figsize=(10, 6))
    plt.scatter(X, y, color="gray", s=20, alpha=0.5, label="Data")
    plt.plot(X, y_pred_lin, color="blue", lw=2, label="Linear fit")
    plt.plot(X, y_pred_poly, color="red", lw=2, label="Polynomial fit (deg 2)")
    plt.xlabel("X")
    plt.ylabel("y")
    plt.title("Linear vs Polynomial Regression on Non-Linear Data")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig("linear_vs_polynomial.png", dpi=150)
    plt.show()
    print("Plot saved to linear_vs_polynomial.png")
