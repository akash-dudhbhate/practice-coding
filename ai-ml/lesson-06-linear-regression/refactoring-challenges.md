# Lesson 06 — Refactoring Challenges

## Refactor 01 (Easy): Manual MSE
### Before
```python
mse = sum((t - p) ** 2 for t, p in zip(y_true, y_pred)) / len(y_true)
```
### After
```python
from sklearn.metrics import mean_squared_error
mse = mean_squared_error(y_true, y_pred)
```

## Refactor 02 (Medium): Manual Fit
### Before
```python
w = sum((x - x.mean()) * (y - y.mean())) / sum((x - x.mean()) ** 2)
b = y.mean() - w * x.mean()
```
### After
```python
from sklearn.linear_model import LinearRegression
model = LinearRegression().fit(X, y)
```

## Refactor 03 (Hard): No Feature Scaling
### Before
```python
model = LinearRegression().fit(X, y)  # features on different scales
```
### After
```python
from sklearn.pipeline import make_pipeline
model = make_pipeline(StandardScaler(), LinearRegression()).fit(X, y)
```
