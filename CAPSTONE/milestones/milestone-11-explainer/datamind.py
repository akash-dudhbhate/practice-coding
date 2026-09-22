"""
MILESTONE 11 — DataMind Explainer
==================================

Level-11 skill applied: explain predictions in plain English.

DataMind predicts a number — but users ask "WHY?"
Build the prompt that an LLM would answer.

TASK:
  Implement `explain_prompt(features, prediction, feature_names)`:
    Returns a prompt string asking an LLM to explain the
    prediction to a non-technical user. Must include:
      - the feature values with their names
      - the prediction
      - instruction: "explain in 2 sentences, no jargon"

  Implement `parse_explanation(llm_response)` — strip whitespace,
  return the clean text (simulating what you'd do with a real
  LLM response).

Run:  python3 datamind.py
Check: python3 check_milestone.py
"""

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
    pass  # M06

def compare(X_basic, X_eng, y):
    pass  # M06

def segment(X, k=None):
    pass  # M07

def profile(X, labels):
    pass  # M07

def neural_fit(X, y, hidden=16, epochs=100):
    pass  # M08

def flatten_image(img):
    pass  # M09

def is_image_like(obj):
    pass  # M09

def make_app():
    pass  # M10


def explain_prompt(features, prediction, feature_names):
    """Build the LLM prompt for explaining a prediction."""
    # MILESTONE 11 — TODO
    pass


def parse_explanation(llm_response):
    """Clean an LLM response string."""
    # MILESTONE 11 — TODO
    pass


if __name__ == "__main__":
    p = explain_prompt([10, 20, 30], 17.1, ["age", "income_k", "spend"])
    print(p)
    print("---")
    print(parse_explanation("  The score is high because income dominates.\n"))
