# Lesson 15 — Easy P02: PCA on high-dimensional data
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# Create high-dimensional dataset (20 features)
X, y = make_classification(n_samples=500, n_features=20, n_informative=10, random_state=42)

# Standardize before PCA
X_scaled = StandardScaler().fit_transform(X)

# Reduce to 2 components
pca = PCA(n_components=2, random_state=42)
X_pca = pca.fit_transform(X_scaled)

print("Explained variance ratio:", pca.explained_variance_ratio_)
print("Total explained variance:", sum(pca.explained_variance_ratio_))

# Plot 2D projection
plt.figure(figsize=(8, 6))
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y, cmap="coolwarm", alpha=0.6, edgecolors="k")
plt.xlabel(f"PC1 ({pca.explained_variance_ratio_[0]:.2%})")
plt.ylabel(f"PC2 ({pca.explained_variance_ratio_[1]:.2%})")
plt.title("PCA: 20D → 2D Projection")
plt.colorbar(label="Class")
plt.tight_layout()
plt.savefig("pca_projection.png", dpi=150)
print("Figure saved to pca_projection.png")
