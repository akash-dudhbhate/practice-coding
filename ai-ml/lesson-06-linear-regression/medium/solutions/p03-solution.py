"""
Compare Simple vs Multiple Regression
=====================================
Use the same dataset with 1 feature vs 3 features.
Compare R^2 and MSE to show the benefit of multiple regression.
"""

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score


def generate_data(n=300, seed=42):
    """Generate data with 3 features where all contribute to target."""
    rng = np.random.RandomState(seed)
    x1 = rng.randn(n) * 10
    x2 = rng.randn(n) * 5
    x3 = rng.randn(n) * 3
    y = 3 * x1 + 2 * x2 - 1 * x3 + rng.randn(n) * 2 + 5
    X = np.column_stack([x1, x2, x3])
    return X, y


if __name__ == "__main__":
    X, y = generate_data()
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # --- Simple regression: only feature 0 ---
    model_simple = LinearRegression()
    model_simple.fit(X_train[:, [0]], y_train)
    y_pred_simple = model_simple.predict(X_test[:, [0]])

    mse_simple = mean_squared_error(y_test, y_pred_simple)
    r2_simple = r2_score(y_test, y_pred_simple)

    # --- Multiple regression: all 3 features ---
    model_multi = LinearRegression()
    model_multi.fit(X_train, y_train)
    y_pred_multi = model_multi.predict(X_test)

    mse_multi = mean_squared_error(y_test, y_pred_multi)
    r2_multi = r2_score(y_test, y_pred_multi)

    print("=== Simple vs Multiple Regression ===\n")
    print(f"{'Metric':<12} {'Simple (1 feat)':<20} {'Multiple (3 feats)':<20}")
    print("-" * 52)
    print(f"{'MSE':<12} {mse_simple:<20.4f} {mse_multi:<20.4f}")
    print(f"{'R^2':<12} {r2_simple:<20.4f} {r2_multi:<20.4f}")

    print("\n=== Interpretation ===")
    print(f"Multiple regression R^2 is higher ({r2_multi:.4f} vs {r2_simple:.4f}).")
    print("Using all 3 features captures more variance in the target.")
    print(f"MSE dropped from {mse_simple:.2f} to {mse_multi:.2f}.")
