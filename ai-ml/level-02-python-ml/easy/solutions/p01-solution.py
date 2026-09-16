"""Level 02 — Python for ML — Easy P01 Solution"""

import numpy as np

def solve():
    np.random.seed(42)
    arr = np.random.randint(0, 100, (4, 5))
    print(f"Shape: {arr.shape}")
    print(f"Dtype: {arr.dtype}")
    print(f"Ndim: {arr.ndim}")
    print(f"Size: {arr.size}")
    print(f"Column means: {arr.mean(axis=0)}")
    return arr

if __name__ == "__main__":
    solve()