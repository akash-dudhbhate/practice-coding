"""
LEVEL 14 — MEDIUM P03 — Batch Classification
=============================================

Classify MANY texts in ONE prompt — much cheaper than one call
per text. Ask for a JSON array back.

PROBLEM:
  Implement `classify_batch(texts, categories)`:
    - build one prompt: "Classify each text into one of
      {categories}. Return a JSON array of labels, in order."
      then list the texts numbered
    - call chat()
    - parse the JSON array
    - return the list of labels

TRY THIS INPUT:   classify_batch(["I love this", "terrible product", "it's ok"],
                       ["positive", "negative", "neutral"])
EXPECTED OUTPUT:  ["positive", "negative", "neutral"] — same length as input

WHY: 1 call for 100 texts > 100 calls. Cost and latency matter.
  (simulated mode returns a plausible array of the right length)

RUN: python3 medium/p03-batch-call.py
CHECK: python3 check.py medium/p03
"""

import sys, os, json
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from llm import chat


def classify_batch(texts, categories):
    """One prompt → list of category labels, same length as texts."""
    # TODO
    pass


if __name__ == "__main__":
    texts = ["I love this", "terrible product", "it's ok"]
    labels = classify_batch(texts, ["positive", "negative", "neutral"])
    for t, l in zip(texts, labels):
        print(f"  [{l}] {t}")
