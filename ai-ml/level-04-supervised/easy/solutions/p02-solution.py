"""Level 04 — Supervised Learning — Easy P02 Solution"""

import numpy as np

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def train_logreg(X, y, lr=0.1, epochs=1000):
    X = np.array(X, dtype=float)
    y = np.array(y, dtype=float)
    w = np.zeros(X.shape[1])
    b = 0.0
    n = len(y)
    for _ in range(epochs):
        z = X @ w + b
        p = sigmoid(z)
        w -= lr * (X.T @ (p - y)) / n
        b -= lr * np.sum(p - y) / n
    return w, b

if __name__ == "__main__":
    X = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]
    y = [0, 0, 0, 1, 1]
    w, b = train_logreg(X, y)
    preds = (sigmoid(np.array(X) @ w + b) > 0.5).astype(int)
    print(f"Accuracy: {(preds == np.array(y)).mean():.4f}")
    print(f"Weights: {w}, Bias: {b:.4f}")
