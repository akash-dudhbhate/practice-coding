# Lesson 06 — Intuition Checks

## Check 01: What does linear regression do?
<details><summary>Answer</summary>
Fits a line (or hyperplane) that minimizes the sum of squared differences between predicted and actual values. y = mx + b for simple, y = w1x1 + w2x2 + ... + b for multiple.
</details>

## Check 02: R²
```python
model.score(X_test, y_test)  # R² = 0.85
```
<details><summary>Answer</summary>
R² = proportion of variance explained. 0.85 means 85% of variance in y is explained by X. Range: 0-1 (can be negative if model is worse than mean).
</details>

## Check 03: Coefficients
```python
model.coef_  # [2.5, -1.3, 0.8]
```
<details><summary>Answer</summary>
Each coefficient shows how much y changes per unit change in that feature (holding others constant). Sign shows direction. Magnitude shows importance (if features are scaled).
</details>

## Check 04: Assumptions
What are the assumptions of linear regression?
<details><summary>Answer</summary>
Linearity, independence, homoscedasticity (constant variance), normality of residuals, no multicollinearity. Violating these can give misleading results.
</details>

## Check 05: MSE vs R²
```python
mean_squared_error(y_test, y_pred)  # A
model.score(X_test, y_test)         # B
```
<details><summary>Answer</summary>
MSE — absolute error in units of y (hard to interpret). R² — relative measure (0-1, easy to interpret). Use both: MSE for comparison, R² for communication.
</details>
