"""
MILESTONE 01 — DataMind Design Doc in Code
===========================================

Level-01 skill applied: define the problem before coding.

TASK:
  Implement `describe()` — returns a dict describing what
  DataMind is, as if you were pitching it:

    {
      "name": "DataMind",
      "problem_type": "supervised",        # or unsupervised
      "tasks": ["load", "clean", "predict", "explain"],
      "users": "data analysts and students",
      "v1_scope": "CSV in → predictions out",
    }

Also implement `predict(features)` — KEEP your milestone-00
weighted sum working. DataMind grows, never resets.

Run:  python3 datamind.py
Check: python3 check_milestone.py
"""

WEIGHTS = [0.5, 0.3, 0.2]
BIAS = 0.1


def predict(features):
    """Weighted sum — milestone 00."""
    # M00 — keep working:
    # return sum(f * w for f, w in zip(features, WEIGHTS)) + BIAS
    pass


def describe():
    """Return the design dict described above."""
    # MILESTONE 01 — TODO
    pass


if __name__ == "__main__":
    print("DataMind v0.1 — design")
    print(describe())
    print(f"predict([10,20,30]) = {predict([10, 20, 30])}")   # still 17.1
