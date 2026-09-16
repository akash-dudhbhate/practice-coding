# Level 20 — Concepts (Detailed Explanations)

Read each section BEFORE attempting its problem. Each concept has:
what it is in plain words → a worked example with real numbers →
why ML cares → the code → what confuses beginners.

This level is the math that lives under the libraries: eigenvectors
(PCA), SVD (compression, LoRA's "rank"), entropy and KL (every loss
function), and the optimizers (GD → Newton → Adam) that train
everything.

---

## Easy

### 1. Eigendecomposition — `p01`

**What it is:** For a square matrix A, an eigenvector v is a
direction the matrix doesn't rotate — it only stretches it:
`A·v = λ·v`. The scalar λ (eigenvalue) is how much it stretches.
A matrix's eigenvectors are its "natural axes."

**Worked example:**
```
A = [[2, 1],
     [1, 2]]          (symmetric — A equals its transpose)

Try v = [1, 1]:
  A·v = [2·1 + 1·1, 1·1 + 2·1] = [3, 3] = 3·[1, 1]
  → [1,1] is an eigenvector with λ = 3

Try v = [1, -1]:
  A·v = [2 - 1, 1 - 2] = [1, -1] = 1·[1, -1]
  → eigenvector with λ = 1

np.linalg.eig(A) → vals [3, 1] (after sorting desc),
  vecs columns ≈ [0.707, 0.707] and [0.707, -0.707] (unit length)
check: A @ vecs[:,0] = [2.12, 2.12] ≈ 3·[0.707, 0.707] ✓
```

**Why ML cares:** Eigenvalues tell you where a transform "wants" to
push things. PCA (medium/p01) IS eigendecomposition of the covariance
matrix — eigenvector = direction of max variance, eigenvalue = how
much variance. Spectral clustering and PageRank are the same math.

**Code:**
```python
def eigendecompose(A):
    vals, vecs = np.linalg.eig(A)
    idx = np.argsort(vals)[::-1]       # descending order
    return vals[idx], vecs[:, idx]     # reorder COLUMNS too
```

**Common confusion:** `np.linalg.eig` returns eigenvectors as
COLUMNS (`vecs[:, i]` is the i-th eigenvector), not rows — and it
returns them unordered. If you sort the values but forget
`vecs[:, idx]`, your eigenpairs no longer match up.

---

### 2. Vector Projection — `p02`

**What it is:** The projection of v onto u is the "shadow" v casts
on the line through u. Formula: `proj_u(v) = (v·u / u·u) · u`. The
scalar `(v·u)/(u·u)` says how many copies of u fit inside v.

**Worked example:**
```
v = [3, 4],  u = [1, 0]  (the x-axis)

v·u = 3·1 + 4·0 = 3
u·u = 1·1 + 0·0 = 1
proj = (3/1) · [1, 0] = [3, 0]     ← v's shadow drops the y-part

Sanity: v = [3,4] is 5 long at ~53°; its shadow on the x-axis
has length 5·cos(53°) ≈ 3 ✓
```

**Why ML cares:** Projection is the atom inside bigger machines:
cosine similarity is a normalized projection; attention scores ask
"how much does this query project onto each key?"; Gram-Schmidt
builds orthogonal bases by repeatedly subtracting projections;
least-squares regression projects the target onto the feature space.

**Code:**
```python
def project(v, u):
    return (np.dot(v, u) / np.dot(u, u)) * u
```

**Common confusion:** `v·u / u·u` is a SCALAR, not a vector — it
scales u. Beginners sometimes return just the scalar, or divide by
`v·v` instead of `u·u` (which projects onto the wrong line's units).

---

### 3. Shannon Entropy — `p03`

**What it is:** Entropy measures a distribution's uncertainty in
BITS: `H(p) = −Σ pᵢ·log₂(pᵢ)`. A bit = one yes/no question's worth
of information. Uniform = maximum surprise; certain = zero.

**Worked example:**
```
Fair coin, p = [0.5, 0.5]:
  H = −(0.5·log₂0.5 + 0.5·log₂0.5)
    = −(0.5·(−1) + 0.5·(−1)) = 1.0 bit

Uniform over 4, p = [0.25]×4:
  H = −4 · (0.25·log₂0.25) = −4·(0.25·(−2)) = 2.0 bits

Certain, p = [1, 0, 0]:
  H = −(1·log₂1 + ...) = −(1·0) = 0 bits
  (the 0·log₂0 terms are DEFINED as 0 — mask them out or NaN)
```

**Why ML cares:** Entropy is everywhere: decision trees pick the
split with the biggest entropy drop (information gain); language-model
perplexity is 2^entropy; cross-entropy loss is entropy plus a KL term
(hard/p02); RL exploration bonuses reward high-entropy policies.

**Code:**
```python
def entropy(p):
    p = p[p > 0]                    # drop zeros BEFORE the log
    return -np.sum(p * np.log2(p))
```

**Common confusion:** `0 · log2(0)` is `0 · (−inf)` = NaN in
floating point — but by convention it equals 0 (an impossible outcome
carries no surprise). Filter zeros first; never log the raw vector.

---

## Medium

### 4. PCA From Scratch — `p01`

**What it is:** PCA finds the directions of maximum variance in data
and projects onto the top-k. It's five steps: center → covariance →
eigendecompose → take top-k eigenvectors → project.

**Worked example:**
```
X = 100 samples × 3 features, scaled so feature 0 varies most
    (X = randn(100,3) @ diag(2, 1, 0.1))

1. Center:     Xc = X - X.mean(axis=0)
               → each column now has mean 0
2. Covariance: C = Xc.T @ Xc / (n-1)        → (3,3), symmetric
               → C[i][j] = how features i,j vary together
3. Eigendecompose C:
               eigenvalues ≈ [4.0, 1.0, 0.01]  ← variance per axis
               eigenvectors = the principal directions
4. W = top-2 eigenvector columns             → (3,2)
5. Z = Xc @ W                                → (100,2)

Z.var(axis=0) ≈ [4.0, 1.0]  — first component holds the most
variance; the ~0.01 third direction got dropped.
λᵢ/Σλ = explained-variance ratio: 4/(4+1+.01) ≈ 80% for comp 1.
```

**Why ML cares:** `sklearn.decomposition.PCA` does exactly this. Now
"we projected onto the first two principal components" in a paper is
no longer magic — it's `Xc @ W`. It's how you squash 768-dim
embeddings to 2-D for plots, and denoise data by dropping
low-variance directions.

**Code:**
```python
def pca_scratch(X, k):
    Xc = X - X.mean(axis=0)
    C = Xc.T @ Xc / (len(X) - 1)
    vals, vecs = np.linalg.eig(C)
    idx = np.argsort(vals)[::-1]
    W = vecs[:, idx[:k]]
    return Xc @ W
```

**Common confusion:** Forgetting to CENTER. Without `X - mean`, the
first "principal component" just points at the data's mean, not the
direction of variance — results look plausible but are wrong.

---

### 5. Gradient Descent (Generic Optimizer) — `p02`

**What it is:** Minimize a function by repeatedly stepping opposite
the gradient: `x ← x − lr·∇f(x)`. Writing it generically — f and df
passed in as callables — is exactly how `torch.optim` works: the
model hands you gradients, you update parameters.

**Worked example:**
```
f(x) = (x − 3)²,  df(x) = 2(x − 3),  start x=0, lr=0.1

step 1: x = 0    − 0.1·2(0−3)    = 0 + 0.6   = 0.60
step 2: x = 0.60 − 0.1·2(0.6−3)  = 0.6+0.48  = 1.08
step 3: x = 1.08 − 0.1·2(−1.92)  = 1.46
...each step closes ~20% of the remaining gap...
after 50 steps: x ≈ 3.0000, f(x) ≈ 1e-28

history = [f(x) after each update] — the loss curve you'd plot
```

**Why ML cares:** Every neural network ever trained ran this loop —
Adam (hard/p03) just adds bookkeeping. The `history` list is how you
diagnose problems: lr too big → history explodes; lr too small →
history plateaus miles from zero.

**Code:**
```python
def gradient_descent(f, df, x0, lr=0.1, iters=100):
    x = np.array(x0, dtype=float)     # handles scalar or vector
    history = []
    for _ in range(iters):
        x = x - lr * df(x)
        history.append(f(x))
    return x, history
```

**Common confusion:** Record `f(x)` AFTER the update, not before —
the history should show the loss going down from step 1. And copy
`x0` into a float array (`np.array(x0, dtype=float)`); integers
truncate every update to whole numbers and never converge.

---

### 6. SVD Compression — `p03`

**What it is:** Any matrix factorizes as `A = U·Σ·Vᵀ` where Σ is
diagonal with singular values sorted descending. Keeping only the
top-k gives the BEST possible rank-k approximation (Eckart–Young
theorem) — the same trick that makes LoRA's "low rank" work.

**Worked example:**
```
A = random 10×8 matrix (m=10, n=8), k=3

A_k = U[:,:3] @ diag(S[:3]) @ Vt[:3,:]     → still (10,8)

storage:  original = m·n         = 80 numbers
          compressed = k·(m+n+1) = 3·(10+8+1) = 57 numbers
          ratio = 57/80 = 0.7125             → 29% smaller

reconstruction error ||A − A_k|| shrinks as k grows;
at k = min(m,n) = 8 it's ~0 (perfect, but no savings).
```

**Why ML cares:** Weight matrices in trained networks are often
effectively low-rank — most singular values are tiny. Truncated SVD
compresses embedding tables; LSA on documents is SVD of the
term-document matrix; LoRA (level-17) bets that the *update* a task
needs is low-rank — same math, opposite direction.

**Code:**
```python
def svd_compress(A, k):
    U, S, Vt = np.linalg.svd(A, full_matrices=False)
    A_hat = U[:, :k] @ np.diag(S[:k]) @ Vt[:k, :]
    m, n = A.shape
    ratio = k * (m + n + 1) / (m * n)
    return A_hat, ratio
```

**Common confusion:** Use `full_matrices=False` — otherwise U is
(m×m) and Vt is (n×n), bigger than you need. Also the storage count
is `k·(m+n+1)`: k columns of U + k singular values + k rows of Vt,
not just `k·m`.

---

## Hard

### 7. Newton's Method — `p01`

**What it is:** Gradient descent uses only the first derivative;
Newton also uses CURVATURE (the second derivative), so it converges
quadratically — correct digits roughly double each step. To find a
root of g: `x ← x − g(x)/g′(x)`.

**Worked example:**
```
Compute √2 by solving g(x) = x² − 2 = 0,  g′(x) = 2x

x ← x − (x²−2)/(2x) = (x + 2/x)/2     ← Heron's formula, ~2000 yrs old

x0 = 1.0
x1 = (1.0 + 2/1.0)/2     = 1.5
x2 = (1.5 + 2/1.5)/2     = 1.4166667
x3 = (1.4167 + 2/1.4167)/2 = 1.4142157
x4 = 1.41421356  ✓  matches np.sqrt(2) — converged in ~4-5 steps!

Early stop: |x_new − x| < 1e-12 → break, count iterations used.
```

**Why ML cares:** The same idea on gradients gives `x ← x − H⁻¹∇f`
where H is the Hessian (matrix of second derivatives). For a
billion-parameter model, H has 10¹⁸ entries — uninvertible — which is
why deep learning uses Adam instead. But papers still cite
Newton/quasi-Newton (L-BFGS) constantly; it's the ideal Adam
approximates.

**Code:**
```python
def newton_sqrt(n, x0, iters=20):
    x = x0
    for i in range(iters):
        x_new = 0.5 * (x + n / x)
        if abs(x_new - x) < 1e-12:
            return x_new, i + 1
        x = x_new
    return x, iters
```

**Common confusion:** Return the iterations ACTUALLY performed, not
always `iters` — early stopping on `|x_new − x| < 1e-12` is the point
(quadratic convergence means ~5 steps, not 20).

---

### 8. KL Divergence — `p02`

**What it is:** `D_KL(p‖q) = Σ pᵢ·log₂(pᵢ/qᵢ)` — the extra bits
needed to encode samples from p using a codebook optimized for q.
If p = q, zero extra bits. If q assigns 0 to something p expects,
the "surprise" is infinite.

**Worked example:**
```
p = [0.5, 0.5],  q = [0.25, 0.75]

KL(p‖p) = Σ p·log₂(1) = 0                    ← same dist, 0 cost

KL(p‖q) = 0.5·log₂(0.5/0.25) + 0.5·log₂(0.5/0.75)
        = 0.5·log₂(2)       + 0.5·log₂(2/3)
        = 0.5·1.0           + 0.5·(−0.585)
        = 0.5 − 0.2925 = 0.2075 bits

KL(q‖p) = 0.25·log₂(0.5) + 0.75·log₂(1.5)
        = −0.25 + 0.438 = 0.188 bits         ← NOT equal to KL(p‖q)!

q = [1.0, 0.0]: q₁=0 but p₁=0.5>0 → KL = +inf
```

**Why ML cares:** It's THE "distance between distributions" in ML:
VAEs penalize KL(latent ‖ prior), RLHF/PPO penalizes KL(policy ‖
reference policy) so the tuned model doesn't drift too far, knowledge
distillation trains a small model to minimize KL to the teacher.
The asymmetry is the feature: punishing "q forgot something p does"
vs "q does extra things" are different design choices.

**Code:**
```python
def kl_divergence(p, q):
    total = 0.0
    for pi, qi in zip(p, q):
        if pi == 0:
            continue                 # term contributes 0
        if qi == 0:
            return np.inf            # q says impossible, p disagrees
        total += pi * np.log2(pi / qi)
    return total
```

**Common confusion:** KL is NOT symmetric — `KL(p‖q) ≠ KL(q‖p)` —
so it's not a true "distance" (mathematicians call it a divergence).
Getting p and q swapped flips the meaning entirely: `KL(p‖q)` asks
"how wrong is q as a model of p?"

---

### 9. Adam Optimizer — `p03`

**What it is:** Adam = momentum (smooth the gradient) + RMSProp
(scale by recent gradient size) + bias correction (fix the cold
start). Two running averages of the gradient g do all the work:
`m` (first moment) and `v` (second moment).

**Worked example:**
```
Recipe per step t (β₁=0.9, β₂=0.999, ε=1e-8):
  m ← 0.9·m + 0.1·g          # smoothed gradient
  v ← 0.999·v + 0.001·g²     # smoothed squared gradient
  m̂ = m/(1−0.9ᵗ);  v̂ = v/(1−0.999ᵗ)   # bias correction
  x ← x − lr·m̂/(√v̂ + ε)

Step 1 on f=(x−3)² at x=0: g = 2(0−3) = −6
  m = 0.1·(−6) = −0.6;      v = 0.001·36 = 0.036
  m̂ = −0.6/(1−0.9) = −6;    v̂ = 0.036/(1−0.999) = 36
  update = lr·(−6)/(√36+ε) = lr·(−1) → x moves +lr toward 3

The magic: without correction, step 1 would be tiny (m starts at 0);
m̂, v̂ rescale so the first step is ≈ lr regardless of |g|.
Dims with consistently big grads → big v̂ → smaller effective steps.
Minimize f = Σ(x−3)² on x0=[0,0,0,0], lr=0.1, 300 iters → [3,3,3,3].
```

**Why ML cares:** This is LITERALLY `torch.optim.Adam` — same
formula, same defaults. It's the default optimizer for almost all of
deep learning because per-parameter adaptive learning rates navigate
loss surfaces where plain GD oscillates or stalls.

**Code:**
```python
def adam_optimize(f, df, x0, lr=0.01, iters=200,
                  beta1=0.9, beta2=0.999, eps=1e-8):
    x = np.array(x0, dtype=float)
    m = np.zeros_like(x); v = np.zeros_like(x)
    history = []
    for t in range(1, iters + 1):
        g = df(x)
        m = beta1 * m + (1 - beta1) * g
        v = beta2 * v + (1 - beta2) * g**2
        m_hat = m / (1 - beta1**t)
        v_hat = v / (1 - beta2**t)
        x = x - lr * m_hat / (np.sqrt(v_hat) + eps)
        history.append(f(x))
    return x, history
```

**Common confusion:** `t` starts at 1, not 0 — `beta1**t` with t=0
makes `1 − 1 = 0` → division by zero. The bias correction exists
precisely because m and v start at 0 and are biased toward it for
the first ~1/(1−β) steps.

---

## Done with concepts? → Try `easy/p01-eigendecomposition.py`
