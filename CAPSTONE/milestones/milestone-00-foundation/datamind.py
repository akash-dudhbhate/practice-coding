"""
MILESTONE 00 — DataMind Foundation
====================================

This is the skeleton of your capstone project. By level 13,
this file will be a complete AI data assistant.

Right now: it just loads numbers and predicts with a weighted sum.
That weighted sum is the SAME math inside every neural network.

TASK:
  Implement `predict(features)` using a weighted sum.
  This is Level-00's core concept applied to a "real" system.

Run:  python3 datamind.py
"""

# ---- Level-00 concepts used here ----
# weighted_sum(inputs, weights, bias) — the neuron

WEIGHTS = [0.5, 0.3, 0.2]   # learned weights (you'll train these in L04)
BIAS = 0.1


def predict(features):
    """Predict a score from features using a weighted sum.

    features: list of 3 numbers, e.g. [10, 20, 30]
    returns: float score
    """
    # MILESTONE 00 — TODO: implement using weighted sum
    # score = features·weights + bias
    pass


if __name__ == "__main__":
    print("DataMind v0.0 — foundation")
    result = predict([10, 20, 30])
    print(f"Prediction for [10, 20, 30]: {result}")
    # Expected: 10*0.5 + 20*0.3 + 30*0.2 + 0.1 = 5+6+6+0.1 = 17.1
