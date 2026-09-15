# Lesson 15 — Common Mistakes

## Mistake 01: Not scaling before clustering
```python
# WRONG
KMeans().fit(X)
# CORRECT
Pipeline([("scaler", StandardScaler()), ("kmeans", KMeans())])
```

## Mistake 02: Arbitrary k
```python
# WRONG — guess k
KMeans(n_clusters=5)
# CORRECT — use elbow or silhouette
for k in range(2, 10):
    score = silhouette_score(X, KMeans(k).fit_predict(X))
```

## Mistake 03: Not setting random_state
```python
KMeans(random_state=42)  # reproducible
```

## Mistake 04: Interpreting clusters as ground truth
```python
# Clusters are patterns, not necessarily meaningful categories
# Validate with domain knowledge
```

## Mistake 05: PCA without scaling
```python
# WRONG — high variance features dominate
PCA().fit(X)
# CORRECT
Pipeline([("scaler", StandardScaler()), ("pca", PCA())])
```
