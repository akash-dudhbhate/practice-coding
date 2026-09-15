# Lesson 08 — Decision Trees & Random Forests

## What you'll learn
- Decision tree basics (splits, leaves, paths)
- Splitting criteria (Gini impurity, entropy)
- Using sklearn DecisionTreeClassifier
- Overfitting in trees (and how to prevent it)
- Random forests (ensemble of trees)
- Feature importance
- Random forest vs decision tree (trade-offs)
- Gradient boosting (brief introduction)

## Lesson

### Decision tree
```python
from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier(max_depth=3, random_state=42)
model.fit(X_train, y_train)
```

### Random forest
```python
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42)
model.fit(X_train, y_train)
print(model.feature_importances_)
```

---

## Your Tasks

### Easy
1. `easy/p01-solve.py` — Train a decision tree on the Iris dataset. Set `max_depth=3`. Print accuracy and visualize the tree using `plot_tree`.
2. `easy/p02-solve.py` — Implement Gini impurity from scratch. Calculate Gini for a node with [3 positive, 2 negative] samples. Verify: 1 - (3/5)² - (2/5)² = 0.48.
3. `easy/p03-solve.py` — Train a decision tree with and without `max_depth` limit. Compare training and test accuracy. Show that unlimited depth overfits (100% train, lower test).

### Medium
4. `medium/p01-solve.py` — Train a random forest on `make_classification` (1000 samples, 20 features). Print accuracy. Extract and plot feature importances. Identify the top 5 features.
5. `medium/p02-solve.py` — Compare decision tree vs random forest on the same dataset. Print train/test accuracy for both. Show that random forest has better test accuracy and less overfitting.
6. `medium/p03-solve.py` — Tune `max_depth` for a decision tree: try depths 1, 3, 5, 10, 20, None. For each, record train and test accuracy. Plot both curves. Identify the optimal depth.

### Hard
7. `hard/p01-solve.py` — Build a complete classification pipeline: load Breast Cancer dataset, compare 3 models (decision tree, random forest, gradient boosting). For each: print accuracy, precision, recall, F1. Create a comparison table.
8. `hard/p02-solve.py` — Implement a simple decision tree from scratch: implement Gini impurity, find the best split, recursively build the tree. Train on a small 2D dataset. Plot the decision boundary.
9. `hard/p03-solve.py` — Build a feature importance analysis: train a random forest, get feature importances, select top 5 features, retrain with only those features. Compare accuracy before and after feature selection. Document whether reducing features hurt.

### How to work
- Write your complete Python solution.
- Remove the TODO comment when done.
- Test with `python <filename>`.
