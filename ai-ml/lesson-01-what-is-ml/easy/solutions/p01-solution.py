"""
Lesson 01 - Easy P01
Classify 3 scenarios as regression, classification, or unsupervised learning.

Solution:
  Scenario 1 -> Regression    (predict a continuous number)
  Scenario 2 -> Classification (predict a discrete category)
  Scenario 3 -> Unsupervised   (no labels, find structure)
"""

# ---------------------------------------------------------------------------
# Scenario definitions
# ---------------------------------------------------------------------------
scenarios = [
    {
        "id": 1,
        "description": "Predict the price of a house given its size, location, and number of bedrooms.",
        "answer": "Regression",
        "reason": "The target (price) is a continuous numeric value, so we use regression.",
    },
    {
        "id": 2,
        "description": "Determine whether an email is spam or not spam based on its content.",
        "answer": "Classification",
        "reason": "The target is a discrete binary label (spam / not spam), so we use classification.",
    },
    {
        "id": 3,
        "description": "Group customers into segments based on purchasing behavior without predefined labels.",
        "answer": "Unsupervised",
        "reason": "There is no labeled target; we discover structure (clusters) in the data, so this is unsupervised learning.",
    },
]

# ---------------------------------------------------------------------------
# Print answers
# ---------------------------------------------------------------------------
for s in scenarios:
    print(f"Scenario {s['id']}: {s['description']}")
    print(f"  -> Type:    {s['answer']}")
    print(f"  -> Reason:  {s['reason']}")
    print()
