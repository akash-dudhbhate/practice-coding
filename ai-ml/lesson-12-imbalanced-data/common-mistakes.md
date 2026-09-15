# Lesson 12 — Common Mistakes

## Mistake 01: Using accuracy
```python
# WRONG — misleading
accuracy_score(y_test, y_pred)
# CORRECT
f1_score(y_test, y_pred)
# or
classification_report(y_test, y_pred)
```

## Mistake 02: Resampling before split
```python
# WRONG — leakage
oversample(X, y)
train_test_split(X)
# CORRECT
train_test_split(X)
oversample(X_train)
```

## Mistake 03: Random oversampling
```python
# WRONG — overfits
RandomOverSampler()
# BETTER
SMOTE()
```

## Mistake 04: Not trying class weights
```python
# Simplest fix — no resampling needed
LogisticRegression(class_weight="balanced")
RandomForestClassifier(class_weight="balanced")
```

## Mistake 05: Ignoring business cost
```python
# False negative (missed cancer) vs false positive (extra test)
# Choose strategy based on relative cost
```
