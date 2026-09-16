# Level 20 — Deep Math for ML

## What You'll Learn
- Eigendecomposition — the math behind PCA and spectral methods
- Vector projection — the building block of attention and cosine similarity
- Shannon entropy — how information theory measures uncertainty
- PCA from scratch — eigendecompose the covariance matrix
- Gradient descent — the generic optimizer under every ML library
- Truncated SVD — matrix compression used in embeddings and LSA
- Newton's method — second-order optimization, converges quadratically
- KL divergence — how "different" two distributions are (RLHF, VAEs)
- Adam — momentum + adaptive learning rates, the default optimizer

This is the level that lets you READ ML PAPERS.

## Prerequisites
- Level 00 (math setup), numpy only

## Problems

### Easy
1. `easy/p01-eigendecomposition.py` — `eigendecompose(A)` → eigenpairs sorted descending
2. `easy/p02-vector-proj.py` — `project(v, u)` → project v onto u
3. `easy/p03-shannon-entropy.py` — `entropy(p)` → Shannon entropy in bits

### Medium
4. `medium/p01-pca-scratch.py` — `pca_scratch(X, k)` → PCA projected data
5. `medium/p02-gradient-descent.py` — `gradient_descent(f, df, x0, lr, iters)` → (x, history)
6. `medium/p03-svd-compress.py` — `svd_compress(A, k)` → (compressed, ratio)

### Hard
7. `hard/p01-newtons-method.py` — `newton_sqrt(n, x0, iters)` → (result, iterations)
8. `hard/p02-kl-divergence.py` — `kl_divergence(p, q)` → KL(p‖q) in bits
9. `hard/p03-adam-optimizer.py` — `adam_optimize(f, df, x0, lr, iters)` → (x, history)

### Project
`project/` — PCA + logistic regression + entropy report, all from scratch.

## Verify

```bash
python3 check.py easy/p01
python3 check.py all
```
