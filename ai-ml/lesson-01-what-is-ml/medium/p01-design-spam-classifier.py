"""
LESSON 01 — What is ML?
MEDIUM P01 — Design a Spam Classifier
========================================

CONCEPT:
  End-to-end thinking: problem type → features → label → data → evaluation.

PROBLEM:
  Design a spam classifier system. Write a function `design()` that returns
  a dictionary answering all 5 questions below.

  Questions:
    1. Is this supervised or unsupervised? Regression or classification?
    2. List 5 features (X) you would extract from each email.
    3. What is the label (y)? What values can it take?
    4. How would you collect training data? (Where does labeled data come from?)
    5. How would you evaluate if your model is good? (Name one metric.)

EXAMPLE OUTPUT:
  {
    "problem_type": "supervised-classification",
    "features": ["sender_domain", "subject_words", "has_links", "num_caps", "email_length"],
    "label": "spam or not_spam (binary: 1 or 0)",
    "data_source": "public datasets like Enron, SpamAssassin, or manual labeling",
    "metric": "precision, recall, or F1"
  }
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
