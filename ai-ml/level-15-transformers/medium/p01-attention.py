"""
LEVEL 15 — Transformers from Scratch
MEDIUM P01 — Scaled Dot-Product Attention
========================================

CONCEPT:
  Attention answers: "for each token, which OTHER tokens should
  it look at, and how much?" Three matrices:

    Q (queries): what each token is LOOKING FOR
    K (keys):    what each token OFFERS / advertises
    V (values):  what each token actually SAYS

  score(i,j) = Q[i] . K[j]  → how much token i cares about token j
  weights = softmax(scores / sqrt(d_k))   → per-row probabilities
  output = weights @ V                    → weighted mix of values

  WHY divide by sqrt(d_k)? Dot products grow with dimension;
  scaling keeps softmax out of the saturated (flat-gradient) zone.

PROBLEM:
  Write `attention(Q, K, V)`:
    - INPUT: Q, K, V — each (seq_len, d_k)
    - OUTPUT: (seq_len, d_k)
    - Steps: scores = Q @ K.T / sqrt(d_k)
             weights = softmax each ROW of scores
             return weights @ V
    - Reuse your softmax_row idea (a helper is fine).

TRY THIS INPUT:
  ```python
  np.random.seed(0)
  Q = np.random.randn(2, 4)
  K = np.random.randn(2, 4)
  V = np.random.randn(2, 4)
  print(attention(Q, K, V))
  ```

EXPECTED OUTPUT:
  ```
  [[-0.1258  0.1386  0.5338 -0.8093]
   [-1.5984  0.4511  0.7344 -0.7686]]
  ```

HINT:
  scores.shape == (seq_len, seq_len). Apply your softmax to each
  row — e.g. np.stack([softmax_row(r) for r in scores]).

CHECK: python3 check.py medium/p01
"""

import numpy as np

# === WRITE YOUR CODE BELOW ===

def attention(Q, K, V):
    """Q, K, V: (seq_len, d_k) arrays -> (seq_len, d_k) output."""
    # TODO: scores = Q @ K.T / sqrt(d_k); softmax rows; @ V
    pass


# === TEST ===
# np.random.seed(0)
# Q = np.random.randn(2, 4); K = np.random.randn(2, 4); V = np.random.randn(2, 4)
# print(attention(Q, K, V))
