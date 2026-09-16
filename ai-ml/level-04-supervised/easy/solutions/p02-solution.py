"""Level 04 Supervised — Easy P02 Solution"""

import numpy as np

def solve():
    def sigmoid(z):
        return 1 / (1 + np.exp(-z))
    X = np.array([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]])
    y = np.array([0, 0, 0, 1, 1])
    weights = np.zeros(X.shape[1])
    bias = 0
    lr = 0.1
    for _ in range(1000):
        z = np.dot(X, weights) + bias
        y_pred = sigmoid(z)
        dw = np.dot(X.T, (y_pred - y)) / len(y)
        db = np.sum(y_pred - y) / len(y)
        weights -= lr * dw
        bias -= lr * db
    predictions = sigmoid(np.dot(X, weights) + bias)
    accuracy = np.mean((predictions > 0.5) == y)
    print(f"Accuracy: {accuracy:.4f}")
    print(f"Weights: {weights}")
    print(f"Bias: {bias:.4f}")
    return weights, bias

if __name__ == "__main__":
    solve()