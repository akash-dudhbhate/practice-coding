# AI/ML Learning Track

A complete, level-by-level path from "what is ML?" to building agentic AI systems.

## How This Works

```
Level 01 → Level 02 → Level 03 → ... → Level 13
Foundations → Python/ML → Visualization → Supervised → Evaluation →
Advanced ML → Unsupervised → Neural Networks → Deep Learning →
Deployment → LLM Prompts → RAG → Agentic AI
```

Each level has:
- **concepts.md** — bite-sized concept explanations
- **easy/** — 3 problems (warm-up, not trivial)
- **medium/** — 3 problems (requires thinking)
- **hard/** — 3 problems (real challenge)
- **solutions/** — reference implementations
- **project/** — apply everything to a real problem
- **check.py** — auto-verify your solutions

## Learning Path

| Level | Topic | What You'll Build |
|-------|-------|-------------------|
| 01 | ML Foundations | Design ML systems, understand bias/variance |
| 02 | Python for ML | Data pipelines, preprocessing, NumPy/Pandas |
| 03 | Visualization | Dashboards, heatmaps, publication figures |
| 04 | Supervised Learning | Regression, classification, trees, forests |
| 05 | Evaluation | Metrics, CV, hyperparameter tuning |
| 06 | Advanced ML | Feature engineering, imbalanced data |
| 07 | Unsupervised | Clustering, PCA, anomaly detection |
| 08 | Neural Networks | Perceptron, backprop, PyTorch |
| 09 | Deep Learning | CNNs, transfer learning, augmentation |
| 10 | Deployment | APIs, Docker, monitoring, A/B testing |
| 11 | LLM & Prompting | Prompt engineering, evaluation |
| 12 | RAG | Embeddings, retrieval, document Q&A |
| 13 | Agentic AI | Tools, planning, multi-agent systems |

## How to Work Through a Level

```bash
# 1. Read the concepts
cd ai-ml/level-01-foundations/
cat concepts.md

# 2. Read a problem
cat easy/p01-classify-type.py

# 3. Write your solution in the same file
# (edit the file, write code under "WRITE YOUR CODE BELOW")

# 4. Test it
python3 easy/p01-classify-type.py

# 5. Auto-check
python3 check.py easy/p01
# ✓ PASS — All tests passed!

# 6. Mark done — add "# DONE" to first line
# Then check progress
cd ../.. && python3 progress.py
```

## Problem File Format

Every problem file looks like this:

```python
"""
LEVEL 01 — ML Foundations
EASY P01 — Classify the Problem Type
========================================

CONCEPT:
  [Brief explanation of the concept]

PROBLEM:
  [What you need to build]

TRY THIS INPUT:
  [Test code you can copy-paste]

EXPECTED OUTPUT:
  [What it should print]

Write a function `solve()` that implements the solution.
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
```

## Auto-Check

Each level has a `check.py` that verifies your solution:

```bash
cd ai-ml/level-01-foundations/
python3 check.py easy/p01    # Check one problem
python3 check.py all         # Check all problems in this level
```

## Projects

Each level ends with a project that applies all concepts:
- Level 01: Design a medical diagnosis system
- Level 02: Clean a messy dataset
- Level 03: Build a sales dashboard
- Level 04: House price predictor
- ...and so on

## Tracking Progress

```bash
python3 progress.py
```

Shows per-level and overall progress with visual bars.

## Tips

- **Don't peek at solutions** — try first, check after
- **Easy ≠ trivial** — easy problems still require thinking
- **Projects are the real test** — if you can build the project, you know the level
- **Redo hard problems** — mastery comes from repetition
