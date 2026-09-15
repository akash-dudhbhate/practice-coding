"""
Text Feature Engineering
========================
Extract manual features from text (length, word count, has_url, has_question_mark)
and combine them with TF-IDF features into a single feature matrix.
"""

import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.sparse import hstack


if __name__ == "__main__":
    # Sample text dataset (12 sentences)
    texts = [
        "The weather is nice today.",
        "How do I learn machine learning?",
        "Check out https://example.com for deals!",
        "Python is a great programming language.",
        "What time is the meeting?",
        "I love reading books on weekends.",
        "Is this the right way to do it?",
        "Visit https://news.com for latest updates.",
        "Data science is an exciting field.",
        "Where can I find good restaurants?",
        "The stock market crashed yesterday.",
        "Can you help me with this problem?",
    ]

    df = pd.DataFrame({"text": texts})

    # --- Extract manual features ---
    df["text_length"] = df["text"].str.len()
    df["word_count"] = df["text"].str.split().str.len()
    df["has_url"] = df["text"].str.contains(r"https?://", regex=True).astype(int)
    df["has_question_mark"] = df["text"].str.contains(r"\?", regex=True).astype(int)

    print("=== Manual features ===")
    print(df)
    print()

    # --- Apply TF-IDF ---
    tfidf = TfidfVectorizer(max_features=50, stop_words="english")
    tfidf_features = tfidf.fit_transform(df["text"])

    print(f"TF-IDF feature matrix shape: {tfidf_features.shape}")
    print(f"TF-IDF vocabulary ({len(tfidf.vocabulary_)} terms):")
    for term, idx in sorted(tfidf.vocabulary_.items(), key=lambda x: x[1])[:10]:
        print(f"  {idx}: {term}")
    print("  ...")
    print()

    # --- Combine manual + TF-IDF features ---
    manual_features = df[["text_length", "word_count", "has_url", "has_question_mark"]].values.astype(float)
    combined = hstack([tfidf_features, manual_features])  # sparse + dense -> sparse

    print(f"Combined feature matrix shape: {combined.shape}")
    print(f"  TF-IDF features:   {tfidf_features.shape[1]}")
    print(f"  Manual features:   {manual_features.shape[1]}")
    print(f"  Total:             {combined.shape[1]}")
