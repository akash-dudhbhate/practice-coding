# Lesson 13 — Refactoring Challenges

## Refactor 01 (Easy): KNN Without Scaling
### Before
```python
model = KNeighborsClassifier().fit(X, y)  # distance-based, needs scaling
```
### After
```python
model = make_pipeline(StandardScaler(), KNeighborsClassifier()).fit(X, y)
```

## Refactor 02 (Medium): Manual K Selection
### Before
```python
for k in range(1, 20):
    model = KNeighborsClassifier(n_neighbors=k).fit(X_train, y_train)
    print(k, model.score(X_test, y_test))
```
### After
```python
gs = GridSearchCV(KNeighborsClassifier(), {"n_neighbors": range(1, 20)}, cv=5)
gs.fit(X, y)
```

## Refactor 03 (Hard): SVM Without Pipeline
### Before
```python
X_scaled = StandardScaler().fit_transform(X)
model = SVC().fit(X_scaled, y)
X_test_scaled = scaler.transform(X_test)
preds = model.predict(X_test_scaled)
```
### After
```python
pipe = make_pipeline(StandardScaler(), SVC()).fit(X, y)
preds = pipe.predict(X_test)
```
