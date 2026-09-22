"""
MILESTONE 02 — DataMind Data Loader
====================================

Level-02 skill applied: clean messy real-world data.

TASK:
  Implement `load_records(raw)` — takes a list of dicts with
  messy values and returns clean ones:
    1. Drop exact duplicates
    2. "age" as string → float; "" → median age
    3. "income" like "$52,000" → 52000.0; "" → None
    4. "country" → uppercase

  Keep `predict` and `describe` from earlier milestones working.

INPUT:
  [{"name":"A","age":"30","country":"usa","income":"$50,000"}, ...]

EXPECTED:
  deduplicated, numeric ages/incomes, "USA" not "usa"

Run:  python3 datamind.py
Check: python3 check_milestone.py
"""

import statistics

WEIGHTS = [0.5, 0.3, 0.2]
BIAS = 0.1


def predict(features):
    # M00 — weighted sum
    pass


def describe():
    # M01 — design dict
    pass


def load_records(raw):
    """Clean a list of messy record dicts → clean list."""
    # MILESTONE 02 — TODO
    pass


if __name__ == "__main__":
    raw = [
        {"name": "Ana", "age": "28", "country": "usa", "income": "$52,000"},
        {"name": "Ana", "age": "28", "country": "usa", "income": "$52,000"},
        {"name": "Ben", "age": "",   "country": "US",  "income": "$61,500"},
        {"name": "Cid", "age": "35", "country": "in",  "income": ""},
    ]
    cleaned = load_records(raw)
    for r in cleaned:
        print(r)
