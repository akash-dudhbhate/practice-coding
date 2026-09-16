# Level 20 — Concepts Reference

## Easy

### Eigendecomposition
- For square A: `A v = λ v` — eigenvector v only gets scaled by λ
- `np.linalg.eig(A)` returns (eigenvalues, eigenvectors-as-columns)
- Symmetric A → real eigenvalues, orthonormal eigenvectors (always `A = A.T` first)
- Sort descending: `idx = np.argsort(vals)[::-1]`, then reorder vecs `[:, idx]`

### Vector Projection
- proj_u(v) = (v·u / u·u) · u — the "shadow" of v on u
- Core of: cosine similarity, attention scores, Gram-Schmidt, least squares

### Shannon Entropy
- H(p) = -Σ pᵢ log₂ pᵢ — expected surprise, measured in bits
- Fair coin → 1 bit; certain outcome → 0 bits
- Convention: 0·log(0) = 0 → mask out zeros before the log

## Medium

### PCA
1. Center: `Xc = X - X.mean(axis=0)`
2. Covariance: `C = Xc.T @ Xc / (n-1)`
3. Eigendecompose C, take top-k eigenvectors W
4. Project: `Xc @ W` → (n, k)
- λᵢ/Σλ = fraction of variance explained by component i

### Gradient Descent
- `x ← x - lr · ∇f(x)` repeated — walk downhill on the loss surface
- lr too big → diverge; too small → slow. Track f(x) each step as `history`
- First-order: uses gradients only. Newton (below) uses curvature too

### Truncated SVD
- `U, S, Vt = np.linalg.svd(A)`; keep top k: `U[:,:k] @ np.diag(S[:k]) @ Vt[:k,:]`
- Best rank-k approximation (Eckart–Young theorem)
- Stored params: k·(m+n+1) vs m·n → ratio tells how much you saved
- Same math as: LSA on documents, compressing embedding matrices

## Hard

### Newton's Method
- Root of g: `x ← x - g(x)/g'(x)` — quadratic convergence (digits double each step)
- sqrt(n): solve g(x) = x²−n = 0 → update `x ← (x + n/x)/2` (Heron's formula)
- In ML: Newton on ∇f gives `x ← x - H⁻¹∇f` (H = Hessian). Too costly in
  high-D → quasi-Newton (L-BFGS) or Adam instead

### KL Divergence
- D_KL(p‖q) = Σ pᵢ log₂(pᵢ/qᵢ) — extra bits coding p with q's codebook
- NOT symmetric: KL(p‖q) ≠ KL(q‖p). Always ≥ 0, = 0 iff p = q
- pᵢ=0 → term is 0. qᵢ=0 while pᵢ>0 → divergence is ∞
- Appears in: VAE loss, RLHF penalty (KL from reference policy), distillation

### Adam
- Combines momentum (m) + RMSProp (v):
  ```
  m ← β₁m + (1−β₁)g          # first moment (mean of grads)
  v ← β₂v + (1−β₂)g²         # second moment (mean of sq grads)
  m̂ = m/(1−β₁ᵗ); v̂ = v/(1−β₂ᵗ)   # bias correction (t starts at 1)
  x ← x − lr · m̂/(√v̂ + ε)
  ```
- Defaults: β₁=0.9, β₂=0.999, ε=1e-8 — torch.optim.Adam's exact recipe
- Per-parameter adaptive lr: big-grad dims get smaller effective steps
