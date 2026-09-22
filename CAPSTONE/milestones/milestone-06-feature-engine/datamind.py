"""
MILESTONE 06 — DataMind Feature Engine
=======================================

Level-06 skill applied: better features → better models.

TASK:
  Implement `add_features(rows)` — for each record dict with
  keys age/income/spend, add derived columns:
    "income_per_age" = income / age
    "high_earner"    = 1 if income > overall median else 0
    "spend_ratio"    = spend / 100.0
  Returns a new list of dicts (don't mutate input).

  Then `compare(X_basic, X_engineered, y)` — trains two models
  (m04 train()) and prints both accuracies, showing whether
  your features helped.

Run:  python3 datamind.py
Check: python3 check_milestone.py
"""

import statistics

WEIGHTS = [0.5, 0.3, 0.2]
BIAS = 0.1


def predict(features):
    pass  # M00

def describe():
    pass  # M01

def load_records(raw):
    pass  # M02

def summarize(rows):
    pass  # M03

def auto_chart(rows, filename="chart.png"):
    pass  # M03

def train(X, y):
    pass  # M04

def model_predict(model, features):
    pass  # M04

def evaluate(model, X_test, y_test):
    pass  # M05

def full_report(X, y):
    pass  # M05


def add_features(rows):
    """Add derived features to each record."""
    # MILESTONE 06 — TODO
    pass


def compare(X_basic, X_eng, y):
    """Print baseline vs engineered accuracy."""
    # MILESTONE 06 — TODO
    pass


if __name__ == "__main__":
    rows = [{"age": 30, "income": 50000, "spend": 60},
            {"age": 45, "income": 80000, "spend": 30},
            {"age": 25, "income": 35000, "spend": 80}]
    print(add_features(rows))
