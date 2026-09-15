# Lesson 01 — Approach Comparison

## Problem: Split Data

### Approach 1: Manual split
```python
split = int(len(X) * 0.8)
X_train, X_test = X[:split], X[split:]
```
**Cons:** No shuffling, may get ordered data.

### Approach 2: train_test_split
```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```

**Winner:** Approach 2 — shuffles, handles y, reproducible.

---

## Problem: Evaluate Model

### Approach 1: Accuracy
```python
accuracy = model.score(X_test, y_test)
```
**Cons:** Misleading on imbalanced data.

### Approach 2: Multiple metrics
```python
from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred))
```

**Winner:** Approach 2 — shows precision, recall, F1.
