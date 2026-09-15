# Lesson 10 — Intuition Checks

## Check 01: Why cross-validation?
<details><summary>Answer</summary>
Single train/test split is noisy — score depends on which samples land in test. CV averages over k different splits, giving more reliable estimate. k=5 or 10 is standard.
</details>

## Check 02: k-fold
```python
cross_val_score(model, X, y, cv=5)
```
<details><summary>Answer</summary>
Splits data into 5 folds. Trains on 4, tests on 1. Repeats 5 times. Returns 5 scores. Average for final estimate.
</details>

## Check 03: Stratified k-fold
```python
StratifiedKFold(n_splits=5)
```
<details><summary>Answer</summary>
Each fold has same class proportion as full data. Essential for imbalanced data. Regular k-fold might have folds with no minority class.
</details>

## Check 04: Grid search
```python
GridSearchCV(model, {"C": [0.1, 1, 10]}, cv=5)
```
<details><summary>Answer</summary>
Tries all parameter combinations. For each, runs 5-fold CV. Returns best params. 3 params × 5 folds = 15 model fits.
</details>

## Check 05: Pipeline
```python
Pipeline([("scaler", StandardScaler()), ("model", LogisticRegression())])
```
<details><summary>Answer</summary>
Chains preprocessing and model. Ensures preprocessing is fit on train fold only (no leakage). Pass to cross_val_score or GridSearchCV.
</details>
