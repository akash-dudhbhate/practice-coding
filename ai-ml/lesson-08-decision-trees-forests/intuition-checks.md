# Lesson 08 — Intuition Checks

## Check 01: How decision trees work
<details><summary>Answer</summary>
Splits data at each node to maximize information gain (or minimize Gini impurity). Creates rules like "if age > 30 and income > 50k → yes". Recursive until pure or max depth.
</details>

## Check 02: Random forest
How does random forest work?
<details><summary>Answer</summary>
Trains many decision trees on random subsets of data and features. Predicts by majority vote (classification) or average (regression). Reduces overfitting, improves generalization.
</details>

## Check 03: Feature importance
```python
model.feature_importances_
```
<details><summary>Answer</summary>
Shows how much each feature contributes to predictions. Useful for feature selection and understanding the model. Sum to 1.0.
</details>

## Check 04: Overfitting signs
```python
train_score = 1.0
test_score = 0.7
```
<details><summary>Answer</summary>
Gap between train and test = overfitting. Tree memorized training data. Fix: limit depth, use random forest, or get more data.
</details>

## Check 05: Pruning
```python
DecisionTreeClassifier(max_depth=5, min_samples_leaf=10)
```
<details><summary>Answer</summary>
Pruning limits tree growth: max_depth (tree depth), min_samples_leaf (minimum samples per leaf), min_samples_split (minimum to split a node). Prevents overfitting.
</details>
