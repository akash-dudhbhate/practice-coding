"""Level 04 — Supervised Learning — Easy P01 Solution"""

import numpy as np

def linreg(x, y):
    x = np.array(x)
    y = np.array(y)
    m = np.sum((x - x.mean()) * (y - y.mean())) / np.sum((x - x.mean()) ** 2)
    b = y.mean() - m * x.mean()
    return m, b

if __name__ == "__main__":
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 5, 4, 5]
    m, b = linreg(x, y)
    print(f"Slope: {m:.4f}")
    print(f"Intercept: {b:.4f}")
    y_pred = m * np.array(x) + b
    r2 = 1 - np.sum((np.array(y) - y_pred) ** 2) / np.sum((np.array(y) - np.mean(y)) ** 2)
    print(f"R²: {r2:.4f}")
