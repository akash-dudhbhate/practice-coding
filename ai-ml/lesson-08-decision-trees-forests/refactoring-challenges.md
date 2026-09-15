# Lesson 08 — Refactoring Challenges

## Refactor 01 (Easy): Single Tree for Complex Data
### Before
```python
model = DecisionTreeClassifier().fit(X, y)  # overfits
```
### After
```python
model = RandomForestClassifier().fit(X, y)  # reduces overfit
```

## Refactor 02 (Medium): No Max Depth
### Before
```python
model = DecisionTreeClassifier().fit(X, y)  # grows until pure leaves
```
### After
```python
model = DecisionTreeClassifier(max_depth=5, min_samples_leaf=10).fit(X, y)
```

## Refactor 03 (Hard): Manual Ensemble
### Before
```python
trees = [DecisionTreeClassifier().fit(X_sample, y_sample) for _ in range(100)]
preds = np.mean([t.predict(X_test) for t in trees], axis=0)
```
### After
```python
model = RandomForestClassifier(n_estimators=100).fit(X, y)
preds = model.predict(X_test)
```
