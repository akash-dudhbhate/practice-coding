"""
LEVEL 00A — What is AI?
MEDIUM P01 — The Tiniest Training Loop
=======================================

CONCEPT:
  Training = repeatedly nudging a weight to reduce error.
  Here we train ONE weight on ONE example. No libraries needed.

  The rule: if prediction is too high, decrease weight.
            if too low, increase it. Step size = how much to nudge.

PROBLEM:
  Write `train_one_step(weight, input_val, true_answer, step)`:
    prediction = weight * input_val
    error = true_answer - prediction
    new_weight = weight + step * error / input_val
    return new_weight

  (The error/input_val formula keeps it simple — one step of
   "gradient descent" without the scary name.)

TRY THIS INPUT:
  ```python
  w = 0.1   # wrong starting weight
  for i in range(10):
      w = train_one_step(w, 1000, 200.0, 0.5)
      print(f"step {i}: weight = {w:.4f}")
  ```

EXPECTED OUTPUT:
  ```
  step 0: weight = 0.1500
  step 1: weight = 0.1750
  step 2: weight = 0.1875
  ...converging toward 0.2 (the correct answer)
  ```

WHY THIS MATTERS:
  This IS training. A neural network does this millions of times
  with millions of weights. The loop shape is identical.

CHECK: python3 check.py medium/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: implement train_one_step(weight, input_val, true_answer, step)


def train_one_step(weight, input_val, true_answer, step):
    """One training step: nudge weight toward the right answer."""
    pass


# === TEST ===
# w = 0.1
# for i in range(10):
#     w = train_one_step(w, 1000, 200.0, 0.5)
#     print(f"step {i}: weight = {w:.4f}")
