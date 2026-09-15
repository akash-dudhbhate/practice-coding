# Lesson 10 — Refactoring Challenges

## Refactor 01 (Easy): Manual CV
### Before
```python
scores = []
for i in range(5):
    X_train, X_test = split(X, i)
    model.fit(X_train)
    scores.append(model.score(X_test))
```
### After
```python
from sklearn.model_selection import cross_val_score
scores = cross_val_score(model, X, y, cv=5)
```

## Refactor 02 (Medium): Manual Grid Search
### Before
```python
best_score = 0
for C in [0.1, 1, 10]:
    for kernel in ["linear", "rbf"]:
        model = SVC(C=C, kernel=kernel).fit(X_train, y_train)
        score = model.score(X_test, y_test)
        if score > best_score: best_score = score; best_params = (C, kernel)
```
### After
```python
from sklearn.model_selection import GridSearchCV
gs = GridSearchCV(SVC(), {"C": [0.1, 1, 10], "kernel": ["linear", "rbf"]}, cv=5)
gs.fit(X, y)
```

## Refactor 03 (Hard): Tuning on Test Set
### Before
```python
for params in param_grid:
    model.fit(X_train, y_train)
    score = model.score(X_test, y_test)  # data leakage!
```
### After
```python
# Use CV on training set only, test set for final eval
gs = GridSearchCV(model, params, cv=5).fit(X_train, y_train)
final_score = gs.score(X_test, y_test)
```
