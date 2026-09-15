"""
Regression with Assumption Checking
===================================
Train a linear regression model and check key assumptions:
1. Linearity: scatter plot of actual vs predicted
2. Homoscedasticity: residuals vs predicted (constant variance)
3. Normality: histogram of residuals
4. Residuals plot: residuals vs fitted values
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_regression
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


if __name__ == "__main__":
    # Generate data
    X, y = make_regression(n_samples=300, n_features=1, noise=10, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Fit model
    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    residuals = y_test - y_pred

    print(f"R^2 (test): {model.score(X_test, y_test):.4f}")
    print(f"Mean residual: {np.mean(residuals):.4f} (should be ~0)")

    fig, axes = plt.subplots(2, 2, figsize=(12, 10))

    # 1. Linearity: actual vs predicted
    ax = axes[0, 0]
    ax.scatter(y_test, y_pred, alpha=0.6, color="steelblue")
    ax.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()],
            "r--", lw=2)
    ax.set_xlabel("Actual")
    ax.set_ylabel("Predicted")
    ax.set_title("Linearity: Actual vs Predicted")

    # 2. Homoscedasticity: residuals vs predicted
    ax = axes[0, 1]
    ax.scatter(y_pred, residuals, alpha=0.6, color="darkorange")
    ax.axhline(y=0, color="red", linestyle="--")
    ax.set_xlabel("Predicted")
    ax.set_ylabel("Residuals")
    ax.set_title("Homoscedasticity: Residuals vs Predicted")

    # 3. Normality: histogram of residuals
    ax = axes[1, 0]
    ax.hist(residuals, bins=20, color="seagreen", edgecolor="black", alpha=0.7)
    ax.set_xlabel("Residuals")
    ax.set_ylabel("Frequency")
    ax.set_title("Normality: Histogram of Residuals")

    # 4. Residuals plot (residuals vs index)
    ax = axes[1, 1]
    ax.scatter(range(len(residuals)), residuals, alpha=0.6, color="purple")
    ax.axhline(y=0, color="red", linestyle="--")
    ax.set_xlabel("Index")
    ax.set_ylabel("Residuals")
    ax.set_title("Residuals Plot (Order)")

    plt.suptitle("Regression Assumption Checking", fontsize=14, y=1.01)
    plt.tight_layout()
    plt.savefig("assumption_checks.png", dpi=150, bbox_inches="tight")
    plt.show()
    print("Assumption check plots saved to assumption_checks.png")

    print("\n=== Assumption Summary ===")
    print("1. Linearity: Points should cluster around the diagonal line.")
    print("2. Homoscedasticity: Residuals should have constant spread (no funnel).")
    print("3. Normality: Residual histogram should be bell-shaped (normal).")
    print("4. Independence: Residuals should show no pattern when plotted in order.")
