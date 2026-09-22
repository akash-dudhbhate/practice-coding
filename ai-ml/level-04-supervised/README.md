# Level 04 — Supervised Learning

> **Math level:** 10th grade is enough. See [MATH-YOU-NEED.md](../MATH-YOU-NEED.md) — it explains every symbol used here.

## What You'll Learn
- Linear and logistic regression FROM SCRATCH (numpy only)
- Gradient descent — how models actually learn
- Decision trees, random forests, gradient boosting
- SVM vs KNN
- Regularization (L1/L2) and feature selection

## Prerequisites
- Level 02 (NumPy, sklearn basics)

## Problems

### Easy
1. `easy/p01-linear-scratch.py` — `linreg(x, y)` → closed-form slope/intercept
2. `easy/p02-logistic-scratch.py` — `sigmoid(z)`, `train_logreg(X,y,...)` → scratch logistic regression
3. `easy/p03-decision-tree.py` — `train_tree()` → sklearn tree on Iris

### Medium
4. `medium/p01-gradient-descent.py` — `gradient_descent()` → iterative learning
5. `medium/p02-random-forest.py` — `train_forest()` → feature importances
6. `medium/p03-svm-knn.py` — `compare_models()` → SVM vs KNN

### Hard
7. `hard/p01-regularization.py` — `compare_regularization()` → L1/L2/Ridge
8. `hard/p02-ensemble-compare.py` — `compare_ensembles()` → 3 models compared
9. `hard/p03-feature-selection.py` — `select_features()` → RFE

### Project
`project/` — House price predictor, from-scratch vs sklearn.

## Verify

```bash
python3 check.py easy/p01
python3 check.py all
```
