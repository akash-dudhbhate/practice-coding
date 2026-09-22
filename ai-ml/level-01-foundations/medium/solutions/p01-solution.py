"""
LEVEL 01 — ML Foundations
MEDIUM P01 — Design a Spam Classifier (Solution)
==================================================
"""

def design():
    """Design a spam classifier system."""
    return {
        "problem_type": "supervised-classification",
        "features": ["sender_domain", "subject_words", "has_links", "num_caps", "email_length"],
        "label": "spam or not_spam (binary: 1 or 0)",
        "data_source": "public datasets like Enron, SpamAssassin, or manual labeling",
        "metric": "precision — false positives (real email in spam) are worse than false negatives"
    }


if __name__ == "__main__":
    result = design()
    for key, value in result.items():
        print(f"{key}: {value}")
