# Lesson 01 — Common Mistakes

## Mistake 01: Training on test data
```python
# WRONG — inflated scores
model.fit(X, y)
model.score(X, y)
# CORRECT
X_train, X_test, y_train, y_test = train_test_split(X, y)
model.fit(X_train, y_train)
model.score(X_test, y_test)
```

## Mistake 02: Data leakage
```python
# WRONG — preprocess before split
X_scaled = scaler.fit_transform(X)
train_test_split(X_scaled)
# CORRECT — split first
X_train, X_test = train_test_split(X)
scaler.fit(X_train)
X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)
```

## Mistake 03: Wrong algorithm for problem
```python
# WRONG — classification algo for regression
LogisticRegression()  # for categories
# CORRECT
LinearRegression()  # for continuous values
```

## Mistake 04: Not setting random_state
```python
# WRONG — different results each run
train_test_split(X, y)
# CORRECT — reproducible
train_test_split(X, y, random_state=42)
```

## Mistake 05: Ignoring class imbalance
```python
# If 99% are class 0, 1% class 1
# 99% accuracy is useless — model just predicts 0
# Use precision, recall, F1 instead
```
