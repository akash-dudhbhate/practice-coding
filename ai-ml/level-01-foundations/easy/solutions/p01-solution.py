"""
LEVEL 01 — ML Foundations
EASY P01 — Classify the Problem Type (Solution)
==================================================
"""

def classify(scenario):
    """Classify a scenario as supervised-regression, supervised-classification, or unsupervised."""
    answers = {
        "A": "supervised-regression",      # House price = predict a number
        "B": "unsupervised",               # No labels, group shoppers
        "C": "supervised-classification",  # Tumor = predict a category
    }
    return answers.get(scenario, "unknown")


if __name__ == "__main__":
    print(classify("A"))
    print(classify("B"))
    print(classify("C"))
