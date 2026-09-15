# Lesson 14 — Coding Check

## Easy

### p01-solve.py — sklearn gradient boosting
- [ ] `GradientBoostingClassifier` trained
- [ ] Accuracy printed
- [ ] Decision tree also trained
- [ ] Comparison: boosting > single tree

### p02-solve.py — XGBoost
- [ ] `XGBClassifier` trained
- [ ] Accuracy printed
- [ ] Compared with sklearn's gradient boosting
- [ ] XGBoost is similar or better

### p03-solve.py — Early stopping
- [ ] `n_iter_no_change=10` set
- [ ] Model trained
- [ ] `n_estimators_` printed (actual trees used)
- [ ] Stopped before the max
- [ ] Overfitting prevented

## Medium

### p01-solve.py — Learning rate comparison
- [ ] LR=0.001 with high n_estimators tested
- [ ] LR=0.01 tested
- [ ] LR=0.1 tested
- [ ] LR=0.3 tested
- [ ] Accuracy printed for each
- [ ] Best combination identified
- [ ] Trade-off explained

### p02-solve.py — XGBoost grid search
- [ ] `max_depth` [3, 5, 7] in grid
- [ ] `learning_rate` [0.01, 0.1] in grid
- [ ] `n_estimators` [100, 500] in grid
- [ ] `GridSearchCV` with cv=5 used
- [ ] Early stopping used
- [ ] Best params printed
- [ ] Best score printed

### p03-solve.py — RF vs GB comparison
- [ ] Random forest tuned and trained
- [ ] Gradient boosting tuned and trained
- [ ] Accuracy printed for both
- [ ] Training time measured for both
- [ ] Prediction time measured for both
- [ ] Comparison table created
- [ ] Best for speed and accuracy identified

## Hard

### p01-solve.py — Complete XGBoost pipeline
- [ ] Real dataset loaded
- [ ] Data preprocessed (scaling if needed)
- [ ] Grid search with 5 hyperparameters
- [ ] Early stopping used
- [ ] CV evaluation
- [ ] Best params printed
- [ ] Test accuracy printed
- [ ] Feature importance plotted

### p02-solve.py — Gradient boosting from scratch
- [ ] Initial prediction (mean) calculated
- [ ] Residuals calculated
- [ ] Sequential tree training implemented
- [ ] Learning rate applied
- [ ] Prediction = sum of trees * LR
- [ ] Trained on regression dataset
- [ ] Loss curve plotted (decreasing)
- [ ] Results compared with sklearn

### p03-solve.py — Boosting library comparison
- [ ] sklearn GradientBoosting trained
- [ ] XGBoost trained
- [ ] LightGBM trained (if available)
- [ ] Training time measured for each
- [ ] Accuracy and F1 for each
- [ ] Memory usage tracked
- [ ] Comparison table created
- [ ] Best for speed identified
- [ ] Best for accuracy identified
