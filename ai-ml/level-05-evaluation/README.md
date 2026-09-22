# Level 05 — Model Evaluation

> **Math level:** 10th grade is enough. See [MATH-YOU-NEED.md](../MATH-YOU-NEED.md) — it explains every symbol used here.

## What You'll Learn
- Accuracy, precision, recall, F1 from scratch
- Confusion matrices
- K-fold cross-validation
- ROC curves and AUC
- Grid search hyperparameter tuning
- Learning curves, precision-recall tradeoffs, nested CV

## Prerequisites
- Level 04 (supervised models)

## Problems

### Easy
1. `easy/p01-metrics-scratch.py` — `compute_metrics(y_true, y_pred)` → accuracy/precision/recall/F1
2. `easy/p02-confusion-matrix.py` — `confusion(y_true, y_pred)` → TP/FP/TN/FN
3. `easy/p03-kfold-cv.py` — `cross_validate()` → mean ± std

### Medium
4. `medium/p01-roc-auc.py` — `plot_roc()` → AUC
5. `medium/p02-grid-search.py` — `grid_search()` → best params
6. `medium/p03-learning-curve.py` — `plot_learning_curve()` → train vs val

### Hard
7. `hard/p01-precision-recall-tradeoff.py` — `find_threshold()` → tune for recall
8. `hard/p02-model-comparison.py` — `compare_all()` → 5 models × 3 metrics
9. `hard/p03-nested-cv.py` — `nested_cv()` → unbiased tuned estimate

### Project
`project/` — Full model evaluation report on a real dataset.

## Verify

```bash
python3 check.py easy/p01
python3 check.py all
```
