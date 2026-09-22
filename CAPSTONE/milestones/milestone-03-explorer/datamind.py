"""
MILESTONE 03 — DataMind Auto-Explorer
======================================

Level-03 skill applied: understand data at a glance.

TASK:
  Implement `summarize(rows)` — takes cleaned records (list of
  dicts from milestone-02) and returns per-column stats:

    {"age":    {"mean": x, "min": x, "max": x},
     "income": {"mean": x, "min": x, "max": x},
     ...}   # only numeric columns; skip None values

  Plus `auto_chart(rows, filename)` — saves a histogram of the
  first numeric column to `filename` (Agg backend, no plt.show).

Run:  python3 datamind.py
Check: python3 check_milestone.py
"""

import statistics

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
    """Numeric stats per column."""
    # MILESTONE 03 — TODO
    pass


def auto_chart(rows, filename="chart.png"):
    """Histogram of first numeric column → save to filename."""
    # MILESTONE 03 — TODO
    # import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
    pass


if __name__ == "__main__":
    rows = [{"age": 28.0, "income": 52000.0},
            {"age": 31.5, "income": 61500.0},
            {"age": 35.0, "income": None}]
    print(summarize(rows))
    auto_chart(rows)
    print("chart.png written")
