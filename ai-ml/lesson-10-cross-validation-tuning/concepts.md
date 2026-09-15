# Lesson 10 — Concepts Explained (Cross-Validation & Hyperparameter Tuning)

> Read this before solving the problems. Each concept explains:
> **What** it is · **Why** it exists · **Where** it's used · **What goes wrong** without it.

---

## Why Cross-Validation?

**What:** Cross-validation (CV) splits data into multiple folds, trains on some, tests on others → more reliable than a single train/test split.

```python
# Single split: can be lucky or unlucky
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model.fit(X_train, y_train)
score = model.score(X_test, y_test)  # one number, high variance

# 5-fold CV: average over 5 splits → more reliable
scores = cross_val_score(model, X, y, cv=5)
print(f"{scores.mean():.3f} ± {scores.std():.3f}")
```

**Why it exists:** A single split might put all hard examples in the test set → low score. Or all easy ones → high score. CV averages over 5 splits → stable estimate → you trust the number.

**Where it's used:** Every model evaluation, hyperparameter tuning, model comparison.

**What goes wrong without it:**
- Single split → high variance (0.75 one run, 0.85 another) → can't trust the number.
- CV on the full dataset after tuning → data leakage → optimistic score. Tune with CV, then evaluate on a held-out test set.
- Not setting `random_state` in CV → different folds each run → non-reproducible.

---

## K-Fold Cross-Validation

**What:** Split data into K equal folds. Train on K-1, test on 1. Repeat K times, each fold is the test set once.

```python
from sklearn.model_selection import cross_val_score, KFold

# 5-fold CV
scores = cross_val_score(model, X, y, cv=5)

# Custom KFold with shuffling
kf = KFold(n_splits=5, shuffle=True, random_state=42)
scores = cross_val_score(model, X, y, cv=kf)
```

**Why it exists:** K-fold ensures every sample is in the test set exactly once → all data is used for both training and testing → efficient and fair.

**Where it's used:** Standard CV for most datasets.

**What goes wrong without it:**
- K=5 or K=10 are common. K=2 → too few splits (high variance). K=n (leave-one-out) → too many splits (slow, high variance).
- Not shuffling → if data is sorted (all class 0 first, then class 1) → some folds have only one class → error. Always shuffle.
- Stratified K-fold for classification → preserves class ratio in each fold. Use `StratifiedKFold` instead of `KFold` for imbalanced data.

---

## Stratified K-Fold

**What:** K-fold that preserves the class distribution in each fold.

```python
from sklearn.model_selection import StratifiedKFold

# For classification: use stratified to maintain class ratio
skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
scores = cross_val_score(model, X, y, cv=skf)

# If data is 90% class 0, 10% class 1:
# Regular KFold → some folds might be 100% class 0 → can't evaluate
# Stratified KFold → each fold is 90/10 → fair evaluation
```

**Why it exists:** Without stratification, imbalanced data → some folds have no minority class → model can't be evaluated on that fold → error or misleading score.

**Where it's used:** Every classification CV with imbalanced data.

**What goes wrong without it:**
- `cross_val_score` with `cv=5` on classification → sklearn automatically uses stratified k-fold. But with custom `KFold`, it doesn't → use `StratifiedKFold` explicitly.
- Stratification only works for classification (preserves class labels). For regression, use `KFold` or `StratifiedKFold` on binned y.
- Very small minority class (< K samples) → some folds still have 0 minority → stratification fails.

---

## Grid Search

**What:** Exhaustively try all combinations of hyperparameters → find the best.

```python
from sklearn.model_selection import GridSearchCV

param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [3, 5, 10, None],
    'min_samples_leaf': [1, 5, 10],
}

grid_search = GridSearchCV(
    RandomForestClassifier(),
    param_grid,
    cv=5,
    scoring='f1',
    n_jobs=-1,  # use all CPU cores
)

grid_search.fit(X_train, y_train)

print(grid_search.best_params_)   # {'max_depth': 10, 'n_estimators': 100, ...}
print(grid_search.best_score_)    # 0.85 (best CV F1)

best_model = grid_search.best_estimator_
```

**Why it exists:** Without grid search, you manually try combinations → tedious, error-prone. Grid search automates it → tries all combinations with CV → finds the best.

**Where it's used:** Every model that needs hyperparameter tuning.

**What goes wrong without it:**
- 3 * 4 * 3 = 36 combinations * 5 CV folds = 180 fits → slow. Use `n_jobs=-1` to parallelize.
- Grid search on the full dataset → data leakage. Always use `X_train` (not X) for tuning, then evaluate on `X_test`.
- Too many parameters → exponential combinations → very slow. Use `RandomizedSearchCV` for large search spaces.

---

## Randomized Search

**What:** Randomly sample hyperparameter combinations → faster than grid search for large spaces.

```python
from sklearn.model_selection import RandomizedSearchCV

param_distributions = {
    'n_estimators': [50, 100, 200, 500, 1000],
    'max_depth': [3, 5, 10, 20, None],
    'min_samples_leaf': [1, 2, 5, 10, 20],
    'max_features': ['sqrt', 'log2', None],
}

random_search = RandomizedSearchCV(
    RandomForestClassifier(),
    param_distributions,
    n_iter=20,        # try 20 random combinations
    cv=5,
    scoring='f1',
    random_state=42,
    n_jobs=-1,
)

random_search.fit(X_train, y_train)
```

**Why it exists:** Grid search with 5^4 = 625 combinations → too slow. Randomized search tries 20 random combinations → finds a near-optimal solution much faster.

**Where it's used:** Large hyperparameter search spaces, when grid search is too slow.

**What goes wrong without it:**
- `n_iter` too low → might miss the best combination. 20-50 is usually good.
- Not setting `random_state` → different results each run → non-reproducible.
- Randomized search is not guaranteed to find the best → but it's close and much faster.

---

## Hyperparameter vs Parameter

**What:**
- **Parameters:** Learned from data during training (weights, coefficients).
- **Hyperparameters:** Set BEFORE training (max_depth, learning_rate, n_estimators).

```python
# Parameters (learned):
model.coef_        # logistic regression weights
model.feature_importances_  # tree feature importance

# Hyperparameters (set by you):
model = RandomForestClassifier(
    n_estimators=100,  # hyperparameter
    max_depth=5,       # hyperparameter
)
```

**Why it exists:** Understanding the difference is crucial. You tune hyperparameters (grid search). Parameters are learned automatically. Confusing them → you try to "tune" learned parameters → doesn't make sense.

**Where it's used:** Every ML model — know which knobs are hyperparameters.

**What goes wrong without it:**
- Trying to set parameters manually → they're learned from data. You can't set `coef_` before training.
- Not tuning hyperparameters → using defaults → might be far from optimal for your data.
- Tuning on test data → data leakage → overfitting to the test set. Always tune on CV with training data only.

---

## Pipeline for Tuning

**What:** Use sklearn pipelines to prevent data leakage during tuning.

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('model', RandomForestClassifier()),
])

param_grid = {
    'model__n_estimators': [50, 100, 200],  # note 'model__' prefix
    'model__max_depth': [3, 5, 10],
}

grid_search = GridSearchCV(pipeline, param_grid, cv=5)
grid_search.fit(X_train, y_train)
# Scaling is done inside CV → no data leakage
```

**Why it exists:** Without a pipeline, scaling the full dataset before CV → the scaler sees the test fold → data leakage → optimistic scores. Pipeline ensures scaling happens inside each CV fold → honest evaluation.

**Where it's used:** Every tuning task with preprocessing (scaling, PCA, feature selection).

**What goes wrong without it:**
- Scaling before CV → test fold is scaled using test statistics → leakage → inflated scores.
- Pipeline parameter names: `model__n_estimators` (step name + __ + parameter). Forgetting `__` → error.
- Not using pipeline for feature selection → selected features include information from test fold → leakage.

---

## Learning Curves

**What:** Plot training and validation scores vs dataset size → diagnose overfitting/underfitting.

```python
from sklearn.model_selection import learning_curve
import matplotlib.pyplot as plt

train_sizes, train_scores, val_scores = learning_curve(
    model, X, y, cv=5, train_sizes=np.linspace(0.1, 1.0, 10)
)

plt.plot(train_sizes, train_scores.mean(axis=1), label='Training')
plt.plot(train_sizes, val_scores.mean(axis=1), label='Validation')
plt.xlabel('Training Set Size')
plt.ylabel('Score')
plt.legend()
```

**Why it exists:**
- Training high, validation low → overfitting → need more data or simpler model.
- Both low → underfitting → need a more complex model or better features.
- Both converging → good → more data won't help much.

**Where it's used:** Diagnosing model performance issues, deciding whether to collect more data.

**What goes wrong without it:**
- Misdiagnosing: thinking you need more data when actually the model is too simple (underfitting).
- Not checking learning curves → you don't know if more data would help → waste time collecting data that won't improve the model.
- Reading the gap: large gap = overfitting, small gap = underfitting (if both are low).
