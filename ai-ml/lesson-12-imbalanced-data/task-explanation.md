# Lesson 12 — Handling Imbalanced Data

## What you'll learn
- The imbalanced data problem (and why accuracy fails)
- Oversampling (Random, SMOTE)
- Undersampling (Random)
- Class weights (penalizing minority errors)
- SMOTE (synthetic minority oversampling)
- Evaluation metrics for imbalanced data (F1, PR-AUC)
- Threshold adjustment (lowering for higher recall)
- Stratified sampling (preserving class ratio)

## Lesson

### Class weights
```python
model = LogisticRegression(class_weight='balanced')
```

### SMOTE in pipeline
```python
from imblearn.pipeline import Pipeline
from imblearn.over_sampling import SMOTE
pipe = Pipeline([('smote', SMOTE()), ('model', RandomForestClassifier())])
```

### Stratified split
```python
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y)
```

---

## Your Tasks

### Easy
1. `easy/p01-solve.py` — Create an imbalanced dataset (95% class 0, 5% class 1). Train logistic regression. Show that accuracy is high but recall for class 1 is near 0. Print the classification report.
2. `easy/p02-solve.py` — Use `class_weight='balanced'` on the same dataset. Compare recall for class 1 with and without class weights. Print both classification reports.
3. `easy/p03-solve.py` — Use `stratify=y` in `train_test_split` on the imbalanced dataset. Verify both train and test have the same class ratio. Print class counts for each.

### Medium
4. `medium/p01-solve.py` — Apply `RandomOverSampler` and `RandomUnderSampler` to the imbalanced dataset. Train a model on each. Compare F1 scores. Print class counts before and after resampling.
5. `medium/p02-solve.py` — Apply SMOTE to the imbalanced dataset. Train a model. Compare F1 with random oversampling. Use `imblearn.pipeline.Pipeline` to ensure SMOTE is applied inside CV (no leakage).
6. `medium/p03-solve.py` — Adjust the decision threshold: train a model, get probabilities, try thresholds 0.3, 0.5, 0.7. For each, print precision, recall, F1. Find the threshold that maximizes F1.

### Hard
7. `hard/p01-solve.py` — Build a complete imbalanced data pipeline: create a 99:1 dataset, compare 4 approaches (baseline, class_weight, SMOTE, SMOTE+undersampling). For each, print F1, PR-AUC, and confusion matrix. Identify the best approach.
8. `hard/p02-solve.py` — Build a fraud detection simulation: create synthetic transaction data (amount, merchant, time, is_fraud). Handle imbalance with SMOTE. Train a model. Plot the precision-recall curve. Find the threshold that gives 80% recall. Report the precision at that threshold.
9. `hard/p03-solve.py` — Build a comparison of evaluation metrics: train a model on imbalanced data. Calculate accuracy, F1, ROC-AUC, PR-AUC. Show that accuracy and ROC-AUC look good but F1 and PR-AUC reveal the truth. Plot both ROC and PR curves. Explain which is more honest.

### How to work
- Write your complete Python solution.
- Remove the TODO comment when done.
- Test with `python <filename>`.
