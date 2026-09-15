# Lesson 06 — Linear Regression

## What you'll learn
- Linear regression basics (y = mx + b)
- Cost function (MSE — Mean Squared Error)
- Gradient descent optimization
- Using scikit-learn for regression
- Multiple linear regression (multiple features)
- R-squared (R²) evaluation metric
- Assumptions of linear regression

## Lesson

### Simple regression
```python
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
```

### Evaluate
```python
from sklearn.metrics import mean_squared_error, r2_score
mse = mean_squared_error(y_test, predictions)
r2 = r2_score(y_test, predictions)
```

---

## Your Tasks

### Easy
1. `easy/p01-solve.py` — Implement simple linear regression from scratch using numpy: calculate slope (m) and intercept (b) using the closed-form formula. Test with a small dataset.
2. `easy/p02-solve.py` — Use scikit-learn to fit a linear regression on a synthetic dataset (use `make_regression`). Print the coefficient, intercept, and R² score.
3. `easy/p03-solve.py` — Implement MSE from scratch (no sklearn). Calculate MSE between two arrays: y_true and y_pred. Verify against `sklearn.metrics.mean_squared_error`.

### Medium
4. `medium/p01-solve.py` — Build a house price predictor: create a synthetic dataset with features (size, bedrooms, age) and prices. Train a multiple linear regression. Print coefficients and interpret them.
5. `medium/p02-solve.py` — Implement gradient descent for linear regression from scratch. Start with m=0, b=0. Update using gradients. Track MSE over 1000 iterations. Plot the loss curve.
6. `medium/p03-solve.py` — Compare simple vs multiple regression: same dataset, first use one feature, then three. Compare R² and MSE. Document which is better and why.

### Hard
7. `hard/p01-solve.py` — Build a complete regression pipeline: load a real dataset (e.g., California Housing from sklearn), preprocess (scale features), train, evaluate with MSE/R², and plot actual vs predicted values.
8. `hard/p02-solve.py` — Implement polynomial regression: use `PolynomialFeatures` to add x², x³ terms. Compare linear vs polynomial fit on non-linear data. Plot both fits. Identify when polynomial overfits.
9. `hard/p03-solve.py` — Build a regression model with assumption checking: fit linear regression, plot residuals, check for linearity (scatter), homoscedasticity (residual plot), and normality (histogram of residuals). Report which assumptions hold.

### How to work
- Write your complete Python solution.
- Remove the TODO comment when done.
- Test with `python <filename>`.
