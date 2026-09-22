"""
LEVEL 05 — Model Evaluation
HARD P02 — Multi-Model Comparison Table
========================================

CONCEPT:
  Never trust one metric or one model. Compare several models on
  several metrics: accuracy (overall), F1 (balance), AUC (ranking).

PROBLEM:
  Write `compare_all()` that:
    1. make_classification(500, 10 features, seed=42); split 80/20
    2. Trains 5 models: LogisticRegression, RandomForest,
       GradientBoosting, SVC(probability=True), KNN — all seed=42
    3. Returns dict: {name: {"accuracy": x, "f1": x, "auc": x}}

TRY THIS INPUT:
  ```python
  r = compare_all()
  print(r['Random Forest']['accuracy'])   # 0.94
  print(r['Gradient Boosting']['auc'])    # ~0.99
  ```

EXPECTED OUTPUT:
  ```
  Logistic Regression    acc=0.8800 f1=0.8723 auc=0.9461
  Random Forest          acc=0.9400 f1=0.9348 auc=0.9893
  Gradient Boosting      acc=0.9500 f1=0.9462 auc=0.9948
  SVM                    acc=0.8800 f1=0.8723 auc=0.9674
  KNN                    acc=0.9000 f1=0.8913 auc=0.9593
  ```

HINT:
  roc_auc_score needs probabilities → model.predict_proba(X_test)[:, 1]

CHECK: python3 check.py hard/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# r = compare_all()
# print(r['Gradient Boosting'])
