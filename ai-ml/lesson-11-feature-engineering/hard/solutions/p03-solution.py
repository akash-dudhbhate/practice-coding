"""
Text Classification Pipeline
=============================
Build a text classification pipeline with 20+ documents in 2 categories.
Combine TF-IDF features with custom features (length, word count, sentiment
words). Train a classifier, evaluate, and show most important features.
"""

import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score
from scipy.sparse import hstack, csr_matrix

np.random.seed(42)

# Sentiment word lists for custom features
POSITIVE_WORDS = {"good", "great", "excellent", "amazing", "love", "best", "fantastic", "wonderful", "awesome", "happy"}
NEGATIVE_WORDS = {"bad", "terrible", "awful", "hate", "worst", "horrible", "disappointing", "poor", "sad", "angry"}


def extract_custom_features(texts):
    """Extract manual features from text."""
    features = []
    for text in texts:
        words = text.lower().split()
        word_set = set(words)
        features.append([
            len(text),                                          # text length
            len(words),                                         # word count
            sum(1 for w in word_set if w in POSITIVE_WORDS),    # positive word count
            sum(1 for w in word_set if w in NEGATIVE_WORDS),    # negative word count
            1 if "?" in text else 0,                            # has question mark
            1 if "!" in text else 0,                            # has exclamation
        ])
    return np.array(features, dtype=float)


if __name__ == "__main__":
    # 24 documents: 12 positive reviews, 12 negative reviews
    positive_reviews = [
        "This movie was great and I loved every minute of it.",
        "An excellent film with amazing performances from the cast.",
        "Best movie I have seen this year, truly fantastic.",
        "Wonderful storyline and awesome visual effects throughout.",
        "I am so happy I watched this, it was a masterpiece.",
        "Great direction and a fantastic script make this a must-see.",
        "Absolutely loved the soundtrack, it was simply wonderful.",
        "The acting was excellent and the plot was amazing.",
        "What a great experience, I would watch it again happily.",
        "Fantastic movie with the best ending I have ever seen.",
        "This film made me so happy, truly a wonderful journey.",
        "Amazing visuals and great storytelling from start to finish.",
    ]
    negative_reviews = [
        "This movie was terrible and I hated every minute of it.",
        "An awful film with disappointing performances from the cast.",
        "Worst movie I have seen this year, truly horrible.",
        "Poor storyline and bad visual effects throughout the film.",
        "I am so angry I watched this, it was a disaster.",
        "Terrible direction and a poor script make this avoidable.",
        "I hated the soundtrack, it was simply awful and sad.",
        "The acting was bad and the plot was disappointing.",
        "What a terrible experience, I would never watch it again.",
        "Horrible movie with the worst ending I have ever seen.",
        "This film made me so sad, truly a poor and awful journey.",
        "Bad visuals and terrible storytelling from start to finish.",
    ]

    texts = positive_reviews + negative_reviews
    labels = [1] * 12 + [0] * 12  # 1 = positive, 0 = negative

    # --- Extract custom features ---
    custom_feats = extract_custom_features(texts)
    custom_names = ["text_length", "word_count", "positive_words", "negative_words", "has_question", "has_exclaim"]

    print("=== Custom features (first 4 docs) ===")
    print(pd.DataFrame(custom_feats[:4], columns=custom_names))
    print()

    # --- TF-IDF features ---
    tfidf = TfidfVectorizer(max_features=100, stop_words="english", ngram_range=(1, 2))
    tfidf_feats = tfidf.fit_transform(texts)

    # --- Combine TF-IDF + custom features ---
    X = hstack([tfidf_feats, csr_matrix(custom_feats)])
    y = np.array(labels)

    print(f"Combined feature matrix: {X.shape} (TF-IDF: {tfidf_feats.shape[1]}, Custom: {custom_feats.shape[1]})\n")

    # --- Train and evaluate ---
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42, stratify=y)
    clf = LogisticRegression(random_state=42, max_iter=1000)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)

    print("=== Classification Report ===")
    print(classification_report(y_test, y_pred, target_names=["Negative", "Positive"]))
    print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}\n")

    # --- Show most important features ---
    # Get feature names (TF-IDF + custom)
    tfidf_names = tfidf.get_feature_names_out().tolist()
    all_names = tfidf_names + custom_names
    coefficients = clf.coef_[0]

    # Top positive (predict positive class) and negative (predict negative class)
    top_pos_idx = np.argsort(coefficients)[-10:][::-1]
    top_neg_idx = np.argsort(coefficients)[:10]

    print("=== Top 10 features predicting POSITIVE ===")
    for i in top_pos_idx:
        print(f"  {all_names[i]:30s}  coef={coefficients[i]:+.4f}")

    print("\n=== Top 10 features predicting NEGATIVE ===")
    for i in top_neg_idx:
        print(f"  {all_names[i]:30s}  coef={coefficients[i]:+.4f}")
