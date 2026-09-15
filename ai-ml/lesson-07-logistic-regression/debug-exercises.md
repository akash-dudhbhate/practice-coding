# Lesson 07 — Debug Exercises

## Debug 01 (Easy: Using Regression for Classification
```python
model = LinearRegression()
model.fit(X, y)  # y is 0 or 1
```
<details><summary>Answer</summary>
**Bug:** Linear regression for classification — predictions can be <0 or >1, no probability interpretation.
**Fix:** `LogisticRegression()`.
</details>

## Debug 02 (Medium: Not Setting Class Weight
```python
model = LogisticRegression()  # imbalanced data
```
<details><summary>Answer</summary>
**Bug:** Default treats all classes equally. Imbalanced data → biased to majority.
**Fix:** `LogisticRegression(class_weight="balanced")`.
</details>

## Debug 03 (Hard: Not Setting Max Iterations
```python
model = LogisticRegression()
model.fit(X, y)  # ConvergenceWarning
```
<details><summary>Answer</summary>
**Bug:** Default max_iter=100 may not converge for complex data.
**Fix:** `LogisticRegression(max_iter=1000)`.
</details>
