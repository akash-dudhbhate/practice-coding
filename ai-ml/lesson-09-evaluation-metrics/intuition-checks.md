# Lesson 09 — Intuition Checks

## Check 01: Precision vs Recall
```python
# Precision: TP / (TP + FP) — of predicted positives, how many are right?
# Recall: TP / (TP + FN) — of actual positives, how many did we find?
```
<details><summary>Answer</summary>
Precision — when model says positive, how often is it right? (minimize false positives). Recall — of all real positives, how many did we catch? (minimize false negatives).
</details>

## Check 02: F1 score
```python
f1 = 2 * (precision * recall) / (precision + recall)
```
<details><summary>Answer</summary>
Harmonic mean of precision and recall. Balances both. 1 = perfect, 0 = worst. Use when you need a single metric for imbalanced data.
</details>

## Check 03: Confusion matrix
```python
[[TN, FP],
 [FN, TP]]
```
<details><summary>Answer</summary>
TN — true negatives (correctly negative). FP — false positives (predicted positive, actually negative). FN — false negatives (predicted negative, actually positive). TP — true positives (correctly positive).
</details>

## Check 04: ROC-AUC
```python
roc_auc_score(y_test, y_proba)
```
<details><summary>Answer</summary>
Area under ROC curve. Measures ranking ability. 0.5 = random, 1.0 = perfect. Threshold-independent. Good for comparing models.
</details>

## Check 05: When to use which metric
<details><summary>Answer</summary>
- Accuracy — balanced data
- Precision — false positives are costly (spam filter)
- Recall — false negatives are costly (cancer detection)
- F1 — balance precision and recall
- ROC-AUC — comparing models, threshold-independent
</details>
