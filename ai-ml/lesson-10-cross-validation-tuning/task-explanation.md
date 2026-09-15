# Lesson 10 — Cross-Validation & Hyperparameter Tuning

## What you'll learn
- Why cross-validation matters (reliable evaluation)
- K-fold cross-validation
- Stratified K-fold (for imbalanced data)
- Grid search (exhaustive hyperparameter search)
- Randomized search (faster alternative)
- Hyperparameters vs parameters
- Pipelines for tuning (preventing data leakage)
- Learning curves (diagnosing overfitting/underfitting)

## Lesson

### Cross-validation
```python
from sklearn.model_selection import cross_val_score
scores = cross_val_score(model, X, y, cv=5)
print(f"{scores.mean():.3f} ± {scores.std():.3f}")
```

### Grid search
```python
from sklearn.model_selection import GridSearchCV
gs = GridSearchCV(model, param_grid, cv=5, scoring='f1')
gs.fit(X_train, y_train)
print(gs.best_params_)
```

---

## Your Tasks

### Easy
1. `easy/p01-solve.py` — Run 5-fold cross-validation on a random forest with the Iris dataset. Print mean and std of accuracy. Compare with a single train/test split.
2. `easy/p02-solve.py` — Use `StratifiedKFold` with 5 folds on an imbalanced dataset (90% class 0). Verify each fold has the same class ratio. Print fold sizes and class counts.
3. `easy/p03-solve.py` — Use `GridSearchCV` to tune `max_depth` (try 1, 3, 5, 10, 20) for a decision tree on `make_classification`. Print the best depth and best score.

### Medium
4. `medium/p01-solve.py` — Use `GridSearchCV` to tune a random forest: `n_estimators` [50, 100, 200] and `max_depth` [3, 5, 10, None]. Print best params, best score, and all results in a table.
5. `medium/p02-solve.py` — Use `RandomizedSearchCV` with 20 iterations on the same parameter space (expanded with more values). Compare the best score and time taken with grid search.
6. `medium/p03-solve.py` — Build a pipeline with `StandardScaler` + `LogisticRegression`. Tune `C` [0.01, 0.1, 1, 10, 100] using `GridSearchCV`. Verify no data leakage (scaling is inside CV).

### Hard
7. `hard/p01-solve.py` — Build a complete tuning pipeline: load a real dataset, create a pipeline (scaler + model), use `GridSearchCV` with 3+ hyperparameters, print best params, evaluate on held-out test set, and compare with default hyperparameters.
8. `hard/p02-solve.py` — Plot learning curves for 3 models (logistic regression, decision tree, random forest) on the same dataset. For each, diagnose: overfitting, underfitting, or good fit. Recommend whether more data would help.
9. `hard/p03-solve.py` — Build a model selection script: compare 3 models (logistic regression, random forest, gradient boosting) using 5-fold CV with 3 metrics (accuracy, F1, AUC). For each model, also tune one key hyperparameter. Print a final comparison table with best model per metric.

### How to work
- Write your complete Python solution.
- Remove the TODO comment when done.
- Test with `python <filename>`.
