"""
MLP regression pipeline
=======================
Build a non-linear regression dataset, train MLPRegressor with different
hidden layer sizes. Plot predictions vs actual. Show overfitting with a large model.
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score


if __name__ == "__main__":
    # Non-linear regression dataset: y = sin(x) + noise
    np.random.seed(42)
    X = np.sort(np.random.rand(300, 1) * 10, axis=0)
    y = np.sin(X).ravel() + np.random.randn(300) * 0.1

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    scaler = StandardScaler()
    X_train_s = scaler.fit_transform(X_train)
    X_test_s = scaler.transform(X_test)

    # Different architectures
    configs = [
        ("Small (8,)", (8,)),
        ("Medium (32,16)", (32, 16)),
        ("Large (128,128,128)", (128, 128, 128)),
    ]

    plt.figure(figsize=(14, 4))
    print(f"{'Architecture':<25} {'Train MSE':<12} {'Test MSE':<12} {'Train R2':<10} {'Test R2':<10}")
    print("-" * 69)

    for idx, (name, size) in enumerate(configs):
        mlp = MLPRegressor(hidden_layer_sizes=size, max_iter=2000,
                           random_state=42, alpha=0.0)
        mlp.fit(X_train_s, y_train)
        y_train_pred = mlp.predict(X_train_s)
        y_test_pred = mlp.predict(X_test_s)

        train_mse = mean_squared_error(y_train, y_train_pred)
        test_mse = mean_squared_error(y_test, y_test_pred)
        train_r2 = r2_score(y_train, y_train_pred)
        test_r2 = r2_score(y_test, y_test_pred)

        print(f"{name:<25} {train_mse:<12.4f} {test_mse:<12.4f} {train_r2:<10.4f} {test_r2:<10.4f}")

        # Plot predictions vs actual
        plt.subplot(1, 3, idx + 1)
        # Sort test for clean plotting
        sort_idx = np.argsort(X_test_s.ravel())
        plt.scatter(X_test_s.ravel(), y_test, s=10, alpha=0.5, label="Actual")
        plt.plot(X_test_s.ravel()[sort_idx], y_test_pred[sort_idx],
                 "r-", linewidth=2, label="Predicted")
        plt.title(name)
        plt.xlabel("X (scaled)")
        plt.ylabel("y")
        plt.legend(fontsize=8)
        plt.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig("mlp_regression_comparison.png", dpi=100, bbox_inches="tight")
    plt.show()
    print("\nPlot saved to mlp_regression_comparison.png")

    # Overfitting demonstration with the large model
    print("\n--- Overfitting Demonstration ---")
    print("The large model (128,128,128) with alpha=0 likely has lower train MSE")
    print("but higher test MSE — it memorizes noise. Adding L2 (alpha) reduces this.")
    mlp_reg = MLPRegressor(hidden_layer_sizes=(128, 128, 128), max_iter=2000,
                           random_state=42, alpha=1.0)
    mlp_reg.fit(X_train_s, y_train)
    print(f"With alpha=1.0: Train MSE={mean_squared_error(y_train, mlp_reg.predict(X_train_s)):.4f}, "
          f"Test MSE={mean_squared_error(y_test, mlp_reg.predict(X_test_s)):.4f}")
