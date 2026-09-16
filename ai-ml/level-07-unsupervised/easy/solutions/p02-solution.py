"""Level 07 Unsupervised — Easy P02 Solution"""

import numpy as np
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

def solve():
    X, _ = make_blobs(n_samples=200, centers=3, random_state=42)
    inertias = []
    K_range = range(1, 11)
    for k in K_range:
        kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
        kmeans.fit(X)
        inertias.append(kmeans.inertia_)
    plt.plot(K_range, inertias, 'bo-')
    plt.xlabel('Number of Clusters (K)')
    plt.ylabel('Inertia')
    plt.title('Elbow Method')
    plt.savefig('elbow.png', dpi=150, bbox_inches='tight')
    plt.show()
    print(f"Inertias: {inertias}")
    return inertias

if __name__ == "__main__":
    solve()