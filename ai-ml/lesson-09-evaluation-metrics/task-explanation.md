# Lesson 09 — Evaluation Metrics

## What you'll learn
- Accuracy (and its limitations)
- Precision and recall (the trade-off)
- F1-score (balancing precision and recall)
- ROC curve and AUC (threshold-free evaluation)
- Precision-recall curve (for imbalanced data)
- Regression metrics (MSE, RMSE, MAE, R²)
- Classification report (comprehensive view)
- Cross-validation for reliable evaluation

## Lesson

### Classification metrics
```python
from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred))
```

### ROC/AUC
```python
from sklearn.metrics import roc_auc_score
auc = roc_auc_score(y_test, model.predict_proba(X_test)[:, 1])
```

### Regression metrics
```python
from sklearn.metrics import mean_squared_error, r2_score
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
```

---

## Your Tasks

### Easy
1. `easy/p01-solve.py` — Implement accuracy, precision, recall, and F1 from scratch. Test with y_true=[0,0,1,1,1] and y_pred=[0,1,1,1,0]. Verify against sklearn.
2. `easy/p02-solve.py` — Train logistic regression on `make_classification`. Print `classification_report`. Interpret each metric (what does precision=0.8 mean?).
3. `easy/p03-solve.py` — Calculate MSE, RMSE, MAE, and R² for a regression model on `make_regression`. Print all four. Explain which is most interpretable.

### Medium
4. `medium/p01-solve.py` — Create an imbalanced dataset (95% class 0, 5% class 1). Train a model. Show that accuracy is high (95%) but recall for class 1 is low. Print the classification report.
5. `medium/p02-solve.py` — Plot the ROC curve for a logistic regression model. Calculate AUC. Add a random baseline line (diagonal). Interpret: AUC=0.9 means what?
6. `medium/p03-solve.py` — Plot the precision-recall curve for the same model. Calculate average precision. Compare with the ROC curve — which is more informative for imbalanced data?

### Hard
7. `hard/p01-solve.py` — Build a metric comparison script: train 3 models (logistic regression, decision tree, random forest) on the same dataset. For each, print accuracy, precision, recall, F1, and AUC. Create a comparison table (pandas DataFrame).
8. `hard/p02-solve.py` — Implement a custom threshold optimizer: get prediction probabilities, sweep thresholds 0.1 to 0.9, calculate F1 for each. Plot F1 vs threshold. Find and print the optimal threshold.
9. `hard/p03-solve.py` — Build a cross-validation evaluation script: use 5-fold CV to evaluate a model with 3 different scoring metrics (accuracy, f1, roc_auc). Print mean ± std for each. Explain why different metrics give different rankings.

### How to work
- Write your complete Python solution.
- Remove the TODO comment when done.
- Test with `python <filename>`.
