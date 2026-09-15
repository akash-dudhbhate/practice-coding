# Lesson 08 — Approach Comparison

## Problem: Classification

### Approach 1: Single decision tree
```python
DecisionTreeClassifier(max_depth=5)
```
**Pros:** Interpretable, fast. **Cons:** Overfits, high variance.

### Approach 2: Random forest
```python
RandomForestClassifier(n_estimators=100)
```
**Pros:** Robust, less overfitting. **Cons:** Less interpretable, slower.

**Winner:** Approach 2 for accuracy. Approach 1 for interpretability.

---

## Problem: Feature Selection

### Approach 1: Feature importance
```python
importances = model.feature_importances_
```

### Approach 2: Domain knowledge
```python
# Select features based on understanding
```

**Winner:** Use both. Importance for data-driven, domain knowledge for context.
