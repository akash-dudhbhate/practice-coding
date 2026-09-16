"""Level 08 Neural Networks — Hard P01 Solution"""

import numpy as np

def solve():
    # Backpropagation for a 2-layer network
    X = np.array([[0,0], [0,1], [1,0], [1,1]])
    y = np.array([[0], [1], [1], [0]])
    np.random.seed(42)
    W1 = np.random.randn(2, 4)
    b1 = np.zeros(4)
    W2 = np.random.randn(4, 1)
    b2 = np.zeros(1)
    lr = 0.5
    losses = []
    for _ in range(5000):
        # Forward
        z1 = X @ W1 + b1
        a1 = np.tanh(z1)
        z2 = a1 @ W2 + b2
        a2 = 1 / (1 + np.exp(-z2))
        loss = np.mean((a2 - y) ** 2)
        losses.append(loss)
        # Backward
        dz2 = 2 * (a2 - y) * a2 * (1 - a2)
        dW2 = a1.T @ dz2
        db2 = np.sum(dz2, axis=0)
        dz1 = dz2 @ W2.T * (1 - a1**2)
        dW1 = X.T @ dz1
        db1 = np.sum(dz1, axis=0)
        # Update
        W1 -= lr * dW1
        b1 -= lr * db1
        W2 -= lr * dW2
        b2 -= lr * db2
    print(f"Final loss: {losses[-1]:.6f}")
    print("Predictions:")
    z1 = X @ W1 + b1
    a1 = np.tanh(z1)
    z2 = a1 @ W2 + b2
    a2 = 1 / (1 + np.exp(-z2))
    for i in range(len(X)):
        print(f"  {X[i]} -> {a2[i][0]:.4f} (expected {y[i][0]})")
    return losses

if __name__ == "__main__":
    solve()