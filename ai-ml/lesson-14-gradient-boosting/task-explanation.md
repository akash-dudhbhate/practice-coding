# Lesson 14 — Gradient Boosting

## What you'll learn
- Gradient boosting concept (sequential trees correcting errors)
- How boosting works (residuals, learning rate)
- sklearn GradientBoostingClassifier
- XGBoost (faster, regularized boosting)
- LightGBM and CatBoost (alternative libraries)
- Learning rate and n_estimators (the key pair)
- Regularization in boosting (max_depth, subsample, L1/L2)
- Feature importance in boosting models

## Lesson

### sklearn gradient boosting
```python
from sklearn.ensemble import GradientBoostingClassifier
model = GradientBoostingClassifier(n_estimators=100, learning_rate=0.1, max_depth=3)
```

### XGBoost with early stopping
```python
from xgboost import XGBClassifier
model = XGBClassifier(n_estimators=500, learning_rate=0.01, early_stopping_rounds=10)
model.fit(X_train, y_train, eval_set=[(X_test, y_test)])
```

---

## Your Tasks

### Easy
1. `easy/p01-solve.py` — Train sklearn's `GradientBoostingClassifier` on `make_classification`. Print accuracy. Compare with a single decision tree.
2. `easy/p02-solve.py` — Train XGBoost on the same dataset. Print accuracy. Compare with sklearn's gradient boosting (should be similar or better).
3. `easy/p03-solve.py` — Train gradient boosting with `n_iter_no_change=10` (early stopping). Print the actual number of trees used (`n_estimators_`). Show that it stops before the max.

### Medium
4. `medium/p01-solve.py` — Compare learning rates: train with LR=0.001, 0.01, 0.1, 0.3 (adjust n_estimators accordingly). For each, print accuracy. Identify the best combination.
5. `medium/p02-solve.py` — Tune XGBoost with grid search: `max_depth` [3, 5, 7], `learning_rate` [0.01, 0.1], `n_estimators` [100, 500]. Print best params and best score. Use early stopping.
6. `medium/p03-solve.py` — Compare random forest vs gradient boosting on the same dataset. For both: tune key hyperparameters, print best accuracy, training time, and prediction time. Create a comparison table.

### Hard
7. `hard/p01-solve.py` — Build a complete XGBoost pipeline: load a real dataset, preprocess, tune with grid search (max_depth, learning_rate, n_estimators, subsample, colsample_bytree), use early stopping, evaluate with CV, and plot feature importance.
8. `hard/p02-solve.py` — Implement gradient boosting from scratch: implement the sequential tree training, residual calculation, and prediction (sum of trees * learning_rate). Use sklearn's DecisionTreeRegressor as the base. Train on a regression dataset. Plot the loss curve.
9. `hard/p03-solve.py` — Build a boosting library comparison: compare sklearn GradientBoosting, XGBoost, LightGBM (if installed) on the same dataset. For each: training time, accuracy, F1, and memory usage. Create a comparison table. Identify the best for speed and the best for accuracy.

### How to work
- Write your complete Python solution.
- Remove the TODO comment when done.
- Test with `python <filename>`.
