"""
LEVEL 20 — Deep Math for ML
MEDIUM P03 — SVD Compression
========================================

CONCEPT:
  Any matrix A (m×n) factorizes as A = U Σ Vᵀ where Σ is diagonal
  with singular values sorted descending. Keeping only the top-k
  gives the BEST rank-k approximation possible (Eckart–Young):

      A_k = U[:,:k] @ diag(S[:k]) @ Vt[:k,:]

  Storage: original m·n numbers → k·(m + n + 1) numbers.
  compression_ratio = k·(m+n+1) / (m·n)  (< 1 means you saved space)

  This is how people compress embedding tables, do LSA on
  documents, and why "the effective rank" of a weight matrix
  matters for LoRA fine-tuning.

PROBLEM:
  Write `svd_compress(A, k)` that returns (A_compressed, ratio):
    - A_compressed: rank-k reconstruction, same shape as A
    - ratio: stored params / original params as above

TRY THIS INPUT:
  ```python
  np.random.seed(42)
  A = np.random.randn(10, 8)
  A_hat, ratio = svd_compress(A, 3)
  print(A_hat.shape)   # (10, 8)
  print(ratio)         # 3*(10+8+1)/(10*8) = 0.7125
  ```

EXPECTED OUTPUT:
  ```
  (10, 8)
  0.7125
  ```
  Reconstruction error ||A - A_hat|| shrinks as k grows;
  at k = min(m,n) it's ~0.

HINT:
  U, S, Vt = np.linalg.svd(A, full_matrices=False)
  A_hat = U[:, :k] @ np.diag(S[:k]) @ Vt[:k, :]
  (equivalently: (U[:,:k] * S[:k]) @ Vt[:k,:] — broadcasting)

CHECK: python3 check.py medium/p03
"""

import numpy as np


# === WRITE YOUR CODE BELOW ===
def svd_compress(A, k):
    # TODO: truncated SVD reconstruction + compression ratio
    pass


# === TEST ===
# np.random.seed(42)
# A = np.random.randn(10, 8)
# A_hat, ratio = svd_compress(A, 3)
# print(A_hat.shape, ratio)
