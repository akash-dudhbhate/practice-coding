# Level 07 — Unsupervised Learning

## What You'll Learn
- K-Means clustering — group unlabeled data
- Elbow method and silhouette score — pick the right K
- PCA for dimensionality reduction and visualization
- DBSCAN — non-spherical clusters
- Hierarchical clustering
- Customer segmentation, anomaly detection, topic modeling

## Prerequisites
- Level 06 (feature engineering)

## Problems

### Easy
1. `easy/p01-kmeans.py` — `cluster()` → K-Means on blobs
2. `easy/p02-elbow-method.py` — `elbow()` → inertia vs K
3. `easy/p03-pca-intro.py` — `pca_2d()` → iris 4D → 2D

### Medium
4. `medium/p01-silhouette.py` — `best_k()` → silhouette scoring
5. `medium/p02-dbscan.py` — `compare_algorithms()` → KMeans vs DBSCAN
6. `medium/p03-hierarchical.py` — `hierarchical()` → agglomerative

### Hard
7. `hard/p01-customer-segmentation.py` — `segment()` → business clusters
8. `hard/p02-anomaly-detection.py` — `detect_anomalies()` → IsolationForest
9. `hard/p03-topic-modeling.py` — `topics()` → NMF on documents

### Project
`project/` — Segment real customer data and profile each segment.

## Verify

```bash
python3 check.py easy/p01
python3 check.py all
```
