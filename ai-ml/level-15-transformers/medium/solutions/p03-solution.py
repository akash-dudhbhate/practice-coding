"""Level 15 — Transformers — Medium P03 Solution"""

import numpy as np


def _softmax_row(scores):
    e = np.exp(scores - np.max(scores))
    return e / e.sum()


def _attention(Q, K, V):
    d_k = Q.shape[1]
    scores = Q @ K.T / np.sqrt(d_k)
    weights = np.stack([_softmax_row(r) for r in scores])
    return weights @ V


def multi_head(X, W_q, W_k, W_v):
    """Project X into Q, K, V with learned weight matrices, then attend.

    X: (seq_len, d_model); W_q/W_k/W_v: (d_model, d_model)
    returns: (seq_len, d_model)
    """
    Q = X @ W_q
    K = X @ W_k
    V = X @ W_v
    return _attention(Q, K, V)


if __name__ == "__main__":
    np.random.seed(1)
    X = np.random.randn(3, 8)
    W_q = np.random.randn(8, 8) * 0.1
    W_k = np.random.randn(8, 8) * 0.1
    W_v = np.random.randn(8, 8) * 0.1
    out = multi_head(X, W_q, W_k, W_v)
    print("shape:", out.shape)
    print("row 0:", out[0])
