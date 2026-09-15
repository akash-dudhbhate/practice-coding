# Lesson 14 — Concepts Explained (Gradient Boosting)

> Read this before solving the problems. Each concept explains:
> **What** it is · **Why** it exists · **Where** it's used · **What goes wrong** without it.

---

## What is Gradient Boosting?

**What:** An ensemble method that builds trees sequentially — each tree corrects the errors of the previous ones.

```python
# Concept:
# Tree 1: fits the data → predictions have errors (residuals)
# Tree 2: fits the residuals of Tree 1 → reduces errors
# Tree 3: fits the residuals of Tree 1+2 → further reduces errors
# ...
# Final prediction = sum of all trees

# Like a team where each member fixes what the previous got wrong
```

**Why it exists:** Random forests build independent trees (no learning from mistakes). Gradient boosting builds sequential trees that learn from errors → often more accurate → dominates Kaggle competitions for tabular data.

**Where it's used:** Tabular data classification/regression, Kaggle competitions, production ML where accuracy matters.

**What goes wrong without it:**
- Too many trees → overfitting (each tree fits noise). Use early stopping.
- Learning rate too high → overfits quickly. Use 0.01-0.1.
- Not scaling → gradient boosting is tree-based → no scaling needed, but outliers can still cause issues.

---

## How Gradient Boosting Works

**What:** The algorithm step by step:

```python
# 1. Start with a simple prediction (mean of y for regression)
initial_pred = y_train.mean()

# 2. Calculate residuals (errors)
residuals = y_train - initial_pred

# 3. Train a tree to predict the residuals
tree1 = DecisionTreeRegressor(max_depth=3)
tree1.fit(X_train, residuals)

# 4. Update predictions: pred += learning_rate * tree1.predict(X)
pred = initial_pred + learning_rate * tree1.predict(X_train)

# 5. Calculate new residuals
residuals = y_train - pred

# 6. Train tree2 on new residuals, and so on...
```

**Why it exists:** Understanding the algorithm helps you tune it. The learning rate controls how much each tree contributes → small LR = slow but stable, large LR = fast but risky.

**Where it's used:** Conceptual understanding → helps with hyperparameter tuning.

**What goes wrong without it:**
- Forgetting the learning rate → each tree's contribution is too large → overfits. Always use a small LR (0.01-0.1).
- Not understanding residuals → you don't know what the trees are learning → can't debug.
- Deep trees in boosting → each tree is too powerful → overfits. Use shallow trees (max_depth=3-5).

---

## Using scikit-learn Gradient Boosting

**What:** sklearn provides `GradientBoostingClassifier` and `GradientBoostingRegressor`.

```python
from sklearn.ensemble import GradientBoostingClassifier

model = GradientBoostingClassifier(
    n_estimators=100,      # number of trees
    learning_rate=0.1,     # contribution of each tree
    max_depth=3,           # tree depth (keep shallow)
    random_state=42,
)
model.fit(X_train, y_train)

# Early stopping
model = GradientBoostingClassifier(
    n_estimators=500,
    learning_rate=0.01,
    n_iter_no_change=10,   # stop if no improvement for 10 rounds
    validation_fraction=0.1,
    tol=1e-4,
)
```

**Why it exists:** Without sklearn, you'd implement the boosting algorithm manually → complex. sklearn provides optimized implementation with early stopping → prevents overfitting.

**Where it's used:** Every gradient boosting task in Python (though XGBoost/LightGBM are often preferred for production).

**What goes wrong without it:**
- `n_estimators=500` without early stopping → might overfit. Use `n_iter_no_change=10`.
- `max_depth=10` → trees too complex → overfits. Use 3-5 for boosting.
- Not using `learning_rate` with `n_estimators` together → low LR needs more trees, high LR needs fewer.

---

## XGBoost

**What:** Extreme Gradient Boosting — a faster, more regularized implementation.

```python
from xgboost import XGBClassifier

model = XGBClassifier(
    n_estimators=100,
    learning_rate=0.1,
    max_depth=3,
    subsample=0.8,         # random fraction of data per tree
    colsample_bytree=0.8,  # random fraction of features per tree
    reg_alpha=0.1,         # L1 regularization
    reg_lambda=1.0,        # L2 regularization
    random_state=42,
    n_jobs=-1,
)
model.fit(X_train, y_train)

# Early stopping
model.fit(
    X_train, y_train,
    eval_set=[(X_test, y_test)],
    early_stopping_rounds=10,
    verbose=False,
)
```

**Why it exists:** sklearn's gradient boosting is slow and lacks features. XGBoost is faster (parallelized), more regularized (prevents overfitting), and handles missing data → dominates tabular ML.

**Where it's used:** Kaggle competitions, production ML, any tabular data task where accuracy matters.

**What goes wrong without it:**
- Not installing: `pip install xgboost`.
- `early_stopping_rounds` without `eval_set` → no validation data → can't stop → error.
- Too many parameters → hard to tune. Start with defaults, then tune learning_rate, max_depth, n_estimators.

---

## LightGBM and CatBoost

**What:** Other popular gradient boosting libraries.

```python
# LightGBM: faster on large datasets, leaf-wise growth
from lightgbm import LGBMClassifier
model = LGBMClassifier(
    n_estimators=100, learning_rate=0.1, max_depth=-1,  # -1 = no limit
    num_leaves=31,  # main parameter (instead of max_depth)
)

# CatBoost: handles categorical features automatically
from catboost import CatBoostClassifier
model = CatBoostClassifier(
    iterations=100, learning_rate=0.1, depth=6,
    cat_features=['city', 'category'],  # specify categorical columns
)
```

**Why it exists:**
- LightGBM → faster than XGBoost on large data, handles high-dimensional features well.
- CatBoost → handles categorical features without manual encoding → great for real-world data with many categories.

**Where it's used:** LightGBM for large datasets. CatBoost for data with many categorical features.

**What goes wrong without it:**
- LightGBM with small data → can overfit (leaf-wise growth is aggressive). Use `num_leaves` carefully.
- CatBoost → slower to train than LightGBM but often more accurate on categorical data.
- Not comparing libraries → you might miss that one works better for your data.

---

## Learning Rate and n_estimators

**What:** The two most important gradient boosting parameters — they work together.

```python
# Rule of thumb: low learning_rate + high n_estimators = best (but slow)
# High learning_rate + low n_estimators = fast but suboptimal

# Common combinations:
# learning_rate=0.1, n_estimators=100  → fast, decent
# learning_rate=0.01, n_estimators=1000 → slow, better
# learning_rate=0.001, n_estimators=5000 → very slow, best (if enough data)

# Always use early stopping to find the right n_estimators
model = XGBClassifier(
    n_estimators=1000,     # upper bound
    learning_rate=0.01,    # small LR
    early_stopping_rounds=20,
)
model.fit(X_train, y_train, eval_set=[(X_test, y_test)])
print(f"Best iteration: {model.best_iteration}")  # actual trees used
```

**Why it exists:** The learning rate controls how much each tree contributes. Small LR → each tree contributes a little → need many trees → slow but accurate. Large LR → each tree contributes a lot → few trees → fast but less accurate.

**Where it's used:** Every gradient boosting model — always tune these together.

**What goes wrong without it:**
- `learning_rate=0.3, n_estimators=1000` → overfits (too much total contribution).
- `learning_rate=0.001, n_estimators=100` → underfits (not enough total contribution).
- Not using early stopping → you guess n_estimators → might overfit or underfit.

---

## Regularization in Boosting

**What:** Techniques to prevent overfitting in gradient boosting.

```python
# 1. Tree-specific regularization
model = XGBClassifier(
    max_depth=3,           # shallow trees
    min_child_weight=5,    # minimum samples per leaf
    gamma=0.1,             # minimum loss reduction to split
)

# 2. Random subsampling
model = XGBClassifier(
    subsample=0.8,         # use 80% of data per tree
    colsample_bytree=0.8,  # use 80% of features per tree
)

# 3. L1/L2 regularization
model = XGBClassifier(
    reg_alpha=0.1,         # L1 (lasso)
    reg_lambda=1.0,        # L2 (ridge)
)
```

**Why it exists:** Gradient boosting is prone to overfitting (each tree fits the residuals → can fit noise). Regularization constrains the trees → better generalization.

**Where it's used:** Every XGBoost/LightGBM model — especially with limited data.

**What goes wrong without it:**
- No regularization + many trees → overfits → great training, poor test.
- Too much regularization → underfits → poor on both.
- Not tuning regularization → defaults might not be optimal for your data. Use grid search.

---

## Feature Importance in Boosting

**What:** Gradient boosting provides feature importance scores.

```python
import matplotlib.pyplot as plt

importances = model.feature_importances_
# Or for XGBoost:
importances = model.feature_importances_

# Plot
sorted_idx = importances.argsort()[::-1]
plt.bar(range(len(importances)), importances[sorted_idx])
plt.xticks(range(len(importances)), [feature_names[i] for i in sorted_idx], rotation=45)
```

**Why it exists:** Like random forests, gradient boosting ranks features → helps with feature selection and model interpretation.

**Where it's used:** Feature selection, model interpretation, understanding the problem.

**What goes wrong without it:**
- Different importance types: 'weight' (split count), 'gain' (loss reduction), 'cover' (samples covered). Use 'gain' for the most informative measure.
- High-cardinality features get inflated importance → use permutation importance for fairness.
- Not using importance for feature selection → you might keep useless features → slower, overfits.
