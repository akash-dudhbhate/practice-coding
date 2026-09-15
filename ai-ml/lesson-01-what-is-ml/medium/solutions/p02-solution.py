"""
Lesson 01 - Medium P02
Explain train/test splits and overfitting.

Solution:
  - Why we split data into train and test sets
  - What overfitting is and how to detect it
  - How to prevent overfitting
"""

# ---------------------------------------------------------------------------
# Explanation 1: Train / Test Split
# ---------------------------------------------------------------------------
print("=" * 70)
print("1. Why split data into train and test sets?")
print("=" * 70)
print(
    """
We split data so we can train on one portion and evaluate on a *separate,
unseen* portion. This simulates how the model will perform on new, real-world
data.

  - Training set (e.g. 70-80%): used to fit model parameters.
  - Test set     (e.g. 20-30%): used ONCE at the end to estimate generalization.

If we evaluate on the same data we trained on, the model may simply memorize
the examples, giving an overly optimistic score that does not reflect real
performance. The test split gives an honest, unbiased estimate.

Common ratios: 70/30, 80/20, or 60/20/20 (train/validation/test).
"""
)

# ---------------------------------------------------------------------------
# Explanation 2: Overfitting
# ---------------------------------------------------------------------------
print("=" * 70)
print("2. What is overfitting and how do you detect it?")
print("=" * 70)
print(
    """
Overfitting happens when a model learns the training data *too well*,
including its noise and outliers, so it fails to generalize to new data.

Symptoms:
  - Training accuracy / R^2 is very high (e.g. 99%).
  - Test accuracy / R^2 is much lower (e.g. 70%).
  - The gap between train and test performance is large.

In other words: the model memorizes instead of learning the underlying pattern.

Example:
  A decision tree that grows until every leaf has one sample will get 100%
  training accuracy but will perform poorly on the test set.
"""
)

# ---------------------------------------------------------------------------
# Explanation 3: Preventing Overfitting
# ---------------------------------------------------------------------------
print("=" * 70)
print("3. How to prevent overfitting")
print("=" * 70)
print(
    """
Strategies:
  1. Use more training data if possible.
  2. Simplify the model (fewer parameters, shallower trees, lower polynomial
     degree).
  3. Regularization (L1 / L2 penalties) to shrink large weights.
  4. Cross-validation to tune hyperparameters on validation folds, not the
     test set.
  5. Early stopping for iterative models (stop when validation loss rises).
  6. Dropout / data augmentation for neural networks.
  7. Pruning for decision trees (max_depth, min_samples_leaf).
  8. Ensemble methods (bagging, random forests) to reduce variance.
"""
)
