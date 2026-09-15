# Lesson 06 — Common Mistakes

## Mistake 01: Not fitting before predicting
```python
# WRONG
model.predict(X_test)
# CORRECT
model.fit(X_train, y_train)
model.predict(X_test)
```

## Mistake 02: Not scaling features
```python
# Features with different scales → coefficients not comparable
# Scale before fitting
scaler.fit(X_train)
model.fit(scaler.transform(X_train), y_train)
```

## Mistake 03: Ignoring multicollinearity
```python
# Check correlation matrix
df.corr()
# Remove highly correlated features (>0.9)
```

## Mistake 04: Extrapolating
```python
# Model trained on houses $100k-$500k
# Predicting $5M house — unreliable
# Don't predict outside training data range
```

## Mistake 05: Not checking residuals
```python
# Always plot residuals
residuals = y_test - model.predict(X_test)
plt.scatter(y_test, residuals)
# Should be random — patterns indicate problems
```
