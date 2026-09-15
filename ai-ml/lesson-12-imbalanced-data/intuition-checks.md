# Lesson 12 — Intuition Checks

## Check 01: What is class imbalance?
<details><summary>Answer</summary>
One class has many more samples than others. E.g., 99% healthy, 1% sick. Model biased toward majority. Accuracy misleading.
</details>

## Check 02: Strategies
What are the main strategies for imbalanced data?
<details><summary>Answer</summary>
1. Resampling — oversample minority (SMOTE), undersample majority
2. Class weights — penalize minority errors more
3. Different threshold — lower decision threshold for minority
4. Different metric — F1, precision-recall AUC
5. Anomaly detection — treat minority as anomaly
</details>

## Check 03: SMOTE
```python
from imblearn.over_sampling import SMOTE
X_res, y_res = SMOTE().fit_resample(X_train, y_train)
```
<details><summary>Answer</summary>
Synthetic Minority Oversampling Technique — creates new minority samples by interpolating between existing ones. Better than random duplication.
</details>

## Check 04: Class weights
```python
LogisticRegression(class_weight="balanced")
```
<details><summary>Answer</summary>
Automatically adjusts weights inversely proportional to class frequency. Minority class errors cost more. No resampling needed.
</details>

## Check 05: PR-AUC vs ROC-AUC
<details><summary>Answer</summary>
ROC-AUC can be misleading on imbalanced data (optimistic). PR-AUC is more informative — focuses on positive class. Use PR-AUC for imbalanced classification.
</details>
