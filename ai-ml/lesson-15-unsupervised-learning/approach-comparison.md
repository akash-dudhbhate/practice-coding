# Lesson 15 — Approach Comparison

## Problem: Find Optimal Clusters

### Approach 1: Elbow method
```python
inertias = [KMeans(k).fit(X).inertia_ for k in range(1, 10)]
# Plot and find elbow
```

### Approach 2: Silhouette score
```python
scores = [silhouette_score(X, KMeans(k).fit_predict(X)) for k in range(2, 10)]
# Pick k with highest score
```

**Winner:** Approach 2 — quantitative, no visual judgment needed.

---

## Problem: Dimensionality Reduction

### Approach 1: PCA
```python
PCA(n_components=2)
```

### Approach 2: t-SNE
```python
from sklearn.manifold import TSNE
TSNE(n_components=2)
```

**Winner:** PCA for preprocessing (preserves variance). t-SNE for visualization (preserves local structure).
