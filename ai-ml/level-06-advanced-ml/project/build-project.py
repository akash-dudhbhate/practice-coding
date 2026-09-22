"""
LEVEL 06 PROJECT — Fraud Detection on Imbalanced Data
======================================================

Real fraud datasets are ~99% legit / 1% fraud. Accuracy is useless
here (predict "legit" always → 99% accurate, 0 frauds caught).

BUILD `detect_fraud()`:
  1. Data: make_classification(2000 samples, weights=[0.95, 0.05],
                               n_features=10, random_state=42)
  2. Split stratified 75/25
  3. Model A: LogisticRegression(max_iter=1000)
     Model B: LogisticRegression(class_weight="balanced")
  4. For each: accuracy, recall (on fraud class), f1, confusion matrix
  5. Also try: oversample minority in TRAIN only → refit model C

PRINT (yours should resemble this):
  ```
  A default : acc=0.97x  recall=0.0x  f1=0.1x
  B balanced: acc=0.9xx  recall=0.8x  f1=0.3x
  C oversampled: acc=0.9xx  recall=0.8x  f1=0.3x
  ```

RETURN: {"A": {...metrics}, "B": {...}, "C": {...}}

KEY LESSON: model A looks "best" by accuracy and is USELESS.
  Which model would you deploy to a bank? Why? (comment your answer)

HINT: oversampling — np.random.choice(fraud_indices, n_needed, replace=True)
"""

# === WRITE YOUR CODE BELOW ===

def detect_fraud():
    # TODO
    pass


if __name__ == "__main__":
    detect_fraud()
