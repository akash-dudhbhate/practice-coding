# Lesson 08 — Debug Exercises

## Debug 01 (Easy: No Max Depth
```python
model = DecisionTreeClassifier()
model.fit(X_train, y_train)
# train score: 1.0, test score: 0.7
```
<details><summary>Answer</summary>
**Bug:** No max_depth — tree grows until pure leaves. Overfitting.
**Fix:** `DecisionTreeClassifier(max_depth=5)`.
</details>

## Debug 02 (Medium: Random Forest Too Few Trees
```python
model = RandomForestClassifier(n_estimators=10)
```
<details><summary>Answer</summary>
**Issue:** 10 trees is too few — high variance, unstable predictions.
**Fix:** `n_estimators=100` (default) or more.
</details>

## Debug 03 (Hard: Not Using OOB Score
```python
model = RandomForestClassifier()
model.fit(X_train, y_train)
# No validation set to check generalization
```
<details><summary>Answer</summary>
**Bug:** Not using out-of-bag samples for validation.
**Fix:** `RandomForestClassifier(oob_score=True)`.
</details>
