"""
LEVEL 15 — Transformers from Scratch
MEDIUM P03 — Projected Attention (Q/K/V Weight Matrices)
========================================

CONCEPT:
  In a real transformer the model doesn't attend on raw
  embeddings — it first projects X through three LEARNED weight
  matrices:

    Q = X @ W_q      K = X @ W_k      V = X @ W_v

  WHY project? The same token needs to play different roles: what
  it looks for (Q), what it advertises (K), and what it says (V)
  are different representations of the same input. W_q/W_k/W_v
  are the learnable parameters that make attention useful.

  (A full "multi-head" version also splits d_model into several
  heads and concatenates — same math, more than once. Here you
  do the projection + one attention pass.)

PROBLEM:
  Write `multi_head(X, W_q, W_k, W_v)`:
    - INPUT: X (seq_len, d_model); W_q, W_k, W_v (d_model, d_model)
    - OUTPUT: (seq_len, d_model)
    - Steps: Q = X@W_q, K = X@W_k, V = X@W_v, then attention(Q,K,V)
      (re-implement or reuse your attention math from medium/p01)

TRY THIS INPUT:
  ```python
  np.random.seed(1)
  X = np.random.randn(3, 8)
  W_q = np.random.randn(8, 8) * 0.1
  W_k = np.random.randn(8, 8) * 0.1
  W_v = np.random.randn(8, 8) * 0.1
  out = multi_head(X, W_q, W_k, W_v)
  print("shape:", out.shape)
  print("row 0:", out[0])
  ```

EXPECTED OUTPUT:
  ```
  shape: (3, 8)
  row 0: [-0.0158  0.1231 -0.164   0.4188 -0.0842 -0.2354 -0.3087 -0.375 ]
  ```

HINT:
  Q, K, V = X @ W_q, X @ W_k, X @ W_v — then the exact same
  attention pipeline as medium/p01.

CHECK: python3 check.py medium/p03
"""

import numpy as np

# === WRITE YOUR CODE BELOW ===

def multi_head(X, W_q, W_k, W_v):
    """X: (seq_len, d_model). W_*: (d_model, d_model).
    Returns (seq_len, d_model)."""
    # TODO: project X into Q, K, V then run scaled dot-product attention
    pass


# === TEST ===
# np.random.seed(1)
# X = np.random.randn(3, 8)
# W_q = np.random.randn(8, 8) * 0.1
# W_k = np.random.randn(8, 8) * 0.1
# W_v = np.random.randn(8, 8) * 0.1
# print(multi_head(X, W_q, W_k, W_v))
