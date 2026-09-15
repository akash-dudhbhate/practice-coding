# Lesson 08 — Concepts Explained (Decision Trees & Random Forests)

> Read this before solving the problems. Each concept explains:
> **What** it is · **Why** it exists · **Where** it's used · **What goes wrong** without it.

---

## Decision Trees

**What:** A tree-like model that makes decisions by splitting data based on feature values.

```python
# Example: should I play tennis?
#           [Outlook?]
#          /     |      \
#    Sunny    Overcast    Rainy
#      |        |          |
#   [Windy?]  PLAY      [Windy?]
#   /    \              /    \
# True  False         True  False
#  |      |            |      |
# NO    YES           NO     YES
```

**Why it exists:** Decision trees are interpretable (you can trace the path), handle non-linear data, and work with both numerical and categorical features. They're the building block of more powerful models (random forests, gradient boosting).

**Where it's used:** Medical diagnosis, loan approval, customer segmentation, any decision-making process that needs interpretability.

**What goes wrong without it:**
- Deep trees overfit (memorize training data) → poor test performance. Limit `max_depth`.
- Small changes in data → completely different tree → unstable. Use random forests for stability.
- Trees bias toward features with more values (high-cardinality features). Use information gain ratio or limit splits.

---

## How Trees Split (Gini, Entropy)

**What:** Trees split nodes using impurity measures — Gini impurity or entropy.

```python
# Gini impurity: probability of misclassifying a random sample
# Gini = 1 - sum(p_i²)  where p_i is the probability of class i
# Gini = 0 → pure node (all same class)
# Gini = 0.5 → 50/50 split (maximum impurity for binary)

# Entropy: measure of disorder
# Entropy = -sum(p_i * log2(p_i))
# Entropy = 0 → pure node
# Entropy = 1 → maximum impurity (binary)

# Information Gain = parent impurity - weighted child impurity
# Tree picks the split that maximizes information gain
```

**Why it exists:** Without a splitting criterion, the tree doesn't know which feature to split on. Gini and entropy quantify how "mixed" a node is → the tree picks splits that reduce impurity → pure leaf nodes.

**Where it's used:** Inside every decision tree algorithm. You usually don't calculate it manually, but understanding it helps you tune the tree.

**What goes wrong without it:**
- Gini vs entropy → usually similar results. Gini is faster (no log computation). Entropy is more interpretable (bits of information).
- Forgetting that trees are greedy → each split is locally optimal, not globally. The tree may not find the best overall structure.
- Impurity = 0 in a leaf → pure, but might be overfitting (one sample per leaf).

---

## Using scikit-learn Decision Trees

**What:** sklearn provides `DecisionTreeClassifier` and `DecisionTreeRegressor`.

```python
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

model = DecisionTreeClassifier(
    max_depth=3,           # limit depth to prevent overfitting
    min_samples_leaf=5,    # minimum samples in a leaf
    criterion='gini',      # or 'entropy'
    random_state=42,
)
model.fit(X_train, y_train)

predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)

# Visualize the tree
plot_tree(model, feature_names=feature_names, class_names=class_names)
```

**Why it exists:** Without sklearn, you'd implement the tree-building algorithm (recursive splitting, impurity calculation) manually → complex. sklearn provides optimized implementation + visualization.

**Where it's used:** Every decision tree task, and as a building block for ensemble methods.

**What goes wrong without it:**
- No `max_depth` → tree grows until pure leaves → overfitting. Always set `max_depth`.
- `min_samples_leaf=1` → leaves with 1 sample → overfitting. Set to 5+ for stability.
- Not setting `random_state` → different tree every run → non-reproducible. Always set it.

---

## Overfitting in Decision Trees

**What:** Deep trees memorize training data → perfect training accuracy, poor test accuracy.

```python
# Overfitting example
deep_tree = DecisionTreeClassifier()  # no limits
deep_tree.fit(X_train, y_train)
print(deep_tree.score(X_train, y_train))  # 1.0 (100% — memorized)
print(deep_tree.score(X_test, y_test))    # 0.75 (poor generalization)

# Fix: limit depth
pruned_tree = DecisionTreeClassifier(max_depth=3, min_samples_leaf=5)
pruned_tree.fit(X_train, y_train)
print(pruned_tree.score(X_train, y_train))  # 0.88 (not perfect)
print(pruned_tree.score(X_test, y_test))    # 0.85 (better generalization)
```

**Why it exists:** Understanding overfitting is crucial. Without limits, trees grow until each leaf has one sample → 100% training accuracy → useless for new data. Pruning (limiting depth, min samples) prevents this.

**Where it's used:** Every decision tree model — always tune `max_depth` and `min_samples_leaf`.

**What goes wrong without it:**
- Training accuracy = 100% → red flag for overfitting. Always check test accuracy.
- Too much pruning (max_depth=1) → underfitting (stump → can't capture patterns).
- Use cross-validation to find the optimal depth → don't tune on test data.

---

## Random Forests

**What:** An ensemble of many decision trees, each trained on a random subset of data and features.

```python
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(
    n_estimators=100,      # number of trees
    max_depth=5,           # limit each tree
    max_features='sqrt',   # random features per split
    random_state=42,
)
model.fit(X_train, y_train)

# Prediction: majority vote across all trees
predictions = model.predict(X_test)

# Feature importance
importances = model.feature_importances_
```

**Why it exists:** A single tree is unstable (small data change → different tree). Random forests average many trees → stable, accurate, and resistant to overfitting. The "random" part (random data + random features) ensures trees are diverse → ensemble is powerful.

**Where it's used:** Classification and regression tasks where accuracy matters more than interpretability — fraud detection, medical diagnosis, recommendation.

**What goes wrong without it:**
- Too many trees (n_estimators=1000) → slow training, diminishing returns. 100 is usually enough.
- Not setting `max_depth` → each tree overfits → but averaging saves random forests. Still, limiting depth improves speed.
- `max_features='sqrt'` is good for classification. For regression, use `max_features='log2'` or `1.0` (all features).

---

## Feature Importance

**What:** Random forests can rank features by how much they improve the splits.

```python
import numpy as np
import matplotlib.pyplot as plt

importances = model.feature_importances_
indices = np.argsort(importances)[::-1]

# Plot
plt.bar(range(len(importances)), importances[indices])
plt.xticks(range(len(importances)), [feature_names[i] for i in indices], rotation=45)
plt.title("Feature Importances")
```

**Why it exists:** Without feature importance, you don't know which features matter → can't simplify the model or understand the problem. Random forests provide this for free → valuable insight.

**Where it's used:** Feature selection, model interpretation, understanding the problem domain.

**What goes wrong without it:**
- Feature importance is model-specific → different models may rank features differently. Don't treat it as ground truth.
- High-cardinality features (many unique values) get inflated importance → bias. Use permutation importance for a fair assessment.
- Correlated features → importance is split between them → each looks less important than it is.

---

## Random Forest vs Decision Tree

**What:** When to use which:

| Decision Tree | Random Forest |
|---|---|
| Interpretable (can trace the path) | Black box (100 trees) |
| Fast to train and predict | Slower (100 trees) |
| Prone to overfitting | Resistant to overfitting |
| Unstable (data change → different tree) | Stable (averages many trees) |
| Good for understanding | Good for accuracy |

**Why it exists:** Understanding the trade-off helps you choose. Need to explain the model? → single tree. Need maximum accuracy? → random forest.

**Where it's used:** Single tree for interpretation and simple rules. Random forest for production models where accuracy matters.

**What goes wrong without it:**
- Using a single tree for production → unstable, overfits → poor real-world performance.
- Using random forest when you need to explain decisions → can't trace a single path through 100 trees.
- Not comparing both → you might miss that a single tree is "good enough" and much simpler.

---

## Gradient Boosting (Brief)

**What:** Another ensemble method — builds trees sequentially, each correcting the previous tree's errors.

```python
from sklearn.ensemble import GradientBoostingClassifier

model = GradientBoostingClassifier(
    n_estimators=100,
    learning_rate=0.1,
    max_depth=3,
)
# Tree 1: fits the data
# Tree 2: fits the residuals (errors of tree 1)
# Tree 3: fits the residuals of tree 1+2
# ... and so on
```

**Why it exists:** Random forests build trees independently (parallel). Gradient boosting builds trees sequentially (each learns from previous mistakes) → often more accurate, but prone to overfitting if learning rate is too high.

**Where it's used:** Kaggle competitions, tabular data, any task where maximum accuracy is needed. XGBoost and LightGBM are popular implementations.

**What goes wrong without it:**
- `learning_rate` too high → overfits quickly. Use 0.01-0.1.
- `n_estimators` too high with high learning rate → overfits. Use early stopping.
- Slower to train than random forest (sequential, can't parallelize). But often more accurate.
