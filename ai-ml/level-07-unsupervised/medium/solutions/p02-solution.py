"""Level 07 Unsupervised — Medium P02 Solution"""

import numpy as np
from sklearn.cluster import KMeans, DBSCAN
from sklearn.datasets import make_moons
import matplotlib.pyplot as plt

def solve():
    X, _ = make_moons(n_samples=200, noise=0.05, random_state=42)
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    # K-Means
    kmeans = KMeans(n_clusters=2, random_state=42, n_init=10)
    labels_km = kmeans.fit_predict(X)
    axes[0].scatter(X[:, 0], X[:, 1], c=labels_km, cmap='viridis')
    axes[0].set_title('K-Means')
    # DBSCAN
    dbscan = DBSCAN(eps=0.3, min_samples=5)
    labels_db = dbscan.fit_predict(X)
    axes[1].scatter(X[:, 0], X[:, 1], c=labels_db, cmap='viridis')
    axes[1].set_title('DBSCAN')
    plt.savefig('kmeans_vs_dbscan.png', dpi=150, bbox_inches='tight')
    plt.show()
    print("K-Means fails on non-spherical data, DBSCAN succeeds")
    return labels_km, labels_db

if __name__ == "__main__":
    solve()