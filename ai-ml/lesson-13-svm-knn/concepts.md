# Lesson 13 — Concepts Explained (SVM & KNN)

> Read this before solving the problems. Each concept explains:
> **What** it is · **Why** it exists · **Where** it's used · **What goes wrong** without it.

---

## K-Nearest Neighbors (KNN)

**What:** KNN classifies a new point by looking at its K nearest neighbors and taking a majority vote.

```python
from sklearn.neighbors import KNeighborsClassifier

model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train, y_train)
predictions = model.predict(X_test)

# For a new point:
# 1. Calculate distance to all training points
# 2. Find the 5 nearest ones
# 3. Majority vote → predicted class
```

**Why it exists:** KNN is the simplest ML algorithm — no training, just memorize the data. It's intuitive (similar things are near each other) and works well for low-dimensional data.

**Where it's used:** Recommendation systems, simple classification, baseline models, anomaly detection.

**What goes wrong without it:**
- Not scaling features → features with large ranges dominate the distance → KNN fails. Always scale.
- K too small (1) → overfitting (noise dominates). K too large (n) → underfitting (predicts majority class). Use CV to find K.
- High-dimensional data → distance becomes meaningless (curse of dimensionality) → KNN fails. Use PCA or a different model.

---

## Choosing K

**What:** The number of neighbors to consider. The most important KNN hyperparameter.

```python
# Try different K values
for k in [1, 3, 5, 7, 10, 20, 50]:
    model = KNeighborsClassifier(n_neighbors=k)
    scores = cross_val_score(model, X_scaled, y, cv=5)
    print(f"K={k}: {scores.mean():.3f}")

# Rule of thumb: K = sqrt(n_samples)
import math
k = math.isqrt(len(X_train))  # ~sqrt(n)
# Use odd K for binary classification to avoid ties
```

**Why it exists:** K controls the bias-variance tradeoff. Small K → low bias, high variance (overfitting). Large K → high bias, low variance (underfitting). The right K balances both.

**Where it's used:** Every KNN model — always tune K.

**What goes wrong without it:**
- K=1 → every point is its own nearest neighbor → overfitting → 100% training accuracy, poor test.
- K=n (all points) → predicts majority class for everything → underfitting.
- Even K for binary classification → ties → KNN picks class 0 by default → biased. Use odd K.

---

## Distance Metrics

**What:** How "near" is defined.

```python
# Euclidean (default): straight-line distance
model = KNeighborsClassifier(n_neighbors=5, metric='euclidean')

# Manhattan: sum of absolute differences (city block)
model = KNeighborsClassifier(n_neighbors=5, metric='manhattan')

# Cosine: angle between vectors (good for text)
from sklearn.neighbors import KNeighborsClassifier
model = KNeighborsClassifier(n_neighbors=5, metric='cosine')
```

**Why it exists:** Different metrics are appropriate for different data. Euclidean for general use, Manhattan for grid-like data, cosine for text/high-dimensional data.

**Where it's used:** KNN, SVM (kernel), clustering — any distance-based algorithm.

**What goes wrong without it:**
- Euclidean on high-dimensional data → all distances are similar → KNN can't distinguish neighbors. Use cosine.
- Manhattan on data with outliers → less sensitive than Euclidean (no squaring).
- Not scaling → distance is dominated by large-scale features → wrong neighbors.

---

## Support Vector Machines (SVM)

**What:** SVM finds the optimal hyperplane that separates classes with the maximum margin.

```python
from sklearn.svm import SVC

model = SVC(kernel='linear', C=1.0)
model.fit(X_train, y_train)

# SVM finds the line that:
# 1. Separates the classes
# 2. Has the maximum margin (distance to nearest points)
# 3. The nearest points are "support vectors"
```

**Why it exists:** SVM maximizes the margin → the separation is as wide as possible → better generalization to new data. Small margin → overfitting. Large margin → robust.

**Where it's used:** Image classification, text classification, bioinformatics — any classification where a clear boundary exists.

**What goes wrong without it:**
- Not scaling → SVM is distance-based → large-scale features dominate → poor boundary. Always scale.
- C too high → overfitting (narrow margin, fits noise). C too low → underfitting (wide margin, misclassifies).
- Linear kernel on non-linear data → poor performance. Use RBF or polynomial kernel.

---

## SVM Kernels

**What:** Kernels transform data into a higher-dimensional space where it's linearly separable.

```python
# Linear kernel: for linearly separable data
model = SVC(kernel='linear')

# RBF kernel: for non-linear data (most common)
model = SVC(kernel='rbf', C=1.0, gamma='scale')

# Polynomial kernel: for polynomial boundaries
model = SVC(kernel='poly', degree=3)

# Sigmoid kernel: like a neural network
model = SVC(kernel='sigmoid')
```

**Why it exists:** Without kernels, SVM can only separate linearly. Non-linear data → poor performance. Kernels project data to a higher dimension → linear separation becomes possible → SVM handles non-linear data.

**Where it's used:** Non-linear classification — most real-world data is non-linear.

**What goes wrong without it:**
- RBF kernel with `gamma` too high → overfitting (each point is its own support vector). Use `gamma='scale'` (default).
- Polynomial with high degree → overfitting + slow. Use degree 2-4.
- Not trying different kernels → might miss that RBF works much better than linear for your data.

---

## SVM Parameters (C and gamma)

**What:** The two key SVM hyperparameters.

```python
# C: regularization (inverse) — controls margin width
# High C → narrow margin, few violations → overfitting
# Low C → wide margin, more violations → underfitting

# gamma: kernel coefficient (RBF) — controls influence range
# High gamma → each point has small influence → complex boundary → overfitting
# Low gamma → each point has large influence → simple boundary → underfitting

# Grid search for C and gamma
param_grid = {
    'C': [0.1, 1, 10, 100],
    'gamma': ['scale', 0.001, 0.01, 0.1, 1],
}
grid = GridSearchCV(SVC(kernel='rbf'), param_grid, cv=5)
```

**Why it exists:** C and gamma control the bias-variance tradeoff. Tuning them is essential for good SVM performance. Default values (C=1, gamma='scale') are a starting point, not optimal.

**Where it's used:** Every SVM model — always tune C and gamma.

**What goes wrong without it:**
- C=1, gamma='scale' → might be far from optimal → poor performance.
- Grid search with too many values → slow. Start with a coarse grid, then refine.
- Not scaling → C and gamma behave differently on unscaled data → tuning is meaningless.

---

## SVM vs KNN vs Other Models

**What:** When to use which:

| KNN | SVM | Random Forest |
|-----|-----|---------------|
| Simple, no training | Finds optimal boundary | Ensemble, robust |
| Slow prediction (all points) | Fast prediction (support vectors) | Fast prediction |
| Needs scaling | Needs scaling | No scaling needed |
| Good for low dimensions | Good for high dimensions | Good for any |
| Sensitive to noise | Robust to noise | Robust to noise |

**Why it exists:** Understanding trade-offs helps you choose the right model for your data and constraints.

**Where it's used:** Model selection for every classification task.

**What goes wrong without it:**
- KNN on high-dimensional data → curse of dimensionality → fails. Use SVM or RF.
- SVM on very large datasets (>100K samples) → slow training (O(n²) to O(n³)). Use RF or logistic regression.
- Not comparing models → you might miss that a simpler model works just as well.

---

## Support Vectors

**What:** The data points closest to the decision boundary. SVM's decision boundary depends ONLY on these points.

```python
model = SVC(kernel='linear')
model.fit(X_train, y_train)

print(model.support_vectors_)     # the support vector points
print(model.n_support_)           # number of support vectors per class
```

**Why it exists:** Understanding support vectors explains SVM's efficiency — only a few points define the boundary, not all data. Removing non-support-vector points doesn't change the model.

**Where it's used:** Model interpretation, understanding which data points matter.

**What goes wrong without it:**
- Too many support vectors → model is complex, might be overfitting. Check `n_support_`.
- Support vectors near the boundary → model is sensitive to these points → outliers here can shift the boundary.
- Not checking support vectors → you miss insight into what drives the model's decisions.
