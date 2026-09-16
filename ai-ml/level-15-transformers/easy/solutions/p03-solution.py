"""Level 15 — Transformers — Easy P03 Solution"""

import numpy as np


def softmax_row(scores):
    """Softmax over a 1D array. Subtracts max first for numerical stability."""
    scores = np.asarray(scores, dtype=float)
    e = np.exp(scores - np.max(scores))
    return e / e.sum()


if __name__ == "__main__":
    print(softmax_row([1.0, 2.0, 3.0]))   # [0.09   0.2447 0.6652]
    print(softmax_row([0.0, 0.0, 0.0]))   # [0.3333 0.3333 0.3333]
    print(softmax_row([1000.0, 1001.0]))  # stable: no overflow
