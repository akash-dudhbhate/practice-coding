"""
MILESTONE 05 — DataMind Evaluator
==================================

Level-05 skill applied: know if your model is actually good.

TASK:
  Implement `evaluate(model, X_test, y_test)` returning:
    {"accuracy": float, "precision": float, "recall": float,
     "f1": float, "confusion": list-of-lists}

  Use sklearn.metrics — average="weighted" for multi-class.

  Then `full_report(X, y)` — splits 80/20 stratified, trains via
  your milestone-04 train(), evaluates, prints a small report,
  returns the metrics dict.

Run:  python3 datamind.py
Check: python3 check_milestone.py
"""

WEIGHTS = [0.5, 0.3, 0.2]
BIAS = 0.1


def predict(features):
    # M00
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
    # M04
    pass

def model_predict(model, features):
    # M04
    pass


def evaluate(model, X_test, y_test):
    """Return metrics dict."""
    # MILESTONE 05 — TODO
    pass


def full_report(X, y):
    """split → train → evaluate → print → return metrics."""
    # MILESTONE 05 — TODO
    pass


if __name__ == "__main__":
    from sklearn.datasets import load_iris
    X, y = load_iris(return_X_y=True)
    print(full_report(X, y))
