"""
LEVEL 15 — Transformers from Scratch
MEDIUM P02 — Positional Encoding
========================================

CONCEPT:
  Attention is order-blind: "cat sat mat" and "mat sat cat" give
  the same set of dot products. But word order matters! Fix:
  ADD a unique "position fingerprint" vector to each token's
  embedding before attention runs.

  The original Transformer uses sine/cosine waves:
    PE[pos, 2i]   = sin(pos / 10000^(2i/d_model))
    PE[pos, 2i+1] = cos(pos / 10000^(2i/d_model))

  Each position gets a different pattern; each dimension pair
  oscillates at a different frequency — like a clock with many
  hands. It's deterministic (no learning needed) and the model
  can infer relative distances from it.

PROBLEM:
  Write `positional_encode(seq_len, d_model)`:
    - OUTPUT: array shape (seq_len, d_model)
    - even-indexed dims get sin, odd-indexed dims get cos
    - dimension pairs (0,1), (2,3), ... share the same frequency

TRY THIS INPUT:
  ```python
  pe = positional_encode(4, 6)
  print("shape:", pe.shape)
  print("row 0:", pe[0])
  print("row 1:", pe[1])
  ```

EXPECTED OUTPUT:
  ```
  shape: (4, 6)
  row 0: [0. 1. 0. 1. 0. 1.]                  (sin(0)=0, cos(0)=1)
  row 1: [0.8415 0.5403 0.0464 0.9989 0.0022 1.    ]
  ```

HINT:
  Vectorized: pos = np.arange(seq_len)[:,None], i = np.arange(d_model)[None,:]
  angle = pos / 10000**(2*(i//2)/d_model)
  pe[:, 0::2] = np.sin(angle[:, 0::2]); pe[:, 1::2] = np.cos(angle[:, 1::2])

CHECK: python3 check.py medium/p02
"""

import numpy as np

# === WRITE YOUR CODE BELOW ===

def positional_encode(seq_len, d_model):
    """Returns (seq_len, d_model) sin/cos position matrix."""
    # TODO: build the PE matrix described above
    pass


# === TEST ===
# pe = positional_encode(4, 6)
# print(pe)
