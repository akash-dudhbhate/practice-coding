# Lesson 09 — Coding Check

## Easy

### p01-solve.py — Metrics from scratch
- [ ] Accuracy implemented: correct / total
- [ ] Precision implemented: TP / (TP + FP)
- [ ] Recall implemented: TP / (TP + FN)
- [ ] F1 implemented: 2 * (P * R) / (P + R)
- [ ] Results match sklearn values
- [ ] No sklearn used for the calculation

### p02-solve.py — Classification report
- [ ] Logistic regression trained
- [ ] `classification_report` printed
- [ ] Precision interpreted ("of predicted positives, X% are correct")
- [ ] Recall interpreted ("of actual positives, X% were found")
- [ ] F1 interpreted ("balance of precision and recall")

### p03-solve.py — Regression metrics
- [ ] `make_regression` used
- [ ] MSE calculated and printed
- [ ] RMSE calculated (sqrt of MSE)
- [ ] MAE calculated and printed
- [ ] R² calculated and printed
- [ ] Most interpretable metric identified (RMSE — same units as y)

## Medium

### p01-solve.py — Imbalanced data demo
- [ ] Dataset created with 95% class 0, 5% class 1
- [ ] Model trained
- [ ] Accuracy printed (high, ~95%)
- [ ] Classification report printed
- [ ] Recall for class 1 is low
- [ ] Explanation: accuracy is misleading for imbalanced data

### p02-solve.py — ROC curve
- [ ] `predict_proba` used for probabilities
- [ ] `roc_curve` used to get FPR, TPR, thresholds
- [ ] ROC curve plotted
- [ ] Random baseline (diagonal) plotted
- [ ] AUC calculated and printed
- [ ] AUC interpreted (0.9 = 90% chance model ranks positive above negative)

### p03-solve.py — PR curve
- [ ] `precision_recall_curve` used
- [ ] PR curve plotted
- [ ] Average precision calculated
- [ ] Compared with ROC curve
- [ ] Explanation: PR is more informative for imbalanced data

## Hard

### p01-solve.py — Metric comparison table
- [ ] 3 models trained: logistic regression, decision tree, random forest
- [ ] For each: accuracy, precision, recall, F1, AUC
- [ ] Results in a pandas DataFrame
- [ ] DataFrame printed as a table
- [ ] Best model for each metric identified
- [ ] Overall best model recommended

### p02-solve.py — Threshold optimizer
- [ ] `predict_proba` used
- [ ] Thresholds 0.1 to 0.9 swept
- [ ] F1 calculated for each threshold
- [ ] F1 vs threshold plotted
- [ ] Optimal threshold identified (max F1)
- [ ] Optimal threshold printed
- [ ] Comparison: default (0.5) vs optimal

### p03-solve.py — Cross-validation evaluation
- [ ] 5-fold CV used
- [ ] 3 scoring metrics: accuracy, f1, roc_auc
- [ ] Mean ± std printed for each
- [ ] Different metrics give different rankings (if applicable)
- [ ] Explanation of why metrics differ
- [ ] `cross_val_score` used correctly
