# Lesson 12 — Refactoring Challenges

## Refactor 01 (Easy): No Class Weight
### Before
```python
model = LogisticRegression().fit(X, y)  # biased toward majority
```
### After
```python
model = LogisticRegression(class_weight="balanced").fit(X, y)
```

## Refactor 02 (Medium): Manual Oversampling
### Before
```python
minority = df[df["label"] == 1]
oversampled = pd.concat([df, minority.sample(1000, replace=True)])
```
### After
```python
from imblearn.over_sampling import RandomOverSampler
X_res, y_res = RandomOverSampler().fit_resample(X, y)
```

## Refactor 03 (Hard): Accuracy on Imbalanced
### Before
```python
print(accuracy_score(y, preds))  # 95% but all predict majority
```
### After
```python
print(classification_report(y, preds))  # shows per-class metrics
# or use balanced_accuracy_score, f1, AUC
```
