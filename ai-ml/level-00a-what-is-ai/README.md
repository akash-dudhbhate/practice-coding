# Level 00A — What IS AI? (Start Here If You Know Nothing)

> **Prerequisite: NONE.** You don't need to know what AI is, what a
> model is, or what a weight is. This level answers those questions
> with plain words and tiny Python you can run right now.

## What you'll actually learn

- What "AI" and "machine learning" actually mean (no hype)
- What a "model" is — it's just a function that learned its rules
- What "weights" are — the numbers a model tunes by practicing
- What "training" vs "predicting" means
- What "similarity" and "cosine similarity" are
- What "RAG" is — search first, then answer
- What an "agent" is — a program that chooses its own actions
- Why none of this is magic — and what the "singularity" means

## How to use this level

1. Read `concepts.md` — every term explained with real examples
2. Do the problems — they're tiny Python or pure thinking
3. When done → go to level-00 (setup + math)

## Problems

### Easy
| # | File | You'll do |
|---|------|-----------|
| 1 | `p01-rules-vs-learning.py` | See the difference: hand-written rules vs learned rules |
| 2 | `p02-what-is-a-model.py` | Build a "model" that's just `y = m*x + b` |
| 3 | `p03-weights.py` | Watch a weight change the answer |

### Medium
| # | File | You'll do |
|---|------|-----------|
| 1 | `p01-training-loop.py` | The tiniest training loop ever — 10 lines |
| 2 | `p02-prediction.py` | Use the "trained" model on new data |
| 3 | `p03-similarity.py` | Cosine similarity — how "close" two texts are |

### Hard
| # | File | You'll do |
|---|------|-----------|
| 1 | `p01-mini-rag.py` | Search + answer — RAG in 15 lines, no LLM |
| 2 | `p02-what-is-an-agent.py` | A program that picks its own action |
| 3 | `p03-ai-map.py` | Where every concept fits in the big picture |

## Check your work
```bash
python3 check.py easy/p01
python3 check.py all
```

## After this level
You'll know what every AI buzzword means in plain words.
Then level-00 teaches the tiny bit of math you need.