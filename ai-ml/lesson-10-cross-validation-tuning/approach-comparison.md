# Lesson 10 — Approach Comparison

## Problem: Evaluate Model

### Approach 1: Single split
```python
X_train, X_test = train_test_split(X)
model.fit(X_train).score(X_test)
```
**Cons:** Noisy — depends on split.

### Approach 2: Cross-validation
```python
cross_val_score(model, X, y, cv=5).mean()
```

**Winner:** Approach 2 — more reliable, uses all data for evaluation.

---

## Problem: Tune Hyperparameters

### Approach 1: Manual
```python
for C in [0.1, 1, 10]:
    model = LogisticRegression(C=C)
    score = cross_val_score(model, X, y).mean()
```

### Approach 2: GridSearchCV
```python
GridSearchCV(model, {"C": [0.1, 1, 10]}, cv=5).fit(X, y)
```

**Winner:** Approach 2 — automated, handles multiple params, returns best model.
