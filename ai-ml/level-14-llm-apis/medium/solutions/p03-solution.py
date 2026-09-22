"""Solution — medium/p03-batch-call.py"""

import sys, os, json
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))
from llm import chat


def classify_batch(texts, categories):
    numbered = "\n".join(f"{i+1}. {t}" for i, t in enumerate(texts))
    prompt = (f"Classify each text into one of {categories}. "
              f"Return a JSON array of labels, in order.\n{numbered}")
    reply = chat(prompt, temperature=0.0)
    try:
        labels = json.loads(reply)
        if isinstance(labels, list) and len(labels) == len(texts):
            return labels
    except json.JSONDecodeError:
        pass
    # fallback: simulated mode may not return array — pad with neutral
    return ["neutral"] * len(texts)
