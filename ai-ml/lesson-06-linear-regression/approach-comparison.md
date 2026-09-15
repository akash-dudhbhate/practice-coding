# Lesson 06 — Approach Comparison

## Problem: Predict Continuous Value

### Approach 1: Linear regression
```python
model = LinearRegression()
```
**Pros:** Simple, interpretable, fast. **Cons:** Only linear relationships.

### Approach 2: Polynomial regression
```python
from sklearn.preprocessing import PolynomialFeatures
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)
model = LinearRegression().fit(X_poly, y)
```
**Pros:** Captures non-linearity. **Cons:** Overfits with high degree.

**Winner:** Start with linear. Add polynomial if residuals show non-linearity.

---

## Problem: Evaluate Regression

### Approach 1: MSE
```python
mean_squared_error(y_test, y_pred)
```

### Approach 2: R²
```python
model.score(X_test, y_test)
```

**Winner:** Use both. MSE for model comparison, R² for interpretation.
