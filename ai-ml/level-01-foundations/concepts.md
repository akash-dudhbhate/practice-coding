# Level 01 — Concepts Reference

## For Easy Problems

### P01: Supervised vs Unsupervised
- **Supervised**: labeled data (input + correct answer). Model learns the mapping.
- **Unsupervised**: no labels. Model finds patterns/groups on its own.
- **Regression**: predict a NUMBER. **Classification**: predict a CATEGORY.

### P02: Features and Labels
- **Features (X)**: inputs — the "clues" the model uses.
- **Label (y)**: output — what you're predicting.
- Example: house price → features: size, bedrooms | label: price

### P03: Traditional vs ML
- **Traditional**: you write rules. `if "free money" in email: spam`
- **ML**: you give examples, model learns the rules.
- Use ML when patterns are complex or constantly changing.

---

## For Medium Problems

### P04: Designing an ML System
Think through these steps in order:
1. Problem type (supervised/unsupervised, regression/classification)
2. Features to extract
3. Label definition
4. Data collection strategy
5. Evaluation metric

### P05: Train/Test Split
- **Why split?** To know if the model generalizes to new data.
- **Typical ratio:** 80/20 or 70/30.
- **Overfitting:** model memorizes training data, fails on new data.
- **Sign:** 99% train accuracy, 60% test accuracy = overfitting.

### P06: Choosing an Algorithm
| Algorithm | Use When |
|-----------|----------|
| Linear Regression | Predict a number |
| Logistic Regression | Predict a category (binary) |
| K-Means | Group unlabeled data |
| Decision Tree | Interpretable, both types |
| Neural Network | Complex patterns (images, text) |

---

## For Hard Problems

### P07: ML Pipeline
8 steps: Define → Collect → Preprocess → Split → Choose → Train → Evaluate → Deploy.
Skipping any step = project failure.

### P08: Confusion Matrix
| | Predicted Yes | Predicted No |
|---|---|---|
| **Actual Yes** | TP | FN |
| **Actual No** | FP | TN |
- **Accuracy** = (TP+TN)/total — misleading for imbalanced data.
- **False Negative** is worse for disease detection (missed case).

### P09: Bias-Variance Tradeoff
- **Bias**: error from oversimplified assumptions → underfitting.
- **Variance**: error from sensitivity to training data → overfitting.
- **Tradeoff**: reducing one increases the other.
- High bias: fix with more complex model. High variance: fix with simpler model, more data, regularization.
