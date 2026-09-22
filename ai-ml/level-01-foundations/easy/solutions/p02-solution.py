"""
LEVEL 01 — ML Foundations
EASY P02 — Identify Features and Labels (Solution)
====================================================
"""

def identify(scenario):
    """Return features and label for a given scenario."""
    answers = {
        "A": {
            "features": ["study_hours", "attendance", "past_scores"],
            "label": "pass_fail"
        },
        "B": {
            "features": ["month", "last_month_sales", "season", "promotions"],
            "label": "total_sales"
        },
    }
    return answers.get(scenario, {"features": [], "label": ""})


if __name__ == "__main__":
    result = identify("A")
    print(f"Features: {result['features']}")
    print(f"Label: {result['label']}")
    result = identify("B")
    print(f"Features: {result['features']}")
    print(f"Label: {result['label']}")
