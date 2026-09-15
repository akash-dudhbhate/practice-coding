# Lesson 15 — Hard P03: Complete clustering analysis on Iris
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans, DBSCAN, AgglomerativeClustering
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score, adjusted_rand_score

# Load Iris (without labels for clustering)
iris = load_iris()
X = iris.data
y_true = iris.target
feature_names = iris.feature_names

X_scaled = StandardScaler().fit_transform(X)

# Apply 3 clustering methods
# 1. K-Means (K=3)
km = KMeans(n_clusters=3, random_state=42, n_init=10)
km_labels = km.fit_predict(X_scaled)

# 2. DBSCAN
db = DBSCAN(eps=0.8, min_samples=5)
db_labels = db.fit_predict(X_scaled)

# 3. Hierarchical
hc = AgglomerativeClustering(n_clusters=3, linkage="ward")
hc_labels = hc.fit_predict(X_scaled)

# Evaluate with silhouette score
methods = {"K-Means": km_labels, "DBSCAN": db_labels, "Hierarchical": hc_labels}
results = []
for name, labels in methods.items():
    # Skip noise points for silhouette
    mask = labels != -1
    if mask.sum() > 1 and len(set(labels[mask])) > 1:
        # Note: silhouette_score does not accept random_state — SonarQube false positive
        sil = silhouette_score(X_scaled[mask], labels[mask])
    else:
        sil = -1
    ari = adjusted_rand_score(y_true, labels)
    results.append({"Method": name, "Silhouette": sil, "Adjusted Rand Index": ari, "Clusters": len(set(labels))})

df = pd.DataFrame(results)
print("=== Clustering Comparison on Iris ===")
print(df.to_string(index=False))

# Visualize with PCA
pca = PCA(n_components=2, random_state=42)
X_pca = pca.fit_transform(X_scaled)

fig, axes = plt.subplots(1, 4, figsize=(18, 5))
for ax, labels, name in zip(axes[:3], [km_labels, db_labels, hc_labels], ["K-Means", "DBSCAN", "Hierarchical"]):
    scatter = ax.scatter(X_pca[:, 0], X_pca[:, 1], c=labels, cmap="Set1", edgecolors="k", alpha=0.7)
    ax.set_title(f"{name} (ARI={adjusted_rand_score(y_true, labels):.2f})")
    ax.set_xlabel("PC1")
    ax.set_ylabel("PC2")

# True labels for reference
axes[3].scatter(X_pca[:, 0], X_pca[:, 1], c=y_true, cmap="Set1", edgecolors="k", alpha=0.7)
axes[3].set_title("True Labels")
axes[3].set_xlabel("PC1")
axes[3].set_ylabel("PC2")

plt.tight_layout()
plt.savefig("iris_clustering.png", dpi=150)
print("\nFigure saved to iris_clustering.png")

print("\n=== Summary ===")
print("K-Means and Hierarchical perform similarly (both find 3 clusters matching species well).")
print("DBSCAN may find fewer/more clusters depending on eps, and may label some points as noise.")
print("Adjusted Rand Index shows how well clustering matches true species labels (1.0 = perfect).")
