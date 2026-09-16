"""
LEVEL 15 — Transformers from Scratch
HARD P01 — A Complete Transformer Block
========================================

CONCEPT:
  One transformer block = attention + two stabilization tricks:

    1. attn = attention(X@W_q, X@W_k, X@W_v)
    2. X1 = layernorm(X + attn)          <- residual + norm
    3. ffn = relu(X1@W1 + b1) @ W2 + b2  <- feed-forward network
    4. out = layernorm(X1 + ffn)         <- residual + norm

  WHY residual (+X)? Lets gradients flow and lets each sublayer
  learn a small CORRECTION instead of a full transformation.

  WHY layernorm? Rescales every row to mean 0 / std 1 so values
  don't explode across stacked blocks.

  WHY the FFN? Attention only MIXES existing information; the
  per-token feed-forward net does the actual "thinking" (nonlinear
  transform, expand then shrink).

PROBLEM:
  Write `transformer_block(X, params)`:
    - X: (seq_len, d_model)
    - params: dict with keys
        "W_q","W_k","W_v": (d_model, d_model)
        "W1": (d_model, d_ff),  "b1": (d_ff,)
        "W2": (d_ff, d_model),  "b2": (d_model,)
    - OUTPUT: (seq_len, d_model) — same shape as X
    - layernorm(x): (x - mean) / sqrt(var + eps), per row,
      eps = 1e-6

TRY THIS INPUT:
  ```python
  np.random.seed(2)
  d = 8
  params = {
      "W_q": np.random.randn(d, d) * 0.1,
      "W_k": np.random.randn(d, d) * 0.1,
      "W_v": np.random.randn(d, d) * 0.1,
      "W1": np.random.randn(d, 16) * 0.1, "b1": np.zeros(16),
      "W2": np.random.randn(16, d) * 0.1, "b2": np.zeros(d),
  }
  X = np.random.randn(4, d)
  out = transformer_block(X, params)
  print("shape:", out.shape)
  print("row 0:", out[0])
  ```

EXPECTED OUTPUT:
  ```
  shape: (4, 8)
  row 0: [-0.7176 -0.0263  2.5145 -0.7954 -0.6394  0.0507 -0.0473 -0.3392]
  ```

HINT:
  Write small helpers: _attention(Q,K,V) and _layernorm(x).
  ReLU = np.maximum(0, x). Residual means literally "+ input".

CHECK: python3 check.py hard/p01
"""

import numpy as np

# === WRITE YOUR CODE BELOW ===

def transformer_block(X, params):
    """One transformer block. X: (seq_len, d_model) -> same shape out."""
    # TODO: attention -> residual+layernorm -> FFN -> residual+layernorm
    pass


# === TEST ===
# np.random.seed(2)
# d = 8
# params = {...see docstring...}
# X = np.random.randn(4, d)
# print(transformer_block(X, params))
