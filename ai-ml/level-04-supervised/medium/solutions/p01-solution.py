"""Level 04 — Supervised Learning — Medium P01 Solution"""

import numpy as np

def gradient_descent():
    np.random.seed(42)
    X = np.random.randn(100)
    y = 3 * X + 2 + np.random.randn(100) * 0.5
    m, b = 0.0, 0.0
    lr = 0.1
    losses = []
    for _ in range(100):
        y_pred = m * X + b
        losses.append(np.mean((y - y_pred) ** 2))
        dm = -2 * np.mean(X * (y - y_pred))
        db = -2 * np.mean(y - y_pred)
        m -= lr * dm
        b -= lr * db
    return m, b, losses

if __name__ == "__main__":
    m, b, losses = gradient_descent()
    print(f"m: {m:.4f}, b: {b:.4f}")
    print(f"Initial MSE: {losses[0]:.4f}")
    print(f"Final MSE: {losses[-1]:.4f}")
