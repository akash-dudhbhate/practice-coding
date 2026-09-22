"""
LEVEL 20 — Deep Math for ML
HARD P02 — KL Divergence
========================================

CONCEPT:
  KL divergence D_KL(p‖q) = Σ pᵢ log₂(pᵢ/qᵢ) measures the extra
  bits needed to encode samples from p using a code optimized
  for q. Properties that show up in every paper:

    - Always ≥ 0, and = 0 iff p == q
    - NOT symmetric: KL(p‖q) ≠ KL(q‖p)
    - If qᵢ = 0 but pᵢ > 0 → divergence is +∞
      (q says "impossible" but p says it happens — infinite surprise)
    - If pᵢ = 0 → that term contributes 0

  Where you'll see it: VAE loss (KL to prior), RLHF/PPO penalty
  (KL from the reference policy), knowledge distillation.

PROBLEM:
  Write `kl_divergence(p, q)` returning KL(p‖q) in bits.
  Handle zeros: skip terms where pᵢ = 0; return np.inf when
  qᵢ = 0 while pᵢ > 0.

TRY THIS INPUT:
  ```python
  p = np.array([0.5, 0.5]); q = np.array([0.25, 0.75])
  print(kl_divergence(p, p))   # 0.0
  print(kl_divergence(p, q))   # 0.5·log2(2) + 0.5·log2(2/3) ≈ 0.2075
  print(kl_divergence(p, np.array([1.0, 0.0])))  # inf
  ```

EXPECTED OUTPUT:
  ```
  0.0
  0.20751874963942185
  inf
  ```

HINT:
  Loop or mask over indices where p > 0:
    if q[i] == 0 → return np.inf
    else acc += p[i] * np.log2(p[i] / q[i])

CHECK: python3 check.py hard/p02
"""

import numpy as np


# === WRITE YOUR CODE BELOW ===
def kl_divergence(p, q):
    # TODO: Σ pᵢ log₂(pᵢ/qᵢ); pᵢ=0 → skip; qᵢ=0 & pᵢ>0 → np.inf
    pass


# === TEST ===
# p = np.array([0.5, 0.5]); q = np.array([0.25, 0.75])
# print(kl_divergence(p, p))
# print(kl_divergence(p, q))
