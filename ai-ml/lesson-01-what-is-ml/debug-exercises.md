# Lesson 01 — Debug Exercises

## Debug 01 (Easy: Wrong Problem Type
```python
# Goal: predict house prices
model = LogisticRegression()  # classification algorithm
```
<details><summary>Answer</summary>
**Bug:** LogisticRegression is for CLASSIFICATION (categories), not REGRESSION (continuous values). Despite the name.
**Fix:** Use `LinearRegression` for predicting continuous prices.
</details>

## Debug 02 (Medium): Training on Test Data
```python
model.fit(X_all, y_all)  # trained on ALL data
score = model.score(X_all, y_all)  # tested on same data
```
<details><summary>Answer</summary>
**Bug:** Training and testing on same data — overfitting, inflated score.
**Fix:** Split first: `X_train, X_test, y_train, y_test = train_test_split(X, y)`.
</details>

## Debug 03 (Hard): Data Leakage
```python
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)  # fit on ALL data
X_train, X_test = train_test_split(X_scaled)
```
<details><summary>Answer</summary>
**Bug:** Scaling before splitting — test data influences scaler (leakage).
**Fix:** Split first, then `scaler.fit(X_train)`, `scaler.transform(X_test)`.
</details>
