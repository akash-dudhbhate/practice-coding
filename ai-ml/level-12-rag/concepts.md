# Level 12 — Concepts (Detailed Explanations)

Read each section BEFORE attempting its problem. Each concept has:
what it is in plain words → a worked example with real numbers →
why ML cares → the code → what confuses beginners.

**Vocabulary for this level:**
- **RAG** = Retrieval-Augmented Generation. The LLM can't read your
  documents, so you *retrieve* the relevant ones and paste them into
  the prompt before it *generates* an answer. Search → then answer.
- **Embedding / vector** — a list of numbers that represents text.
  Similar text → similar numbers → math can compare "meaning."
- **Corpus** — your collection of documents.

The whole level builds one pipeline piece by piece:
`chunk docs → embed → store → retrieve → (rerank) → generate answer`

---

## Easy

### 1. TF-IDF + Cosine Similarity — `p01`

**What it is:** Two steps that turn text into a similarity score.
**TF-IDF** (Term Frequency–Inverse Document Frequency) turns text
into a vector where each dimension is a word, and the value is how
*important* that word is (common in this doc, rare overall = high).
**Cosine similarity** measures the angle between two vectors:
1.0 = identical direction, 0.0 = unrelated.

**Worked example:** with a tiny 4-word vocabulary:
```
vocab = [learning, machine, cooking, neural]

"machine learning"  → [1, 1, 0, 0]
"deep learning"     → [1, 0, 0, 0]     shares "learning"
"cooking recipe"    → [0, 0, 1, 0]     shares nothing

cosine("machine learning", "deep learning"):
  dot   = 1·1 + 1·0 + 0·0 + 0·0 = 1
  norms = √2 × √1 = 1.41
  score = 1 / 1.41 ≈ 0.71        ← similar!

cosine("machine learning", "cooking recipe") = 0  ← unrelated
```

**Why ML cares:** This is the simplest way to give text a numeric
"meaning." Real systems use neural embeddings (OpenAI, sentence-
transformers) that capture semantics better, but TF-IDF is the same
idea with zero ML needed — and it's what you'll implement here.

**Code:**
```python
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def similarity(text1, text2):
    vec = TfidfVectorizer().fit_transform([text1, text2])
    return cosine_similarity(vec[0], vec[1])[0][0]
```

**Common confusion:** TF-IDF only sees *shared words*, not meaning.
"car" and "automobile" score 0 because no word is literally shared —
that's a keyword-matching limit, not a bug.

---

### 2. Simple Retrieval — `p02`

**What it is:** The "R" in RAG. Embed every document once, embed the
query the same way, compute cosine similarity between the query and
every doc, and return the top_k highest-scoring docs.

**Worked example:**
```python
docs  = ["ML is a subset of AI", "Deep learning uses neural nets",
         "Cooking requires recipes", "NLP processes text"]
query = "What is machine learning?"

scores (after TF-IDF + cosine):
  "ML is a subset of AI"            → 0.32
  "Deep learning uses neural nets"  → 0.32
  "Cooking requires recipes"        → 0.00
  "NLP processes text"              → 0.00

top_k=2 → return the two 0.32 docs
```

**Why ML cares:** This is literally the core of every "chat with your
docs" product. Notion AI, PDF-chat apps, and internal search all do
exactly this (with fancier embeddings). If retrieval returns the
wrong doc, the LLM gets the wrong context and answers wrong —
retrieval quality IS answer quality.

**Code:**
```python
def retrieve(query, docs, top_k):
    vectorizer = TfidfVectorizer()
    doc_vecs = vectorizer.fit_transform(docs)
    q_vec = vectorizer.transform([query])
    scores = cosine_similarity(q_vec, doc_vecs).flatten()
    ranked = sorted(zip(docs, scores), key=lambda x: -x[1])
    return ranked[:top_k]
```

**Common confusion:** `fit_transform` goes on the DOCS (it learns
the vocabulary from them); the query only gets `transform` (mapped
into that same vocabulary). Fitting on the query would give it a
different vector space where similarity means nothing.

---

### 3. Text Chunking — `p03`

**What it is:** LLMs have a context window (a max input length), and
long docs are also bad retrieval targets — the relevant paragraph
gets "diluted" inside a huge document. So you split docs into
overlapping chunks. **Overlap** = the last few characters of one
chunk repeat at the start of the next, so a sentence cut in half
still exists whole in one of the chunks.

**Worked example:** `chunk_size=50`, `overlap=10`, `step = 50-10 = 40`
```
text = "Machine learning is a subset of artificial intelligence. ..."

chunk 0: text[0:50]   = "Machine learning is a subset of artificial intelli"
chunk 1: text[40:90]  = "al intelligence. It uses algorithms to learn patte"
                          ^^ repeats chars 40-49 — "artificial intelligence"
                             stays readable even though it was cut
chunk 2: text[80:130] = ...
```

**Why ML cares:** Every RAG system chunks. Too small → chunks lose
context ("it" refers to nothing). Too big → irrelevant text dilutes
the signal and overflows the context window. Overlap is the cheap
fix for "the answer was split across a chunk boundary."

**Code:**
```python
def chunk_text(text, chunk_size, overlap):
    step = chunk_size - overlap
    return [text[i:i + chunk_size]
            for i in range(0, len(text), step)]
```

**Common confusion:** `step` is NOT `chunk_size`. With size 50 and
overlap 10 you advance 40 characters per chunk — using 50 would
produce zero overlap and defeat the point.

---

## Medium

### 4. Vector Store — `p01`

**What it is:** A "database" that stores (document, vector) pairs
and answers "give me the docs most similar to this query vector."
Conceptually: `store = [(doc, vec), ...]`, and search = compute
similarity to every stored vec, sort, take top_k.

**Worked example:**
```python
store after adding docs:
  [("ML is great",            [0.7, 0.7, 0.0, ...]),
   ("Python is a language",   [0.0, 0.0, 0.9, ...]),
   ("Deep learning is fun",   [0.6, 0.8, 0.0, ...])]

query "Tell me about AI" → [0.5, 0.6, 0.0, ...]
cosine to each → [0.85, 0.10, 0.90]
top 2 → "Deep learning is fun", "ML is great"
```

**Why ML cares:** This is the entire product of vector databases
(Pinecone, Weaviate, Chroma, FAISS). They add speed tricks
(indexing billions of vectors) and persistence, but the core is
exactly what you'll write: store vectors, rank by similarity.

**Code:**
```python
def vector_store(docs, query, top_k):
    vec = TfidfVectorizer()
    doc_vecs = vec.fit_transform(docs)          # the "store"
    q = vec.transform([query])                  # the "index lookup"
    scores = cosine_similarity(q, doc_vecs).flatten()
    idx = scores.argsort()[::-1][:top_k]        # descending top_k
    return [(docs[i], scores[i]) for i in idx]
```

**Common confusion:** A vector store is NOT a normal database with
extra features — it has no notion of "exact match." It answers
"what's *closest*?" not "what equals X?". Searching for text it has
never seen still returns the nearest docs (possibly bad ones).

---

### 5. Reranking — `p02`

**What it is:** First-pass retrieval is fast but crude — it ranks
hundreds of docs quickly. A **reranker** takes only the top results
and re-scores them with a slower, more careful method. Two stages:
cheap recall first, precision second.

**Worked example:**
```python
retrieved = [("Old doc about AI", 0.6),
             ("Recent ML advances", 0.5),
             ("Ancient history", 0.4)]
query = "machine learning advances"

new_score = old_score + 0.1 × (query words found in doc)

  "Old doc about AI"     → 0.6 + 0.1×0 = 0.60  (no query words)
  "Recent ML advances"   → 0.5 + 0.1×1 = 0.60  (matches "advances")
  "Ancient history"      → 0.4 + 0.1×0 = 0.40

reranked: Recent ML advances / Old doc about AI tie at 0.60,
Ancient history stays last.
```

**Why ML cares:** Production RAG almost always reranks. Real systems
use a cross-encoder model (a neural net that reads query+doc
together) instead of word counting, but the idea is identical: the
first ranker is a fast filter, the second is the careful judge.

**Code:**
```python
def rerank(query, retrieved_docs):
    qwords = set(query.lower().split())
    rescored = []
    for doc, score in retrieved_docs:
        bonus = 0.1 * len(set(doc.lower().split()) & qwords)
        rescored.append((doc, score + bonus))
    return sorted(rescored, key=lambda x: -x[1])
```

**Common confusion:** Reranking reorders the *existing* results —
it can't rescue a relevant doc that retrieval never returned.
Garbage in, reranked garbage out.

---

### 6. Hybrid Search — `p03`

**What it is:** Combine two different scoring methods:
- **Keyword score** — what fraction of the query's words literally
  appear in the doc (exact matching, catches jargon/IDs/names)
- **Semantic score** — cosine similarity of the vectors (catches
  synonyms and related meaning)

`final = 0.5 × keyword + 0.5 × semantic`

**Worked example:** query = "machine learning"
```
doc: "AI and machine learning"
  keyword  = 2/2 query words found = 1.00
  semantic = 0.30 (TF-IDF cosine)
  final    = 0.5×1.00 + 0.5×0.30 = 0.65   ← wins

doc: "ML models learn patterns"
  keyword  = 0/2 = 0.00   ("ML" ≠ "machine" literally)
  semantic = 0.20         (topic still related)
  final    = 0.5×0.00 + 0.5×0.20 = 0.10
```

**Why ML cares:** Neither method alone is enough. Semantic search
misses exact strings ("error code E-4021"); keyword search misses
synonyms ("car" vs "automobile"). Hybrid is standard in modern
search (Elasticsearch + vectors, "BM25 + dense retrieval").

**Code:**
```python
def hybrid_search(query, docs, top_k):
    q_words = set(query.lower().split())
    vec = TfidfVectorizer()
    doc_vecs = vec.fit_transform(docs)
    sem = cosine_similarity(vec.transform([query]), doc_vecs).flatten()
    scored = []
    for doc, s in zip(docs, sem):
        kw = len(q_words & set(doc.lower().split())) / len(q_words)
        scored.append((doc, 0.5 * kw + 0.5 * s))
    return sorted(scored, key=lambda x: -x[1])[:top_k]
```

**Common confusion:** The 0.5/0.5 weights are a tunable dial, not
law. Legal/code search wants more keyword weight; conceptual
questions want more semantic weight.

---

## Hard

### 7. The RAG Pipeline — `p01`

**What it is:** The full loop end to end: `query → retrieve best
doc → build a prompt containing that doc → generate an answer
grounded in it.` The "generate" step is usually an LLM, but a
template shows the pattern without needing one.

**Worked example:**
```python
docs  = ["ML is a subset of AI", "Deep learning uses neural nets"]
query = "What is ML?"

1. retrieve → "ML is a subset of AI"   (highest cosine score)
2. generate → f"Based on: {doc}\n{query} is related to {doc}."
   → "Based on: ML is a subset of AI
      What is ML? is related to ML is a subset of AI."
```
With a real LLM, step 2 is:
`"Answer using ONLY this context: {doc}\nQuestion: {query}"`

**Why ML cares:** This is THE architecture for grounding LLMs on
private data — docs, tickets, codebases — without fine-tuning. It
also reduces hallucination: the model answers from retrieved text
instead of its fuzzy memory.

**Code:**
```python
def rag(query, docs):
    doc, _ = retrieve(query, docs, top_k=1)[0]     # from easy/p02
    answer = f"Based on: {doc}\n{query} is related to {doc}."
    return doc, answer
```

**Common confusion:** RAG does NOT retrain the model. The doc is
just pasted into the prompt — the model's weights never change.
That's why you can update facts by editing documents, not models.

---

### 8. RAG Evaluation — `p02`

**What it is:** Measure retrieval quality with a test set: pairs of
(question, expected_doc). For each question, run retrieval and
check if the expected doc came back in the top-k. The metric is
`accuracy = correct_retrievals / total_questions` — same idea as
classification accuracy, applied to retrieval.

**Worked example:**
```python
questions = ["What is ML?", "What is deep learning?"]
answers   = ["ML is AI", "Deep learning uses neural nets"]

q1 retrieves "ML is AI"                    → match  ✓
q2 retrieves "Deep learning uses neural nets" → match ✓

accuracy = 2/2 = 1.00
```

**Why ML cares:** "It seems to work" is how RAG systems silently
rot. You need numbers: does a new chunking strategy help? Does a
new embedding model help? Only a retrieval test set can tell you.
(This metric is often called "recall@k" or "hit rate".)

**Code:**
```python
def evaluate_rag(questions, docs, answers):
    correct = 0
    for q, expected in zip(questions, answers):
        top_doc, _ = retrieve(q, docs, top_k=1)[0]
        if top_doc == expected:
            correct += 1
    return correct / len(questions)
```

**Common confusion:** This evaluates RETRIEVAL, not the final
answer. A system can retrieve the right doc and still generate a
wrong answer from it — full eval has a second stage for answer
correctness (usually LLM-graded).

---

### 9. Query Rewriting — `p03`

**What it is:** Users type short, vague, jargon-y queries ("What is
ML?") while your docs use full terms ("machine learning"). Query
rewriting fixes the query BEFORE retrieval: expand abbreviations,
add implied context, fix ambiguity. Better query → better retrieval.

**Worked example:**
```
"What is ML?"          → "What is machine learning?"
"Tell me about NLP"    → "Tell me about natural language processing"
"CV vs DL"             → "computer vision vs deep learning"
```
Now the doc "machine learning is a subset of AI" literally shares
words with the query — TF-IDF can find it, whereas "ML" matched
nothing.

**Why ML cares:** In production this is often done BY an LLM (one
call rewrites the query, a second retrieves). It's also how
conversational RAG handles follow-ups — "tell me more about it"
gets rewritten to include what "it" refers to.

**Code:**
```python
def rewrite_query(query):
    expansions = {"ML": "machine learning", "DL": "deep learning",
                  "AI": "artificial intelligence",
                  "NLP": "natural language processing",
                  "CV": "computer vision", "RL": "reinforcement learning"}
    return " ".join(expansions.get(w.strip("?.,!"), w)
                    for w in query.split())
```

**Common confusion:** Replace whole WORDS only. Blind string
replacement turns "HTML" into "HTmachine learning" — split on
whitespace and match tokens, don't use `str.replace` on substrings.

---

## Done with concepts? → Try `easy/p01-similarity.py`
