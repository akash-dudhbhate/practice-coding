# Lesson 14 — Debug Exercises

## Debug 01 (Easy: Too Many Estimators
```python
model = GradientBoostingClassifier(n_estimators=10000)
```
<details><summary>Answer</summary>
**Bug:** Too many estimators — overfits, very slow.
**Fix:** Use early stopping or n_estimators=100-500.
</details>

## Debug 02 (Medium: High Learning Rate
```python
model = GradientBoostingClassifier(learning_rate=1.0)
```
<details><summary>Answer</summary>
**Bug:** Learning rate too high — overshoots optimal solution, unstable.
**Fix:** Use 0.01-0.1. Lower rate + more estimators = better.
</details>

## Debug 03 (Hard: Not Using Early Stopping
```python
model = XGBClassifier(n_estimators=1000)
model.fit(X_train, y_train)  # trains all 1000 even if best at 200
```
<details><summary>Answer</summary>
**Bug:** No early stopping — trains unnecessary estimators, may overfit.
**Fix:** `model.fit(X_train, y_train, early_stopping_rounds=10, eval_set=[(X_test, y_test)])`.
</details>
