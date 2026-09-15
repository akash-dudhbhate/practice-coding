# Lesson 10 — Coding Check

## Easy

### p01-solve.py — 5-fold CV
- [ ] `cross_val_score` with cv=5 used
- [ ] Mean accuracy printed
- [ ] Std accuracy printed
- [ ] Single split accuracy also shown
- [ ] CV mean is more stable than single split

### p02-solve.py — Stratified K-fold
- [ ] Imbalanced dataset created (90% class 0)
- [ ] `StratifiedKFold` with 5 folds used
- [ ] Each fold's class ratio printed
- [ ] All folds have similar class ratios
- [ ] Fold sizes printed

### p03-solve.py — Grid search for max_depth
- [ ] `GridSearchCV` used with max_depth values [1, 3, 5, 10, 20]
- [ ] cv=5 specified
- [ ] Best depth printed
- [ ] Best score printed
- [ ] Decision tree used as the model

## Medium

### p01-solve.py — Random forest grid search
- [ ] `n_estimators` [50, 100, 200] in grid
- [ ] `max_depth` [3, 5, 10, None] in grid
- [ ] `GridSearchCV` with cv=5 used
- [ ] Best params printed
- [ ] Best score printed
- [ ] All results in a table (cv_results_ as DataFrame)

### p02-solve.py — Randomized search comparison
- [ ] Expanded parameter space used
- [ ] `RandomizedSearchCV` with n_iter=20
- [ ] Best score printed
- [ ] Time taken measured and printed
- [ ] Compared with grid search (score and time)
- [ ] Randomized search is faster with similar score

### p03-solve.py — Pipeline + tuning
- [ ] `Pipeline` with StandardScaler + LogisticRegression
- [ ] `C` [0.01, 0.1, 1, 10, 100] tuned
- [ ] Parameter name uses `model__C` prefix
- [ ] `GridSearchCV` with cv=5 used
- [ ] Scaling is inside CV (no leakage)
- [ ] Best C and best score printed

## Hard

### p01-solve.py — Complete tuning pipeline
- [ ] Real dataset loaded (e.g., Breast Cancer)
- [ ] Pipeline created (scaler + model)
- [ ] 3+ hyperparameters tuned
- [ ] `GridSearchCV` with cv=5 used
- [ ] Best params printed
- [ ] Evaluated on held-out test set
- [ ] Compared with default hyperparameters
- [ ] Improvement documented

### p02-solve.py — Learning curves
- [ ] `learning_curve` used for 3 models
- [ ] Training and validation scores plotted
- [ ] For each model: diagnosed (overfit/underfit/good)
- [ ] Logistic regression: likely underfit or good
- [ ] Decision tree: likely overfit
- [ ] Random forest: likely good fit
- [ ] Recommendation: more data would help if validation is still rising

### p03-solve.py — Model selection script
- [ ] 3 models compared: LR, RF, GB
- [ ] 5-fold CV used
- [ ] 3 metrics: accuracy, F1, AUC
- [ ] One hyperparameter tuned per model
- [ ] Final comparison table created
- [ ] Best model per metric identified
- [ ] Overall best model recommended
