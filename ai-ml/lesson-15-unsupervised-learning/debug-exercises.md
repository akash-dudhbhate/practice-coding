# Lesson 15 — Debug Exercises

## Debug 01 (Easy: Not Scaling Before K-Means
```python
kmeans = KMeans(n_clusters=3)
kmeans.fit(X)  # unscaled
```
<details><summary>Answer</summary>
**Bug:** K-means uses distances — unscaled features dominate.
**Fix:** Scale first: `StandardScaler().fit_transform(X)`.
</details>

## Debug 02 (Medium: Wrong Number of Clusters
```python
kmeans = KMeans(n_clusters=10)  # chosen arbitrarily
```
<details><summary>Answer</summary>
**Bug:** No method used to determine optimal k.
**Fix:** Use elbow method or silhouette score to find optimal k.
</details>

## Debug 03 (Hard: Not Setting random_state
```python
kmeans = KMeans(n_clusters=3)
# different results each run
```
<details><summary>Answer</summary>
**Bug:** K-means is sensitive to initialization. Different runs give different clusters.
**Fix:** `KMeans(n_clusters=3, random_state=42)`.
</details>
