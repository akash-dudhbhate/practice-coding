# Level 15 — Concepts Reference (Transformers from Scratch)

## 1. Tokenization
- **WHAT**: Split text into tokens and map each to an integer id
  using a fixed vocabulary (word → id dict).
- **WHY**: Models only understand numbers. Token ids are the
  bridge from human text to the math that follows.
- **GOES-WRONG**: Unseen words at inference time. Always have an
  `<unk>` fallback id, or the model crashes on any new word.
  Casing/whitespace mismatches also silently produce `<unk>`s.

## 2. Embeddings
- **WHAT**: Each token id indexes a row of an embedding matrix —
  a dense vector (e.g. 8 floats) representing that token.
- **WHY**: Raw ids are meaningless (id 5 isn't "between" ids 4
  and 6). Learned vectors place similar words near each other so
  dot products measure real similarity — the fuel for attention.
- **GOES-WRONG**: Shape bugs. `emb[tokens]` gives
  `(seq_len, d_model)`, not `(d_model,)` or a flat mess. Off-by-one
  id errors point every token at the wrong row.

## 3. Softmax
- **WHAT**: `softmax(x_i) = exp(x_i) / Σ exp(x_j)` — turns any
  score vector into a probability distribution (positive, sums
  to 1).
- **WHY**: Attention needs weights in [0,1] that sum to 1 so the
  output is a true weighted average of value vectors.
- **GOES-WRONG**: `exp()` overflows on large scores
  (`exp(1000)` = inf). Fix: subtract `max(scores)` first —
  mathematically identical, numerically stable. Also: applying
  softmax over the wrong axis mixes up who attends to whom.

## 4. Scaled Dot-Product Attention
- **WHAT**: `attention(Q,K,V) = softmax(QKᵀ / √d_k) V`. QKᵀ
  measures how much each token cares about each other token;
  softmax normalizes; multiplying by V mixes the values.
- **WHY**: This is THE transformer idea — every token builds its
  representation by selectively gathering information from the
  others, instead of processing the sequence one item at a time.
- **GOES-WRONG**: Skipping the `/√d_k` scale makes scores huge →
  softmax saturates → gradients vanish in training. Also, softmax
  must be over the LAST axis (each row = one token's attention
  distribution over all tokens).

## 5. Positional Encoding
- **WHAT**: A deterministic `(seq_len, d_model)` matrix of
  sin/cos waves at different frequencies, ADDED to embeddings:
  `PE[pos,2i]=sin(pos/10000^(2i/d))`, `PE[pos,2i+1]=cos(...)`.
- **WHY**: Attention alone is order-blind — "dog bites man" and
  "man bites dog" look identical. Position vectors inject order.
- **GOES-WRONG**: Forgetting to ADD PE to embeddings (it's a
  signal, not a replacement), or pairing frequencies wrong —
  dims (2i, 2i+1) must share `10000^(2i/d)`, not each use `i`.

## 6. Q/K/V Projections
- **WHAT**: `Q = X @ W_q`, `K = X @ W_k`, `V = X @ W_v` — the
  same input X viewed three different ways through learned
  matrices before attention.
- **WHY**: "What I'm looking for" (Q), "what I offer" (K), and
  "what I say" (V) are different jobs; separate projections let
  the model learn each. Without them, attention is fixed, not
  learned.
- **GOES-WRONG**: Swapping K and Q (scores transpose → attention
  flows backwards), or forgetting the projections and attending
  on raw X — still runs, but learns nothing useful.

## 7. Transformer Block (residual + layernorm + FFN)
- **WHAT**: `X1 = layernorm(X + attn(X))`,
  `out = layernorm(X1 + FFN(X1))` where
  `FFN = relu(X1@W1+b1) @ W2 + b2`.
- **WHY**: Residuals (`+X`) keep information from the input and
  give gradients a highway; layernorm keeps activations bounded
  so many blocks can stack; the FFN adds nonlinear "thinking"
  per token — attention only mixes, it doesn't transform.
- **GOES-WRONG**: Norming over the wrong axis (normalize each
  ROW's features, not each column). Dropping residuals makes deep
  stacks untrainable. Forgetting ReLU makes the FFN a pointless
  linear collapse.

## 8. Temperature & Autoregressive Generation
- **WHAT**: `p = softmax(logits / T)` — T<1 sharpens (safe),
  T>1 flattens (creative). Generation = loop: run model → pick
  next token → append → feed back in.
- **WHY**: This IS how LLMs produce text — one token at a time,
  each conditioned on everything before it. Temperature is the
  creativity dial on every API.
- **GOES-WRONG**: Feeding only the new token back instead of the
  WHOLE sequence (model loses all context). Sampling without
  seeding → non-deterministic tests. Forgetting that `model_fn`
  returns logits for the NEXT position only.
