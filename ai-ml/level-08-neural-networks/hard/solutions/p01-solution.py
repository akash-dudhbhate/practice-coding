"""Level 08 — Neural Networks — Hard P01 Solution"""

import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def train_manual():
    np.random.seed(42)
    X = np.array([[0,0],[0,1],[1,0],[1,1]], dtype=float)
    y = np.array([0,1,1,0], dtype=float).reshape(-1, 1)
    # Larger initial weights help break symmetry on XOR
    W1 = np.array([[5.0, -5.0], [-5.0, 5.0]])
    b1 = np.array([[-2.5, -2.5]])
    W2 = np.array([[5.0], [5.0]])
    b2 = np.array([[-2.5]])
    lr = 0.5
    losses = []
    for epoch in range(20000):
        h = sigmoid(X @ W1 + b1)
        out = sigmoid(h @ W2 + b2)
        loss = np.mean((y - out) ** 2)
        losses.append(loss)
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
    preds, losses = train_manual()
    print(f"Final loss: {losses[-1]:.6f}")
    for x, p in zip([[0,0],[0,1],[1,0],[1,1]], preds):
        print(f"{x} -> {p:.4f}")
