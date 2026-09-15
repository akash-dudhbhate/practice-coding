# Lesson 09 — Refactoring Challenges

## Refactor 01 (Easy): Manual Confusion Matrix
### Before
```python
tp = sum((t == 1) & (p == 1) for t, p in zip(y, preds))
fp = sum((t == 0) & (p == 1) for t, p in zip(y, preds))
```
### After
```python
from sklearn.metrics import confusion_matrix
tn, fp, fn, tp = confusion_matrix(y, preds).ravel()
```

## Refactor 02 (Medium): Manual F1
### Before
```python
precision = tp / (tp + fp)
recall = tp / (tp + fn)
f1 = 2 * precision * recall / (precision + recall)
```
### After
```python
from sklearn.metrics import f1_score
f1 = f1_score(y, preds)
```

## Refactor 03 (Hard): Multiple Metrics Manual
### Before
```python
acc = accuracy_score(y, p)
prec = precision_score(y, p)
rec = recall_score(y, p)
f1 = f1_score(y, p)
```
### After
```python
from sklearn.metrics import classification_report
print(classification_report(y, p))
```
