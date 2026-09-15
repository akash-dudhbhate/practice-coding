# Lesson 03 — Concepts Explained (NumPy Fundamentals)

> Read this before solving the problems. Each concept explains:
> **What** it is · **Why** it exists · **Where** it's used · **What goes wrong** without it.

---

## NumPy Arrays (ndarray)

**What:**
A NumPy array (`ndarray`) is a grid of values, all of the same type, indexed by a tuple of integers. Unlike a Python list, it's stored in contiguous memory and supports vectorized operations.

```python
import numpy as np

# Create from a list
arr = np.array([1, 2, 3, 4, 5])           # 1D array, shape (5,)
mat = np.array([[1, 2, 3], [4, 5, 6]])     # 2D array, shape (2, 3)

# Useful constructors
zeros = np.zeros((3, 4))       # 3x4 matrix of 0.0
ones = np.ones(5)              # 1D array of 1.0
range_arr = np.arange(0, 10, 2)  # [0, 2, 4, 6, 8]
linspace = np.linspace(0, 1, 5)  # [0.0, 0.25, 0.5, 0.75, 1.0]

# Key attributes
print(arr.shape)    # (5,) — dimensions
print(arr.dtype)    # int64 — data type
print(arr.ndim)     # 1 — number of dimensions
print(arr.size)     # 5 — total number of elements
```

**Why it exists:** Python lists are flexible but slow — each element is a separate Python object with overhead. NumPy arrays store data in contiguous C-level memory, making operations 10-100x faster. This is the foundation of all numerical computing in Python.

**Where it's used:**
- Every ML library (scikit-learn, PyTorch, TensorFlow) uses arrays as the base data structure.
- Image processing — images are 3D arrays (height × width × channels).
- Scientific computing — physics simulations, signal processing.
- Data pipelines — feature matrices are 2D NumPy arrays.

**What goes wrong without it:**
- Using Python lists for math → `list1 + list2` concatenates instead of adding element-wise → wrong results.
- Looping over lists for element-wise math → 100x slower than vectorized NumPy → code times out on real datasets.
- Mixing types in a NumPy array → dtype gets upcast to a common type (e.g., int + float → all float) → unexpected type changes.
- Creating arrays with `np.array()` on nested lists of unequal length → creates an array of Python objects, not a proper numeric array → vectorized ops fail.

---

## Array Shape and Reshaping

**What:**
Shape is the tuple describing the size of each dimension. Reshaping changes the shape without changing the data. A 1D array of 12 elements can become 2×6, 3×4, 4×3, 6×2, or 12×1.

```python
import numpy as np

arr = np.arange(12)           # shape (12,) — 1D
mat = arr.reshape(3, 4)       # shape (3, 4) — 2D
back = mat.reshape(-1)        # shape (12,) — back to 1D (-1 means "infer this dimension")
col = arr.reshape(-1, 1)      # shape (12, 1) — column vector
row = arr.reshape(1, -1)      # shape (1, 12) — row vector

# Transpose
mat_T = mat.T                 # shape (4, 3) — rows become columns

# Flatten vs Ravel
flat1 = mat.flatten()         # returns a copy
flat2 = mat.ravel()           # returns a view (shares memory)
```

**Why it exists:** ML algorithms expect specific shapes. Scikit-learn wants `(n_samples, n_features)` — a 2D array. A single sample must be shaped `(1, n_features)`, not `(n_features,)`. Reshaping lets you adapt data to what the algorithm expects without copying data unnecessarily.

**Where it's used:**
- Preparing features for sklearn: `X = arr.reshape(-1, 1)` to make a 1D array 2D.
- Image processing: flattening a 28×28 image to 784 for a dense neural network.
- Batch processing: reshaping `(batch, height, width, channels)` for CNNs.
- Matrix operations: transposing for dot products.

**What goes wrong without it:**
- Passing a 1D array to sklearn → `ValueError: Expected 2D array, got 1D array instead` → crash.
- Reshaping to incompatible sizes → `ValueError: cannot reshape array of size 12 into shape (5,3)` → 12 ≠ 15.
- Confusing `(n,)` (1D) with `(n, 1)` (2D column) or `(1, n)` (2D row) → shapes don't match in matrix multiplication → `ValueError` or silently wrong results.
- Using `reshape` on a non-contiguous array → sometimes returns a copy instead of a view → modifying it doesn't change the original → confusing bugs.

---

## Indexing and Slicing

**What:**
NumPy indexing lets you access individual elements, sub-arrays, or filtered subsets. It extends Python list indexing to multiple dimensions.

```python
import numpy as np

arr = np.array([10, 20, 30, 40, 50])
mat = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Basic indexing
arr[0]          # 10 — first element
arr[-1]         # 50 — last element
mat[1, 2]       # 6 — row 1, col 2

# Slicing
arr[1:4]        # [20, 30, 40] — elements 1 to 3
mat[0:2, 1:3]   # [[2, 3], [5, 6]] — rows 0-1, cols 1-2
mat[:, 0]       # [1, 4, 7] — all rows, column 0
mat[1, :]       # [4, 5, 6] — row 1, all columns

# Boolean indexing (masking)
mask = arr > 25
arr[mask]       # [30, 40, 50] — elements where condition is True
arr[arr > 25]   # same thing, one-liner

# Fancy indexing (integer array)
indices = [0, 2, 4]
arr[indices]    # [10, 30, 50]
```

**Why it exists:** You constantly need to select subsets of data — filter rows, pick columns, extract a region of an image, or select samples meeting a condition. NumPy indexing makes this fast and expressive without Python loops.

**Where it's used:**
- Filtering data: `X[y == 1]` — get all samples of class 1.
- Selecting features: `X[:, [0, 2, 5]]` — pick specific columns.
- Train/test indexing: `X_train, X_test = X[train_idx], X[test_idx]`.
- Image cropping: `image[100:300, 200:400]` — crop a region.
- Conditional replacement: `arr[arr < 0] = 0` — clip negative values to zero.

**What goes wrong without it:**
- Using a Python loop to filter → 50x slower than boolean indexing → code times out.
- `mat[1][2]` vs `mat[1, 2]` — chained indexing creates intermediate copies → slower and doesn't work for assignment (`mat[1][2] = 0` may not modify the original).
- Boolean indexing returns a copy, not a view → `filtered = arr[arr > 5]; filtered[0] = 999` doesn't change `arr` → confusion.
- Slicing with wrong dimension order on images → you transpose the image accidentally → displayed sideways or upside down.

---

## Broadcasting

**What:**
Broadcasting is NumPy's rule for performing operations on arrays of different shapes. The smaller array is "stretched" (virtually, without copying data) to match the larger one.

```python
import numpy as np

# Scalar + array — scalar broadcasts to every element
np.array([1, 2, 3]) + 10        # [11, 12, 13]

# 1D + 2D — 1D broadcasts across rows
mat = np.array([[1, 2, 3], [4, 5, 6]])  # shape (2, 3)
row = np.array([10, 20, 30])             # shape (3,)
mat + row                                # [[11, 22, 33], [14, 25, 36]]

# Column vector + row vector → matrix (outer operation)
col = np.array([[1], [2]])  # shape (2, 1)
row = np.array([10, 20, 30])  # shape (3,)
col + row                   # shape (2, 3): [[11, 21, 31], [12, 22, 32]]
```

**Broadcasting rules:** Compare shapes right-to-left. Dimensions are compatible if they're equal or one of them is 1. Otherwise, `ValueError`.

**Why it exists:** Without broadcasting, you'd need to explicitly replicate (tile) the smaller array to match the larger one — wasting memory and writing verbose code. Broadcasting makes common patterns (add a bias to every row, scale each column) one-liners.

**Where it's used:**
- Adding bias terms: `logits + bias` where bias is 1D and logits is 2D.
- Normalizing features: `X - X.mean(axis=0)` — subtract column means from every row.
- Scaling: `X / X.std(axis=0)` — divide each column by its std.
- Distance computation: `X**2 + Y**2` where X and Y have different shapes.
- Batch operations in neural networks.

**What goes wrong without it:**
- `ValueError: operands could not be broadcast together with shapes (3,) and (2,)` → shapes don't align → crash.
- Subtracting a row mean instead of a column mean → `X - X.mean(axis=1)` with wrong axis → normalizes rows instead of columns → wrong feature scaling → model performs poorly.
- Forgetting to reshape a 1D array to a column vector `(n, 1)` → broadcasting goes the wrong direction → silent shape mismatch → wrong results without error.
- Broadcasting a `(3,)` array with a `(2, 3)` array works, but `(3,)` with `(2, 4)` fails → confusing if you don't understand the rules.

---

## Vectorized Operations

**What:**
Vectorized operations apply a function to an entire array at once, using optimized C code under the hood. No Python loops needed.

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

# Arithmetic — element-wise, no loop
arr * 2              # [2, 4, 6, 8, 10]
arr ** 2             # [1, 4, 9, 16, 25]
np.sqrt(arr)         # [1.0, 1.41, 1.73, 2.0, 2.24]
np.exp(arr)          # exponential of each element

# Aggregations
arr.sum()            # 15
arr.mean()           # 3.0
arr.max()            # 5
arr.std()            # 1.41
np.median(arr)       # 3.0

# Axis-wise aggregations on 2D
mat = np.array([[1, 2, 3], [4, 5, 6]])
mat.sum(axis=0)      # [5, 7, 9] — sum of each column
mat.sum(axis=1)      # [6, 15] — sum of each row
mat.mean(axis=0)     # [2.5, 3.5, 4.5] — mean of each column
```

**Why it exists:** A Python `for` loop doing `arr[i] * 2` runs the interpreter for each element. NumPy's vectorized op runs a single C function over all elements — 10-100x faster. On large datasets, this is the difference between seconds and minutes.

**Where it's used:**
- Feature computation: `np.log(X + 1)` — log-transform all features at once.
- Distance matrices: `np.sqrt(((X[:, None] - X[None, :]) ** 2).sum(axis=2))`.
- Activation functions: `1 / (1 + np.exp(-x))` — sigmoid on an entire layer.
- Data normalization: `(X - X.min()) / (X.max() - X.min())`.
- Loss functions: `((y_pred - y_true) ** 2).mean()` — MSE in one line.

**What goes wrong without it:**
- Python loop over 1M elements → takes 5 seconds. Vectorized → 5 milliseconds. You literally can't train models with loops.
- Using `math.sqrt()` on an array → `TypeError: only length-1 arrays can be converted to Python scalars` → must use `np.sqrt()`.
- Wrong axis in aggregation → `mat.sum(axis=0)` gives column sums when you wanted row sums → wrong feature statistics → wrong normalization.
- Forgetting that aggregations reduce a dimension → `mat.mean(axis=0)` on shape (2,3) gives shape (3,) → downstream shape mismatch.

---

## Random Number Generation

**What:**
NumPy provides a random module for generating arrays of random numbers — uniform, normal, integers, shuffling, and sampling. The modern API uses `np.random.default_rng()`.

```python
import numpy as np

rng = np.random.default_rng(seed=42)  # reproducible random generator

# Uniform random [0, 1)
rng.random(5)                  # 1D array of 5 uniform random floats
rng.random((3, 4))             # 3x4 array of uniform random floats

# Normal (Gaussian) distribution
rng.normal(loc=0, scale=1, size=5)     # mean=0, std=1, 5 samples
rng.normal(loc=100, scale=15, size=1000)  # 1000 samples, mean=100, std=15

# Random integers
rng.integers(low=0, high=10, size=5)   # [3, 7, 1, 9, 4] — 5 random ints in [0, 10)

# Shuffle and sample
arr = np.arange(10)
rng.shuffle(arr)               # shuffles in-place
sample = rng.choice(arr, size=3, replace=False)  # pick 3 without replacement

# Set seed for reproducibility
np.random.seed(42)             # legacy API — global seed
```

**Why it exists:** ML relies on randomness — initializing weights, shuffling data, splitting train/test, sampling mini-batches, adding noise for data augmentation. You need controlled, reproducible randomness. The `seed` makes it reproducible: same seed → same random numbers → same results every run.

**Where it's used:**
- Train/test splits — random shuffling before splitting.
- Weight initialization in neural networks — random starting weights.
- Data augmentation — random rotations, noise, crops.
- Stochastic Gradient Descent — random mini-batch sampling.
- Monte Carlo simulations — sampling from distributions.
- Creating synthetic datasets for testing.

**What goes wrong without it:**
- No seed set → different results every run → can't debug, can't reproduce, can't compare models fairly.
- Using `np.random.seed()` (global) in a library → affects all code that uses numpy random → unpredictable side effects in other parts of the program.
- `rng.integers(high=10)` includes 0 but excludes 10 → off-by-one if you expected 10 to be possible.
- `rng.shuffle()` modifies in-place → if you still need the original order, you've lost it → use `rng.permutation()` instead for a copy.
- Not using `replace=False` in `choice` → you can sample the same element twice → duplicated data points.

---

## Array Concatenation and Stacking

**What:**
NumPy lets you combine arrays along existing or new axes. `concatenate` joins along an existing axis. `vstack` and `hstack` are convenience wrappers. `stack` creates a new axis.

```python
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Stack along new axis
np.stack([a, b])           # shape (2, 3): [[1,2,3], [4,5,6]]
np.stack([a, b], axis=1)   # shape (3, 2): [[1,4], [2,5], [3,6]]

# Vertical stack (stack rows)
np.vstack([a, b])          # shape (2, 3): [[1,2,3], [4,5,6]]

# Horizontal stack (stack columns)
np.hstack([a, b])          # shape (6,): [1,2,3,4,5,6]

# Concatenate along existing axis (for 2D)
m1 = np.array([[1, 2], [3, 4]])
m2 = np.array([[5, 6]])
np.concatenate([m1, m2], axis=0)  # shape (3, 2) — add row
np.concatenate([m1, m2.T], axis=1)  # shape (2, 3) — add column
```

**Why it exists:** You constantly need to combine data — adding new features (columns), adding new samples (rows), combining predictions from multiple models, or building batch arrays from individual samples.

**Where it's used:**
- Adding a bias column: `np.hstack([X, np.ones((n, 1))])`.
- Combining train and validation sets after tuning: `np.vstack([X_train, X_val])`.
- Building feature matrices: `np.stack([feat1, feat2, feat3], axis=1)`.
- Mini-batch construction: stacking individual samples into a batch.

**What goes wrong without it:**
- `np.concatenate([a, b])` on 1D arrays → joins them into a longer 1D array when you wanted a 2D stack → wrong shape → downstream errors.
- Dimension mismatch → `ValueError: all the input array dimensions for the concat axis must match exactly` → one array has 3 columns, the other has 4 → crash.
- Using `vstack` on 2D arrays with different column counts → error. You must ensure matching dimensions on the non-stacked axis.
- Confusing `stack` (new axis) vs `concatenate` (existing axis) → `np.stack` on two (3,) arrays gives (2,3), `np.concatenate` gives (6,) → very different results.

---

## Linear Algebra Operations

**What:**
NumPy's `linalg` module provides matrix operations: dot product, matrix multiplication, inverse, determinant, eigenvalues, and solving linear systems.

```python
import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Dot product / matrix multiplication
A @ B              # [[19, 22], [43, 50]] — matrix multiply (Python 3.5+)
A.dot(B)           # same thing
np.matmul(A, B)    # same thing

# Vector dot product
v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])
v1 @ v2            # 32 — dot product (scalar)

# Transpose
A.T                # [[1, 3], [2, 4]]

# Inverse
np.linalg.inv(A)   # [[-2, 1], [1.5, -0.5]]

# Determinant
np.linalg.det(A)   # -2.0

# Solve linear system Ax = b
b = np.array([5, 11])
x = np.linalg.solve(A, b)  # [1., 2.] — solves A @ x = b

# Eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)
```

**Why it exists:** Linear algebra is the mathematical foundation of ML. Linear regression is solving a matrix equation. PCA is eigenvalue decomposition. Neural network forward passes are chains of matrix multiplications. NumPy makes these operations fast and correct.

**Where it's used:**
- Linear regression: `weights = np.linalg.inv(X.T @ X) @ X.T @ y` (normal equation).
- PCA: eigenvalue decomposition of the covariance matrix.
- Neural networks: `output = X @ W + b` — every layer is a matrix multiply.
- Distance computation: `np.sqrt(((a - b) ** 2).sum())` — Euclidean distance.
- Image transformations: rotation and scaling matrices.

**What goes wrong without it:**
- Using `*` instead of `@` → element-wise multiplication instead of matrix multiplication → completely wrong results, no error.
- Inverting a singular (non-invertible) matrix → `LinAlgError: Singular matrix` → crash. This happens when features are collinear (perfectly correlated).
- Shape mismatch in `@` → `ValueError: matmul: Input operand 1 has a mismatch` → inner dimensions don't match (e.g., (2,3) @ (2,3) fails, need (2,3) @ (3,2)).
- Computing inverse numerically on ill-conditioned matrices → huge numerical errors → garbage weights → use `np.linalg.solve()` instead of `inv()` for stability.
