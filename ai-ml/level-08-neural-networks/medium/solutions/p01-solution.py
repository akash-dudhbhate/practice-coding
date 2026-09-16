"""Level 08 — Neural Networks — Medium P01 Solution"""

import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def solve_xor():
    np.random.seed(42)
    X = np.array([[0,0],[0,1],[1,0],[1,1]], dtype=float)
    y = np.array([0,1,1,0], dtype=float).reshape(-1, 1)
    W1 = np.random.randn(2, 2) * 0.5
    b1 = np.zeros((1, 2))
    W2 = np.random.randn(2, 1) * 0.5
    b2 = np.zeros((1, 1))
    lr = 0.5
    losses = []
    for epoch in range(1000):
        # Forward
        h = sigmoid(X @ W1 + b1)
        out = sigmoid(h @ W2 + b2)
        loss = np.mean((y - out) ** 2)
        losses.append(loss)
        # Backward
        d_out = (out - y) * out * (1 - out)
        d_h = (d_out @ W2.T) * h * (1 - h)
        W2 -= lr * (h.T @ d_out) / 4
        b2 -= lr * np.mean(d_out, axis=0, keepdims=True)
        W1 -= lr * (X.T @ d_h) / 4
        b1 -= lr * np.mean(d_h, axis=0, keepdims=True)
    h = sigmoid(X @ W1 + b1)
    preds = sigmoid(h @ W2 + b2)
    return preds.flatten(), losses

if __name__ == "__main__":
    preds, losses = solve_xor()
    for x, p in zip([[0,0],[0,1],[1,0],[1,1]], preds):
        print(f"{x} -> {p:.4f}")
    print(f"Final loss: {losses[-1]:.6f}")
