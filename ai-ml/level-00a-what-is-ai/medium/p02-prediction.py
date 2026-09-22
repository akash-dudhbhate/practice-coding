"""
LEVEL 00A — What is AI?
MEDIUM P02 — Prediction = Using the Model
==========================================

CONCEPT:
  After training, you FREEZE the weights and just compute.
  "Inference" = fancy word for "using the trained model."

  Our trained weight was 0.2. But a real model has MANY weights —
  one per feature. Price = w1*size + w2*rooms + w3*age + bias.

PROBLEM:
  Write `predict_price(size, rooms, age)` using:
    weights = [0.15, 5.0, -0.5]  # per sqft, per room, per year
    bias = 10.0
    price = size*0.15 + rooms*5.0 + age*(-0.5) + 10.0

TRY THIS INPUT:
  ```python
  print(predict_price(1500, 3, 10))   # 1500sqft, 3 rooms, 10yrs old
  ```

EXPECTED OUTPUT:
  ```
  245.0
  ```
  (1500*0.15 + 3*5.0 + 10*(-0.5) + 10.0 = 225 + 15 - 5 + 10 = 245)

WHY THIS MATTERS:
  More features = more weights. GPT has billions — same formula.

CHECK: python3 check.py medium/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: implement predict_price(size, rooms, age)


def predict_price(size, rooms, age):
    """House price prediction with 3 features."""
    pass


# === TEST ===
# print(predict_price(1500, 3, 10))
