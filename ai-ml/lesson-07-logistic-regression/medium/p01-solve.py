"""
LESSON — Logistic Regression
MEDIUM P01 — Build a spam classifier: create synthetic email features (word counts, links, caps ratio). Train logistic regression. Print confusion matrix and precision/recall. Interpret results.
==================================================

CONCEPT:
  See concepts.md in this lesson folder for detailed explanations.

PROBLEM:
  Build a spam classifier: create synthetic email features (word counts, links, caps ratio). Train logistic regression. Print confusion matrix and precision/recall. Interpret results


Write a function `solve()` that implements the solution.

# Check your answer: compare with solutions/p01-solution.py
"""

TRY THIS INPUT:
  Add this test code at the bottom of your file:

  ```python
  X, y = generate_email_data()
  feature_names = ["Suspicious Words", "Num Links", "Caps Ratio"]

  # Call your function
  result = solve(...)
  print(result)
  ```

EXPECTED OUTPUT:
  Run the solution file to see expected output:
    python3 medium/solutions/p01-solution.py

  Then compare your output format with theirs.

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
