"""Level 20 — Deep Math for ML — Medium P01 Solution"""

import numpy as np


def pca_scratch(X, k):
    Xc = X - X.mean(axis=0)
    n = X.shape[0]
    C = Xc.T @ Xc / (n - 1)
    vals, vecs = np.linalg.eig(C)
    idx = np.argsort(vals)[::-1]
    W = vecs[:, idx[:k]]
    return Xc @ W


if __name__ == "__main__":
    np.random.seed(42)
    X = np.random.randn(100, 3) @ np.diag([2.0, 1.0, 0.1])
    Z = pca_scratch(X, 2)
    print(Z.shape)
    print(Z.var(axis=0))
