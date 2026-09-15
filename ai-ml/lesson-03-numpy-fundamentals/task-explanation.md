# Lesson 03 — NumPy Fundamentals

## What you'll learn
- How to create and manipulate NumPy arrays (the backbone of all ML in Python).
- How to use indexing, slicing, and boolean masks to select data.
- How broadcasting lets you operate on arrays of different shapes.
- How vectorized operations replace slow Python loops.
- How to use linear algebra operations for ML math.

## Lesson

### Why NumPy?
Python lists are slow for math. NumPy arrays store data in contiguous memory and run operations in optimized C code — 10-100x faster. Every ML library (sklearn, PyTorch, TensorFlow) is built on top of array-like structures.

### The key ideas
- **Array**: a grid of same-type values. Shape tells you the dimensions.
- **Reshaping**: change the shape without changing the data. Critical for matching what ML APIs expect.
- **Indexing**: select elements, rows, columns, or filtered subsets — no loops needed.
- **Broadcasting**: operate on arrays of different shapes by "stretching" the smaller one.
- **Vectorization**: apply operations to entire arrays at once — no Python loops.
- **Random**: controlled, reproducible randomness with seeds.

### Shape conventions in ML
```
X = (n_samples, n_features)    — feature matrix, always 2D
y = (n_samples,)               — labels, usually 1D
single sample = (1, n_features) — must be 2D for sklearn
image = (height, width, channels) — 3D for color images
```

---

## Your Tasks

This lesson has **9 practice problems** across three difficulty levels. Start with `easy/` and work your way up. Write your complete solution from scratch in each file.

### Easy (start here)
1. `easy/p01-solve.py` — **Create and inspect arrays**: Create a 4×5 array of random integers (0-100) with a fixed seed. Print its shape, dtype, ndim, size, and the mean of each column. Return the array and the column means.
2. `easy/p02-solve.py` — **Indexing and slicing**: Given a 5×5 matrix, extract: the center 3×3 submatrix, the last row, the first column, and all elements greater than 10. Return each as a separate array.
3. `easy/p03-solve.py` — **Reshape and transpose**: Given a 1D array of 24 elements, reshape it to (2, 3, 4), then transpose to (4, 3, 2), then flatten back to 1D. Return all three arrays and verify the flattened version matches the original.

### Medium
4. `medium/p01-solve.py` — **Broadcasting operations**: Given a 2D array of student scores (rows=students, cols=subjects), use broadcasting to: subtract the mean of each subject (column) from every score, then divide by the std of each subject. Return the standardized scores (shape unchanged, each column has mean≈0, std≈1).
5. `medium/p02-solve.py` — **Vectorized computation vs loop**: Implement Euclidean distance between two 1D arrays two ways: (a) with a Python for-loop, (b) with vectorized NumPy. Time both on arrays of size 1,000,000 and return both the distance and the speedup ratio.
6. `medium/p03-solve.py` — **Boolean masking and conditional replacement**: Given a 2D array, replace all negative values with 0, replace all values above 100 with 100 (clipping), and count how many values were changed in each operation. Return the clipped array and both counts.

### Hard
7. `hard/p01-solve.py` — **Linear regression with NumPy**: Implement linear regression from scratch using the normal equation: `w = (X^T X)^{-1} X^T y`. Add a bias column (column of 1s) to X. Fit on synthetic data, predict, and compute MSE. Return the weights, predictions, and MSE.
8. `hard/p02-solve.py` — **Pairwise distance matrix**: Given a 2D array of N points (shape N×D), compute the full N×N pairwise Euclidean distance matrix using ONLY broadcasting and vectorized ops (no loops). Return the distance matrix. Verify diagonal is all zeros.
9. `hard/p03-solve.py` — **Mini-batch generator**: Write a function that takes a feature matrix X, labels y, batch_size, and shuffle=True. If shuffle, randomly permute the data (with a seed for reproducibility). Yield mini-batches of (X_batch, y_batch) as a generator. Demonstrate by iterating through a 1000-sample dataset with batch_size=128 and printing each batch's shape.

### How to work
- Open a problem file, read the problem description in the docstring header.
- Write your complete solution from scratch (function signature + body).
- Remove the TODO line when done.
- Run `python <filename>` to test your solution.
- When done, tell me and I'll review. Say **"give me next task"** to advance.
