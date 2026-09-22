"""Level 12 — RAG Systems — Easy P01 Solution"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def similarity(text1, text2):
    vec = TfidfVectorizer()
    X = vec.fit_transform([text1, text2])
    return cosine_similarity(X[0:1], X[1:2])[0][0]

if __name__ == "__main__":
    s1 = similarity("machine learning is great", "deep learning uses neural nets")
    s2 = similarity("machine learning is great", "cooking recipes and food")
    print(f"{s1:.4f}")
    print(f"{s2:.4f}")
