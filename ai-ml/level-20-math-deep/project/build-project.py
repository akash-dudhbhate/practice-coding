"""
LEVEL 20 PROJECT — Paper Math Capstone
=========================================================

Combine the whole level: PCA + gradient descent + information
theory — everything you need to read the methods section of an
ML paper.

BUILD `run_pipeline()`:
  1. np.random.seed(42). Make a 2-class dataset in 10-D:
       class 0: mean 0 at origin,      100 samples, N(0, I)
       class 1: mean 3 along axis 0,   100 samples, N(0, I)
     Stack into X (200×10), y (200,).
  2. PCA: center X, eigendecompose covariance, project to 2-D
     (reuse your medium/p01 logic). Print variance explained:
     λᵢ/Σλ for the top 2 components.
  3. Train logistic regression ON THE 2-D DATA with gradient
     descent (your medium/p02 loop):
       z = Z @ w + b;  p = sigmoid(z)
       loss = binary cross-entropy;  w ← w − lr·∇w
     500 iters, lr=0.5.
  4. Report:
       - accuracy on the training data
       - mean entropy of predicted probabilities
         (confident model → low entropy)
       - KL divergence between the two classes' mean
         predicted-probability distributions
  5. Return (accuracy, mean_entropy, kl)

EXPECTED OUTPUT:
  ```
  Variance explained: [~0.9, ~0.03]
  Accuracy: ~1.00   (classes are far apart — easy)
  Mean entropy: <0.1  (confident predictions)
  ```

BONUS EXPERIMENTS (comment what you observe):
  - Move class means closer (mean 1 instead of 3) → entropy rises
  - Project to 5-D instead of 2 → same accuracy? Why?
  - Swap GD for your Adam (hard/p03) → fewer iters needed?

WHY THIS IS THE PAPER-MATH LEVEL: eigenfaces, spectral methods,
loss surfaces, and KL penalties are the vocabulary of every
methods section you'll ever read.
"""

import numpy as np


# === WRITE YOUR CODE BELOW ===
def run_pipeline():
    # TODO
    pass


if __name__ == "__main__":
    acc, ent, kl = run_pipeline()
    print(f"Accuracy: {acc:.4f} | entropy: {ent:.4f} | KL: {kl:.4f}")
