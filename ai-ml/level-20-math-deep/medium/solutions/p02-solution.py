"""Level 20 — Deep Math for ML — Medium P02 Solution"""

import numpy as np


def gradient_descent(f, df, x0, lr=0.1, iters=100):
    x = np.array(x0, dtype=float)
    history = []
    for _ in range(iters):
        x = x - lr * df(x)
        history.append(f(x))
    return x, history


if __name__ == "__main__":
    f = lambda x: (x - 3.0) ** 2
    df = lambda x: 2.0 * (x - 3.0)
    x, hist = gradient_descent(f, df, 0.0, lr=0.1, iters=50)
    print(x, hist[-1])
