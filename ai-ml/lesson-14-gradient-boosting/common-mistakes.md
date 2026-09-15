# Lesson 14 — Common Mistakes

## Mistake 01: Not tuning learning rate
```python
# WRONG — default may not be optimal
GradientBoostingClassifier()  # lr=0.1
# CORRECT — try different values
{"learning_rate": [0.01, 0.05, 0.1, 0.2]}
```

## Mistake 02: Too many estimators without early stopping
```python
# WRONG — overfits
XGBClassifier(n_estimators=10000)
# CORRECT
XGBClassifier(n_estimators=1000, early_stopping_rounds=10)
```

## Mistake 03: Not using max_depth
```python
# Individual trees should be shallow (3-8)
# Deep trees + boosting = overfitting
XGBClassifier(max_depth=6)
```

## Mistake 04: Ignoring subsample
```python
# Use stochastic gradient boosting
XGBClassifier(subsample=0.8, colsample_bytree=0.8)
# Random subset of data and features per tree
```

## Mistake 05: Not using GPU
```python
# XGBoost and LightGBM support GPU
XGBClassifier(tree_method="gpu_hist")
```
