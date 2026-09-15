# Lesson 07 — Approach Comparison

## Problem: Binary Classification

### Approach 1: Logistic regression
```python
LogisticRegression()
```
**Pros:** Interpretable, fast, probabilities. **Cons:** Linear decision boundary.

### Approach 2: Decision tree
```python
DecisionTreeClassifier()
```
**Pros:** Non-linear, interpretable. **Cons:** Overfits easily.

**Winner:** Start with logistic regression (baseline). Try trees if non-linear.

---

## Problem: Adjust Threshold

### Approach 1: Default (0.5)
```python
y_pred = model.predict(X_test)
```

### Approach 2: Custom threshold
```python
y_proba = model.predict_proba(X_test)[:, 1]
y_pred = (y_proba > 0.3).astype(int)
```

**Winner:** Approach 2 — adjust based on whether false positives or false negatives are worse.
