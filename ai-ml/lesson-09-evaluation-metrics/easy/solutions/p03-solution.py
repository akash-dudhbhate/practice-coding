"""
Calculate MSE, RMSE, MAE, R^2 for Regression
============================================
Train linear regression on make_regression and calculate all four metrics.
Print each and explain which is most interpretable.
"""

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score


if __name__ == "__main__":
    X, y = make_regression(n_samples=300, n_features=5, noise=20, random_state=42)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print("=== Regression Metrics ===\n")
    print(f"MSE:  {mse:.4f}")
    print(f"RMSE: {rmse:.4f}")
    print(f"MAE:  {mae:.4f}")
    print(f"R^2:  {r2:.4f}")

    print("\n=== Explanation ===")
    print(f"MSE  - Mean Squared Error: average of squared errors. Penalizes large errors more.")
    print(f"       Units: squared target units (hard to interpret directly).")
    print(f"RMSE - Root Mean Squared Error: square root of MSE. Same units as target.")
    print(f"       Most interpretable for understanding typical error magnitude.")
    print(f"MAE  - Mean Absolute Error: average of absolute errors. Same units as target.")
    print(f"       Less sensitive to outliers than RMSE.")
    print(f"R^2  - Coefficient of determination: proportion of variance explained (0-1).")
    print(f"       Most interpretable for understanding model quality (0=worst, 1=perfect).")
    print(f"\nRMSE ({rmse:.2f}) is the most interpretable error metric: 'predictions are off by ~{rmse:.2f} on average'.")
    print(f"R^2 ({r2:.4f}) is the most interpretable quality metric: '{r2*100:.1f}% of variance is explained'.")
