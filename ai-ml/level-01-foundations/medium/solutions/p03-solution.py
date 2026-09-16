"""
LEVEL 01 — ML Foundations
MEDIUM P03 — Match Algorithm to Problem (Solution)
=====================================================
"""

def match(scenario):
    """Match a scenario to the best algorithm."""
    answers = {
        "A": "linear-regression",      # Temperature = predict a number
        "B": "kmeans-clustering",      # Grouping customers = unsupervised clustering
        "C": "logistic-regression",    # Spam classification = binary category
        "D": "linear-regression",      # House prices = predict a number
        "E": "neural-network",         # Object recognition = complex patterns
    }
    return answers.get(scenario, "unknown")


if __name__ == "__main__":
    for s in ["A", "B", "C", "D", "E"]:
        print(f"{s}: {match(s)}")
