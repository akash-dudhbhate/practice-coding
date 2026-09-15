# Lesson 01 — Intuition Checks

## Check 01: Supervised vs Unsupervised
What's the difference?
<details><summary>Answer</summary>
Supervised — labeled data (input → known output). Examples: classification, regression. Unsupervised — no labels, find patterns. Examples: clustering, dimensionality reduction.
</details>

## Check 02: Classification vs Regression
```python
# A: predict whether email is spam (spam/not spam)
# B: predict house price ($)
```
<details><summary>Answer</summary>
A — classification (discrete categories). B — regression (continuous value). If output is a category → classification. If output is a number → regression.
</details>

## Check 03: Overfitting
What is overfitting?
<details><summary>Answer</summary>
Model memorizes training data, fails on new data. Like a student who memorizes answers but can't solve new problems. Signs: high train score, low test score.
</details>

## Check 04: Features vs Labels
```python
X = data[["age", "income", "location"]]  # ?
y = data["purchased"]  # ?
```
<details><summary>Answer</summary>
X = features (inputs used for prediction). y = label/target (what we predict). Features describe, labels are what we want to predict.
</details>

## Check 05: Train/test split ratio
Why not 50/50?
<details><summary>Answer</summary>
More training data = better model. But need enough test data for reliable evaluation. 80/20 or 70/30 is standard. Small datasets may need cross-validation instead.
</details>
