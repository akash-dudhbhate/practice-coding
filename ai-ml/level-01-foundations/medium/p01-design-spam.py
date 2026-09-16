"""
LEVEL 01 — ML Foundations
MEDIUM P01 — Design a Spam Classifier
========================================

CONCEPT:
  Designing an ML system isn't just "pick an algorithm." You need:
    1. Problem type (supervised/unsupervised, regression/classification)
    2. Features to extract from raw data
    3. Label definition
    4. Data collection strategy
    5. Evaluation metric

PROBLEM:
  Design a spam classifier. Write a function `design()` that returns
  a dictionary answering all 5 questions.

  Questions:
    1. Is this supervised or unsupervised? Regression or classification?
    2. List 5 features you'd extract from each email.
    3. What is the label? What values can it take?
    4. How would you collect training data?
    5. What metric would you use to evaluate?

TRY THIS INPUT:
  ```python
  result = design()
  print(result["problem_type"])  # "supervised-classification"
  print(result["features"])      # ["sender_domain", "subject_words", ...]
  print(result["metric"])        # "precision" or "recall" or "f1"
  ```

EXPECTED OUTPUT:
  ```
  {
    "problem_type": "supervised-classification",
    "features": ["sender_domain", "subject_words", "has_links", "num_caps", "email_length"],
    "label": "spam or not_spam",
    "data_source": "public datasets like Enron or manual labeling",
    "metric": "precision"
  }
  ```

Write your function below.
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# Uncomment to test your solution:
# result = design()
# for key, value in result.items():
#     print(f"{key}: {value}")
