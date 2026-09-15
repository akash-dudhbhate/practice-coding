# Lesson 15 — Hard P01: Customer segmentation pipeline
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score

# Create synthetic customer data
np.random.seed(42)
n = 300
data = pd.DataFrame({
    "age": np.random.randint(18, 70, n),
    "income": np.random.randn(n) * 20000 + 60000,
    "spending_score": np.random.uniform(1, 100, n),
})

# Scale features
X = StandardScaler().fit_transform(data)

# Find optimal K with elbow + silhouette
k_range = range(2, 11)
inertias = [KMeans(k, random_state=42, n_init=10).fit(X).inertia_ for k in k_range]
sil_scores = [silhouette_score(X, KMeans(k, random_state=42, n_init=10).fit_predict(X)) for k in k_range]
best_k = list(k_range)[np.argmax(sil_scores)]
print(f"Optimal K (silhouette): {best_k}")

# Apply K-Means with optimal K
km = KMeans(n_clusters=best_k, random_state=42, n_init=10)
labels = km.fit_predict(X)
data["cluster"] = labels

# Visualize with PCA (2D)
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

plt.figure(figsize=(10, 7))
for c in range(best_k):
    mask = labels == c
    plt.scatter(X_pca[mask, 0], X_pca[mask, 1], label=f"Cluster {c}", alpha=0.7, edgecolors="k")
plt.xlabel(f"PC1 ({pca.explained_variance_ratio_[0]:.2%})")
plt.ylabel(f"PC2 ({pca.explained_variance_ratio_[1]:.2%})")
plt.title("Customer Segmentation (PCA 2D)")
plt.legend()
plt.tight_layout()
plt.savefig("customer_segmentation.png", dpi=150)
print("Figure saved to customer_segmentation.png")

# Interpret each cluster
print("\n=== Cluster Interpretation ===")
for c in range(best_k):
    cluster_data = data[data["cluster"] == c]
    print(f"\nCluster {c} ({len(cluster_data)} customers):")
    print(f"  Avg Age: {cluster_data['age'].mean():.1f}")
    print(f"  Avg Income: ${cluster_data['income'].mean():,.0f}")
    print(f"  Avg Spending Score: {cluster_data['spending_score'].mean():.1f}")
