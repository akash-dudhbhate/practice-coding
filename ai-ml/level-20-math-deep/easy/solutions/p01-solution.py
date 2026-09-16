"""Level 20 — Deep Math for ML — Easy P01 Solution"""

import numpy as np


def eigendecompose(A):
    vals, vecs = np.linalg.eig(A)
    idx = np.argsort(vals)[::-1]
    return vals[idx], vecs[:, idx]


if __name__ == "__main__":
    A = np.array([[2.0, 1.0], [1.0, 2.0]])
    vals, vecs = eigendecompose(A)
    print(vals)
    print(vecs)
