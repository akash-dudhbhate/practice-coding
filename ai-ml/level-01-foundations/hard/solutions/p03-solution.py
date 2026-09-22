"""
LEVEL 01 — ML Foundations
HARD P03 — Bias-Variance Tradeoff (Solution)
===============================================
"""

def explain():
    """Explain bias-variance tradeoff concepts."""
    return {
        "bias": "Error from oversimplified assumptions — model is too simple",
        "variance": "Error from sensitivity to training data — model memorizes noise",
        "high_bias": "underfitting",
        "high_variance": "overfitting",
        "tree_100_65": "high variance (overfitting) — fix: prune the tree, limit depth",
        "linear_70_70": "high bias (underfitting) — fix: use a more complex model",
        "tradeoff": "Reducing bias increases variance and vice versa — it's a balance"
    }


if __name__ == "__main__":
    result = explain()
    for key, value in result.items():
        print(f"{key}: {value}")
