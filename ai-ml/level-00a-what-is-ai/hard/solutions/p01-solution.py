"""Solution — hard/p01-mini-rag.py"""


def _sim(t1, t2):
    s1, s2 = set(t1.lower().split()), set(t2.lower().split())
    shared, total = s1 & s2, s1 | s2
    return len(shared) / len(total) if total else 0.0


def mini_rag(question, docs):
    best, best_score = None, 0.0
    for doc in docs:
        score = _sim(question, doc)
        if score > best_score:
            best, best_score = doc, score
    return best if best else "I don't know"
