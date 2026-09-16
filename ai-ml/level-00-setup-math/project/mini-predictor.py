"""
LEVEL 00 PROJECT — Mini Prediction Engine
==========================================

Apply Level-00 math to build a tiny predictor — no libraries.

TASK:
  You have house data: [size_sqft, bedrooms, age_years]
  and learned weights [200, 10000, -500] plus bias 50000.

  Implement `predict_price(features)` using weighted sum.

  Then predict prices for:
    [1500, 3, 10]  → ?
    [800, 2, 50]   → ?
    [2500, 5, 2]   → ?

BONUS (thinking stretch):
  - What does a NEGATIVE weight on age_years mean?
  - If all features doubled, what happens to the prediction?

This "predictor" is the same math a linear regression model
computes — you're building ML intuition before the libraries.
"""

WEIGHTS = [200, 10000, -500]
BIAS = 50000


def predict_price(features):
    """Predict house price = features · weights + bias."""
    # TODO: implement (use your dot-product logic)
    pass


if __name__ == "__main__":
    test_houses = [
        [1500, 3, 10],
        [800, 2, 50],
        [2500, 5, 2],
    ]
    for h in test_houses:
        print(f"{h} -> ${predict_price(h):,.0f}")

    # Expected outputs:
    # [1500,3,10] → 1500*200 + 3*10000 + 10*(-500) + 50000 = 375,000
    # [800,2,50]  → 800*200 + 2*10000 + 50*(-500) + 50000  = 205,000
    # [2500,5,2]  → 2500*200 + 5*10000 + 2*(-500) + 50000  = 599,000
