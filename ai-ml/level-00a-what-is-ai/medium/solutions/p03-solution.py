"""Solution — medium/p03-similarity.py"""


def similarity(text1, text2):
    set1 = set(text1.lower().split())
    set2 = set(text2.lower().split())
    shared = set1 & set2
    total = set1 | set2
    return len(shared) / len(total) if total else 0.0
