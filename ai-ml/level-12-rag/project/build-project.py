"""
LEVEL 12 PROJECT — Mini RAG Over Your Notes
============================================

Build a complete retrieval pipeline over a personal knowledge
base — chunk → embed → store → retrieve → answer.

DATA: NOTES below — 8 short "notes" (your fake second brain).

BUILD:
  1. `chunk_notes(notes, chunk_size=80, overlap=20)` → list of chunks
     (each note may split into several overlapping chunks)
  2. `build_store(chunks)` → fitted TfidfVectorizer + doc matrix
  3. `ask(query, vectorizer, matrix, chunks, top_k=2)` →
     retrieves top chunks, returns answer string:
     "From your notes: {chunk1} | {chunk2}"

TEST QUERIES to verify:
  - "how do I fix overfitting"  → should find the regularization note
  - "git commands"              → should find the git note
  - "dinner ideas"              → should find the recipe note

EXPECTED (roughly):
  ```
  Query: how do I fix overfitting
  From your notes: regularization and dropout prevent... | ...
  ```

BONUS: add `evaluate()` — 5 queries with expected-note keywords,
  report retrieval accuracy like hard/p02.

HINT: keep chunks as (text, source_note_id) tuples so answers
  can cite which note they came from.
"""

NOTES = [
    "Overfitting fix: use regularization, dropout, or more data. Cross-validation detects it early.",
    "Git basics: git add stages changes, git commit saves them, git push uploads to remote.",
    "Pasta recipe: boil water, add salt, cook spaghetti 9 min, drain, add sauce.",
    "Python tips: use list comprehensions, f-strings for formatting, virtualenv for deps.",
    "ML workflow: clean data first, split train/test, baseline model, then iterate.",
    "Meeting notes: project deadline moved to Friday, design review on Tuesday.",
    "Workout plan: 3 sets of squats, pushups, planks. Rest day on Sunday.",
    "Reading list: 'Deep Learning' by Goodfellow, 'Hands-On ML' by Geron.",
]


def chunk_notes(notes, chunk_size=80, overlap=20):
    # TODO
    pass


def build_store(chunks):
    # TODO: return (vectorizer, tfidf_matrix)
    pass


def ask(query, vectorizer, matrix, chunks, top_k=2):
    # TODO
    pass


if __name__ == "__main__":
    chunks = chunk_notes(NOTES)
    vec, mat = build_store(chunks)
    for q in ["how do I fix overfitting", "git commands", "dinner ideas"]:
        print(f"Query: {q}")
        print(ask(q, vec, mat, chunks))
        print()
