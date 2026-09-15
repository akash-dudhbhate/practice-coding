"""
Gradient Descent for Linear Regression (from Scratch)
======================================================
Implement gradient descent to fit y = m*x + b.
Start with m=0, b=0, run 1000 iterations, track MSE, and plot the loss curve.
"""

import numpy as np
import matplotlib.pyplot as plt


def gradient_descent(x, y, learning_rate=0.01, iterations=1000):
    """Fit simple linear regression via gradient descent.

    Returns fitted m, b, and the list of MSE values per iteration.
    """
    x = np.array(x, dtype=float)
    y = np.array(y, dtype=float)
    n = len(x)

    m = 0.0
    b = 0.0
    mse_history = []

    for _ in range(iterations):
        y_pred = m * x + b

        # Gradients
        dm = (-2 / n) * np.sum(x * (y - y_pred))
        db = (-2 / n) * np.sum(y - y_pred)

        # Update
        m -= learning_rate * dm
        b -= learning_rate * db

        # Track MSE
        mse = np.mean((y - y_pred) ** 2)
        mse_history.append(mse)

    return m, b, mse_history


if __name__ == "__main__":
    # Dataset
    x = np.array([1, 2, 3, 4, 5], dtype=float)
    y = np.array([2, 4, 5, 4, 5], dtype=float)

    m, b, mse_history = gradient_descent(x, y, learning_rate=0.01, iterations=1000)

    print(f"Fitted slope (m):     {m:.4f}")
    print(f"Fitted intercept (b): {b:.4f}")
    print(f"Final MSE:            {mse_history[-1]:.6f}")

    # Plot loss curve
    plt.figure(figsize=(8, 5))
    plt.plot(mse_history, color="blue")
    plt.xlabel("Iteration")
    plt.ylabel("MSE (Loss)")
    plt.title("Gradient Descent: Loss vs Iterations")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig("gradient_descent_loss.png", dpi=150)
    plt.show()
    print("Loss curve saved to gradient_descent_loss.png")
