"""Level 07 Unsupervised — Medium P03 Solution"""

import numpy as np
from sklearn.cluster import AgglomerativeClustering
from sklearn.datasets import make_blobs
from scipy.cluster.hierarchy import dendrogram, linkage
import matplotlib.pyplot as plt

def solve():
    X, _ = make_blobs(n_samples=50, centers=3, random_state=42)
    # Dendrogram
    linked = linkage(X, method='ward')
    plt.figure(figsize=(10, 6))
    dendrogram(linked)
    plt.title('Hierarchical Clustering Dendrogram')
    plt.xlabel('Sample Index')
    plt.ylabel('Distance')
    plt.savefig('dendrogram.png', dpi=150, bbox_inches='tight')
    plt.show()
    # Clustering
    hc = AgglomerativeClustering(n_clusters=3)
    labels = hc.fit_predict(X)
    print(f"Cluster labels: {labels}")
    return labels

if __name__ == "__main__":
    solve()