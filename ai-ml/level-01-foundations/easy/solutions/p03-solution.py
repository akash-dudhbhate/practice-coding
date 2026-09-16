"""
LEVEL 01 — ML Foundations
EASY P03 — Traditional vs ML (Solution)
==========================================
"""

def choose(scenario):
    """Return 'traditional' or 'ml' for a given scenario."""
    answers = {
        "A": "traditional",  # Shopping cart total — simple math, fixed rules
        "B": "ml",           # Spam detection — patterns constantly change
        "C": "traditional",  # Sorting — fixed algorithm
        "D": "ml",           # Face recognition — complex patterns
    }
    return answers.get(scenario, "unknown")


if __name__ == "__main__":
    for s in ["A", "B", "C", "D"]:
        print(f"{s}: {choose(s)}")
