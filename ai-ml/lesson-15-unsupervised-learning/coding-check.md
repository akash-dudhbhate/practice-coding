# Lesson 15 — Coding Check

## Easy

### p01-solve.py — K-Means on blobs
- [ ] `make_blobs` with 3 clusters used
- [ ] Data scaled
- [ ] K-Means with K=3 trained
- [ ] Clusters plotted with different colors
- [ ] Cluster centers printed
- [ ] Centers are at the blob centers

### p02-solve.py — PCA visualization
- [ ] High-dimensional dataset created (20 features)
- [ ] Data scaled
- [ ] PCA with 2 components applied
- [ ] 2D projection plotted
- [ ] Explained variance ratio printed
- [ ] Total explained variance > 50%

### p03-solve.py — Isolation Forest
- [ ] Dataset with injected outliers created
- [ ] `IsolationForest` trained
- [ ] Outliers identified (-1)
- [ ] Normal vs outlier points visualized
- [ ] Injected outliers are detected

## Medium

### p01-solve.py — Elbow + silhouette
- [ ] K=1 to 10 tested
- [ ] Inertia vs K plotted (elbow method)
- [ ] Elbow identified
- [ ] Silhouette score for K=2 to 10 calculated
- [ ] Silhouette vs K plotted
- [ ] Both methods compared
- [ ] Optimal K identified

### p02-solve.py — K-Means vs DBSCAN
- [ ] `make_moons` dataset created
- [ ] K-Means applied and plotted
- [ ] DBSCAN applied and plotted
- [ ] K-Means fails (spherical clusters on moon data)
- [ ] DBSCAN succeeds (follows the moon shape)
- [ ] Comparison clear

### p03-solve.py — Hierarchical clustering
- [ ] Small dataset created
- [ ] Dendrogram plotted
- [ ] Cut at a level for 3 clusters
- [ ] Hierarchical clusters visualized
- [ ] K-Means clusters also computed
- [ ] Both compared (visual or adjusted Rand index)

## Hard

### p01-solve.py — Customer segmentation
- [ ] Synthetic customer data created (age, income, spending)
- [ ] Data scaled
- [ ] Elbow method applied
- [ ] Silhouette score calculated
- [ ] Optimal K chosen
- [ ] K-Means applied
- [ ] PCA used for 2D visualization
- [ ] Clusters plotted
- [ ] Each cluster interpreted (e.g., "young high-spenders")
- [ ] Business interpretation provided

### p02-solve.py — Anomaly detection comparison
- [ ] Dataset with 5% anomalies created
- [ ] Isolation Forest applied
- [ ] DBSCAN applied (noise = anomalies)
- [ ] Local Outlier Factor applied
- [ ] For each: anomalies detected
- [ ] Detection rate calculated (if ground truth)
- [ ] Results visualized
- [ ] Comparison table created
- [ ] Best method identified

### p03-solve.py — Complete clustering analysis
- [ ] Real dataset loaded (Iris without labels)
- [ ] K-Means applied
- [ ] DBSCAN applied
- [ ] Hierarchical clustering applied
- [ ] Silhouette score for each
- [ ] PCA visualization for each
- [ ] Adjusted Rand index (vs true labels)
- [ ] Comparison table created
- [ ] Best clustering method identified
- [ ] Results interpreted
