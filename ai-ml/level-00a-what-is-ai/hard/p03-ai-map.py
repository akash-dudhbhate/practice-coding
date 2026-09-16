"""
LEVEL 00A — What is AI?
HARD P03 — The AI Map (Where Everything Fits)
==============================================

CONCEPT:
  Every AI buzzword fits into one pipeline:

    DATA → TRAINING → MODEL (weights) → PREDICTION → ANSWER

  Extras on top:
    RAG    = search docs BEFORE predicting
    AGENT  = model picks WHICH tool to use
    FINE-TUNE = adjust existing weights on YOUR data
    DEPLOY = put the model behind an API so apps can use it

PROBLEM:
  Write `where_does_it_fit(concept)` that maps each buzzword
  to its stage. Return one of: "data", "training", "model",
  "prediction", "rag", "agent", "deploy", "unknown"

  Mapping:
    "dataset", "csv", "labeled examples" → "data"
    "gradient descent", "loss", "epoch", "backprop" → "training"
    "weights", "parameters", "layers", "neural network" → "model"
    "inference", "classify", "predict" → "prediction"
    "retrieval", "vector store", "embedding search" → "rag"
    "tool use", "tool calling", "react loop", "autonomous" → "agent"
    "api", "server", "docker", "endpoint" → "deploy"
    anything else → "unknown"

TRY THIS INPUT:
  ```python
  print(where_does_it_fit("gradient descent"))
  print(where_does_it_fit("vector store"))
  print(where_does_it_fit("docker"))
  print(where_does_it_fit("pizza"))
  ```

EXPECTED OUTPUT:
  ```
  training
  rag
  deploy
  unknown
  ```

WHY THIS MATTERS:
  This map is your GPS for the next 20 levels. Every concept
  you'll learn has a spot on it — no magic, just stages.

CHECK: python3 check.py hard/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: implement where_does_it_fit(concept)


def where_does_it_fit(concept):
    """Map a buzzword to its stage in the AI pipeline."""
    pass


# === TEST ===
# print(where_does_it_fit("gradient descent"))
# print(where_does_it_fit("vector store"))
# print(where_does_it_fit("docker"))
# print(where_does_it_fit("pizza"))
