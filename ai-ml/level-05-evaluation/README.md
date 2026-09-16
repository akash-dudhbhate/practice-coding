# Level 05 Evaluation — Model Evaluation & Tuning

## What You'll Learn
- Accuracy, precision, recall, F1
- Confusion matrix
- ROC and AUC
- Cross-validation
- Hyperparameter tuning
- Learning curves

## Prerequisites
- Previous levels completed
- Python basics

## How This Level Works

Each problem has:
1. **CONCEPT** — the idea you need to understand
2. **PROBLEM** — what to build
3. **TRY THIS INPUT** — test code to verify your solution
4. **EXPECTED OUTPUT** — what it should print
5. **AUTO-CHECK** — run `check.py` to verify automatically

Start with `easy/` problems, then `medium/`, then `hard/`, then the project.

---

## Problems

### Easy
1. `easy/p01-metrics-scratch.py` — Implement accuracy, precision, recall, and F1 from scratch. ...
2. `easy/p02-confusion-matrix.py` — Build a confusion matrix from predictions. Print TP, FP, TN,...
3. `easy/p03-kfold-cv.py` — Run 5-fold cross-validation on a model. Print mean and std o...

### Medium
4. `medium/p01-roc-auc.py` — Plot ROC curve and calculate AUC for a classifier....
5. `medium/p02-grid-search.py` — Use GridSearchCV to tune hyperparameters. Print best params ...
6. `medium/p03-learning-curve.py` — Plot learning curve showing train vs validation error over t...

### Hard
7. `hard/p01-precision-recall-tradeoff.py` — Find the threshold that gives 80% recall. Report precision a...
8. `hard/p02-model-comparison.py` — Compare 5 models with 3 metrics each. Print a comparison tab...
9. `hard/p03-nested-cv.py` — Implement nested cross-validation for unbiased model evaluat...

### Project
`project/` — Build a model evaluation dashboard comparing multiple classifiers with all metrics.

---

## Verify Your Work

```bash
# Run a problem
python3 easy/p01-metrics-scratch.py

# Check your answer
python3 check.py easy/p01
```

When `check.py` says "PASS", add `# DONE` to the first line and move on.
