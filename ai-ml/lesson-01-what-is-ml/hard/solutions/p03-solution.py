"""
Lesson 01 - Hard P03
Explain bias, variance, and the bias-variance tradeoff.

Solution:
  - Bias: error from wrong assumptions in the model.
  - Variance: error from sensitivity to small fluctuations in training data.
  - Tradeoff: lowering bias usually raises variance, and vice versa.
"""

# ---------------------------------------------------------------------------
# 1. Bias
# ---------------------------------------------------------------------------
print("=" * 70)
print("1. BIAS")
print("=" * 70)
print(
    """
Bias is the error introduced by approximating a real-world problem, which may
be complex, with a simplified model.

  - High bias -> the model is too simple and systematically misses the true
    relationship. It *underfits* the data.
  - Low bias  -> the model is flexible enough to capture the true pattern.

Example:
  Fitting a straight line (linear regression) to data that follows a curve
  produces high bias -- the line cannot bend to match the curve.

Symptoms of high bias:
  - High training error
  - High test error  (both are bad -> underfitting)
"""
)

# ---------------------------------------------------------------------------
# 2. Variance
# ---------------------------------------------------------------------------
print("=" * 70)
print("2. VARIANCE")
print("=" * 70)
print(
    """
Variance measures how much the model's predictions change when it is trained
on different subsets of the data.

  - High variance -> the model is overly sensitive to the specific training
    samples; it *overfits* and generalizes poorly.
  - Low variance  -> the model is stable across different training sets.

Example:
  A very deep decision tree that memorizes every training point will produce
  wildly different predictions if trained on a slightly different sample.

Symptoms of high variance:
  - Low training error
  - High test error   (big gap -> overfitting)
"""
)

# ---------------------------------------------------------------------------
# 3. The Tradeoff
# ---------------------------------------------------------------------------
print("=" * 70)
print("3. THE BIAS-VARIANCE TRADEOFF")
print("=" * 70)
print(
    """
Total error can be decomposed as:

    Total Error = Bias^2 + Variance + Irreducible Error

  - Irreducible error is noise in the data we cannot remove.
  - As model complexity increases:
      * Bias  decreases  (the model can fit more complex patterns)
      * Variance increases (the model becomes more sensitive to training data)

The GOAL is to find the "sweet spot" -- the complexity where total error is
minimized.

  Too simple  -> high bias,  low variance  (underfitting)
  Too complex -> low bias,   high variance (overfitting)
  Just right  -> balanced    -> lowest total error

How to manage the tradeoff:
  - Reduce bias : use a more flexible model, add features, reduce regularization.
  - Reduce variance: more training data, regularization, ensemble methods
    (bagging / random forests), dropout, pruning, cross-validation.
"""
)

# ---------------------------------------------------------------------------
# 4. Visual summary (text table)
# ---------------------------------------------------------------------------
print("=" * 70)
print("4. SUMMARY TABLE")
print("=" * 70)
print(
    f"{'Complexity':<12} {'Bias':<12} {'Variance':<12} {'Result':<20}"
)
print("-" * 56)
print(f"{'Low':<12} {'High':<12} {'Low':<12} {'Underfitting':<20}")
print(f"{'Medium':<12} {'Medium':<12} {'Medium':<12} {'Good fit':<20}")
print(f"{'High':<12} {'Low':<12} {'High':<12} {'Overfitting':<20}")
