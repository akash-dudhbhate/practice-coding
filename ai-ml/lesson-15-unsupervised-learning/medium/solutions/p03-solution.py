# Lesson 15 — Medium P03: Hierarchical clustering with dendrogram
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import AgglomerativeClustering, KMeans
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.preprocessing import StandardScaler

# Generate small dataset
X, _ = make_blobs(n_samples=30, centers=3, random_state=42, cluster_std=1.5)
X = StandardScaler().fit_transform(X)

# Compute linkage matrix for dendrogram
Z = linkage(X, method="ward")

# Plot dendrogram
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

dendrogram(Z, ax=ax1, color_threshold=5)
ax1.set_title("Dendrogram")
ax1.set_xlabel("Sample Index")
ax1.set_ylabel("Distance")
ax1.axhline(y=5, color="red", linestyle="--", label="Cut at 3 clusters")
ax1.legend()

# Cut at a level to get 3 clusters
hc = AgglomerativeClustering(n_clusters=3, linkage="ward")
hc_labels = hc.fit_predict(X)

# K-Means for comparison
km = KMeans(n_clusters=3, random_state=42, n_init=10)
km_labels = km.fit_predict(X)

ax2.scatter(X[:, 0], X[:, 1], c=hc_labels, cmap="Set1", edgecolors="k", s=80)
ax2.set_title("Hierarchical Clustering (3 clusters)")
ax2.set_xlabel("Feature 1")
ax2.set_ylabel("Feature 2")

plt.tight_layout()
plt.savefig("hierarchical_clustering.png", dpi=150)
print("Figure saved to hierarchical_clustering.png")

# Compare with K-Means
agreement = np.mean(hc_labels == km_labels)
print(f"\nCluster label agreement with K-Means: {agreement:.2%}")
print("(Note: labels may differ due to ordering, but cluster assignments should be similar.)")
print("\nBoth methods identify 3 clusters. Hierarchical clustering provides a")
print("dendrogram showing the full hierarchy of merges, useful for understanding")
print("cluster structure at different levels of granularity.")
