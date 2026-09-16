# Level 07 — Concepts Reference

## Easy

### K-Means
- `KMeans(n_clusters=3, n_init=10)` → `.labels_`, `.cluster_centers_`
- Iterates: assign → update centers → repeat

### Elbow Method
- Plot inertia vs K; the "elbow" is the sweet spot
- Inertia drops fast until true K, then barely improves

### PCA
- `PCA(n_components=2)` — project to 2D for visualization
- `explained_variance_ratio_` — info kept per component

## Medium

### Silhouette Score
- `silhouette_score(X, labels)` — 1 = perfect separation
- Try K=2..7, pick the max — numeric alternative to elbow

### DBSCAN
- Density-based: no assumed shape, finds outliers as noise (-1)
- `eps` = neighborhood radius; `min_samples` = min cluster size
- Beats K-Means on crescents, rings, irregular shapes

### Hierarchical Clustering
- `AgglomerativeClustering(n_clusters=3)` — bottom-up merging
- Produces a dendrogram showing merge order

## Hard

### Customer Segmentation
- Scale → cluster → `groupby('cluster').mean()` → interpret segments
- Business value: target each segment differently

### Isolation Forest
- `IsolationForest(contamination=0.1)` — flags anomalies as -1
- Anomalies are easy to isolate in random split trees

### Topic Modeling
- `TfidfVectorizer` → `NMF(n_components=2)` → top words per topic
- Discovers themes in documents without labels
