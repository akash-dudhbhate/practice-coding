"""
Lesson 01 - Medium P01
Design a full spam classifier by answering 5 design questions.

Solution:
  Q1. What kind of ML problem is this?
  Q2. What features would you use?
  Q3. How would you collect and label data?
  Q4. What algorithm would you start with?
  Q5. How would you evaluate it?
"""

# ---------------------------------------------------------------------------
# Design answers
# ---------------------------------------------------------------------------
design = {
    "Q1_problem_type": {
        "answer": "Binary classification",
        "explanation": (
            "Each email is labeled as either 'spam' (1) or 'not spam' (0). "
            "The model learns a decision boundary that separates the two classes."
        ),
    },
    "Q2_features": {
        "answer": [
            "word_frequencies (e.g., 'free', 'win', 'click here')",
            "character_frequencies / n-gram counts",
            "email_length (characters / words)",
            "num_capitalized_words",
            "num_exclamation_marks",
            "has_url (boolean)",
            "num_urls",
            "sender_domain_reputation_score",
            "subject_line_length",
            "presence_of_attachments",
        ],
        "explanation": (
            "Features capture textual patterns and metadata that correlate with spam. "
            "TF-IDF or count-based encodings turn text into numeric vectors the model can use."
        ),
    },
    "Q3_data_collection": {
        "answer": "Collect labeled emails from multiple sources",
        "explanation": (
            "1. Use public datasets (e.g., Enron Spam, SpamAssassin Public Corpus).\n"
            "2. Augment with user-reported spam/ham from your own email system.\n"
            "3. Ensure balanced classes and label each email as spam (1) or ham (0).\n"
            "4. Remove personally-identifiable information for privacy.\n"
            "5. Split into train/validation/test sets."
        ),
    },
    "Q4_algorithm": {
        "answer": "Start with Naive Bayes (MultinomialNB), then try Logistic Regression / Linear SVM",
        "explanation": (
            "Naive Bayes is fast, works well with text count features, and provides a strong baseline. "
            "Logistic Regression and Linear SVM with TF-IDF features often improve accuracy while staying interpretable."
        ),
    },
    "Q5_evaluation": {
        "answer": "Use precision, recall, F1-score, and confusion matrix; avoid accuracy alone",
        "explanation": (
            "Spam detection is typically imbalanced (most email is ham). Accuracy can be misleading. "
            "Precision matters (don't flag good email as spam); recall matters (catch as much spam as possible). "
            "F1 balances both. Use a held-out test set and cross-validation for robust estimates."
        ),
    },
}

# ---------------------------------------------------------------------------
# Print the design
# ---------------------------------------------------------------------------
for key, val in design.items():
    q_label = key.replace("_", " ").title()
    print(f"{q_label}")
    print(f"  Answer: {val['answer']}")
    print(f"  Why:    {val['explanation']}")
    print()
