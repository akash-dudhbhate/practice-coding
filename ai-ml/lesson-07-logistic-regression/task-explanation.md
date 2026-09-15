# Lesson 07 — Logistic Regression

## What you'll learn
- Logistic regression (classification, not regression)
- Sigmoid function (squashing to probability)
- Using scikit-learn LogisticRegression
- Decision boundary (linear separation)
- Confusion matrix (TP, TN, FP, FN)
- Precision, recall, F1-score
- Multiclass classification (one-vs-rest, multinomial)
- Regularization (L1, L2, C parameter)

## Lesson

### Basic classification
```python
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(X_train, y_train)
preds = model.predict(X_test)
probs = model.predict_proba(X_test)
```

### Evaluation
```python
from sklearn.metrics import precision_score, recall_score, f1_score
print(precision_score(y_test, preds), recall_score(y_test, preds))
```

---

## Your Tasks

### Easy
1. `easy/p01-solve.py` — Implement the sigmoid function from scratch. Test with values: 0, 5, -5, 100, -100. Verify outputs are between 0 and 1.
2. `easy/p02-solve.py` — Use sklearn to train logistic regression on `make_classification` (binary). Print accuracy, precision, recall, and F1-score.
3. `easy/p03-solve.py` — Implement a confusion matrix from scratch (2x2). Calculate TP, TN, FP, FN. Verify against `sklearn.metrics.confusion_matrix`.

### Medium
4. `medium/p01-solve.py` — Build a spam classifier: create synthetic email features (word counts, links, caps ratio). Train logistic regression. Print confusion matrix and precision/recall. Interpret results.
5. `medium/p02-solve.py` — Plot the decision boundary of a logistic regression on 2D synthetic data. Use `meshgrid` and `contourf`. Show the boundary and data points.
6. `medium/p03-solve.py` — Train multiclass logistic regression on the Iris dataset (3 classes). Print accuracy, confusion matrix, and per-class precision/recall using `classification_report`.

### Hard
7. `hard/p01-solve.py` — Build a complete binary classification pipeline: load Breast Cancer dataset, preprocess (scale), train logistic regression with different C values (0.01, 1, 100), compare precision/recall/F1 for each. Plot the effect of C.
8. `hard/p02-solve.py` — Implement logistic regression from scratch using gradient descent. Implement sigmoid, cost (log-loss), and gradient. Train on synthetic data. Plot the loss curve and decision boundary.
9. `hard/p03-solve.py` — Build a threshold optimization script: train logistic regression, get probabilities, sweep thresholds from 0.1 to 0.9. For each threshold, calculate precision, recall, F1. Plot precision-recall curve. Find the optimal threshold for F1.

### How to work
- Write your complete Python solution.
- Remove the TODO comment when done.
- Test with `python <filename>`.
