"""Level 20 — Deep Math for ML — Easy P03 Solution"""

import numpy as np


def entropy(p):
    p = np.asarray(p, dtype=float)
    p = p[p > 0]
    return float(-np.sum(p * np.log2(p)))


if __name__ == "__main__":
    print(entropy(np.array([0.5, 0.5])))
    print(entropy(np.array([0.25] * 4)))
    print(entropy(np.array([1.0, 0.0, 0.0])))
