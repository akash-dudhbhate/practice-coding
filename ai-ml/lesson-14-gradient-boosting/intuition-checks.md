# Lesson 14 — Intuition Checks

## Check 01: How gradient boosting works
<details><summary>Answer</summary>
Trains models sequentially. Each new model corrects errors of previous ones. Like a team where each member focuses on what previous members got wrong. Combines weak learners into strong learner.
</details>

## Check 02: Learning rate
```python
learning_rate=0.1  # A
learning_rate=0.01 # B
```
<details><summary>Answer</summary>
A — fast learning, may overshoot. B — slow learning, more stable, needs more estimators. Trade-off: low rate + many trees vs high rate + few trees. Low rate usually better.
</details>

## Check 03: XGBoost vs LightGBM vs CatBoost
<details><summary>Answer</summary>
XGBoost — most popular, well-documented. LightGBM — faster, handles large data. CatBoost — best for categorical features. All are gradient boosting implementations.
</details>

## Check 04: Feature importance
```python
model.feature_importances_
```
<details><summary>Answer</summary>
Shows which features are used most in splits. Useful for feature selection. XGBoost also has SHAP values for better interpretability.
</details>

## Check 05: Overfitting signs
```python
train_score = 1.0
test_score = 0.75
```
<details><summary>Answer</summary>
Gap = overfitting. Fix: lower learning rate, fewer estimators, more regularization (max_depth, subsample), early stopping.
</details>
