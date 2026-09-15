# Lesson 15 — Unsupervised Learning

## What you'll learn
- What unsupervised learning is (no labels)
- K-Means clustering (partitioning into K clusters)
- Choosing K (elbow method, silhouette score)
- Silhouette score (clustering quality)
- DBSCAN (density-based clustering, noise detection)
- Hierarchical clustering (dendrograms)
- PCA (dimensionality reduction)
- Anomaly detection (Isolation Forest)

## Lesson

### K-Means
```python
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
clusters = kmeans.fit_predict(X_scaled)
```

### PCA
```python
from sklearn.decomposition import PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)
```

### Anomaly detection
```python
from sklearn.ensemble import IsolationForest
iso = IsolationForest(contamination=0.05)
outliers = iso.fit_predict(X)
```

---

## Your Tasks

### Easy
1. `easy/p01-solve.py` — Generate synthetic data with 3 clusters (`make_blobs`). Apply K-Means with K=3. Plot the clusters with different colors. Print the cluster centers.
2. `easy/p02-solve.py` — Apply PCA to a high-dimensional dataset (`make_classification` with 20 features). Reduce to 2 components. Plot the 2D projection. Print explained variance ratio.
3. `easy/p03-solve.py` — Use `IsolationForest` on a dataset with injected outliers. Print which points are outliers (-1). Visualize normal vs outlier points.

### Medium
4. `medium/p01-solve.py` — Use the elbow method: run K-Means with K=1 to 10. Plot inertia vs K. Identify the elbow. Then use silhouette score for K=2 to 10. Compare both methods.
5. `medium/p02-solve.py` — Compare K-Means and DBSCAN on non-spherical data (`make_moons`). Plot both clusterings. Show that K-Means fails (spherical assumption) but DBSCAN succeeds.
6. `medium/p03-solve.py` — Apply hierarchical clustering to a small dataset. Plot the dendrogram. Cut at a level to get 3 clusters. Compare with K-Means clusters.

### Hard
7. `hard/p01-solve.py` — Build a customer segmentation pipeline: create synthetic customer data (age, income, spending score), scale, find optimal K with elbow + silhouette, apply K-Means, visualize clusters with PCA (2D), and interpret each cluster (e.g., "young high-spenders").
8. `hard/p02-solve.py` — Build an anomaly detection pipeline: create a dataset with 5% anomalies, compare Isolation Forest, DBSCAN, and Local Outlier Factor. For each: detect anomalies, calculate detection rate (if ground truth known), and visualize. Create a comparison table.
9. `hard/p03-solve.py` — Build a complete clustering analysis: load a real dataset (e.g., Iris without labels), apply 3 clustering methods (K-Means, DBSCAN, Hierarchical), evaluate each with silhouette score, visualize with PCA, and compare results. Since Iris has true labels, also compare with actual species (adjusted Rand index).

### How to work
- Write your complete Python solution.
- Remove the TODO comment when done.
- Test with `python <filename>`.
