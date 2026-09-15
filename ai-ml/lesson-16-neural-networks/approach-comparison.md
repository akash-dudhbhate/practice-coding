# Lesson 16 — Approach Comparison

## Problem: Prevent Overfitting

### Approach 1: Dropout
```python
Dropout(0.5)
```

### Approach 2: Regularization
```python
Dense(64, kernel_regularizer=l2(0.01))
```

### Approach 3: Early stopping
```python
EarlyStopping(patience=10)
```

**Winner:** Use all three. Early stopping is essential. Dropout + L2 for extra regularization.

---

## Problem: Choose Optimizer

### Approach 1: SGD
```python
SGD(learning_rate=0.01)
```
**Pros:** Can find better minima. **Cons:** Needs tuning.

### Approach 2: Adam
```python
Adam(learning_rate=0.001)
```

**Winner:** Adam — default choice, adaptive learning rate, less tuning.
