# Lesson 03 — Coding Check

Use this to verify your solutions before asking for review. Run each file and check the outputs against these criteria.

## Easy

### p01-solve.py — Create and inspect arrays
- [ ] Uses `np.random.default_rng(seed=42)` or `np.random.seed(42)` for reproducibility.
- [ ] Creates a 4×5 array with `rng.integers(0, 100, size=(4, 5))`.
- [ ] Prints shape `(4, 5)`, dtype (int64), ndim `2`, size `20`.
- [ ] Column means computed with `arr.mean(axis=0)` → shape `(5,)`.
- [ ] Test: re-running produces the exact same array (seed works).
- [ ] Test: column means array has 5 values, each between 0 and 100.

### p02-solve.py — Indexing and slicing
- [ ] Center 3×3: `mat[1:4, 1:4]` → shape `(3, 3)`.
- [ ] Last row: `mat[-1]` or `mat[4, :]` → shape `(5,)`.
- [ ] First column: `mat[:, 0]` → shape `(5,)`.
- [ ] Elements > 10: `mat[mat > 10]` → 1D array of filtered values.
- [ ] Test: with input `np.arange(25).reshape(5, 5)`, center 3×3 = `[[6,7,8],[11,12,13],[16,17,18]]`.
- [ ] Test: elements > 10 from `np.arange(25).reshape(5,5)` = `[11, 12, ..., 24]` (14 values).

### p03-solve.py — Reshape and transpose
- [ ] Original: `np.arange(24)` → shape `(24,)`.
- [ ] Reshaped to `(2, 3, 4)` → 3D array.
- [ ] Transposed to `(4, 3, 2)` → `.transpose(2, 1, 0)` or `.T`.
- [ ] Flattened back with `.reshape(-1)` or `.ravel()`.
- [ ] Test: `np.array_equal(flattened, original)` returns `True`.
- [ ] Test: reshaped array has 24 elements, transposed has 24 elements (no data lost).

## Medium

### p01-solve.py — Broadcasting operations
- [ ] Subtracts column means using broadcasting: `scores - scores.mean(axis=0)`.
- [ ] Divides by column std: `result / scores.std(axis=0)`.
- [ ] No loops used — pure vectorized operations.
- [ ] Test: output shape matches input shape.
- [ ] Test: `np.allclose(result.mean(axis=0), 0, atol=1e-10)` → True (column means ≈ 0).
- [ ] Test: `np.allclose(result.std(axis=0), 1, atol=1e-10)` → True (column stds ≈ 1).

### p02-solve.py — Vectorized vs loop
- [ ] Loop version: iterates element by element, accumulates squared differences.
- [ ] Vectorized version: `np.sqrt(np.sum((a - b) ** 2))` or `np.linalg.norm(a - b)`.
- [ ] Both return the same distance value (within floating point tolerance).
- [ ] Times both with `time.time()` or `timeit`.
- [ ] Test: speedup ratio (loop_time / vectorized_time) > 10x on 1M elements.
- [ ] Test: distances match: `abs(loop_dist - vec_dist) < 1e-6`.

### p03-solve.py — Boolean masking and clipping
- [ ] Replaces negatives: `arr[arr < 0] = 0`.
- [ ] Replaces values > 100: `arr[arr > 100] = 100`.
- [ ] Counts negatives before replacement and >100 values before replacement.
- [ ] Returns clipped array and both counts.
- [ ] Test: input `[[-5, 50, 150], [10, -20, 80], [200, 5, -1]]` → output `[[0, 50, 100], [10, 0, 80], [100, 5, 0]]`.
- [ ] Test: negative count = 3, over-100 count = 2.
- [ ] Test: no values < 0 or > 100 in the output.

## Hard

### p01-solve.py — Linear regression with normal equation
- [ ] Adds bias column: `X_with_bias = np.hstack([X, np.ones((n, 1))])` or `np.c_[X, np.ones(n)]`.
- [ ] Computes weights: `w = np.linalg.inv(X_b.T @ X_b) @ X_b.T @ y`.
- [ ] Predicts: `y_pred = X_b @ w`.
- [ ] Computes MSE: `np.mean((y_pred - y) ** 2)`.
- [ ] Test: with `X = np.array([[1], [2], [3], [4]])`, `y = np.array([2, 4, 6, 8])`, weights ≈ `[2, 0]` (slope=2, intercept=0).
- [ ] Test: MSE ≈ 0.0 for perfectly linear data.
- [ ] Test: predictions shape matches y shape.

### p02-solve.py — Pairwise distance matrix
- [ ] No Python loops used for the distance computation.
- [ ] Uses broadcasting: `(X[:, None, :] - X[None, :, :])` → shape `(N, N, D)`.
- [ ] Computes `np.sqrt(np.sum(diff ** 2, axis=2))` → shape `(N, N)`.
- [ ] Test: diagonal is all zeros: `np.allclose(np.diag(distances), 0)`.
- [ ] Test: matrix is symmetric: `np.allclose(distances, distances.T)`.
- [ ] Test: with 3 points `[[0,0], [3,4], [0,0]]`, distance[0,1] = 5.0, distance[0,2] = 0.0.
- [ ] Test: shape is `(N, N)` where N = number of input points.

### p03-solve.py — Mini-batch generator
- [ ] Function is a generator (uses `yield`, not `return`).
- [ ] If `shuffle=True`, uses `rng.permutation(len(X))` to shuffle indices.
- [ ] Yields `(X_batch, y_batch)` tuples.
- [ ] Each batch has `batch_size` rows (except possibly the last).
- [ ] Test: with 1000 samples and batch_size=128, yields 8 batches (7 of 128, 1 of 104).
- [ ] Test: with `shuffle=False`, first batch = first 128 rows of X.
- [ ] Test: with seed=42 and shuffle=True, re-running gives the same batch order.
- [ ] Test: X_batch shape is `(128, n_features)`, y_batch shape is `(128,)`.

## How to verify

Run each file to test your solution:
```bash
python easy/p01-solve.py
python medium/p01-solve.py
python hard/p01-solve.py
```
