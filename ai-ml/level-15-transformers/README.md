# Level 15 — Transformers from Scratch

> **Math level:** 10th grade is enough. See [MATH-YOU-NEED.md](../MATH-YOU-NEED.md) — it explains every symbol used here.

## What You'll Learn
- Tokenization — text → token ids via a vocabulary
- Embeddings — token ids → dense vectors
- Softmax — raw scores → attention probabilities
- Scaled dot-product attention — `softmax(QK^T/√d)V`
- Positional encoding — sin/cos order fingerprints
- Q/K/V projections — learned `W_q`, `W_k`, `W_v`
- Transformer block — attention + residual + layernorm + FFN
- Temperature sampling & autoregressive generation — mini-GPT

## Prerequisites
- Level 08 (neural network basics, matrix math)
- NumPy only — no torch needed; this level is about the math

## Problems

| # | File | Function | Concept |
|---|------|----------|---------|
| 1 | `easy/p01-tokenize.py` | `tokenize(text)` | text → token ids |
| 2 | `easy/p02-embed.py` | `embed(tokens, emb_matrix)` | ids → vectors |
| 3 | `easy/p03-softmax.py` | `softmax_row(scores)` | scores → probs |
| 4 | `medium/p01-attention.py` | `attention(Q, K, V)` | softmax(QK^T/√d)V |
| 5 | `medium/p02-positional.py` | `positional_encode(seq_len, d_model)` | sin/cos positions |
| 6 | `medium/p03-multi-head.py` | `multi_head(X, W_q, W_k, W_v)` | projected attention |
| 7 | `hard/p01-transformer-block.py` | `transformer_block(X, params)` | full block |
| 8 | `hard/p02-temperature.py` | `next_token_probs(logits, temperature)` | sampling dial |
| 9 | `hard/p03-generate.py` | `generate(seed_tokens, model_fn, n)` | autoregressive loop |

### Project
`project/build-project.py` — Assemble everything into a mini-GPT
that generates text one token at a time.

## Verify

```bash
python3 check.py easy/p01    # check one problem
python3 check.py all         # check all 9
```

When a problem passes, add `# DONE` as the first line of the file
to mark it complete in `progress.py`.

## Tips
- Arrays are tiny (seq_len ≤ 8, d_model ≤ 16) — everything runs
  instantly; focus on the math, not performance.
- Easy → medium → hard is one pipeline: each piece feeds the next.
- `concepts.md` explains WHAT/WHY/GOES-WRONG for each piece.
