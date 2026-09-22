"""Level 15 — Transformers — Hard P01 Solution"""

import numpy as np


def _softmax_row(scores):
    e = np.exp(scores - np.max(scores))
    return e / e.sum()


def _attention(Q, K, V):
    d_k = Q.shape[1]
    scores = Q @ K.T / np.sqrt(d_k)
    weights = np.stack([_softmax_row(r) for r in scores])
    return weights @ V


def _layernorm(x, eps=1e-6):
    """Normalize each row to mean 0 / std 1 (over the feature axis)."""
    mean = x.mean(axis=-1, keepdims=True)
    var = x.var(axis=-1, keepdims=True)
    return (x - mean) / np.sqrt(var + eps)


def transformer_block(X, params):
    """One transformer block: attention -> residual+norm -> FFN -> residual+norm.

    X: (seq_len, d_model)
    params keys: W_q, W_k, W_v (d,d); W1 (d,d_ff), b1 (d_ff,);
                 W2 (d_ff,d), b2 (d,)
    returns: (seq_len, d_model)
    """
    # 1. self-attention sublayer with residual connection + layernorm
    attn_out = _attention(X @ params["W_q"], X @ params["W_k"], X @ params["W_v"])
    X1 = _layernorm(X + attn_out)

    # 2. feed-forward sublayer (expand -> ReLU -> shrink) + residual + norm
    ffn = np.maximum(0, X1 @ params["W1"] + params["b1"]) @ params["W2"] + params["b2"]
    out = _layernorm(X1 + ffn)
    return out


if __name__ == "__main__":
    np.random.seed(2)
    d = 8
    params = {
        "W_q": np.random.randn(d, d) * 0.1,
        "W_k": np.random.randn(d, d) * 0.1,
        "W_v": np.random.randn(d, d) * 0.1,
        "W1": np.random.randn(d, 16) * 0.1,
        "b1": np.zeros(16),
        "W2": np.random.randn(16, d) * 0.1,
        "b2": np.zeros(d),
    }
    X = np.random.randn(4, d)
    out = transformer_block(X, params)
    print("shape:", out.shape)
    print("row 0:", out[0])
