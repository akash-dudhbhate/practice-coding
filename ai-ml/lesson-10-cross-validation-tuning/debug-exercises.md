# Lesson 10 — Debug Exercises

## Debug 01 (Easy: CV on All Data After Preprocessing
```python
X_scaled = scaler.fit_transform(X)
scores = cross_val_score(model, X_scaled, y)
```
<details><summary>Answer</summary>
**Bug:** Scaling before CV — test folds influence scaler (leakage).
**Fix:** Use Pipeline: `Pipeline([("scaler", scaler), ("model", model)])`.
</details>

## Debug 02 (Medium: Grid Search Without CV
```python
GridSearchCV(model, param_grid, cv=None)
```
<details><summary>Answer</summary>
**Bug:** cv=None uses default (5), but if you meant no CV, you lose evaluation.
**Fix:** Always specify cv explicitly: `cv=5`.
</details>

## Debug 03 (Hard: Tuning on Test Data
```python
# Try many params, pick best on test set
for params in param_list:
    model.fit(X_train, y_train)
    score = model.score(X_test, y_test)
# This overfits to test set!
```
<details><summary>Answer</summary>
**Bug:** Selecting hyperparameters based on test set = test set becomes validation set. Overfits.
**Fix:** Use GridSearchCV with CV on TRAIN data only. Test set used ONCE at the end.
</details>
