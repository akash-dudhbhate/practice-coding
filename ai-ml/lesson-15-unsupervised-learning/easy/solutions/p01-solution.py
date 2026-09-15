"""
K-Means Clustering on make_blobs
=================================
Generate 3 clusters with make_blobs, run K-Means with K=3, plot the clusters,
and print the cluster centers.
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

np.random.seed(42)


if __name__ == "__main__":
    # Generate 3 clusters
    X, y_true = make_blobs(n_samples=300, centers=3, cluster_std=1.0, random_state=42)

    # K-Means with K=3
    kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
    labels = kmeans.fit_predict(X)

    print("=== K-Means (K=3) ===")
    print(f"Cluster centers:\n{kmeans.cluster_centers_}")
    print(f"\nCluster assignments (first 20): {labels[:20]}")
    print(f"Inertia (within-cluster SSE): {kmeans.inertia_:.2f}")

    # Plot
    plt.figure(figsize=(8, 6))
    plt.scatter(X[:, 0], X[:, 1], c=labels, cmap="viridis", s=30, alpha=0.7, edgecolors="k")
    plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1],
                c="red", marker="X", s=200, label="Centroids", edgecolors="k")
    plt.xlabel("Feature 1")
    plt.ylabel("Feature 2")
    plt.title("K-Means Clustering (K=3)")
    plt.legend()
    plt.tight_layout()
    plt.savefig("kmeans_clusters.png", dpi=150)
    print("\nPlot saved to kmeans_clusters.png")
