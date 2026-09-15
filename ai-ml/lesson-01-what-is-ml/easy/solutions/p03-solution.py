"""
Lesson 01 - Easy P03
Decide whether to use traditional programming or machine learning for 4 scenarios.

Rule of thumb:
  - Traditional programming: rules are clear, stable, and few; the logic can be
    written down as explicit if/else steps.
  - Machine learning: patterns are complex, hard to hand-code, or the data is
    large and messy; the relationship must be *learned* from examples.
"""

# ---------------------------------------------------------------------------
# Scenario definitions
# ---------------------------------------------------------------------------
scenarios = [
    {
        "id": 1,
        "description": "Calculate the factorial of a number.",
        "answer": "Traditional programming",
        "reason": "Factorial has a simple, exact mathematical formula (n! = n x (n-1) x ... x 1). No need to learn from data.",
    },
    {
        "id": 2,
        "description": "Detect fraudulent credit-card transactions from millions of historical records.",
        "answer": "Machine learning",
        "reason": "Fraud patterns are complex, constantly evolving, and impossible to capture with hand-written rules. ML learns subtle patterns from large data.",
    },
    {
        "id": 3,
        "description": "Sort a list of numbers in ascending order.",
        "answer": "Traditional programming",
        "reason": "Sorting has well-known, exact algorithms (e.g., merge sort). The rules never change and there is a guaranteed correct answer.",
    },
    {
        "id": 4,
        "description": "Recommend products to a user based on their browsing and purchase history.",
        "answer": "Machine learning",
        "reason": "Personalized recommendations depend on complex user behavior patterns that are impractical to hand-code. ML excels at learning preferences from data.",
    },
]

# ---------------------------------------------------------------------------
# Print answers
# ---------------------------------------------------------------------------
for s in scenarios:
    print(f"Scenario {s['id']}: {s['description']}")
    print(f"  -> Approach: {s['answer']}")
    print(f"  -> Reason:   {s['reason']}")
    print()
