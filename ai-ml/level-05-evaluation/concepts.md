# Level 05 — Concepts Reference

## Easy

### Metrics
- Accuracy = (TP+TN)/total — misleading on imbalanced data
- Precision = TP/(TP+FP) — "of my YES calls, how many right?"
- Recall = TP/(TP+FN) — "of actual YES, how many caught?"
- F1 = 2PR/(P+R) — balances both

### Confusion Matrix
- TP | FN
- FP | TN
- All metrics derive from these four numbers.

### K-Fold CV
- `cross_val_score(model, X, y, cv=5)` → 5 scores
- Mean = performance estimate, std = stability

## Medium

### ROC / AUC
- Plot TPR vs FPR across all thresholds
- AUC 1.0 = perfect; 0.5 = coin flip
- Needs `predict_proba`, not just `predict`

### Grid Search
- `GridSearchCV(model, param_grid, cv=3)` — tries every combo
- `.best_params_`, `.best_score_`

### Learning Curve
- `learning_curve(model, X, y, cv=5, train_sizes=linspace(0.1,1,10))`
- Train-val gap → overfitting; both low → underfitting

## Hard

### Threshold Tuning
- Default threshold 0.5 isn't sacred — precision_recall_curve
- Lower threshold → more recall, less precision

### Multi-Model Comparison
- Compare accuracy + F1 + AUC across several models
- No single "best" — depends on the metric that matters

### Nested CV
- Outer loop evaluates; inner loop tunes — no tuning leakage
- `cross_val_score(GridSearchCV(...), X, y, cv=5)`
