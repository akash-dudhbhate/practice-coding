"""Level 07 — Unsupervised Learning — Hard P03 Solution"""

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import NMF

def topics():
    docs = [
        "python machine learning model data neural network",
        "deep learning pytorch neural network training model",
        "recipe cooking food kitchen ingredients bake",
        "cooking delicious meal recipe dinner food"
    ]
    vec = TfidfVectorizer(stop_words='english')
    X = vec.fit_transform(docs)
    nmf = NMF(n_components=2, random_state=42)
    W = nmf.fit_transform(X)
    feature_names = vec.get_feature_names_out()
    topic_words = []
    for i in range(2):
        top_idx = nmf.components_[i].argsort()[-5:][::-1]
        topic_words.append([feature_names[j] for j in top_idx])
    return topic_words, W

if __name__ == "__main__":
    words, W = topics()
    for i, ws in enumerate(words):
        print(f"Topic {i}: {', '.join(ws)}")
    print(W.shape)
