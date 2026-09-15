# Lesson 07 — Refactoring Challenges

## Refactor 01 (Easy): Manual Sigmoid
### Before
```python
def sigmoid(z): return 1 / (1 + 2.718 ** (-z))
```
### After
```python
from scipy.special import expit
# or use sklearn LogisticRegression (handles it internally)
```

## Refactor 02 (Medium): Manual Classification
### Before
```python
probs = model.predict_proba(X)
preds = [1 if p > 0.5 else 0 for p in probs[:, 1]]
```
### After
```python
preds = model.predict(X)  # uses 0.5 threshold by default
```

## Refactor 03 (Hard): Manual Threshold Tuning
### Before
```python
best_f1 = 0
for t in np.arange(0.1, 1.0, 0.1):
    preds = (probs > t).astype(int)
    f1 = f1_score(y, preds)
    if f1 > best_f1: best_f1 = f1; best_t = t
```
### After
```python
from sklearn.metrics import precision_recall_curve
prec, rec, thresholds = precision_recall_curve(y, probs)
f1s = 2 * prec * rec / (prec + rec)
best_t = thresholds[f1s.argmax()]
```
