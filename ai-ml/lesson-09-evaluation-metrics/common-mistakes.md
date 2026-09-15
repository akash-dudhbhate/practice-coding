# Lesson 09 — Common Mistakes

## Mistake 01: Only using accuracy
```python
# WRONG — misleading on imbalanced data
model.score(X_test, y_test)
# CORRECT
print(classification_report(y_test, y_pred))
```

## Mistake 02: Confusion matrix arguments swapped
```python
# WRONG
confusion_matrix(y_pred, y_test)
# CORRECT
confusion_matrix(y_test, y_pred)
```

## Mistake 03: Not choosing metric based on problem
```python
# Cancer detection → optimize recall
# Spam filter → optimize precision
# Choose based on business cost
```

## Mistake 04: Not looking at confusion matrix
```python
# Always check where errors are
# Are false positives or false negatives more common?
```

## Mistake 05: Comparing models with different thresholds
```python
# Use ROC-AUC for threshold-independent comparison
# Or fix threshold and compare precision/recall
```
