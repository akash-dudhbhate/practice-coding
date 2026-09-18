# Level 12 — Concepts (Detailed Explanations)

Read each section BEFORE attempting its problem. Each concept explains:
What it is · Why it exists · Where it's used · What goes wrong without it ·
worked example · code · expected output.

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

**Why it exists:** Computers can't compare text directly — they
need numbers. TF-IDF was invented to weight words by importance so
"the" doesn't dominate (raw counts make stopwords look important).
Cosine exists because a raw dot product rewards longer documents —
measuring the ANGLE normalizes length away.

**Where it's used:** Classic information retrieval and keyword
search. Real systems use neural embeddings (OpenAI,
sentence-transformers) that capture semantics better, but TF-IDF
is the same idea with zero ML — and it's what you'll implement
here.

**What goes wrong without it:** Score by raw word counts → "the"
and "is" outrank meaningful words. Score by raw dot product → the
longest doc always wins regardless of relevance. And know the
limit: TF-IDF only sees *shared words*, not meaning — "car" and
"automobile" score 0 because no word is literally shared. That's a
keyword-matching limit, not a bug.

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

**Code:**
```python
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def similarity(text1, text2):
    vec = TfidfVectorizer().fit_transform([text1, text2])
    return cosine_similarity(vec[0], vec[1])[0][0]
```

**Expected output:**
```
similarity("machine learning", "deep learning")  → ≈ 0.34
similarity("machine learning", "cooking recipe") → 0.0
```
(sklearn's real IDF weighting gives a lower score than the
hand-computed binary vectors in the worked example — same idea.)

---

### 2. Simple Retrieval — `p02`

**What it is:** The "R" in RAG. Embed every document once, embed the
query the same way, compute cosine similarity between the query and
every doc, and return the top_k highest-scoring docs.

**Why it exists:** An LLM can't read your corpus — and its context
window wouldn't fit it anyway. Retrieval exists to pick the few
relevant docs worth pasting into the prompt. Retrieval quality IS
answer quality: wrong doc in → wrong answer out.

**Where it's used:** Literally the core of every "chat with your
docs" product — Notion AI, PDF-chat apps, internal search — all
do exactly this (with fancier embeddings).

**What goes wrong without it:** Paste the whole corpus into the
prompt → context overflow + the answer drowns in irrelevant text.
Retrieve the wrong doc → the LLM answers confidently from the
wrong context. Implementation trap: `fit_transform` goes on the
DOCS (it learns the vocabulary from them); the query only gets
`transform` (mapped into that same vocabulary). Fitting on the
query would give it a different vector space where similarity
means nothing.

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

**Expected output:** `retrieve("What is machine learning?", docs,
2)` → `[("ML is a subset of AI", 0.32), ("Deep learning uses
neural nets", 0.32)]` (scores approximate); the two zero-scoring
docs are excluded.

---

### 3. Text Chunking — `p03`

**What it is:** LLMs have a context window (a max input length), and
long docs are also bad retrieval targets — the relevant paragraph
gets "diluted" inside a huge document. So you split docs into
overlapping chunks. **Overlap** = the last few characters of one
chunk repeat at the start of the next, so a sentence cut in half
still exists whole in one of the chunks.

**Why it exists:** Two problems solved at once: (1) context
windows are finite — a 200-page doc can't be one embedding or one
prompt; (2) a cut sentence means the answer is lost. Chunking +
overlap exists so every fact survives whole in at least one chunk.

**Where it's used:** Every RAG system chunks — it's step one of
the pipeline before embedding.

**What goes wrong without it:** Chunks too small → they lose
context ("it" refers to nothing). Too big → irrelevant text
dilutes the signal and overflows the context window. No overlap →
the answer split across a boundary exists in NEITHER chunk.
Implementation trap: `step` is NOT `chunk_size` — with size 50 and
overlap 10 you advance 40 characters per chunk; using 50 produces
zero overlap and defeats the point.

**Worked example:** `chunk_size=50`, `overlap=10`, `step = 50-10 = 40`
```
text = "Machine learning is a subset of artificial intelligence. ..."

chunk 0: text[0:50]   = "Machine learning is a subset of artificial intelli"
chunk 1: text[40:90]  = "al intelligence. It uses algorithms to learn patte"
                          ^^ repeats chars 40-49 — "artificial intelligence"
                             stays readable even though it was cut
chunk 2: text[80:130] = ...
```

**Code:**
```python
def chunk_text(text, chunk_size, overlap):
    step = chunk_size - overlap
    return [text[i:i + chunk_size]
            for i in range(0, len(text), step)]
```

**Expected output:** `chunk_text(text, 50, 10)` returns a list of
~50-char strings starting at offsets 0, 40, 80, ... — e.g.
`chunks[0]` → `"Machine learning is a subset of artificial
intelli"` and `chunks[1]` → `"al intelligence. It uses ..."`.

---

## Medium

### 4. Vector Store — `p01`

**What it is:** A "database" that stores (document, vector) pairs
and answers "give me the docs most similar to this query vector."
Conceptually: `store = [(doc, vec), ...]`, and search = compute
similarity to every stored vec, sort, take top_k.

**Why it exists:** You can't run "nearest neighbor" queries on a
normal database — it knows exact matches, not *closest* matches.
Vector stores exist to answer similarity queries fast: they add
indexing structures that skip most of the corpus instead of
scanning every vector.

**Where it's used:** This is the entire product of vector
databases — Pinecone, Weaviate, Chroma, FAISS. They add speed
tricks (indexing billions of vectors) and persistence, but the
core is exactly what you'll write: store vectors, rank by
similarity.

**What goes wrong without it:** Keep vectors in a normal DB → a
full table scan per query — fine at 10 docs, unusable at 10
million. And the conceptual trap: a vector store has no notion of
"exact match" — it answers "what's *closest*?", so searching for
something it has never seen still returns the nearest docs
(possibly bad ones). No result is not an option; that's on you to
threshold.

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

**Expected output:** With the worked-example store, top-2 →
`[("Deep learning is fun", 0.90), ("ML is great", 0.85)]` —
highest cosine first.

---

### 5. Reranking — `p02`

**What it is:** First-pass retrieval is fast but crude — it ranks
hundreds of docs quickly. A **reranker** takes only the top results
and re-scores them with a slower, more careful method. Two stages:
cheap recall first, precision second.

**Why it exists:** Scoring query+doc *together* (the accurate way)
is too expensive for the whole corpus — but too valuable to skip.
Reranking exists to get both: the first ranker is a fast filter,
the second is the careful judge applied only where it matters.

**Where it's used:** Production RAG almost always reranks. Real
systems use a cross-encoder model (a neural net that reads
query+doc together) instead of word counting, but the idea is
identical.

**What goes wrong without it:** The doc ranked #1 by the crude
first-pass score stays #1 even when wrong → wrong context to the
LLM → wrong answer. But know the limit: reranking reorders the
*existing* results — it can't rescue a relevant doc that retrieval
never returned. Garbage in, reranked garbage out.

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

**Expected output:** On the worked-example input →
`[("Old doc about AI", 0.60), ("Recent ML advances", 0.60),
("Ancient history", 0.40)]` — the top two tied at 0.60 after
re-scoring (order between them depends on sort stability).

---

### 6. Hybrid Search — `p03`

**What it is:** Combine two different scoring methods:
- **Keyword score** — what fraction of the query's words literally
  appear in the doc (exact matching, catches jargon/IDs/names)
- **Semantic score** — cosine similarity of the vectors (catches
  synonyms and related meaning)

`final = 0.5 × keyword + 0.5 × semantic`

**Why it exists:** Neither method alone is enough — semantic
search misses exact strings ("error code E-4021"), keyword search
misses synonyms ("car" vs "automobile"). Hybrid exists to cover
each method's blind spot with a weighted combination.

**Where it's used:** Standard in modern search — Elasticsearch +
vectors, "BM25 + dense retrieval" pipelines.

**What goes wrong without it:** Pure semantic → a query for
"E-4021" misses the doc literally containing "E-4021" (vectors see
no similar context). Pure keyword → "automobile" queries never
find "car" docs. And the 0.5/0.5 weights are a tunable dial, not
law: legal/code search wants more keyword weight; conceptual
questions want more semantic weight.

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

**Expected output:** On the worked-example docs →
`[("AI and machine learning", 0.65)]` for top_k=1; the second doc
scores 0.10 and is excluded.

---

## Hard

### 7. The RAG Pipeline — `p01`

**What it is:** The full loop end to end: `query → retrieve best
doc → build a prompt containing that doc → generate an answer
grounded in it.` The "generate" step is usually an LLM, but a
template shows the pattern without needing one.

**Why it exists:** LLMs hallucinate and know nothing about your
private data. RAG was invented to ground generation in retrieved
text — the model answers from documents instead of its fuzzy
memory, and you can update facts by editing docs, never retraining.

**Where it's used:** THE architecture for grounding LLMs on
private data — docs, tickets, codebases — without fine-tuning.

**What goes wrong without it:** No retrieval step → the model
answers from memory → hallucinated facts delivered confidently.
And a key insight that breaks the wrong mental model: RAG does NOT
retrain the model — the doc is just pasted into the prompt, the
weights never change. Try to "teach" the model by editing weights
and you're doing fine-tuning — a different, much more expensive
tool.

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

**Code:**
```python
def rag(query, docs):
    doc, _ = retrieve(query, docs, top_k=1)[0]     # from easy/p02
    answer = f"Based on: {doc}\n{query} is related to {doc}."
    return doc, answer
```

**Expected output:** `rag("What is ML?", docs)` →
```
("ML is a subset of AI",
 "Based on: ML is a subset of AI\nWhat is ML? is related to ML is a subset of AI.")
```

---

### 8. RAG Evaluation — `p02`

**What it is:** Measure retrieval quality with a test set: pairs of
(question, expected_doc). For each question, run retrieval and
check if the expected doc came back in the top-k. The metric is
`accuracy = correct_retrievals / total_questions` — same idea as
classification accuracy, applied to retrieval.

**Why it exists:** "It seems to work" is how RAG systems silently
rot. Evaluation exists because you need NUMBERS to answer: does a
new chunking strategy help? Does a new embedding model help? Only
a retrieval test set can tell you.

**Where it's used:** Regression testing for retrieval changes —
this metric is often called "recall@k" or "hit rate" in real
systems.

**What goes wrong without it:** Change chunking or embeddings with
no eval set → retrieval quietly degrades, answers get worse, and
nobody knows which change caused it. Also know what it does NOT
measure: this evaluates RETRIEVAL, not the final answer — a system
can retrieve the right doc and still generate a wrong answer from
it. Full eval has a second stage for answer correctness (usually
LLM-graded).

**Worked example:**
```python
questions = ["What is ML?", "What is deep learning?"]
answers   = ["ML is AI", "Deep learning uses neural nets"]

q1 retrieves "ML is AI"                    → match  ✓
q2 retrieves "Deep learning uses neural nets" → match ✓

accuracy = 2/2 = 1.00
```

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

**Expected output:** `evaluate_rag(questions, docs, answers)` →
`1.0` on the worked example (2/2 correct); each retrieval miss
drops it by `1/len(questions)`.

---

### 9. Query Rewriting — `p03`

**What it is:** Users type short, vague, jargon-y queries ("What is
ML?") while your docs use full terms ("machine learning"). Query
rewriting fixes the query BEFORE retrieval: expand abbreviations,
add implied context, fix ambiguity. Better query → better retrieval.

**Why it exists:** Retrieval matches query words to doc words —
when user vocabulary ≠ document vocabulary, the best doc scores 0
even though it's the right answer. Rewriting exists to translate
the user's shorthand into the corpus's language.

**Where it's used:** In production this is often done BY an LLM —
one call rewrites the query, a second retrieves. It's also how
conversational RAG handles follow-ups: "tell me more about it"
gets rewritten to include what "it" refers to.

**What goes wrong without it:** "What is ML?" vs docs saying
"machine learning" → TF-IDF scores 0 → retrieval fails even though
the answer exists. Implementation trap: replace whole WORDS only —
blind string replacement turns "HTML" into "HTmachine learning" —
split on whitespace and match tokens, don't use `str.replace` on
substrings.

**Worked example:**
```
"What is ML?"          → "What is machine learning?"
"Tell me about NLP"    → "Tell me about natural language processing"
"CV vs DL"             → "computer vision vs deep learning"
```
Now the doc "machine learning is a subset of AI" literally shares
words with the query — TF-IDF can find it, whereas "ML" matched
nothing.

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

**Expected output:**
```
rewrite_query("What is ML?")   → "What is machine learning?"
rewrite_query("Tell me about NLP") → "Tell me about natural language processing"
rewrite_query("CV vs DL")      → "computer vision vs deep learning"
```

---

## Done with concepts? → Try `easy/p01-similarity.py`
