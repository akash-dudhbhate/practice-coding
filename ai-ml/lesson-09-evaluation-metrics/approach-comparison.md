# Lesson 09 — Approach Comparison

## Problem: Evaluate Classifier

### Approach 1: Accuracy only
```python
model.score(X_test, y_test)
```
**Cons:** Misleading on imbalanced data.

### Approach 2: Full report
```python
print(classification_report(y_test, y_pred))
```

**Winner:** Approach 2 — shows precision, recall, F1 per class.

---

## Problem: Choose Metric

### Approach 1: Optimize accuracy
```python
# Good for balanced data
```

### Approach 2: Optimize based on cost
```python
# False negatives costly → maximize recall
# False positives costly → maximize precision
```

**Winner:** Approach 2 — always align metric with business goal.
