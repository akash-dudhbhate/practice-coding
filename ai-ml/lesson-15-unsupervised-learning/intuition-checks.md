# Lesson 15 — Intuition Checks

## Check 01: Supervised vs unsupervised
<details><summary>Answer</summary>
Supervised — labeled data, predict target. Unsupervised — no labels, find structure. Clustering (group similar), dimensionality reduction (compress), anomaly detection (find outliers).
</details>

## Check 02: K-means
How does K-means work?
<details><summary>Answer</summary>
1. Choose k random centroids. 2. Assign each point to nearest centroid. 3. Move centroid to mean of assigned points. 4. Repeat 2-3 until convergence. Minimizes within-cluster variance.
</details>

## Check 03: Elbow method
```python
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k).fit(X)
    print(k, kmeans.inertia_)
# Plot — look for "elbow" where inertia stops decreasing rapidly
```
<details><summary>Answer</summary>
Inertia = sum of squared distances to centroids. Decreases as k increases. Elbow point = optimal k (diminishing returns after).
</details>

## Check 04: PCA
```python
pca = PCA(n_components=2)
X_2d = pca.fit_transform(X)
```
<details><summary>Answer</summary>
Principal Component Analysis — projects data onto directions of maximum variance. Reduces dimensions while preserving information. `explained_variance_ratio_` shows how much variance each component captures.
</details>

## Check 05: Silhouette score
```python
silhouette_score(X, labels)
```
<details><summary>Answer</summary>
Measures cluster quality. Range -1 to 1. 1 = well clustered, 0 = overlapping, -1 = misclassified. Better than inertia for choosing k.
</details>
