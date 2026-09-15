# Lesson 12 — Approach Comparison

## Problem: Handle Imbalance

### Approach 1: Resampling
```python
SMOTE().fit_resample(X_train, y_train)
```

### Approach 2: Class weights
```python
LogisticRegression(class_weight="balanced")
```

**Winner:** Approach 2 first (simpler). Approach 1 if class weights insufficient.

---

## Problem: Evaluate

### Approach 1: ROC-AUC
```python
roc_auc_score(y_test, y_proba)
```
**Cons:** Optimistic on imbalanced data.

### Approach 2: PR-AUC
```python
average_precision_score(y_test, y_proba)
```

**Winner:** Approach 2 — better for imbalanced data.
