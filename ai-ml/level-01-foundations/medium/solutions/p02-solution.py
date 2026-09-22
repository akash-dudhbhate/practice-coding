"""
LEVEL 01 — ML Foundations
MEDIUM P02 — Train vs Test Split (Solution)
==============================================
"""

def explain():
    """Explain train/test split concepts."""
    return {
        "why_split": "To evaluate if the model generalizes to unseen data",
        "typical_ratio": "80/20",
        "overfitting": "Model memorizes training data including noise, fails on new data",
        "interpret": "Classic overfitting — the model memorized, didn't learn"
    }


if __name__ == "__main__":
    result = explain()
    for key, value in result.items():
        print(f"{key}: {value}")
