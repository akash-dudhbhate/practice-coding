# Lesson 14 — Refactoring Challenges

## Refactor 01 (Easy): GBDT Without Early Stopping
### Before
```python
model = GradientBoostingClassifier(n_estimators=1000).fit(X, y)  # may overfit
```
### After
```python
model = GradientBoostingClassifier(n_estimators=1000, validation_fraction=0.1,
                                    n_iter_no_change=10).fit(X, y)
```

## Refactor 02 (Medium): sklearn GBDT for Large Data
### Before
```python
model = GradientBoostingClassifier().fit(X_large, y_large)  # slow
```
### After
```python
import lightgbm as lgb
model = lgb.LGBMClassifier().fit(X_large, y_large)  # much faster
```

## Refactor 03 (Hard): Manual Stacking
### Before
```python
preds1 = model1.predict(X)
preds2 = model2.predict(X)
final = np.mean([preds1, preds2], axis=0)
```
### After
```python
from sklearn.ensemble import StackingClassifier
model = StackingClassifier([("rf", RandomForestClassifier()), ("gb", GradientBoostingClassifier())])
model.fit(X, y)
```
