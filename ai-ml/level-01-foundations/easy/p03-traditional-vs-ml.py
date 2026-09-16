"""
LEVEL 01 — ML Foundations
EASY P03 — Traditional vs ML
================================

CONCEPT:
  Traditional programming = you write the RULES yourself.
    Example: `if "free money" in email: return "spam"`

  ML = you give examples, the model learns the rules.
    Example: `model.fit(emails, labels)` → `model.predict(new_email)`

  Rule of thumb: simple fixed rules → traditional.
                 Complex or changing patterns → ML.

PROBLEM:
  For each scenario, decide whether to use traditional programming or ML.
  Write a function `choose(scenario)` that returns "traditional" or "ml".

  Scenarios:
    A) Calculate the total of a shopping cart
    B) Detect spam in emails
    C) Sort a list of names alphabetically
    D) Recognize faces in photos

TRY THIS INPUT:
  ```python
  print(choose("A"))  # "traditional" — simple math, fixed rules
  print(choose("B"))  # "ml" — spam patterns constantly change
  print(choose("C"))  # "traditional" — sorting is a fixed algorithm
  print(choose("D"))  # "ml" — faces are complex patterns
  ```

EXPECTED OUTPUT:
  ```
  traditional
  ml
  traditional
  ml
  ```

Write your function below.
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# Uncomment to test your solution:
# print(choose("A"))
# print(choose("B"))
# print(choose("C"))
# print(choose("D"))
