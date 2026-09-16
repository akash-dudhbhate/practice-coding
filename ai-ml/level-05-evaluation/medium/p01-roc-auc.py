"""
LEVEL 05 — Model Evaluation
MEDIUM P01 — ROC Curve and AUC
========================================

CONCEPT:
  ROC curve = plot of True Positive Rate vs False Positive Rate
  across every possible threshold.
  AUC = area under that curve. 1.0 = perfect, 0.5 = random.

  You need predict_proba (probabilities), not just predictions.

PROBLEM:
  Write `plot_roc()` that:
    1. make_classification(200, 10 features, seed=42); split 80/20
    2. LogisticRegression(seed=42), get predict_proba[:, 1]
    3. roc_curve + auc → plot the curve, save 'roc_curve.png'
    4. Return the AUC value

TRY THIS INPUT:
  ```python
  a = plot_roc()
  print(f"{a:.4f}")
  ```

EXPECTED OUTPUT:
  ```
  0.8854
  ```

HINT:
  from sklearn.metrics import roc_curve, auc
  fpr, tpr, _ = roc_curve(y_test, y_prob); auc(fpr, tpr)

CHECK: python3 check.py medium/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# a = plot_roc()
# print(a)
