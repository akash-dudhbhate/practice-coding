"""
MILESTONE 04 — DataMind Real Predictor
=======================================

Level-04 skill applied: replace the hand-tuned weighted sum with
a learned model.

TASK:
  Implement `train(X, y)` — fits LogisticRegression(max_iter=200)
  and returns the model.
  Implement `model_predict(model, features)` — wraps model.predict.

  Then in __main__: train on iris, show that predict() (milestone-00)
  still works AND model_predict gives real learned predictions.

  The old weighted-sum predict() stays — it's now DataMind's
  "baseline" (every system needs a baseline to beat).

Run:  python3 datamind.py
Check: python3 check_milestone.py
"""

WEIGHTS = [0.5, 0.3, 0.2]
BIAS = 0.1


def predict(features):
    # M00 — baseline weighted sum
    pass


def describe():
    # M01
    pass


def load_records(raw):
    # M02
    pass


def summarize(rows):
    # M03
    pass


def auto_chart(rows, filename="chart.png"):
    # M03
    pass


def train(X, y):
    """Fit LogisticRegression, return model."""
    # MILESTONE 04 — TODO
    pass


def model_predict(model, features):
    """model.predict on one feature list → int class."""
    # MILESTONE 04 — TODO
    pass


if __name__ == "__main__":
    from sklearn.datasets import load_iris
    X, y = load_iris(return_X_y=True)
    model = train(X, y)
    print(f"Baseline (m00): {predict([10, 20, 30])}")
    print(f"Learned (m04):  {model_predict(model, [5.1, 3.5, 1.4, 0.2])}")
