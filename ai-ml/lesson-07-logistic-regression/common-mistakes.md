# Lesson 07 — Common Mistakes

## Mistake 01: Linear regression for classification
```python
# WRONG
LinearRegression()  # for 0/1 target
# CORRECT
LogisticRegression()
```

## Mistake 02: Not handling imbalance
```python
# WRONG — biased to majority
LogisticRegression()
# CORRECT
LogisticRegression(class_weight="balanced")
```

## Mistake 03: Using predict instead of predict_proba
```python
# WRONG — loses probability info
model.predict(X_test)
# CORRECT — get probabilities
model.predict_proba(X_test)[:, 1]
```

## Mistake 04: Not tuning C
```python
# Try different C values
LogisticRegression(C=0.1)
LogisticRegression(C=10)
# Use GridSearchCV
```

## Mistake 05: Not scaling
```python
# Logistic regression is scale-sensitive (regularization)
# Scale features before fitting
```
