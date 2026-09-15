"""
Lesson 03 - Medium P02
Euclidean distance: loop-based vs vectorized NumPy. Time both on 1M elements.

Solution:
  1. Generate two random vectors of 1,000,000 elements each.
  2. Compute Euclidean distance with a Python loop.
  3. Compute the same with vectorized NumPy.
  4. Time both and compare.
"""

import numpy as np
import time

# ---------------------------------------------------------------------------
# 1. Generate two large random vectors
# ---------------------------------------------------------------------------
np.random.seed(42)
N = 1_000_000
a = np.random.randn(N)
b = np.random.randn(N)

print(f"Vector size: {N:,} elements")
print()

# ---------------------------------------------------------------------------
# 2. Loop-based Euclidean distance
# ---------------------------------------------------------------------------
# Solution: Sum of squared differences, then square root. This is slow because
# the loop runs in Python, not in compiled C code.
start = time.perf_counter()
squared_sum = 0.0
for i in range(N):
    diff = a[i] - b[i]
    squared_sum += diff * diff
dist_loop = squared_sum ** 0.5
time_loop = time.perf_counter() - start

print(f"Loop-based distance:   {dist_loop:.6f}")
print(f"Loop-based time:       {time_loop:.4f} seconds")
print()

# ---------------------------------------------------------------------------
# 3. Vectorized NumPy Euclidean distance
# ---------------------------------------------------------------------------
# Solution: Use np.sqrt(np.sum((a - b) ** 2)) or np.linalg.norm(a - b).
# The entire computation runs in compiled C, making it orders of magnitude faster.
start = time.perf_counter()
dist_vectorized = np.sqrt(np.sum((a - b) ** 2))
time_vectorized = time.perf_counter() - start

print(f"Vectorized distance:   {dist_vectorized:.6f}")
print(f"Vectorized time:       {time_vectorized:.6f} seconds")
print()

# Alternative using np.linalg.norm
start = time.perf_counter()
dist_norm = np.linalg.norm(a - b)
time_norm = time.perf_counter() - start

print(f"np.linalg.norm distance: {dist_norm:.6f}")
print(f"np.linalg.norm time:     {time_norm:.6f} seconds")
print()

# ---------------------------------------------------------------------------
# 4. Compare results and speedup
# ---------------------------------------------------------------------------
print("=" * 50)
print("COMPARISON")
print("=" * 50)
print(f"  Results match: {np.isclose(dist_loop, dist_vectorized)}")
print(f"  Speedup (loop / vectorized): {time_loop / time_vectorized:.1f}x")
print()
print("  Key takeaway: Vectorized NumPy operations avoid Python-level loops")
print("  and run in optimized C code, delivering huge speedups on large data.")
