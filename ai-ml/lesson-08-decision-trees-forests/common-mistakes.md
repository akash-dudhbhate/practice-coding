# Lesson 08 — Common Mistakes

## Mistake 01: No max depth
```python
# WRONG — overfits
DecisionTreeClassifier()
# CORRECT
DecisionTreeClassifier(max_depth=5, min_samples_leaf=10)
```

## Mistake 02: Too few trees in forest
```python
# WRONG — unstable
RandomForestClassifier(n_estimators=10)
# CORRECT
RandomForestClassifier(n_estimators=100)
```

## Mistake 03: Not using random_state
```python
# WRONG — different results each run
RandomForestClassifier()
# CORRECT — reproducible
RandomForestClassifier(random_state=42)
```

## Mistake 04: Ignoring feature importance
```python
# Check which features matter
importances = model.feature_importances_
# Remove unimportant features
```

## Mistake 05: Not tuning hyperparameters
```python
# Use GridSearchCV
param_grid = {"max_depth": [3, 5, 10, None], "min_samples_leaf": [1, 5, 10]}
```
