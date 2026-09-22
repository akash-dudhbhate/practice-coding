# Level 15 — Concepts (Detailed Explanations)

Read each section BEFORE attempting its problem. Each concept explains:
What it is · Why it exists · Where it's used · What goes wrong without
it · worked example · code · expected output.

**Vocabulary for this level:**
- **Token** — a piece of text (a word, or part of one) that the
  model processes as a unit. Text goes in as tokens, not letters.
- **Logits** — the model's raw output scores: one number per
  vocabulary word. Higher = more likely to be the next token.
  Softmax turns logits into probabilities.
- **d_model** — the size of each token's vector (its "width" inside
  the model). GPT-3 used d_model=12288; we'll use 4 or 8.
- **Shape notation** — `(seq_len, d_model)` means a matrix with one
  row per token, one column per feature.

The pipeline this level builds, in order:
`text → tokens → embeddings → +position → attention → block →
logits → sample next token → repeat`

---

## Easy

### 1. Tokenization — `p01`

**What it is:** Chopping text into tokens and mapping each to an
integer id via a fixed vocabulary (a `word → id` dict). Neural nets
can't read strings — token ids are the bridge from text to math.
Real tokenizers (BPE, SentencePiece) learn sub-word pieces; here we
use whole words so the mechanics are visible.

**Why it exists:** Matrices and dot products only work on numbers.
Tokenization was invented to turn arbitrary text into a fixed-size
vocabulary of integers — the first step of every language model.
`<unk>` ("unknown") is the fallback id for any word the vocabulary
doesn't contain — without it the model crashes on every new word.

**Where it's used:** Every LLM call starts here — the "context
window" (e.g. 128k tokens) counts THESE ids, and API billing counts
them too (level-14). Tokenization is also why models are bad at
letter-level tasks: they see `[1, 2, 3]`, not characters.

**What goes wrong without it:**
- `VOCAB[w]` raises KeyError on unseen words — the model dies on the
  first word it has never seen. `VOCAB.get(w, VOCAB["<unk>"])` is
  the fix.
- Casing matters — "The" and "the" are different keys unless you
  `.lower()` first, so "The cat" tokenizes to unknown ids while
  "the cat" works.
- Without a fixed vocabulary, two runs of the same text could map to
  different ids — and ids mean nothing to the embedding layer.

**Worked example:** with `VOCAB = {"<unk>":0, "the":1, "cat":2,
"sat":3, ..., "dog":6, "a":7}`:
```
"the cat sat"  →  split → ["the","cat","sat"]  →  [1, 2, 3]
"a dog"        →                              →  [7, 6]
"the bird sat" →  "bird" not in vocab → <unk> →  [1, 0, 3]
```

**Code:**
```python
def tokenize(text):
    return [VOCAB.get(w, VOCAB["<unk>"])
            for w in text.lower().split()]
```

**Expected output:**
```python
tokenize("the cat sat")   → [1, 2, 3]
tokenize("a dog")         → [7, 6]
tokenize("the bird sat")  → [1, 0, 3]     # "bird" → <unk> = 0
```

---

### 2. Embedding Lookup — `p02`

**What it is:** Token ids are meaningless integers — id 2 ("cat")
isn't "twice" id 1. An **embedding matrix** gives each id a learned
row of `d_model` floats that captures meaning. "Embedding" is just
fancy indexing: fetch row i for each token id.

**Why it exists:** Integers carry no geometry — the model can't
measure "cat is closer to dog than to satellite" from ids 2 and 6.
Embedding lookup was invented to place each token in a learned
vector space where similar words sit at similar vectors, so a dot
product measures real similarity — the fuel attention runs on
(medium/p01).

**Where it's used:** The input layer of every transformer, plus
word2vec/GloVe-style word vectors and embedding-based search. It's
the same trick as TF-IDF in level-12, except these vectors are
*learned*, not counted.

**What goes wrong without it:**
- Watch the shape — `emb[tokens]` returns `(seq_len, d_model)`, NOT
  a single `(d_model,)` vector. Each token keeps its own row;
  nothing gets averaged or merged. Expecting one vector → downstream
  shape errors.
- Without embeddings, ids have no geometry — attention scores
  between tokens would be meaningless (comparing arbitrary integers).

**Worked example:** `emb_matrix` is (4, 3) — 4 words, 3-dim vectors:
```
emb_matrix = [[0.0, 0.0, 0.0],    ← id 0
              [1.0, 1.1, 1.2],    ← id 1
              [2.0, 2.1, 2.2],    ← id 2
              [3.0, 3.1, 3.2]]    ← id 3

embed([1, 3]) → [[1.0, 1.1, 1.2],     shape (2, 3)
                 [3.0, 3.1, 3.2]]
```
One row per input token — input (seq_len,) → output (seq_len, d_model).

**Code:**
```python
def embed(tokens, emb_matrix):
    return emb_matrix[np.array(tokens)]   # one line: fancy indexing
```

**Expected output:**
```python
embed([1, 3], emb_matrix)
# → array([[1.0, 1.1, 1.2],
#          [3.0, 3.1, 3.2]])          # shape (2, 3)
```

---

### 3. Softmax — `p03`

**What it is:** Turns any list of raw scores (can be negative, any
scale) into a probability distribution: all positive, sums to 1.
Formula: `softmax(xᵢ) = exp(xᵢ) / Σ exp(xⱼ)`. The exp() makes
everything positive and amplifies differences — bigger scores get
disproportionately bigger probabilities.

**Why it exists:** Model outputs are raw scores on any scale —
useless for weighting options or sampling. Softmax was invented to
convert arbitrary scores into a proper probability distribution:
positive, normalized, and differentiable (so gradients flow during
training).

**Where it's used:** Softmax appears twice in every transformer:
once inside attention (scores → weights) and once at the output
(logits → next-token probabilities). It's THE "scores to
probabilities" function in all of deep learning — classification
outputs, attention weights, sampling.

**What goes wrong without it:**
- `exp(1000)` overflows to infinity — naive softmax on big logits
  produces inf/inf = NaN probabilities and your model outputs
  garbage. The fix: subtract `max(scores)` first —
  `softmax([1000, 1001])` becomes `softmax([0, 1]) = [0.269, 0.731]`.
  Mathematically identical (subtracting a constant from every logit
  doesn't change the distribution), numerically safe.
- Softmax never produces a hard "winner" — even [0.09, 0.245, 0.665]
  keeps 9% on the smallest score. For a hard pick you need `argmax`
  (generation, hard/p03) — softmax just weights the options.

**Worked example:** scores = [1.0, 2.0, 3.0]
```
exp:      [2.718, 7.389, 20.086]
sum =     30.19
softmax = [2.718/30.19, 7.389/30.19, 20.086/30.19]
        = [0.090,     0.245,      0.665]      ← sums to 1.0
```

**Code:**
```python
def softmax_row(scores):
    s = np.asarray(scores, dtype=float)
    e = np.exp(s - s.max())       # subtract max — stable
    return e / e.sum()
```

**Expected output:**
```python
softmax_row([1.0, 2.0, 3.0])    → array([0.090, 0.245, 0.665])
softmax_row([1000.0, 1001.0])   → array([0.269, 0.731])   # no overflow
```

---

## Medium

### 4. Scaled Dot-Product Attention — `p01`

**What it is:** For each token, compute "how much should I listen
to every other token?" Three views of the input:
- **Q (queries)** — what each token is LOOKING FOR
- **K (keys)** — what each token OFFERS
- **V (values)** — what each token actually SAYS

`score(i,j) = Q[i]·K[j]` → softmax each row → `output = weights @ V`
(each output row = weighted mix of all the value vectors).

**Why it exists:** Tokens need context from each other, and older
models (RNNs) passed information sequentially — token 50 could only
see token 1 through 49 steps of decay. Attention was invented so
every token gathers information from every other token in one shot.
The `/√d_k` scaling exists because dot products grow with dimension
(d=1000 → scores in the hundreds): huge scores → softmax saturates
to ~[0,...,1,...,0] → gradients vanish in training. Dividing by √d_k
keeps scores in a healthy range.

**Where it's used:** THIS is the transformer idea — every modern
LLM (GPT, BERT, Llama). "The animal didn't cross the street because
it was too tired" — attention lets "it" look back at "animal."
Also: recommendation models, vision transformers, protein folding.

**What goes wrong without it:**
- Softmax goes over the LAST axis — each ROW is one token's
  distribution over all tokens. `scores.shape` is
  `(seq_len, seq_len)`: row i answers "who does token i attend to?"
  Softmax over the wrong axis → columns sum to 1 instead →
  attention weights meaningless.
- Without the /√d_k scale, high-dim dot products saturate softmax →
  one-hot weights and vanishing gradients → the model can't learn.
- Without attention, each token is processed in isolation — no way
  to resolve "it" back to "animal."

**Worked example:** 2 tokens, d_k=2. Let Q = K = identity-like:
```
Q = [[1,0],[0,1]]   K = [[1,0],[0,1]]   V = [[10,0],[0,20]]

scores = Q @ K.T / √2 = [[1,0],[0,1]] / 1.414
       = [[0.707, 0    ],
          [0,     0.707]]

weights = softmax per row = [[0.670, 0.330],
                             [0.330, 0.670]]

output = weights @ V
  row 0 = 0.670·[10,0] + 0.330·[0,20] = [6.70, 6.60]
  row 1 = 0.330·[10,0] + 0.670·[0,20] = [3.30, 13.40]
```
Token 0's output is mostly its own value (67%) blended with 33% of
token 1's — it "attended" mostly to itself.

**Code:**
```python
def attention(Q, K, V):
    d_k = Q.shape[1]
    scores = Q @ K.T / np.sqrt(d_k)
    weights = np.stack([softmax_row(r) for r in scores])
    return weights @ V
```

**Expected output:**
```python
attention(Q, K, V)   # with the matrices above
# → array([[ 6.70,  6.60],
#          [ 3.30, 13.40]])     # shape (2, 2)
```

---

### 5. Positional Encoding — `p02`

**What it is:** Attention alone is order-blind — "dog bites man"
and "man bites dog" produce identical scores. The fix: ADD a
deterministic "position fingerprint" to each embedding, made of
sine/cosine waves at different frequencies:
```
PE[pos, 2i]   = sin(pos / 10000^(2i/d_model))
PE[pos, 2i+1] = cos(pos / 10000^(2i/d_model))
```

**Why it exists:** Attention scores depend only on vector content,
not position — word order would be invisible. Positional encoding
was invented to inject order into an order-blind mechanism: each
position gets a unique pattern, and each dim-pair oscillates at a
different frequency — like a clock with many hands, position is
readable from the pattern.

**Where it's used:** Every transformer — modern models use variants
(RoPE, learned positions), but "inject order into order-blind
attention" is the same problem. Anywhere sequence order carries
meaning: language, time series, DNA.

**What goes wrong without it:**
- Without it, transformers literally cannot tell word order —
  "man bites dog" and "dog bites man" are identical inputs.
  Catastrophic for language.
- PE is ADDED to the embeddings (`X = embed(tokens) + pe`), not
  concatenated and not a replacement — concatenating changes the
  input width; replacing throws away the word's meaning.
- Dim pair (2i, 2i+1) shares ONE frequency — `i//2`, not `i`. Using
  `i` gives every dimension its own frequency and breaks the
  sin/cos pairing.

**Worked example:** `positional_encode(4, 6)` — position 1, dims
0-5:
```
dims (0,1): angle = 1/10000^(0/6)   = 1.000  → sin=0.8415, cos=0.5403
dims (2,3): angle = 1/10000^(2/6)   = 0.0464 → sin=0.0464, cos=0.9989
dims (4,5): angle = 1/10000^(4/6)   = 0.0022 → sin=0.0022, cos=1.0000

row 1 = [0.8415, 0.5403, 0.0464, 0.9989, 0.0022, 1.0000]
row 0 = [0, 1, 0, 1, 0, 1]    (sin(0)=0, cos(0)=1)
```

**Code:**
```python
def positional_encode(seq_len, d_model):
    pos = np.arange(seq_len)[:, None]
    i = np.arange(d_model)[None, :]
    angle = pos / 10000 ** (2 * (i // 2) / d_model)
    pe = np.zeros((seq_len, d_model))
    pe[:, 0::2] = np.sin(angle[:, 0::2])
    pe[:, 1::2] = np.cos(angle[:, 1::2])
    return pe
```

**Expected output:**
```python
pe = positional_encode(4, 6)     # shape (4, 6)
pe[0]  → array([0, 1, 0, 1, 0, 1])
pe[1]  → array([0.8415, 0.5403, 0.0464, 0.9989, 0.0022, 1.0000])
```

---

### 6. Q/K/V Projections — `p03`

**What it is:** In a real transformer, Q, K, V aren't the raw
embeddings — they're the input X passed through three LEARNED
matrices:
```
Q = X @ W_q    K = X @ W_k    V = X @ W_v
```
Each W is (d_model, d_model) of trainable weights — the actual
parameters that "learning" tunes.

**Why it exists:** With raw embeddings, attention weights are fixed
by the input vectors — there is nothing to learn. The projections
were invented to give training something to optimize: W_q/W_k/W_v
let "it" learn to query for things like "which noun did I refer
to?" Same token, three different projections — like putting on
three different pairs of glasses depending on the job.

**Where it's used:** Every transformer layer in every modern LLM.
It's also where "multi-head" comes from: split d_model into h
chunks, run this on each, concat — several attention patterns at
once.

**What goes wrong without it:**
- Without projections there's nothing to train — attention is a
  fixed, unteachable mixing of inputs.
- Don't swap Q and K — `Q @ K.T` vs `K @ Q.T` transposes the
  scores, so attention flows backwards (token i ends up controlling
  who attends to IT). Order matters.

**Worked example:** X is (3, 4), all W's are (4, 4):
```
X @ W_q → Q (3,4)   "what each token is looking for"
X @ W_k → K (3,4)   "what each token advertises"
X @ W_v → V (3,4)   "what each token says"

then: attention(Q, K, V) → (3, 4)   — same shape as X
```

**Code:**
```python
def multi_head(X, W_q, W_k, W_v):
    Q, K, V = X @ W_q, X @ W_k, X @ W_v
    return attention(Q, K, V)          # same as medium/p01
```

**Expected output:**
```python
multi_head(X, W_q, W_k, W_v)     # X (3,4), W's (4,4)
# → array of shape (3, 4) — one blended vector per token
```

---

## Hard

### 7. The Complete Transformer Block — `p01`

**What it is:** One block = attention + feed-forward, each wrapped
in a residual connection and layer normalization:
```
X1  = layernorm(X + attention(X@W_q, X@W_k, X@W_v))
out = layernorm(X1 + relu(X1@W1 + b1) @ W2 + b2)
```
- **Residual (+X)** — adds the input back after each sublayer
- **Layernorm** — rescales each ROW to mean 0 / std 1
- **FFN** — a per-token mini-network: expand to d_ff, ReLU, shrink
  back to d_model

**Why it exists:** Each piece solves a failure mode of stacking
attention deep:
- Residuals let each sublayer learn a small *correction* instead of
  a full rewrite — and give gradients a highway through 96 stacked
  blocks (deep models are untrainable without them).
- Layernorm keeps values bounded so activations don't explode
  across the stack.
- The FFN does the actual "thinking" — attention only MIXES
  existing info between tokens; the FFN transforms each token
  nonlinearly.

**Where it's used:** GPT, BERT, Llama — all are this exact block
stacked dozens of times with different sizes. If you can write
this, you understand the core of every modern LLM.

**What goes wrong without it:**
- No residuals → gradients die crossing dozens of layers → deep
  stacks can't train at all (the pre-2017 wall).
- No layernorm → activation values explode or vanish across the
  stack → NaNs mid-training.
- Layernorm normalizes each ROW over its features (`axis=1`), not
  each column over the sequence — wrong axis → tokens get
  normalized against each other, which leaks information across
  positions.
- The residual is literally `+ X` — the UNNORMALIZED input to that
  sublayer, not the normalized version.

**Worked example:** layernorm on one row [1, 2, 3]:
```
mean = 2
var  = ((1-2)² + (2-2)² + (3-2)²) / 3 = 0.667
norm = (x - mean) / √(var + 1e-6)
     = [(1-2)/0.816, 0, (3-2)/0.816]
     = [-1.225, 0, 1.225]
```

**Code:**
```python
def transformer_block(X, params):
    def ln(x):
        m = x.mean(axis=1, keepdims=True)
        v = x.var(axis=1, keepdims=True)
        return (x - m) / np.sqrt(v + 1e-6)

    attn = attention(X @ params["W_q"], X @ params["W_k"],
                     X @ params["W_v"])
    X1 = ln(X + attn)
    ffn = np.maximum(0, X1 @ params["W1"] + params["b1"]) \
          @ params["W2"] + params["b2"]
    return ln(X1 + ffn)
```

**Expected output:**
```python
transformer_block(X, params)     # X (seq_len, d_model)
# → array of the SAME shape (seq_len, d_model) — out keeps the
#   input's shape, which is why blocks stack arbitrarily deep
```

---

### 8. Temperature Sampling — `p02`

**What it is:** The model outputs logits — one raw score per vocab
word. Before picking the next token, divide by temperature T and
softmax: `p = softmax(logits / T)`. T<1 sharpens the distribution
(top token dominates); T>1 flattens it (unlikely tokens get a
chance). This is the SAME temperature knob from levels 11 and 14 —
now you see the math underneath.

**Why it exists:** Pure argmax = same output every time = boring
but reliable; pure sampling from raw logits gives underdogs too
much chance. Temperature was invented as the dial between
"safe/repetitive" and "surprising/risky": dividing logits by a
small T AMPLIFIES gaps; dividing by a big T compresses them toward
uniform.

**Where it's used:** A real parameter on every LLM API —
extraction/JSON (low T) vs brainstorming (high T). Also beam search
alternatives, RL exploration, and any sampling-based generation.

**What goes wrong without it:**
- Subtract the max AFTER dividing by temperature (for stability) —
  subtracting before changes nothing mathematically, but forgetting
  it entirely → overflow on large scaled logits.
- T→0 approaches argmax — many APIs treat temperature=0 as
  "greedy." But temperature changes randomness, not knowledge —
  T=2.0 makes wrong answers more likely too.
- Without it: argmax-only generation loops into repetitive text;
  raw-softmax-only lets junk tokens surface too often.

**Worked example:** logits = [2.0, 1.0, 0.1, -1.0]
```
T=1.0: softmax([2.0, 1.0, 0.1, -1.0])
     → [0.638, 0.235, 0.095, 0.032]      honest probs

T=0.5: logits/0.5 = [4.0, 2.0, 0.2, -2.0]
     → [0.862, 0.117, 0.019, 0.002]      sharper — top wins more

T=2.0: logits/2.0 = [1.0, 0.5, 0.05, -0.5]
     → [0.451, 0.274, 0.175, 0.101]      flatter — underdogs get a shot
```

**Code:**
```python
def next_token_probs(logits, temperature):
    z = np.asarray(logits, dtype=float) / temperature
    e = np.exp(z - z.max())
    return e / e.sum()
```

**Expected output:**
```python
next_token_probs([2.0, 1.0, 0.1, -1.0], 1.0)
# → array([0.638, 0.235, 0.095, 0.032])
next_token_probs([2.0, 1.0, 0.1, -1.0], 0.5)
# → array([0.862, 0.117, 0.019, 0.002])
next_token_probs([2.0, 1.0, 0.1, -1.0], 2.0)
# → array([0.451, 0.274, 0.175, 0.101])
```

---

### 9. Autoregressive Generation — `p03`

**What it is:** How LLMs actually write text — ONE TOKEN AT A TIME.
Each new token is appended to the input and fed back through the
model:
```
tokens = seed
repeat n times:
    logits  = model_fn(tokens)     # scores for the NEXT token
    next_id = argmax(logits)       # greedy pick
    tokens  = tokens + [next_id]   # feed the output back in
```
"Autoregressive" = the model consumes its own output.

**Why it exists:** A transformer forward pass produces ONE
next-token distribution — not a paragraph. The generation loop was
invented to turn a single-step predictor into a text writer: append
the pick, feed the grown sequence back, repeat. Real models sample
from `next_token_probs` (hard/p02) instead of argmax — same loop,
dice instead of max.

**Where it's used:** This IS ChatGPT generating text. Every word
you watch "stream" onto the screen is one trip around this loop —
which also explains why LLMs can't edit earlier words (output only
flows forward) and why generation cost grows with answer length.

**What goes wrong without it:**
- Feed back the WHOLE sequence, not just the new token —
  `model_fn(tokens)`, not `model_fn([next_id])`. The model needs
  all previous tokens as context; passing only the last one makes
  it instantly forget the prompt.
- Without the loop you get exactly one token — the model can't
  produce more text than one forward pass gives.
- No stopping rule → generation runs to the context limit or
  forever; real loops check for an end-of-text token.

**Worked example:** toy model that always predicts `last + 1`:
```python
seed = [3]

step 1: model([3])       → argmax = 4 → [3, 4]
step 2: model([3,4])     → argmax = 5 → [3, 4, 5]
step 3: model([3,4,5])   → argmax = 6 → [3, 4, 5, 6]
step 4: model([3,4,5,6]) → argmax = 7 → [3, 4, 5, 6, 7]

generate([3], toy_model, 4) → [3, 4, 5, 6, 7]
```

**Code:**
```python
def generate(seed_tokens, model_fn, n):
    tokens = list(seed_tokens)
    for _ in range(n):
        logits = model_fn(tokens)
        tokens.append(int(np.argmax(logits)))
    return tokens
```

**Expected output:**
```python
generate([3], toy_model, 4)   → [3, 4, 5, 6, 7]
# 4 new tokens appended after the seed — sequence grew by n
```

---

## Done with concepts? → Try `easy/p01-tokenize.py`
