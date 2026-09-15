# Lesson 14 — Approach Comparison

## Problem: Classification

### Approach 1: Random forest
```python
RandomForestClassifier(n_estimators=100)
```
**Pros:** Simple, robust. **Cons:** Can't correct own errors.

### Approach 2: XGBoost
```python
XGBClassifier(n_estimators=100, learning_rate=0.1)
```
**Pros:** Often higher accuracy. **Cons:** More tuning needed.

**Winner:** XGBoost for competitions/accuracy. RF for simplicity.

---

## Problem: Tune XGBoost

### Approach 1: Grid search
```python
GridSearchCV(model, {"max_depth": [3, 5, 7], "learning_rate": [0.01, 0.1]})
```

### Approach 2: Optuna
```python
import optuna
def objective(trial):
    params = {"max_depth": trial.suggest_int("max_depth", 3, 10)}
    ...
```

**Winner:** Approach 2 — smarter search, better for large spaces.
