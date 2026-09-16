"""Level 15 — Transformers — Medium P01 Solution"""

import numpy as np


def _softmax_row(scores):
    e = np.exp(scores - np.max(scores))
    return e / e.sum()


def attention(Q, K, V):
    """Single-head scaled dot-product attention.

    Q, K, V: shape (seq_len, d_k)
    returns: shape (seq_len, d_k) — each row is a weighted mix of V's rows.
    """
    d_k = Q.shape[1]
    scores = Q @ K.T / np.sqrt(d_k)              # (seq, seq) — who attends to whom
    weights = np.stack([_softmax_row(r) for r in scores])  # row-wise softmax
    return weights @ V


if __name__ == "__main__":
    np.random.seed(0)
    Q = np.random.randn(2, 4)
    K = np.random.randn(2, 4)
    V = np.random.randn(2, 4)
    print(attention(Q, K, V))
