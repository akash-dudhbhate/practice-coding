"""Level 08 — Neural Networks — Easy P01 Solution"""

import numpy as np

def train_perceptron():
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    y = np.array([0, 1, 1, 1])
    w = np.array([0.1, 0.1])
    b = 0.0
    for epoch in range(20):
        for i in range(4):
            pred = 1 if np.dot(X[i], w) + b > 0 else 0
            if y[i] == 1 and pred == 0:
                w += X[i]
                b += 0.1
            elif y[i] == 0 and pred == 1:
                w -= X[i]
                b -= 0.1
    return w, b

if __name__ == "__main__":
    w, b = train_perceptron()
    print(f"Weights: {w}, Bias: {b:.4f}")
    for x in [[0,0],[0,1],[1,0],[1,1]]:
        print(f"{x} -> {1 if np.dot(x,w)+b>0 else 0}")
