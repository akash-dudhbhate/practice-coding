# Lesson 07 — Concepts Explained (Logistic Regression)

> Read this before solving the problems. Each concept explains:
> **What** it is · **Why** it exists · **Where** it's used · **What goes wrong** without it.

---

## What is Logistic Regression?

**What:** Despite the name, logistic regression is a CLASSIFICATION algorithm, not regression. It predicts the probability that an input belongs to a class.

```python
# Binary classification: spam (1) or not spam (0)
# Logistic regression outputs a probability (0 to 1)
# p(spam | email) = 0.85 → 85% chance of being spam
# Threshold: if p > 0.5 → classify as spam

# The sigmoid function squashes any value to [0, 1]
# sigmoid(z) = 1 / (1 + e^(-z))
# z = m*x + b (linear combination)
```

**Why it exists:** Linear regression outputs any value (-∞ to ∞) → can't be a probability. Logistic regression uses the sigmoid function → output is always between 0 and 1 → interpretable as probability.

**Where it's used:** Binary classification — spam detection, disease diagnosis, churn prediction, credit approval.

**What goes wrong without it:**
- Using linear regression for classification → outputs outside [0, 1] → can't interpret as probability.
- Forgetting the threshold → logistic regression outputs probabilities, not classes. You must threshold (usually 0.5) to get class labels.
- Multiclass with logistic regression → use `multi_class='multinomial'` or one-vs-rest. Default may not work for 3+ classes.

---

## The Sigmoid Function

**What:** Sigmoid squashes any real number to the range (0, 1).

```python
import numpy as np

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

sigmoid(0)    # 0.5 (boundary)
sigmoid(5)    # 0.993 (very positive → class 1)
sigmoid(-5)   # 0.007 (very negative → class 0)
sigmoid(100)  # 1.0 (saturated)
```

**Why it exists:** Without sigmoid, the linear output (z) can be any value → can't be a probability. Sigmoid maps z to (0, 1) → probability. The S-shape means: confident predictions (far from 0) → close to 0 or 1, uncertain predictions (near 0) → close to 0.5.

**Where it's used:** Logistic regression, neural network output layers (binary classification), any model that outputs probabilities.

**What goes wrong without it:**
- `sigmoid(1000)` → overflow in `np.exp(-1000)` → returns 0 → `1/1 = 1`. Works but may warn. Use `np.clip(z, -500, 500)`.
- Sigmoid saturates: for large |z|, the gradient is near 0 → learning slows down (vanishing gradient in neural networks).
- Threshold at 0.5 is not always optimal. For imbalanced data, use a different threshold (e.g., 0.3 for rare events).

---

## Using scikit-learn

**What:** scikit-learn provides `LogisticRegression` with a simple API.

```python
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix

# Data
X = [[25, 50000], [35, 80000], [45, 120000]]  # age, income
y = [0, 0, 1]  # 0 = won't buy, 1 = will buy

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

model = LogisticRegression()
model.fit(X_train, y_train)

# Predict classes
predictions = model.predict(X_test)  # [0, 1, 0]

# Predict probabilities
probabilities = model.predict_proba(X_test)  # [[0.7, 0.3], [0.2, 0.8], ...]
# First column: P(class 0), second column: P(class 1)
```

**Why it exists:** Without sklearn, you'd implement gradient descent for logistic regression manually → error-prone. sklearn provides optimized, regularized implementation.

**Where it's used:** Every binary classification task in Python ML.

**What goes wrong without it:**
- `predict()` returns class labels (0/1). `predict_proba()` returns probabilities. Mixing them up → wrong evaluation.
- `predict_proba()` returns a 2D array (n_samples, n_classes). Column 0 = P(class 0), column 1 = P(class 1). Use `[:, 1]` for P(class 1).
- Default regularization (C=1.0) → may underfit. Increase C (less regularization) for more complex data.

---

## Decision Boundary

**What:** The line (or hyperplane) that separates the classes.

```python
# For 2 features: the boundary is a line
# m1*x1 + m2*x2 + b = 0
# Points above the line → class 1, below → class 0

# Visualizing the boundary
import numpy as np
import matplotlib.pyplot as plt

# Create a mesh
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1),
                      np.arange(y_min, y_max, 0.1))

# Predict on mesh
Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

# Plot
plt.contourf(xx, yy, Z, alpha=0.3)
plt.scatter(X[:, 0], X[:, 1], c=y)
```

**Why it exists:** Understanding the decision boundary helps you see how the model separates classes. Linear boundary → straight line. If classes aren't linearly separable → logistic regression performs poorly.

**Where it's used:** Model interpretation, understanding model limitations, feature engineering decisions.

**What goes wrong without it:**
- Non-linearly separable data with logistic regression → poor accuracy. Use polynomial features or a non-linear model (SVM, random forest).
- Decision boundary is linear → can't capture complex patterns (e.g., XOR). This is a fundamental limitation.
- High-dimensional data → can't visualize the boundary. Use PCA to reduce to 2D for visualization.

---

## Confusion Matrix

**What:** A table showing correct and incorrect predictions by class.

```python
from sklearn.metrics import confusion_matrix

y_true = [0, 0, 1, 1, 0, 1]
y_pred = [0, 1, 1, 1, 0, 0]

cm = confusion_matrix(y_true, y_pred)
# [[2, 1],   ← actual 0: 2 correct, 1 wrong
#  [1, 2]]   ← actual 1: 1 wrong, 2 correct

# Layout:
#                Predicted 0    Predicted 1
# Actual 0       True Neg       False Pos
# Actual 1       False Neg      True Pos
```

**Why it exists:** Accuracy alone is misleading (90% accuracy on imbalanced data where 90% is class 0 → predict everything as 0). The confusion matrix shows WHERE the errors are → false positives vs false negatives.

**Where it's used:** Every classification model evaluation.

**What goes wrong without it:**
- Confusing the layout: sklearn's confusion matrix is `[[TN, FP], [FN, TP]]`. Other tools may use different layouts. Always check.
- Ignoring the confusion matrix for imbalanced data → high accuracy but terrible recall for the minority class.
- Not using `normalize=True` for comparison across datasets with different sizes.

---

## Precision, Recall, F1-Score

**What:** Metrics that handle class imbalance better than accuracy.

```python
from sklearn.metrics import precision_score, recall_score, f1_score

# Precision: of all predicted positives, how many are correct?
# = TP / (TP + FP)
# High precision → few false alarms

# Recall: of all actual positives, how many did we find?
# = TP / (TP + FN)
# High recall → few missed positives

# F1: harmonic mean of precision and recall
# = 2 * (precision * recall) / (precision + recall)
# Balances both

precision = precision_score(y_true, y_pred)
recall = recall_score(y_true, y_pred)
f1 = f1_score(y_true, y_pred)
```

**Why it exists:** Accuracy hides problems in imbalanced data. A spam detector with 99% accuracy might miss 50% of spam (if spam is 1% of emails). Precision/recall/F1 reveal the true performance.

**Where it's used:** Every classification evaluation, especially with imbalanced data.

**What goes wrong without it:**
- Optimizing precision → recall drops (model only predicts positive when very confident → misses many). Optimizing recall → precision drops (predicts everything as positive → many false alarms).
- F1 is the balance. But if false positives and false negatives have different costs → use Fβ (weighted) or look at precision and recall separately.
- Choosing the wrong metric for the business problem → model looks good but is useless in practice.

---

## Multiclass Classification

**What:** Logistic regression can handle 3+ classes using one-vs-rest or multinomial.

```python
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris

# Iris dataset: 3 classes (setosa, versicolor, virginica)
X, y = load_iris(return_X_y=True)

model = LogisticRegression(multi_class='multinomial', solver='lbfgs')
model.fit(X, y)

# predict() returns class labels (0, 1, 2)
# predict_proba() returns probabilities for each class
probs = model.predict_proba(X[:1])  # [[0.8, 0.15, 0.05]]
```

**Why it exists:** Real-world problems often have 3+ classes (digit recognition: 10 classes, sentiment: 3 classes). Multiclass logistic regression extends binary to handle these.

**Where it's used:** Digit recognition, sentiment analysis, image classification (simple cases).

**What goes wrong without it:**
- `multi_class='ovr'` (one-vs-rest): trains N binary classifiers. Simple but can produce inconsistent probabilities.
- `multi_class='multinomial'`: trains one model with softmax. Better probabilities but needs a compatible solver (`lbfgs`, `saga`).
- Forgetting to set the solver → default may not support multinomial → warning or error.

---

## Regularization (L1, L2)

**What:** Regularization prevents overfitting by penalizing large coefficients.

```python
# L2 regularization (default): shrinks coefficients toward 0
model = LogisticRegression(penalty='l2', C=1.0)

# L1 regularization: some coefficients become exactly 0 (feature selection)
model = LogisticRegression(penalty='l1', solver='liblinear')

# C is inverse of regularization strength
# C=1.0 → default. C=100 → less regularization (more overfitting risk)
# C=0.01 → more regularization (more underfitting risk)
```

**Why it exists:** Without regularization, logistic regression can overfit (large coefficients → sensitive to noise). Regularization constrains coefficients → better generalization.

**Where it's used:** Every logistic regression model — the default C=1.0 applies L2 regularization.

**What goes wrong without it:**
- C too high (100) → overfitting (memorizes training data, poor test performance).
- C too low (0.001) → underfitting (too simple, poor on both train and test).
- L1 with the wrong solver → `LogisticRegression(penalty='l1', solver='lbfgs')` → error. L1 needs `liblinear` or `saga`.
