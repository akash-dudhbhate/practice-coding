# Lesson 12 — Concepts Explained (Handling Imbalanced Data)

> Read this before solving the problems. Each concept explains:
> **What** it is · **Why** it exists · **Where** it's used · **What goes wrong** without it.

---

## The Imbalanced Data Problem

**What:** When one class vastly outnumbers the other(s). E.g., 99% legitimate transactions, 1% fraud.

```python
import numpy as np
# 1000 samples: 990 class 0, 10 class 1
y = np.array([0]*990 + [1]*10)

# Problem: model predicts all as 0 → 99% accuracy → but catches 0% fraud
# Accuracy is misleading → need different metrics and techniques
```

**Why it exists:** Real-world data is often imbalanced — fraud, disease, churn, defects. Models trained on imbalanced data bias toward the majority class → minority class (the one we care about) is missed.

**Where it's used:** Fraud detection, medical diagnosis, anomaly detection, rare event prediction.

**What goes wrong without it:**
- 99% accuracy on imbalanced data → looks great but is useless (predicts majority class only).
- Model never sees enough minority examples → can't learn the minority pattern.
- Standard train/test split → some folds might have no minority class → error.

---

## Resampling: Oversampling

**What:** Duplicate minority class samples to balance the dataset.

```python
from imblearn.over_sampling import RandomOverSampler, SMOTE

# Random oversampling: duplicate minority samples
ros = RandomOverSampler(random_state=42)
X_resampled, y_resampled = ros.fit_resample(X, y)

# SMOTE: synthesize new minority samples
smote = SMOTE(random_state=42)
X_resampled, y_resampled = smote.fit_resample(X, y)
# Creates synthetic samples by interpolating between minority neighbors
```

**Why it exists:** Without oversampling, the model sees few minority examples → can't learn. Oversampling gives the model more minority examples → learns the pattern better.

**Where it's used:** Imbalanced classification — fraud, disease, churn.

**What goes wrong without it:**
- Random oversampling → duplicates → overfitting (same samples seen multiple times).
- SMOTE → creates synthetic samples → better than duplication, but can create unrealistic samples at class boundaries.
- Oversampling before train/test split → synthetic samples leak into test → inflated scores. Always resample ONLY the training fold.

---

## Resampling: Undersampling

**What:** Remove majority class samples to balance the dataset.

```python
from imblearn.under_sampling import RandomUnderSampler

rus = RandomUnderSampler(random_state=42)
X_resampled, y_resampled = rus.fit_resample(X, y)
# 990 majority → 10 (matches minority count)
```

**Why it exists:** Without undersampling, the majority class dominates → model biases toward it. Undersampling reduces the majority → balanced training → model learns both classes equally.

**Where it's used:** When you have plenty of data and can afford to discard majority samples.

**What goes wrong without it:**
- Random undersampling → discards potentially useful majority data → information loss.
- Undersampling to match a tiny minority (10 samples) → training set of 20 → too small → poor model.
- Combining over + undersampling (SMOTE + Tomek) → often better than either alone.

---

## Class Weights

**What:** Penalize errors on the minority class more heavily during training.

```python
from sklearn.linear_model import LogisticRegression

# 'balanced' → automatically adjusts weights inversely proportional to class frequency
model = LogisticRegression(class_weight='balanced')

# Manual weights
model = LogisticRegression(class_weight={0: 1, 1: 10})
# Error on class 1 costs 10x more than error on class 0
```

**Why it exists:** Without class weights, the model treats all errors equally → optimizing accuracy → predicts majority. Class weights make minority errors expensive → model pays attention to the minority.

**Where it's used:** When you don't want to resample (preserve data) but want balanced learning. Most sklearn classifiers support `class_weight`.

**What goes wrong without it:**
- `class_weight='balanced'` → might overcompensate → too many false positives. Tune the weight.
- Not all models support class weights → check the documentation.
- Class weights + resampling → double-counting → too aggressive. Use one or the other.

---

## SMOTE (Synthetic Minority Oversampling)

**What:** Create synthetic minority samples by interpolating between existing minority samples.

```python
from imblearn.over_sampling import SMOTE
from imblearn.pipeline import Pipeline  # NOTE: imblearn's Pipeline, not sklearn's

pipeline = Pipeline([
    ('smote', SMOTE(random_state=42)),
    ('model', RandomForestClassifier()),
])

# SMOTE is applied inside CV folds → no data leakage
scores = cross_val_score(pipeline, X, y, cv=5, scoring='f1')
```

**Why it exists:** Random oversampling duplicates → overfitting. SMOTE creates new, synthetic samples → more diverse training data → less overfitting. The synthetic samples are realistic (interpolated between real neighbors).

**Where it's used:** The most popular oversampling technique for tabular imbalanced data.

**What goes wrong without it:**
- SMOTE before train/test split → synthetic samples in test → leakage. Use imblearn's Pipeline (applies SMOTE inside CV).
- SMOTE on high-dimensional data (text, images) → synthetic samples are noisy → poor results. Use SMOTE-NC for mixed data types.
- SMOTE creates samples between ANY two minority neighbors → can bridge across class boundaries → noisy samples. Use SMOTE + Tomek links to clean boundaries.

---

## Evaluation for Imbalanced Data

**What:** Use the right metrics — NOT accuracy.

```python
from sklearn.metrics import (
    classification_report, f1_score, precision_recall_curve,
    average_precision_score, roc_auc_score
)

# F1, precision, recall → better than accuracy
print(classification_report(y_test, y_pred))

# PR-AUC → best for imbalanced data
pr_auc = average_precision_score(y_test, y_probs)

# ROC-AUC → can be misleading for extreme imbalance
roc_auc = roc_auc_score(y_test, y_probs)
```

**Why it exists:** Accuracy is dominated by the majority class. F1, precision, recall focus on the minority class → honest evaluation. PR-AUC is the gold standard for imbalanced data.

**Where it's used:** Every imbalanced classification evaluation.

**What goes wrong without it:**
- Reporting accuracy → 99% looks great but the model catches 0% of the minority → useless.
- Using ROC-AUC for extreme imbalance → can look good even when PR-AUC is terrible. Always check PR-AUC.
- Not looking at the confusion matrix → can't see if the model is catching the minority at all.

---

## Threshold Adjustment

**What:** Lower the decision threshold to catch more minority samples.

```python
# Default threshold: 0.5
# Lower threshold: 0.3 → predict positive more often → higher recall, lower precision

y_probs = model.predict_proba(X_test)[:, 1]
y_pred_adjusted = (y_probs > 0.3).astype(int)

# Now the model catches more minority samples (higher recall)
# But also has more false positives (lower precision)
```

**Why it exists:** Default threshold (0.5) is optimized for balanced data. For imbalanced data, the model is conservative (rarely predicts minority) → low recall. Lowering the threshold → predicts minority more often → catches more → higher recall.

**Where it's used:** When recall is more important than precision (e.g., disease screening — better to have false alarms than miss cases).

**What goes wrong without it:**
- Threshold too low (0.1) → predicts almost everything as positive → high recall, terrible precision → too many false alarms.
- Not using CV to choose the threshold → overfitting to the test set. Use a validation set.
- Not documenting the threshold → others use 0.5 → different results → confusion.

---

## Stratified Sampling

**What:** Ensure train/test splits preserve the class ratio.

```python
from sklearn.model_selection import train_test_split, StratifiedKFold

# Stratified train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y  # preserves class ratio
)

# Stratified K-fold
skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
```

**Why it exists:** Without stratification, a random split might put all minority samples in the test set → training set has no minority → model can't learn. Stratification ensures both sets have the same class ratio → fair evaluation.

**Where it's used:** Every imbalanced classification — always use `stratify=y` in train_test_split.

**What goes wrong without it:**
- Random split on 1% minority → some folds might have 0% minority → model can't train or evaluate.
- Forgetting `stratify=y` → train set might be 99.5% majority, test 98.5% → inconsistent → unreliable.
- `cross_val_score` with `cv=5` on classification → sklearn auto-uses stratified. But custom `KFold` → not stratified → use `StratifiedKFold`.
