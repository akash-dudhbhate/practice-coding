# Lesson 06 — Concepts Explained (Linear Regression)

> Read this before solving the problems. Each concept explains:
> **What** it is · **Why** it exists · **Where** it's used · **What goes wrong** without it.

---

## What is Linear Regression?

**What:** Linear regression fits a straight line through data points to model the relationship between a dependent variable (y) and one or more independent variables (x).

```python
# Simple linear regression: y = mx + b
# y = dependent variable (what we predict)
# x = independent variable (feature)
# m = slope (how much y changes per unit x)
# b = intercept (y when x = 0)

# Example: predicting house price from size
# price = 150 * size + 50000
# A 1000 sq ft house → 150 * 1000 + 50000 = 200,000
```

**Why it exists:** Linear regression is the simplest model for understanding relationships between variables. It's interpretable (you can see the equation), fast to train, and serves as a baseline for more complex models.

**Where it's used:** Price prediction, sales forecasting, trend analysis, any continuous value prediction where the relationship is roughly linear.

**What goes wrong without it:**
- Using linear regression for non-linear data → poor fit → high error. Check the data with a scatter plot first.
- Extrapolating beyond the data range → unreliable predictions (a line that fits 1000-2000 sq ft may not fit 5000 sq ft).
- Ignoring outliers → they pull the line toward themselves → skewed model.

---

## The Cost Function (MSE)

**What:** Mean Squared Error measures how far predictions are from actual values.

```python
import numpy as np

# MSE = (1/n) * sum((y_true - y_pred) ** 2)
y_true = np.array([3, 5, 7])
y_pred = np.array([2, 5, 8])

mse = np.mean((y_true - y_pred) ** 2)  # 0.667
```

**Why it exists:** Without a cost function, you can't measure how good your model is. MSE quantifies the error → lower is better. The training process minimizes MSE.

**Where it's used:** Every regression model evaluation, gradient descent optimization.

**What goes wrong without it:**
- MSE is sensitive to outliers (squared error → large errors dominate). Use MAE (Mean Absolute Error) for outlier-resistant evaluation.
- MSE is in squared units (dollars² for price prediction). Use RMSE (Root MSE) for interpretable units (dollars).
- Comparing MSE across different datasets → meaningless (scale-dependent). Use R² for normalized comparison.

---

## Gradient Descent

**What:** An optimization algorithm that iteratively adjusts parameters to minimize the cost function.

```python
# Gradient descent for linear regression
# Start with random m and b
# Update: m = m - learning_rate * dMSE/dm
#         b = b - learning_rate * dMSE/db

m, b = 0, 0
learning_rate = 0.01
n = len(x)

for epoch in range(1000):
    y_pred = m * x + b
    dm = (-2/n) * sum(x * (y - y_pred))  # gradient for m
    db = (-2/n) * sum(y - y_pred)        # gradient for b
    m = m - learning_rate * dm
    b = b - learning_rate * db
```

**Why it exists:** For simple models, you can solve analytically (normal equation). For complex models (neural networks), no closed-form solution exists → gradient descent is the standard optimizer.

**Where it's used:** Training almost all ML models — linear regression, logistic regression, neural networks.

**What goes wrong without it:**
- Learning rate too high → overshoots the minimum → diverges (loss increases).
- Learning rate too low → takes forever to converge → impractical.
- Getting stuck in local minima → for linear regression (convex), this doesn't happen. For neural networks, it can.

---

## Using scikit-learn

**What:** scikit-learn provides a simple API for linear regression.

```python
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Data
X = [[1000], [1500], [2000], [2500]]  # house sizes
y = [200000, 280000, 350000, 420000]  # prices

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train
model = LinearRegression()
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)

# Evaluate
mse = mean_squared_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print(f"Slope: {model.coef_}")        # [150]
print(f"Intercept: {model.intercept_}")  # 50000
print(f"MSE: {mse}")
print(f"R²: {r2}")
```

**Why it exists:** Without scikit-learn, you'd implement the math yourself → error-prone. sklearn provides optimized, tested implementations → focus on modeling, not implementation.

**Where it's used:** Every regression task in Python ML.

**What goes wrong without it:**
- `X` must be 2D: `[[1000]]` not `[1000]`. `model.fit([1000], y)` → error. Reshape: `np.array(X).reshape(-1, 1)`.
- Not splitting train/test → model memorizes data → overfitting. Always split.
- Forgetting to fit before predict → `model.predict()` on unfitted model → error.

---

## Multiple Linear Regression

**What:** Linear regression with multiple features.

```python
# price = m1*size + m2*bedrooms + m3*age + b
X = [[1000, 3, 10], [1500, 4, 5], [2000, 4, 20]]  # size, bedrooms, age
y = [200000, 280000, 350000]

model = LinearRegression()
model.fit(X, y)

print(model.coef_)  # [m1, m2, m3] — coefficient per feature
print(model.intercept_)  # b
```

**Why it exists:** Real-world predictions depend on multiple factors. Multiple regression captures the combined effect of all features.

**Where it's used:** Any prediction with multiple input features.

**What goes wrong without it:**
- Multicollinearity: highly correlated features → unstable coefficients → hard to interpret. Check correlation matrix.
- Feature scaling: features with different scales (size: 1000-3000, bedrooms: 2-5) → coefficients are not comparable. Scale features first.
- Categorical features: must be encoded (one-hot encoding) before using in regression.

---

## R-squared (R²)

**What:** R² measures how much of the variance in y is explained by the model. Range: 0 to 1.

```python
# R² = 0 → model explains none of the variance (as good as predicting the mean)
# R² = 1 → model explains all the variance (perfect predictions)
# R² < 0 → model is worse than predicting the mean

r2 = r2_score(y_test, predictions)
# 0.85 → 85% of variance explained
```

**Why it exists:** MSE is scale-dependent (can't compare across datasets). R² is normalized → 0.85 means the same thing regardless of whether you're predicting dollars or cents.

**Where it's used:** Every regression model evaluation.

**What goes wrong without it:**
- R² always increases when you add features (even useless ones). Use Adjusted R² for fair comparison with different feature counts.
- High R² doesn't mean the model is good → could be overfitting. Check R² on test data, not training.
- R² = 1 on training data → overfitting (memorized the data). Real-world R² is usually 0.5-0.9.

---

## Assumptions of Linear Regression

**What:** Linear regression works best when these assumptions hold:

1. **Linearity:** Relationship between x and y is linear.
2. **Independence:** Observations are independent (no time-series correlation).
3. **Homoscedasticity:** Residuals have constant variance (no funnel shape).
4. **Normality:** Residuals are normally distributed.
5. **No multicollinearity:** Features are not highly correlated.

```python
import matplotlib.pyplot as plt

# Check linearity: scatter plot
plt.scatter(X, y)

# Check residuals: residual plot
residuals = y_test - predictions
plt.scatter(predictions, residuals)
plt.axhline(y=0, color='r')  # should be random around 0
```

**Why it exists:** Violating assumptions → model is unreliable, predictions are biased, confidence intervals are wrong. Checking assumptions ensures the model is valid.

**Where it's used:** After fitting a linear regression → check assumptions before trusting the model.

**What goes wrong without it:**
- Non-linear data with linear regression → poor fit. Use polynomial regression or a non-linear model.
- Heteroscedasticity (funnel-shaped residuals) → predictions are less reliable for extreme values. Transform y (log, sqrt).
- Multicollinearity → coefficients are unstable (small data change → big coefficient change). Remove correlated features.
