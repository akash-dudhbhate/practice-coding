"""Level 04 Supervised — Easy P01 Solution"""

import numpy as np

def solve():
    x = np.array([1, 2, 3, 4, 5])
    y = np.array([2, 4, 5, 4, 5])
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    numerator = np.sum((x - x_mean) * (y - y_mean))
    denominator = np.sum((x - x_mean) ** 2)
    m = numerator / denominator
    b = y_mean - m * x_mean
    y_pred = m * x + b
    r2 = 1 - np.sum((y - y_pred) ** 2) / np.sum((y - y_mean) ** 2)
    print(f"Slope: {m:.4f}")
    print(f"Intercept: {b:.4f}")
    print(f"R²: {r2:.4f}")
    return m, b

if __name__ == "__main__":
    solve()