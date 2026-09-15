# Lesson 06 — Debug Exercises

## Debug 01 (Easy: Not Fitting Model
```python
model = LinearRegression()
predictions = model.predict(X_test)  # not fitted!
```
<details><summary>Answer</summary>
**Bug:** Model not fitted. Need to call `model.fit(X_train, y_train)` first.
**Fix:** `model.fit(X_train, y_train); predictions = model.predict(X_test)`.
</details>

## Debug 02 (Medium: Multicollinearity
```python
# Features: "house_size_sqft" and "house_size_sqm"
# These are perfectly correlated
model.fit(X, y)
```
<details><summary>Answer</summary>
**Bug:** Multicollinearity — redundant features make coefficients unstable.
**Fix:** Remove one of the correlated features.
</details>

## Debug 03 (Hard: Not Checking Residuals
```python
model.fit(X_train, y_train)
print(model.score(X_test, y_test))  # R² = 0.9, looks good
# But residuals show patterns — model is biased
```
<details><summary>Answer</summary>
**Bug:** High R² doesn't mean model is correct. Residuals should be random. Patterns indicate non-linearity or missing features.
**Fix:** Plot residuals: `plt.scatter(y_pred, y_test - y_pred)`.
</details>
