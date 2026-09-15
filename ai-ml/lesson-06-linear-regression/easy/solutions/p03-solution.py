"""
Implement MSE from Scratch
==========================
Implement Mean Squared Error manually and verify against
sklearn.metrics.mean_squared_error.
"""

import numpy as np
from sklearn.metrics import mean_squared_error


def mse_from_scratch(y_true, y_pred):
    """Calculate Mean Squared Error manually.

    MSE = (1/n) * sum((y_true_i - y_pred_i)^2)
    """
    y_true = np.array(y_true, dtype=float)
    y_pred = np.array(y_pred, dtype=float)
    n = len(y_true)
    return np.sum((y_true - y_pred) ** 2) / n


if __name__ == "__main__":
    # Test dataset
    y_true = [3.0, -0.5, 2.0, 7.0]
    y_pred = [2.5, 0.0, 2.0, 8.0]

    my_mse = mse_from_scratch(y_true, y_pred)
    sk_mse = mean_squared_error(y_true, y_pred)

    print(f"My MSE:        {my_mse:.6f}")
    print(f"sklearn MSE:  {sk_mse:.6f}")
    print(f"Match:        {np.isclose(my_mse, sk_mse)}")

    # Additional test with random data
    np.random.seed(42)
    y_true2 = np.random.randn(100)
    y_pred2 = y_true2 + np.random.randn(100) * 0.1

    my_mse2 = mse_from_scratch(y_true2, y_pred2)
    sk_mse2 = mean_squared_error(y_true2, y_pred2)
    print(f"\nRandom data - My MSE: {my_mse2:.6f}")
    print(f"Random data - sklearn MSE: {sk_mse2:.6f}")
    print(f"Match: {np.isclose(my_mse2, sk_mse2)}")
