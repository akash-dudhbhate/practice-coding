"""
LEVEL 01 — ML Foundations
HARD P02 — Confusion Matrix Intuition (Solution)
====================================================
"""

def analyze():
    """Analyze a medical test confusion matrix."""
    return {
        "TP": 70,
        "FP": 30,
        "TN": 890,
        "FN": 10,
        "accuracy": 0.96,
        "worse_error": "false-negative"  # missing a disease is worse than a false alarm
    }


if __name__ == "__main__":
    result = analyze()
    for key, value in result.items():
        print(f"{key}: {value}")
