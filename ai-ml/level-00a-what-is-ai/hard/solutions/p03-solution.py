"""Solution — hard/p03-ai-map.py"""

STAGE_MAP = {
    "data":       ["dataset", "csv", "labeled examples"],
    "training":   ["gradient descent", "loss", "epoch", "backprop"],
    "model":      ["weights", "parameters", "layers", "neural network"],
    "prediction": ["inference", "classify", "predict"],
    "rag":        ["retrieval", "vector store", "embedding search"],
    "agent":      ["tool use", "tool calling", "react loop", "autonomous"],
    "deploy":     ["api", "server", "docker", "endpoint"],
}


def where_does_it_fit(concept):
    c = concept.lower()
    for stage, keywords in STAGE_MAP.items():
        if any(k in c for k in keywords):
            return stage
    return "unknown"
