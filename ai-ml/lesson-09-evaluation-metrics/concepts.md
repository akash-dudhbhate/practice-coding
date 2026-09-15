# Lesson 09 — Concepts Explained (Evaluation Metrics)

> Read this before solving the problems. Each concept explains:
> **What** it is · **Why** it exists · **Where** it's used · **What goes wrong** without it.

---

## Accuracy

**What:** The fraction of predictions that are correct.

```python
from sklearn.metrics import accuracy_score

y_true = [0, 0, 1, 1, 1]
y_pred = [0, 1, 1, 1, 0]
accuracy = accuracy_score(y_true, y_pred)  # 0.6 (3 out of 5 correct)
```

**Why it exists:** Simplest metric — what fraction did we get right? Good for balanced datasets where all classes matter equally.

**Where it's used:** Quick model assessment, balanced datasets.

**What goes wrong without it:**
- Imbalanced data: 90% class 0, 10% class 1 → predict all as 0 → 90% accuracy → useless model. Accuracy hides this.
- Not knowing the baseline: if 90% is class 0, a model that always predicts 0 has 90% accuracy. Your model must beat this baseline.
- Accuracy doesn't tell you WHICH classes are confused. Use a confusion matrix for that.

---

## Precision and Recall

**What:**
- **Precision:** Of all predicted positives, how many are actually positive? (TP / (TP + FP))
- **Recall:** Of all actual positives, how many did we find? (TP / (TP + FN))

```python
from sklearn.metrics import precision_score, recall_score

# Spam filter example:
# Precision: of emails marked as spam, how many were actually spam?
#   High precision → few false alarms (good for user trust)
# Recall: of all actual spam, how many did we catch?
#   High recall → few spam in inbox (good for spam prevention)

precision = precision_score(y_true, y_pred)  # 0.67
recall = recall_score(y_true, y_pred)        # 0.67
```

**Why it exists:** Accuracy hides the trade-off between false positives and false negatives. Precision and recall expose it → you can optimize for your specific need.

**Where it's used:** Every classification task — choose based on the cost of errors.

**What goes wrong without it:**
- Optimizing precision only → recall drops (model only predicts positive when very confident → misses many).
- Optimizing recall only → precision drops (predict everything as positive → many false alarms).
- Not knowing which matters more for your problem → wrong optimization target.

---

## F1-Score

**What:** Harmonic mean of precision and recall. Balances both.

```python
from sklearn.metrics import f1_score

# F1 = 2 * (precision * recall) / (precision + recall)
# F1 = 1 → perfect (both precision and recall are 1)
# F1 = 0 → worst (either precision or recall is 0)

f1 = f1_score(y_true, y_pred)
```

**Why it exists:** You usually can't maximize both precision and recall simultaneously. F1 gives a single number that balances both → useful for comparison and optimization.

**Where it's used:** When you need a single metric that considers both precision and recall — especially for imbalanced data.

**What goes wrong without it:**
- F1 treats precision and recall equally. If false positives are 10x more expensive than false negatives → use Fβ with β < 1. If false negatives are worse → β > 1.
- F1 = 0 when either precision or recall is 0 → can be misleading. Look at both separately too.
- Macro F1 (average across classes) vs weighted F1 (weighted by class frequency) → choose based on whether you care about minority classes (macro) or overall (weighted).

---

## ROC Curve and AUC

**What:** ROC (Receiver Operating Characteristic) plots true positive rate vs false positive rate at different thresholds. AUC (Area Under Curve) summarizes it.

```python
from sklearn.metrics import roc_curve, roc_auc_score
import matplotlib.pyplot as plt

# Get probabilities (not class labels)
y_probs = model.predict_proba(X_test)[:, 1]

# ROC curve
fpr, tpr, thresholds = roc_curve(y_test, y_probs)

# Plot
plt.plot(fpr, tpr)
plt.plot([0, 1], [0, 1], 'r--')  # random baseline
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve')

# AUC
auc = roc_auc_score(y_test, y_probs)  # 0.5 = random, 1.0 = perfect
```

**Why it exists:** Accuracy/precision/recall depend on a fixed threshold (usually 0.5). ROC shows performance across ALL thresholds → comprehensive view. AUC summarizes it in one number → easy comparison.

**Where it's used:** Model comparison, threshold selection, medical testing, any binary classification where you want to see the full picture.

**What goes wrong without it:**
- AUC = 0.5 → model is random (no better than guessing). AUC < 0.5 → worse than random (flip your predictions).
- ROC can be misleading for highly imbalanced data → use Precision-Recall curve instead.
- Comparing AUC across different datasets → not meaningful (AUC depends on the data distribution).

---

## Precision-Recall Curve

**What:** Plots precision vs recall at different thresholds. Better than ROC for imbalanced data.

```python
from sklearn.metrics import precision_recall_curve, average_precision_score

precision, recall, thresholds = precision_recall_curve(y_test, y_probs)

plt.plot(recall, precision)
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.title('Precision-Recall Curve')

ap = average_precision_score(y_test, y_probs)
```

**Why it exists:** ROC can look good even when the model is bad on imbalanced data (because true negative rate is inflated by many negatives). PR curve focuses on the positive class → more honest for imbalanced data.

**Where it's used:** Imbalanced datasets — fraud detection, disease diagnosis, rare event prediction.

**What goes wrong without it:**
- PR curve doesn't have a baseline of 0.5 like ROC. The baseline is the prevalence of the positive class (e.g., 0.01 for 1% fraud).
- Average precision (AP) summarizes the PR curve → useful for comparison.
- PR curve can be jagged → use `step` post-implication for proper visualization.

---

## Regression Metrics (MSE, RMSE, MAE, R²)

**What:** Metrics for regression models (predicting continuous values).

```python
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import numpy as np

y_true = [3, 5, 7, 9]
y_pred = [2, 5, 8, 8]

mse = mean_squared_error(y_true, y_pred)     # 0.75 (squared error)
rmse = np.sqrt(mse)                           # 0.87 (same units as y)
mae = mean_absolute_error(y_true, y_pred)     # 0.75 (absolute error)
r2 = r2_score(y_true, y_pred)                 # 0.925 (explained variance)
```

**Why it exists:** Different metrics highlight different aspects:
- MSE/RMSE → penalize large errors heavily (squared).
- MAE → robust to outliers (linear penalty).
- R² → normalized (0-1), comparable across datasets.

**Where it's used:** Every regression model evaluation.

**What goes wrong without it:**
- MSE is in squared units (dollars²) → hard to interpret. Use RMSE (dollars).
- MAE vs MSE: if outliers are important → MSE. If outliers are noise → MAE.
- R² on training data → overfitting hides. Always evaluate on test data.

---

## Classification Report

**What:** A single function that prints precision, recall, F1, and support for each class.

```python
from sklearn.metrics import classification_report

print(classification_report(y_test, predictions))
#               precision    recall  f1-score   support
#           0       0.85      0.90      0.87       100
#           1       0.80      0.70      0.75        50
#    accuracy                           0.83       150
#   macro avg       0.83      0.80      0.81       150
# weighted avg       0.83      0.83      0.83       150
```

**Why it exists:** Instead of calling 4 functions (precision, recall, F1, support), one call shows everything → convenient and comprehensive.

**Where it's used:** Every classification evaluation — always look at the full report.

**What goes wrong without it:**
- `macro avg` → unweighted average (treats all classes equally). Good for imbalanced data.
- `weighted avg` → weighted by support (class frequency). Good for overall performance.
- `support` → number of samples per class. Check this to spot imbalance.

---

## Cross-Validation for Evaluation

**What:** Evaluate the model on multiple train/test splits → more reliable than a single split.

```python
from sklearn.model_selection import cross_val_score

# 5-fold cross-validation
scores = cross_val_score(model, X, y, cv=5, scoring='f1')
print(f"F1: {scores.mean():.3f} ± {scores.std():.3f}")
```

**Why it exists:** A single train/test split can be lucky or unlucky → misleading. Cross-validation averages over 5 splits → more reliable estimate of model performance.

**Where it's used:** Every model evaluation — use CV for the final assessment.

**What goes wrong without it:**
- Single split → high variance (one split might give 0.85, another 0.75). CV averages → stable estimate.
- `scoring` parameter → must match your goal. Default is accuracy → wrong for imbalanced data. Use `scoring='f1'` or `scoring='roc_auc'`.
- CV on the full dataset after tuning → data leakage. Tune on CV, then evaluate on a held-out test set.
