"""Level 07 Unsupervised — Medium P01 Solution"""

import numpy as np
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
from sklearn.metrics import silhouette_score

def solve():
    X, _ = make_blobs(n_samples=200, centers=3, random_state=42)
    best_k = 2
    best_score = -1
    for k in range(2, 8):
        kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
        labels = kmeans.fit_predict(X)
        score = silhouette_score(X, labels)
        print(f"K={k}: silhouette={score:.4f}")
        if score > best_score:
            best_score = score
            best_k = k
    print(f"Best K: {best_k} (silhouette={best_score:.4f})")
    return best_k, best_score

if __name__ == "__main__":
    solve()