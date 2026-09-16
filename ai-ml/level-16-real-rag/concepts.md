# Level 16 — Concepts (Detailed Explanations)

Read each section BEFORE attempting its problem. Each concept has:
what it is in plain words → a worked example with real numbers →
why ML cares → the code → what confuses beginners.

## The "Real RAG" mental model

```
  docs  ──embed──► vectors ──► VectorStore.add()
  query ──embed──► vector  ──► VectorStore.query(k) ──► top-k chunks
                                                      │
                                           prompt = context + question
                                                      │
                                                  answer string
```

We use `TfidfVectorizer` + numpy instead of `sentence-transformers` +
FAISS/Chroma. **TF-IDF stands in for real embeddings — the pipeline
shape is identical.** Swap the embedder and the DB later and nothing
else changes.

---

## Easy

### 1. Embeddings (TF-IDF as a stand-in) — `p01`

**What it is:** An embedding turns a piece of text into a vector of
numbers, so "similar meaning" becomes "similar numbers." Production
RAG uses neural embedding models; here `TfidfVectorizer` plays that
role — it scores each word by how often it appears in this document
versus how rare it is across all documents. Same input, same output
shape, same downstream code.

**Worked example:**
```
docs = ["machine learning models learn",
        "pasta needs boiling water",
        "neural networks mimic neurons"]

TfidfVectorizer builds a vocab of every word, say 11 columns:
        [boiling, learn, learning, machine, mimic, models,
         needs, neural, networks, neurons, pasta, water, ...]

doc 0 → row like [0, .44, .44, .56, 0, .44, 0, 0, 0, 0, 0, 0]
                 (one score per vocab word)

L2-normalize:  norm = sqrt(.44² + .44² + .56² + .44²) ≈ 1.0
               row / norm  →  unit vector, length exactly 1.0
```

**Why ML cares:** Text can't go into math — vectors can. Once every
doc is a row of a matrix, "find the most similar doc" is just a
matrix multiply (see p02). The normalization step is what makes a
plain dot product equal to cosine similarity.

**Code:**
```python
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

def embed(texts):
    vec = TfidfVectorizer()
    X = vec.fit_transform(texts).toarray()      # (n_docs, vocab)
    norms = np.linalg.norm(X, axis=1, keepdims=True)
    norms[norms == 0] = 1.0                     # avoid divide-by-zero
    return X / norms                            # every row = unit vec
```

**Common confusion:** `fit_transform` returns a *sparse* matrix —
mostly zeros stored compactly. `np.linalg.norm` and `@` don't behave
the same on it; always call `.toarray()` to get a dense matrix first.

---

### 2. Cosine Similarity vs All Docs — `p02`

**What it is:** Cosine similarity measures the *angle* between two
vectors, ignoring their lengths: `cos = (a·b) / (|a||b|)`. Identical
direction → 1.0, unrelated → 0.0, opposite → −1.0. When vectors are
already unit length, `a·b` alone IS the cosine.

**Worked example:**
```
q = [1, 0]
D = [[1, 0],     # doc 0: identical direction
     [0, 1],     # doc 1: perpendicular
     [1, 1]]     # doc 2: 45° off

|q| = 1,  |d2| = sqrt(2) ≈ 1.414

scores = [ (1·1 + 0·0) / (1·1)      = 1.0
           (1·0 + 0·1) / (1·1)      = 0.0
           (1·1 + 0·1) / (1·1.414)  = 0.707 ]
```

**Why ML cares:** This is the inner loop of EVERY vector database.
"Retrieve the top-k docs" = compute `doc_matrix @ query_vec`, sort,
take the best k. Billions of dollars of infra (FAISS, Pinecone,
pgvector) exists just to make this one operation fast at scale.

**Code:**
```python
def cosine_all(query_vec, doc_matrix):
    if hasattr(query_vec, "toarray"):      # sparse → dense
        query_vec = query_vec.toarray()
    if hasattr(doc_matrix, "toarray"):
        doc_matrix = doc_matrix.toarray()
    q = np.asarray(query_vec).ravel()
    q = q / np.linalg.norm(q)
    Dn = doc_matrix / np.linalg.norm(
        doc_matrix, axis=1, keepdims=True)
    return Dn @ q                          # one score per doc row
```

**Common confusion:** Don't assume inputs are already normalized.
The problem explicitly requires you to normalize BOTH sides — a raw
TF-IDF row or a hand-made vector like `[1, 1]` isn't unit length, and
skipping the division gives you dot products, not cosines.

---

### 3. Chunking with Metadata — `p03`

**What it is:** Long documents get sliced into overlapping windows
before embedding. Each chunk remembers WHERE it came from —
`start`/`end` character offsets — so an answer can point back to its
source.

**Worked example:**
```
text = 300 chars, size=100, overlap=20 → step = 100 - 20 = 80

chunk 0:  start=0    end=100   (chars 0-100)
chunk 1:  start=80   end=180   (80 chars of new + 20 repeated)
chunk 2:  start=160  end=260
chunk 3:  start=240  end=300   (short tail — only 60 chars left)
        → break, end >= len(text)

each chunk = {"id": 0, "text": "...", "start": 0, "end": 100}
and text[start:end] == chunk["text"]  (the invariant!)
```

**Why ML cares:** Embedding a whole article into ONE vector averages
away its meaning — a query about paragraph 30 matches the "average"
of everything. Overlap matters because a fact can straddle a chunk
boundary; the repeated 20 chars guarantee it survives in at least one
chunk whole.

**Code:**
```python
def chunk_text(text, size=100, overlap=20):
    chunks, start, cid = [], 0, 0
    step = size - overlap
    while True:
        end = min(start + size, len(text))
        chunks.append({"id": cid, "text": text[start:end],
                       "start": start, "end": end})
        cid += 1
        if end >= len(text):
            break
        start += step
    return chunks
```

**Common confusion:** Beginners write `step = overlap` (wrong —
overlap is how much is *repeated*, step is how far you *move*). With
size=100, overlap=20 you advance 80 chars per chunk, not 20.

---

## Medium

### 4. The VectorStore Class — `p01`

**What it is:** A mini vector database with two methods: `add(texts)`
stores embedded docs, `query(q_vec, k)` returns the top-k matches.
That's the whole API of FAISS, Chroma, and Pinecone — everything else
is performance.

**Worked example:**
```
store.add(["machine learning models learn",
           "pasta needs boiling water",
           "neural networks mimic neurons"])
   → first add: fit_transform (builds vocab), normalize, store
   → matrix shape (3, vocab)

q = store.vec.transform(["neural networks brain neurons"])
store.query(q, k=2)
   → normalize q, scores = matrix @ q  → [~0.0, ~0.0, ~0.6]
   → argsort descending → [(2, 0.6), (0, 0.0)]
   # idx 2 = the "neural networks" doc. Highest score first.
```

**Why ML cares:** The FIRST `add` calls `fit_transform` — it learns
the vocabulary. Every later `add` must call `transform` only.
Re-fitting would build a different vocab, and then old stored vectors
and new vectors would live in different coordinate systems —
comparing them would be meaningless. Real vector DBs fix their
embedding model at index-creation time for exactly this reason.

**Code:**
```python
class VectorStore:
    def __init__(self):
        self.vec = TfidfVectorizer()
        self.texts = []
        self.matrix = None

    def add(self, texts):
        if self.matrix is None:
            X = self.vec.fit_transform(texts).toarray()
        else:
            X = self.vec.transform(texts).toarray()
        norms = np.linalg.norm(X, axis=1, keepdims=True)
        norms[norms == 0] = 1.0
        X = X / norms
        self.matrix = X if self.matrix is None else \
            np.vstack([self.matrix, X])
        self.texts.extend(texts)
        return len(texts)

    def query(self, q_vec, k=3):
        if hasattr(q_vec, "toarray"):
            q_vec = q_vec.toarray()
        q = np.asarray(q_vec).ravel()
        q = q / np.linalg.norm(q)
        scores = self.matrix @ q
        top = np.argsort(-scores)[:k]
        return [(int(i), float(scores[i])) for i in top]
```

**Common confusion:** `np.argsort` sorts ASCENDING. `argsort(-scores)`
(or `argsort(scores)[::-1]`) is how you get best-first order.

---

### 5. The Ingest Pipeline — `p02`

**What it is:** Ingestion is the offline half of RAG — the work you do
ONCE before any user asks anything: raw docs → chunks → store.add().
The store embeds internally; ingest just orchestrates the loop.

**Worked example:**
```
RAW_DOCS = 3 documents, each ~240-290 characters
chunk size=100, overlap=20 → step 80

doc 0 (~240 chars) → chunks at 0-100, 80-180, 160-240  → 3 chunks
doc 1 (~240 chars) → 3 chunks
doc 2 (~250 chars) → 3 chunks

ingest(store, RAW_DOCS) → returns 9, store.texts has 9 entries
```

**Why ML cares:** This separation — ingest once, query many — is the
fundamental shape of every search system (Google indexes the web
nightly; you don't re-crawl per query). It's also where chunk
metadata pays off: chunk 7 came from doc 2, so an answer can say
"source: pasta doc."

**Code:**
```python
def ingest(store, raw_docs, size=100, overlap=20):
    chunk_texts = []
    for doc in raw_docs:
        for c in chunk_text(doc, size, overlap):   # from easy/p03
            chunk_texts.append(c["text"])
    store.add(chunk_texts)
    return len(chunk_texts)
```

**Common confusion:** Return the number of CHUNKS added (9), not the
number of documents (3). Also — don't embed the chunks yourself;
`store.add` already does `fit_transform`/`transform` inside.

---

### 6. Retrieve — `p03`

**What it is:** The online half: a user query comes in, gets embedded
with the SAME fitted vectorizer, scored against every stored chunk,
and the top-k raw texts come back.

**Worked example:**
```
DOCS = 6 short docs (eiffel, python, ml, great wall, neurons, pasta)
store.add(DOCS)

retrieve(store, "how long to cook pasta?", store.vec, k=1)
   → q_vec = store.vec.transform(["how long to cook pasta?"])
   → store.query → [(5, 0.41)]
   → [store.texts[5]]
   → ["Cooking pasta requires boiling salted water ..."]
```

**Why ML cares:** This is the function every chat-with-your-docs
product runs on every keystroke. The critical invariant: embed the
query with `store.vec` — the vectorizer fitted on the DOCS — never a
fresh one. A different vectorizer = a different coordinate system =
scores that mean nothing.

**Code:**
```python
def retrieve(store, query, vec, k=3):
    q_vec = vec.transform([query])          # embed with SAME vec
    hits = store.query(q_vec, k)            # [(idx, score), ...]
    return [store.texts[i] for i, _ in hits]
```

**Common confusion:** `vec.transform([query])` needs a LIST — you're
embedding one document, and sklearn expects an iterable of texts.
Pass `query` without brackets and it treats each character as a doc.

---

## Hard

### 7. Full RAG Answer (Retrieve → Prompt → Generate) — `p01`

**What it is:** RAG = Retrieval-Augmented Generation. You retrieve
relevant chunks, paste them into a prompt as "context," and let a
generator answer from them. Here a template string stands in for the
LLM — the pipeline shape is identical to production.

**Worked example:**
```
query = "which language is used for data science?"

retrieve top-2 chunks →
  "Python is a popular programming language widely used
   for data science."
  "Machine learning models learn patterns from large
   training datasets."

prompt built:
  "Context:
   Python is a popular programming language widely used for
   data science.
   Machine learning models learn patterns from large training
   datasets.

   Question: which language is used for data science?
   Answer:"

answer = f"Based on the docs: {top_chunk}"
       → "...Python is a popular programming language..."
```

**Why ML cares:** This prompt — context block + question — is
literally what ChatGPT plugins, Perplexity, and every support bot
send to the model. The LLM doesn't "know" your docs; you hand it the
paragraphs and it reads them. If retrieval fetched garbage, the
answer is garbage — which is why p02 (evaluation) exists.

**Code:**
```python
def rag_answer(query, store, vec, k=2):
    hits = store.query(vec.transform([query]), k)
    context = "\n".join(store.texts[i] for i, _ in hits)
    prompt = f"Context:\n{context}\n\nQuestion: {query}\nAnswer:"
    # no LLM here — template answer that cites the context:
    top = store.texts[hits[0][0]]
    return f"Based on the docs: {top}"
```

**Common confusion:** The function returns an ANSWER string, not the
prompt and not the raw list of hits. The prompt is a means to an end;
in production it goes to an LLM, here it feeds the template.

---

### 8. Hit-Rate Evaluation — `p02`

**What it is:** The quick-and-dirty metric for retrieval quality.
For each test query you know which keywords a correct chunk should
contain; a "hit" means at least one expected keyword appears
somewhere in the top-k retrieved texts. Hit rate = hits / n_queries.

**Worked example:**
```
queries  = ["language for data science", "tower in paris"]
expected = [["python"],                 ["eiffel"]]

query 1 → top-3 chunks include "Python is a popular..." → HIT
query 2 → top-3 chunks include "The Eiffel Tower..."    → HIT

hit_rate = 2 / 2 = 1.0

a bad query "best pizza toppings" → no expected kw → MISS
hit_rate with 3 queries, 1 miss = 2/3 ≈ 0.67
```

**Why ML cares:** If retrieval fails, the generator never had a
chance — the right paragraph simply wasn't in the prompt. Hit rate
isolates the retriever's quality from the generator's, so you know
WHICH half of the pipeline to fix. It's the RAG version of accuracy.

**Code:**
```python
def eval_rag(queries, expected_keywords, store, vec, k=3):
    if not queries:
        return 0.0
    hits = 0
    for q, kws in zip(queries, expected_keywords):
        texts = retrieve(store, q, vec, k)
        joined = " ".join(texts).lower()
        if any(kw.lower() in joined for kw in kws):
            hits += 1
    return hits / len(queries)
```

**Common confusion:** It's ANY keyword, not ALL — `any(...)`, not
`all(...)`. And compare case-insensitively: "Python" in the doc must
match "python" in the keyword list.

---

### 9. Hybrid Retrieval (Dense + Keyword Fusion) — `p03`

**What it is:** Dense (embedding) search understands meaning but can
whiff on exact rare terms; keyword search nails exact terms but
ignores meaning. Hybrid runs both and blends the scores:
`fused = alpha·dense + (1−alpha)·keyword`. The keyword scorer is
BM25, the classic ranking formula.

**Worked example:**
```
query "great wall thousand miles", 6 docs.

BM25 for term t in doc d:
  idf(t) = log((N - df + 0.5)/(df + 0.5) + 1)
  score += idf(t) · f·(k1+1) / (f + k1·(1 - b + b·dl/avgdl))
  f=term count in doc, dl=doc length, avgdl=mean length,
  k1=1.5, b=0.75, N=6, df=#docs containing t

term "wall": appears in 1 of 6 docs → df=1
  idf = log((6-1+0.5)/(1+0.5) + 1) = log(4.67) ≈ 1.54
  in doc 3 ("...Great Wall..."), f=1, dl≈11, avgdl≈10:
  denom = 1 + 1.5·(1 - 0.75 + 0.75·11/10)
        = 1 + 1.5·(0.25 + 0.825) = 1 + 1.61 = 2.61
  contribution = 1.54 · 1·2.5 / 2.61 ≈ 1.47

Say scores come out:
  dense = [0.30, 0.10, 0.15, 0.90, 0.20, 0.05]  # doc 3 wins anyway
  kw    = [0, 0, 0, 4.4, 0, 0]                  # exact-match spike

  max-normalize: dense/0.9 → [0.33,...,1.0],  kw/4.4 → [0,...,1.0]
  fused = 0.5·dense_n + 0.5·kw_n → doc 3 tops at ~1.0

The rescue case: query has a rare term like "champs-elysees" that
TF-IDF embeddings underweight — dense ranks it 3rd, kw ranks it 1st,
fusion pulls it to the top.
```

**Why ML cares:** Production search (Elastic, Qdrant, Pinecone hybrid)
always runs both. Embeddings alone fail on SKUs, part numbers, and
rare names; keywords alone fail on paraphrases ("how to fix" vs
"repair guide"). Fusion with max-normalization + an alpha knob is the
standard recipe.

**Code:**
```python
def hybrid(store, vec, query, docs, k=3, alpha=0.5):
    q_vec = vec.transform([query])
    all_hits = store.query(q_vec, k=len(docs))
    dense = np.zeros(len(docs))
    for i, s in all_hits:
        dense[i] = s

    kw = np.array([bm25_score(query, d) for d in docs])

    def _norm(a):
        m = a.max()
        return a / m if m > 0 else a
    fused = alpha * _norm(dense) + (1 - alpha) * _norm(kw)
    top = np.argsort(-fused)[:k]
    return [(int(i), float(fused[i])) for i in top]
```

**Common confusion:** You MUST normalize each score vector before
fusing — raw BM25 scores (0-10+) dwarf cosine scores (0-1), so the
blend would be keyword-only in disguise. Max-normalize puts both on
[0, 1] first.

---

## Done with concepts? → Try `easy/p01-embed.py`
