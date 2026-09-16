"""Level 08 Neural Networks — Easy P01 Solution"""

import numpy as np

def solve():
    # OR gate: (0,0)->0, (0,1)->1, (1,0)->1, (1,1)->1
    X = np.array([[0,0], [0,1], [1,0], [1,1]])
    y = np.array([0, 1, 1, 1])
    weights = np.zeros(2)
    bias = 0
    lr = 0.1
    for _ in range(100):
        for i in range(len(X)):
            z = np.dot(X[i], weights) + bias
            pred = 1 if z > 0 else 0
            weights += lr * (y[i] - pred) * X[i]
            bias += lr * (y[i] - pred)
    print(f"Weights: {weights}")
    print(f"Bias: {bias:.4f}")
    for i in range(len(X)):
        z = np.dot(X[i], weights) + bias
        pred = 1 if z > 0 else 0
        print(f"{X[i]} -> {pred} (expected {y[i]})")
    return weights, bias

if __name__ == "__main__":
    solve()