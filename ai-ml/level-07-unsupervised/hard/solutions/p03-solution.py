"""Level 07 Unsupervised — Hard P03 Solution"""

from sklearn.decomposition import LatentDirichletAllocation
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np

def solve():
    docs = [
        "machine learning is great for prediction",
        "deep learning uses neural networks",
        "data science involves statistics",
        "python is a programming language",
        "machine learning models need data",
        "neural networks are powerful",
        "statistics helps understand data",
        "python is popular for ml",
    ]
    vectorizer = CountVectorizer(stop_words='english')
    X = vectorizer.fit_transform(docs)
    lda = LatentDirichletAllocation(n_components=2, random_state=42)
    lda.fit(X)
    feature_names = vectorizer.get_feature_names_out()
    for topic_idx, topic in enumerate(lda.components_):
        top_words = [feature_names[i] for i in topic.argsort()[-5:]]
        print(f"Topic {topic_idx}: {', '.join(top_words)}")
    return lda

if __name__ == "__main__":
    solve()