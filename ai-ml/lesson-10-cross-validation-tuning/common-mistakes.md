# Lesson 10 — Common Mistakes

## Mistake 01: Data leakage in CV
```python
# WRONG — scale before CV
X_scaled = scaler.fit_transform(X)
cross_val_score(model, X_scaled, y)
# CORRECT — pipeline
pipe = Pipeline([("scaler", StandardScaler()), ("model", model)])
cross_val_score(pipe, X, y)
```

## Mistake 02: Tuning on test set
```python
# WRONG — overfits to test
for params in param_list:
    score = model.fit(X_train, y_train).score(X_test, y_test)
# CORRECT — GridSearchCV on train
GridSearchCV(model, params, cv=5).fit(X_train, y_train)
```

## Mistake 03: Not using stratified CV
```python
# WRONG — may miss minority class
cross_val_score(model, X, y, cv=5)
# CORRECT — for classification
cross_val_score(model, X, y, cv=StratifiedKFold(5))
```

## Mistake 04: Too many parameters in grid
```python
# WRONG — 1000s of combinations
GridSearchCV(model, {"a": range(100), "b": range(100)})
# CORRECT — focused search
GridSearchCV(model, {"a": [1, 10, 100], "b": [0.1, 1, 10]})
```

## Mistake 05: Not using RandomizedSearchCV for large spaces
```python
# For large param spaces, use RandomizedSearchCV
# Samples random combinations — faster than grid
```
