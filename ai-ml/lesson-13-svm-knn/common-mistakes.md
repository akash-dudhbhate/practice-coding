# Lesson 13 — Common Mistakes

## Mistake 01: Not scaling for distance-based models
```python
# WRONG — SVM/KNN need scaling
SVC().fit(X_train, y_train)
# CORRECT
Pipeline([("scaler", StandardScaler()), ("svm", SVC())])
```

## Mistake 02: KNN with k=1
```python
# WRONG — overfits
KNeighborsClassifier(n_neighbors=1)
# CORRECT
KNeighborsClassifier(n_neighbors=5)
```

## Mistake 03: Not tuning SVM parameters
```python
# Tune C and gamma
GridSearchCV(SVC(), {"C": [0.1, 1, 10], "gamma": ["scale", "auto", 0.1]})
```

## Mistake 04: Using KNN on large datasets
```python
# KNN is slow at prediction (compares to all training points)
# Use for small/medium datasets
# For large data, use approximate NN (annoy, faiss)
```

## Mistake 05: Not trying different kernels
```python
# Start with rbf (default)
# Try linear for high-dimensional data
# Try poly for specific non-linear patterns
```
