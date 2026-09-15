"""
Simple Linear Regression from Scratch
======================================
Implement simple linear regression using the closed-form (ordinary least squares)
formula for slope (m) and intercept (b).

Formula:
  m = sum((x_i - x_mean)(y_i - y_mean)) / sum((x_i - x_mean)^2)
  b = y_mean - m * x_mean
"""

import numpy as np


def simple_linear_regression(x, y):
    """Fit y = m*x + b using the closed-form OLS formula."""
    x = np.array(x, dtype=float)
    y = np.array(y, dtype=float)

    x_mean = np.mean(x)
    y_mean = np.mean(y)

    # Numerator: sum of (x - x_mean)(y - y_mean)
    numerator = np.sum((x - x_mean) * (y - y_mean))
    # Denominator: sum of (x - x_mean)^2
    denominator = np.sum((x - x_mean) ** 2)

    m = numerator / denominator
    b = y_mean - m * x_mean
    return m, b


def predict(x, m, b):
    """Predict y values using the fitted line."""
    return m * np.array(x, dtype=float) + b


def r_squared(y_true, y_pred):
    """Calculate R^2 coefficient of determination."""
    y_true = np.array(y_true, dtype=float)
    y_pred = np.array(y_pred, dtype=float)
    ss_res = np.sum((y_true - y_pred) ** 2)
    ss_tot = np.sum((y_true - np.mean(y_true)) ** 2)
    return 1 - ss_res / ss_tot


if __name__ == "__main__":
    # Small test dataset: hours studied vs exam score
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 5, 4, 5]

    m, b = simple_linear_regression(x, y)
    print(f"Slope (m):     {m:.4f}")
    print(f"Intercept (b): {b:.4f}")

    y_pred = predict(x, m, b)
    print(f"Predictions:   {y_pred}")
    print(f"R^2:           {r_squared(y, y_pred):.4f}")

    # Predict for a new value
    new_x = 6
    print(f"Predicted y for x={new_x}: {predict([new_x], m, b)[0]:.4f}")
