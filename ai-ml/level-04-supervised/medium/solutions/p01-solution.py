"""Level 04 Supervised — Medium P01 Solution"""

import numpy as np
import matplotlib.pyplot as plt

def solve():
    np.random.seed(42)
    X = np.random.randn(100, 1)
    y = 3 * X.flatten() + 2 + np.random.randn(100) * 0.5
    m, b = 0.0, 0.0
    lr = 0.01
    losses = []
    for i in range(1000):
        y_pred = m * X.flatten() + b
        mse = np.mean((y - y_pred) ** 2)
        losses.append(mse)
        dm = -2 * np.mean(X.flatten() * (y - y_pred))
        db = -2 * np.mean(y - y_pred)
        m -= lr * dm
        b -= lr * db
    print(f"Final m: {m:.4f}, b: {b:.4f}")
    print(f"Final MSE: {losses[-1]:.4f}")
    plt.plot(losses)
    plt.xlabel('Iteration')
    plt.ylabel('MSE')
    plt.title('Gradient Descent Loss')
    plt.savefig('gradient_descent.png', dpi=150, bbox_inches='tight')
    plt.show()
    return m, b

if __name__ == "__main__":
    solve()