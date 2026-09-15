# Lesson 13 — Approach Comparison

## Problem: Classification

### Approach 1: SVM
```python
SVC(kernel="rbf")
```
**Pros:** Good for high-dimensional, non-linear. **Cons:** Slow on large data, needs scaling.

### Approach 2: KNN
```python
KNeighborsClassifier(n_neighbors=5)
```
**Pros:** Simple, no training. **Cons:** Slow prediction, sensitive to irrelevant features.

**Winner:** SVM for accuracy. KNN for simplicity/baseline.

---

## Problem: Non-linear Data

### Approach 1: SVM with rbf kernel
```python
SVC(kernel="rbf", C=1, gamma="scale")
```

### Approach 2: Random forest
```python
RandomForestClassifier()
```

**Winner:** Try both. SVM for small/medium data. RF for larger data.
