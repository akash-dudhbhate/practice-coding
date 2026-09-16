"""Level 20 — Deep Math for ML — Hard P02 Solution"""

import numpy as np


def kl_divergence(p, q):
    p = np.asarray(p, dtype=float)
    q = np.asarray(q, dtype=float)
    total = 0.0
    for pi, qi in zip(p, q):
        if pi == 0.0:
            continue
        if qi == 0.0:
            return np.inf
        total += pi * np.log2(pi / qi)
    return float(total)


if __name__ == "__main__":
    p = np.array([0.5, 0.5])
    q = np.array([0.25, 0.75])
    print(kl_divergence(p, p))
    print(kl_divergence(p, q))
    print(kl_divergence(p, np.array([1.0, 0.0])))
