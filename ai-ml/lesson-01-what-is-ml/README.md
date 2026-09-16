# Lesson 01 — What is ML?

## Quick Reference

### Supervised vs Unsupervised
- **Supervised**: labeled data (input + answer). Examples: spam detection, price prediction.
- **Unsupervised**: no labels, model finds patterns. Examples: customer segmentation.

### Regression vs Classification
- **Regression**: predict a NUMBER (price, temperature).
- **Classification**: predict a CATEGORY (spam/ham, dog/cat/bird).

### Features (X) vs Label (y)
- **Features (X)**: inputs the model uses (size, bedrooms, location).
- **Label (y)**: what you're predicting (price, spam/not-spam).

### Traditional vs ML
- **Traditional**: you write rules. `if "free money" in email: spam`
- **ML**: you give examples, model learns rules. `model.fit(emails, labels)`

### Train/Test Split
- **Train**: model learns from this (~80%).
- **Test**: used ONLY to evaluate (~20%). Never train on test data.

### Overfitting
- Model memorizes training data but fails on new data.
- Sign: high train accuracy, low test accuracy.
- Fix: simpler model, more data, regularization.

### Underfitting
- Model too simple, fails on both train and test.
- Fix: more complex model, better features.

### Bias-Variance Tradeoff
- **High bias** → underfitting (too simple).
- **High variance** → overfitting (too complex).
- Can't have both low — it's a balance.

---

## Common Mistakes

```python
# WRONG — training on test data
model.fit(X, y)
model.score(X, y)

# CORRECT
X_train, X_test, y_train, y_test = train_test_split(X, y)
model.fit(X_train, y_train)
model.score(X_test, y_test)
```

---

## Your Tasks

This lesson has **9 practice problems** across three difficulty levels.

### Easy
1. `easy/p01-classify-problem-type.py` — classify 3 scenarios
2. `easy/p02-identify-features-labels.py` — identify X and y
3. `easy/p03-traditional-vs-ml.py` — choose traditional or ML

### Medium
4. `medium/p01-design-spam-classifier.py` — design a spam classifier
5. `medium/p02-train-test-split.py` — explain train/test splits
6. `medium/p03-match-algorithm-to-problem.py` — match algorithms

### Hard
7. `hard/p01-full-ml-pipeline-design.py` — design a full ML pipeline
8. `hard/p02-confusion-matrix-intuition.py` — calculate TP/FP/TN/FN
9. `hard/p03-bias-variance-tradeoff.py` — explain bias-variance tradeoff

### Project
`project-spam-classifier.py` — apply everything to design a spam classifier

### How to work
1. Read the problem file
2. Write your solution (replace the TODO)
3. Run `python <filename>` to test
4. Check against `solutions/p0X-solution.py`
5. Run `python ../../progress.py` to track progress
