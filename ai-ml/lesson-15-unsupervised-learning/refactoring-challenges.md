# Lesson 15 — Refactoring Challenges

## Refactor 01 (Easy): Manual K-Means Init
### Before
```python
centroids = X[np.random.choice(len(X), 3, replace=False)]
for _ in range(100):
    # assign, update centroids
```
### After
```python
from sklearn.cluster import KMeans
model = KMeans(n_clusters=3).fit(X)
```

## Refactor 02 (Medium): No Scaling Before Clustering
### Before
```python
model = KMeans(n_clusters=3).fit(X)  # features on different scales
```
### After
```python
model = make_pipeline(StandardScaler(), KMeans(n_clusters=3)).fit(X)
```

## Refactor 03 (Hard): Manual Elbow
### Before
```python
for k in range(1, 10):
    model = KMeans(n_clusters=k).fit(X)
    print(k, model.inertia_)
# visually find elbow
```
### After
```python
from sklearn.metrics import silhouette_score
for k in range(2, 10):
    labels = KMeans(n_clusters=k).fit_predict(X)
    print(k, silhouette_score(X, labels))
```
