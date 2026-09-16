"""
Level 16 Checker — Real RAG
=============================
Usage:
    python3 check.py easy/p01
    python3 check.py all
"""

import importlib.util
import os
import sys
import glob
import numpy as np


def load_mod(fp):
    spec = importlib.util.spec_from_file_location("work", fp)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


DOCS = [
    "Python is a popular programming language for data science",
    "Machine learning models learn patterns from data",
    "Pasta needs boiling salted water for nine minutes",
    "Neural networks are loosely inspired by brain neurons",
    "Git commit saves a snapshot of your code changes",
    "The Eiffel Tower is in Paris and made of iron",
]


def check_easy_p01(mod):
    if not hasattr(mod, 'embed'):
        return False, "Function 'embed' not found"
    M = mod.embed(DOCS)
    if not isinstance(M, np.ndarray) or M.shape[0] != 6:
        return False, f"Expected (6, vocab) array, got {getattr(M,'shape',M)}"
    norms = np.linalg.norm(M, axis=1)
    if not np.allclose(norms, 1.0, atol=1e-3):
        return False, f"Rows should be L2-normalized, norms={norms}"
    return True, "All tests passed!"


def check_easy_p02(mod):
    if not hasattr(mod, 'cosine_all'):
        return False, "Function 'cosine_all' not found"
    doc_matrix = np.eye(4)
    q = np.array([1.0, 0, 0, 0])
    scores = mod.cosine_all(q, doc_matrix)
    if len(scores) != 4 or abs(scores[0] - 1.0) > 1e-3:
        return False, f"cosine with identical vector should be 1.0, got {scores}"
    return True, "All tests passed!"


def check_easy_p03(mod):
    if not hasattr(mod, 'chunk_text'):
        return False, "Function 'chunk_text' not found"
    text = "a" * 250
    chunks = mod.chunk_text(text, size=100, overlap=20)
    if not isinstance(chunks, list) or len(chunks) < 2:
        return False, f"Expected ≥2 chunks, got {len(chunks) if isinstance(chunks,list) else chunks}"
    c0 = chunks[0]
    if not isinstance(c0, dict) or c0.get("text") != text[:100]:
        return False, f"First chunk should be dict with 'text' key, got {c0}"
    return True, "All tests passed!"


def check_medium_p01(mod):
    if not hasattr(mod, 'VectorStore'):
        return False, "Class 'VectorStore' not found"
    store = mod.VectorStore()
    n = store.add(DOCS)
    if n != 6:
        return False, f"add() should return 6, got {n}"
    q = store.vec.transform(["machine learning"])
    hits = store.query(q, 2)
    if not isinstance(hits, list) or len(hits) != 2:
        return False, f"query should return 2 hits, got {hits}"
    if "machine learning" not in store.texts[hits[0][0]].lower():
        return False, f"Top hit should be the ML doc, got '{store.texts[hits[0][0]]}'"
    return True, "All tests passed!"


def check_medium_p02(mod):
    if not hasattr(mod, 'ingest') or not hasattr(mod, 'VectorStore'):
        return False, "Need 'ingest' and 'VectorStore'"
    store = mod.VectorStore()
    n = mod.ingest(store, DOCS)
    if n < 6:
        return False, f"ingest should add ≥6 chunks, got {n}"
    if store.matrix is None or len(store.texts) < 6:
        return False, "Store should hold ≥6 texts after ingest"
    return True, "All tests passed!"


def check_medium_p03(mod):
    if not hasattr(mod, 'retrieve') or not hasattr(mod, 'VectorStore'):
        return False, "Need 'retrieve' and 'VectorStore'"
    store = mod.VectorStore()
    store.add(DOCS)
    results = mod.retrieve(store, "machine learning models", store.vec, k=2)
    if not isinstance(results, list) or len(results) != 2:
        return False, f"Expected 2 texts, got {results}"
    if "machine learning" not in results[0].lower():
        return False, f"Top result should mention ML, got '{results[0]}'"
    return True, "All tests passed!"


def check_hard_p01(mod):
    if not hasattr(mod, 'rag_answer') or not hasattr(mod, 'VectorStore'):
        return False, "Need 'rag_answer' and 'VectorStore'"
    store = mod.VectorStore()
    store.add(DOCS)
    ans = mod.rag_answer("which language for data science?", store, store.vec)
    if not isinstance(ans, str) or len(ans) < 10:
        return False, f"Expected answer string, got {ans!r}"
    if "python" not in ans.lower():
        return False, f"Answer should cite the Python doc, got '{ans[:80]}'"
    return True, "All tests passed!"


def check_hard_p02(mod):
    if not hasattr(mod, 'eval_rag') or not hasattr(mod, 'VectorStore'):
        return False, "Need 'eval_rag' and 'VectorStore'"
    store = mod.VectorStore()
    store.add(DOCS)
    queries = ["what language for data", "cooking pasta", "saving code"]
    expected = [["python"], ["pasta"], ["git"]]
    score = mod.eval_rag(queries, expected, store, store.vec)
    if not isinstance(score, float) or not 0.0 <= score <= 1.0:
        return False, f"Hit-rate should be float in [0,1], got {score}"
    if score < 2/3:
        return False, f"Expected ≥2/3 hits on this corpus, got {score:.2f}"
    return True, "All tests passed!"


def check_hard_p03(mod):
    if not hasattr(mod, 'hybrid') or not hasattr(mod, 'VectorStore'):
        return False, "Need 'hybrid' and 'VectorStore'"
    store = mod.VectorStore()
    store.add(DOCS)
    results = mod.hybrid(store, store.vec, "python data", DOCS, k=2)
    if not isinstance(results, list) or len(results) == 0:
        return False, f"Expected non-empty results, got {results}"
    first = results[0]
    # Accept either [(idx,score)] or [text,...]
    if isinstance(first, tuple):
        text = DOCS[first[0]]
    else:
        text = first
    if "python" not in str(text).lower():
        return False, f"Top hybrid result should be the Python doc, got '{text}'"
    return True, "All tests passed!"


CHECKS = {
    "easy/p01": check_easy_p01,   "easy/p02": check_easy_p02,
    "easy/p03": check_easy_p03,
    "medium/p01": check_medium_p01, "medium/p02": check_medium_p02,
    "medium/p03": check_medium_p03,
    "hard/p01": check_hard_p01,   "hard/p02": check_hard_p02,
    "hard/p03": check_hard_p03,
}


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 check.py <difficulty/pXX> or 'all'")
        return
    target = sys.argv[1]
    if target == "all":
        for cid in sorted(CHECKS):
            run_one(cid)
        return
    run_one(target)


def run_one(cid):
    if cid not in CHECKS:
        print(f"Unknown: {cid}")
        return
    diff, num = cid.split("/")
    nc = num.lstrip("p")
    d = os.path.join(os.path.dirname(__file__), diff)
    ms = [f for f in glob.glob(os.path.join(d, f"p{nc}-*.py"))
          if "solutions" not in f]
    w = ms[0] if ms else None
    if not w:
        print(f"{cid}: FILE NOT FOUND")
        return
    try:
        mod = load_mod(w)
        passed, msg = CHECKS[cid](mod)
        print(f"{cid}: {'PASS' if passed else 'FAIL'} — {msg}")
        if passed:
            with open(w) as f:
                if "DONE" not in f.readline().strip():
                    print("  → add '# DONE' to mark complete")
    except Exception as e:
        print(f"{cid}: ERROR — {e}")


if __name__ == "__main__":
    main()
