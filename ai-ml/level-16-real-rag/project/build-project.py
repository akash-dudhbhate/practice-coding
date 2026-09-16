"""
LEVEL 16 PROJECT — Mini Real-RAG Over a Knowledge Base
=======================================================

Wire the whole level together: an embedder (TfidfVectorizer standing
in for sentence-transformers), a VectorStore (standing in for
FAISS/Chroma), ingestion with chunking + metadata, retrieval, a
template "generator", and a hit-rate eval.

DATA: KB below — 6 knowledge-base articles, several long enough to
need chunking.

BUILD:
  1. `VectorStore`   — .add(texts) / .query(q_vec, k) → [(idx, score)]
                       (expose .vec and .texts)
  2. `ingest(store, docs, size=120, overlap=30)` — chunk with
     {id, text, start, end} metadata → store.add → return chunk count
  3. `retrieve(store, query, k=3)` — embed query → top chunk texts
  4. `rag_answer(store, query)` — retrieve → answer string citing
     the top chunk(s)
  5. `evaluate(store)` — run TEST_QUERIES, print the hit-rate

TEST QUERIES:
  - "how do I stop my model overfitting"  → regularization article
  - "refund policy"                       → returns article
  - "reset my password"                   → accounts article

EXPECTED (roughly):
  ```
  Query: refund policy
  Based on the docs: ...30 days...receipt...
  Hit-rate: 1.00
  ```

BONUS: add `hybrid=True` to retrieve() — fuse dense cosine with a
  BM25-ish keyword score (see hard/p03) so exact-term queries win.
"""

KB = [
    "Overfitting happens when a model memorizes training data instead of "
    "learning patterns. Fixes: add L1/L2 regularization, use dropout, get "
    "more data, or stop training early. Cross-validation detects it early "
    "by measuring generalization on held-out folds.",

    "Refunds: customers may return any item within 30 days of purchase "
    "with a receipt for a full refund. Digital goods are refundable "
    "within 14 days if unused. Refunds are issued to the original "
    "payment method within 5 business days.",

    "Account help: to reset your password, click 'Forgot password' on the "
    "login page and follow the email link. If the email does not arrive, "
    "check spam or contact support. Sessions expire after 24 hours of "
    "inactivity for security.",

    "Deployment checklist: pin dependency versions, set environment "
    "variables for secrets, run the test suite in CI, build a Docker "
    "image, tag it with the git SHA, and roll out with a canary release "
    "before full production traffic.",

    "Python performance tips: prefer list comprehensions over loops, use "
    "generators for large data, profile with cProfile before optimizing, "
    "and reach for numpy vectorization when a hot loop does math on "
    "arrays of numbers.",

    "Team workflow: open a pull request early as a draft, keep changes "
    "under 400 lines, request two reviewers, squash-merge to main, and "
    "write a changelog entry for anything user-facing.",
]

TEST_QUERIES = [
    ("how do I stop my model overfitting", ["regularization", "dropout"]),
    ("refund policy", ["refund", "receipt"]),
    ("reset my password", ["password", "login"]),
]


class VectorStore:
    # TODO: __init__ with self.vec / self.texts / self.matrix
    # TODO: .add(texts) → fit on first add, transform after → count
    # TODO: .query(q_vec, k) → [(idx, score)] sorted desc
    pass


def ingest(store, docs, size=120, overlap=30):
    # TODO: chunk each doc ({id, text, start, end}) → store.add → count
    pass


def retrieve(store, query, k=3):
    # TODO: embed query → store.query → top-k chunk texts
    pass


def rag_answer(store, query):
    # TODO: retrieve → build prompt → answer string citing context
    pass


def evaluate(store):
    # TODO: hit-rate over TEST_QUERIES
    pass


if __name__ == "__main__":
    store = VectorStore()
    n = ingest(store, KB)
    print(f"Ingested {n} chunks")
    for q, _ in TEST_QUERIES:
        print(f"\nQuery: {q}")
        print(rag_answer(store, q))
    print(f"\nHit-rate: {evaluate(store):.2f}")
