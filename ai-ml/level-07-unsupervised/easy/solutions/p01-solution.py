"""Level 07 Unsupervised — Easy P01 Solution"""

import numpy as np
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

def solve():
    X, _ = make_blobs(n_samples=200, centers=3, random_state=42)
    kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
    labels = kmeans.fit_predict(X)
    print(f"Cluster centers:\n{kmeans.cluster_centers_}")
    print(f"Labels (first 10): {labels[:10]}")
    plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis')
    plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1],
                c='red', marker='X', s=200, label='Centers')
    plt.legend()
    plt.savefig('kmeans.png', dpi=150, bbox_inches='tight')
    plt.show()
    return labels, kmeans.cluster_centers_

if __name__ == "__main__":
    solve()