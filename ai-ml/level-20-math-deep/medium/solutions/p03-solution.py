"""Level 20 — Deep Math for ML — Medium P03 Solution"""

import numpy as np


def svd_compress(A, k):
    U, S, Vt = np.linalg.svd(A, full_matrices=False)
    A_hat = U[:, :k] @ np.diag(S[:k]) @ Vt[:k, :]
    m, n = A.shape
    ratio = k * (m + n + 1) / (m * n)
    return A_hat, ratio


if __name__ == "__main__":
    np.random.seed(42)
    A = np.random.randn(10, 8)
    A_hat, ratio = svd_compress(A, 3)
    print(A_hat.shape, ratio)
    print("recon error:", np.linalg.norm(A - A_hat))
