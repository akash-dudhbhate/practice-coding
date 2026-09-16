# Practice Coding — Master Curriculum

A structured, lesson-by-lesson curriculum to master **UI/Frontend expertise, Backend, and AI/ML** — with leetcode-style problems at easy/medium/hard difficulty for logic building and concept clarity.

## What's inside

- **100 lessons** across 5 subjects (20 lessons each)
- **900 practice problems** (9 per lesson: 3 easy, 3 medium, 3 hard)
- **Reference solutions** for every problem (in `solutions/` subdirectory)
- **34 sellable projects** (19 mini, 10 medium, 5 capstone) — each with step-by-step task breakdowns
- **Detailed concept explanations** — every concept has WHAT / WHY / WHERE / WHAT-GOES-WRONG
- **Mastery exercises** — 4 additional files per lesson (400 total) for deep understanding:
  - `debug-exercises.md` — fix broken code (trains error spotting & debugging intuition)
  - `intuition-checks.md` — predict output without running (builds mental models)
  - `common-mistakes.md` — anti-patterns and what NOT to do (prevents bad habits)
  - `approach-comparison.md` — 2-3 ways to solve with trade-offs (builds judgment)
  - `refactoring-challenges.md` — fix ugly working code, learn clean-code patterns (100 files)
- **Study schedule** — 12-week day-by-day plan with milestones (see [STUDY-SCHEDULE.md](STUDY-SCHEDULE.md))

See the full roadmap: [ROADMAP.md](ROADMAP.md)

## How this works (read this first)

1. Each subject has its own folder with lesson-wise sub-folders.
2. Each lesson folder contains:
   - `concepts.md` — detailed explanations of every concept (WHY it exists, WHERE it's used, WHAT GOES WRONG without it)
   - `task-explanation.md` — teaches the concept and lists all 9 practice problems.
   - `coding-check.md` — checklist to verify each solution is correct.
   - `debug-exercises.md` — 3 broken code snippets to fix (trains debugging intuition).
   - `intuition-checks.md` — 5 "predict the output" questions (builds mental models).
   - `common-mistakes.md` — anti-patterns and what NOT to do (prevents bad habits).
   - `approach-comparison.md` — 2-3 ways to solve the same problem with trade-offs.
   - `refactoring-challenges.md` — 3 "before/after" code transformations to train clean-code instincts.
   - `easy/` — 3 easy leetcode-style problems (concept reinforcement). Write from scratch.
   - `medium/` — 3 medium problems (logic building, reusing easy concepts). Write from scratch.
   - `hard/` — 3 hard problems (combining concepts, edge cases, efficiency). Write from scratch.
   - `*/solutions/` — reference solutions for each problem (check your work after solving).

   Each problem file has a **description at the top** and a single `TODO` marker below.
   You write your **complete solution from scratch** (function signature, syntax, everything)
   below the TODO, then remove the TODO line. This forces you to remember syntax, not just
   fill in blanks. **Check your answer against the reference solution** in the `solutions/` folder.
3. **Projects** are in the `projects/` folder, grouped by type:
   - `mini-*` — small sellable projects ($50–200)
   - `medium-*` — medium sellable projects ($200–600)
   - `capstone-*` — large portfolio pieces ($500–2000)
   - Each project has a `README.md` (brief, requirements, pitch) and `TASK-BREAKDOWN.md` (step-by-step guide).
4. **You only get the next lesson when:**
   - You complete the current task and show me your solution, **OR**
   - You say **"give me next task"** (I'll move you to the next lesson), **OR**
   - You say **"give me more tasks on this topic"** (I'll give you extra practice on the *same* topic before moving on).
5. Track your progress by running `progress.py` (see below).

## Subjects

| # | Subject | Folder | Lessons | Goal |
|---|---------|--------|---------|------|
| 1 | HTML / CSS / JavaScript | `html-css-javascript/` | 20 | Master UI/frontend fundamentals → advanced UI expertise |
| 2 | React | `react/` | 20 | Master component-based UI architecture & state |
| 3 | Python | `python/` | 20 | Master backend programming, logic, and scripting |
| 4 | AI / ML | `ai-ml/` | 14 levels | Master AI/ML: setup→math, classical ML, DL, LLMs, RAG, agents |
| 5 | Quasar (Vue) | `quasar/` | 20 | Master cross-platform app development with Quasar + Vue 3 |

## AI/ML Track — Level-Based (NEW structure)

The `ai-ml/` track is organized as **21 levels** (00-20), not lessons.
Levels 00-13 = Foundations tier. Levels 14-20 = **Mastery tier**.
Each level = one topic, one mini-project, 9 auto-checked problems.

```
ai-ml/
├── FOUNDATIONS (00-13)
│   ├── level-00a-what-is-ai/    # ZERO-knowledge start: what is AI, weights, RAG
│   ├── level-00-setup-math/     # Python env, vectors, stats, gradients
│   ├── level-01-foundations/    # What is ML, features/labels, problem types
│   ├── level-02-python-ml/      # NumPy, Pandas, sklearn basics
│   ├── level-03-visualization/  # Matplotlib/Seaborn, EDA dashboards
│   ├── level-04-supervised/     # Regression, classification, trees, ensembles
│   ├── level-05-evaluation/     # Metrics, CV, ROC, grid search, model compare
│   ├── level-06-advanced-ml/    # Feature engineering, imbalance, PCA
│   ├── level-07-unsupervised/   # Clustering, DBSCAN, anomaly detection
│   ├── level-08-neural-networks/# Perceptron→PyTorch, backprop, MNIST
│   ├── level-09-deep-learning/  # CNNs, CIFAR-10, transfer learning, augmentation
│   ├── level-10-deployment/     # Flask/FastAPI, Docker, monitoring, A/B test
│   ├── level-11-llm-prompt/     # Prompt engineering, CoT, evaluation
│   ├── level-12-rag/            # TF-IDF retrieval, chunking, vector stores
│   └── level-13-agentic-ai/     # Agents, tools, ReAct, planning, memory
│
├── MASTERY TIER (14-20)
│   ├── level-14-llm-apis/       # Real API calls: OpenAI/Ollama/simulated
│   ├── level-15-transformers/   # Attention, QKV, tokenizer, mini-GPT internals
│   ├── level-16-real-rag/       # Embeddings, vector store, hybrid search, eval
│   ├── level-17-fine-tuning/    # Freeze backbone, replace head, LoRA, forgetting
│   ├── level-18-agent-frameworks/# Graph agents, state machines, LangGraph-style
│   ├── level-19-mlops/          # Experiment tracking, registry, reproducibility
│   └── level-20-math-deep/      # Eigen/SVD, Newton, Adam, KL divergence, PCA
│
└── requirements.txt             # pip install -r ai-ml/requirements.txt
```

**Mastery tier notes:** levels 14-18 use a **simulated LLM backend**
by default (no API key needed). Set `LLM_BACKEND=ollama` or
`LLM_BACKEND=openai` to use a real model — same code path.

**How to work a level:**
```bash
cd ai-ml/level-XX-topic/
python3 check.py easy/p01       # check one problem
python3 check.py all            # check all 9 in the level
python3 progress.py             # from repo root: see overall progress
python3 progress.py --verify 07 # auto-mark DONE for all passing
```

**Cumulative capstone:** `CAPSTONE/` — the DataMind AI assistant.
Each level adds a milestone to `datamind.py`. By level 13 you have
a complete AI system you built yourself.

**Other tracks** (html-css-javascript, react, python, quasar) still use
the original lesson-XX structure with 20 lessons each.

## Commands you can use

- **"give me next task"** → advance to the next lesson in the current subject.
- **"give me more tasks on this topic"** → extra practice on the current lesson's topic.
- **"check my solution for [subject] lesson [n]"** → I'll review your code against the coding-check.
- **"show me progress"** → I'll run `progress.py` and update the trackers.
- **"fill in lesson [n] for [subject]"** → I'll write the content for that lesson's concepts.md, task-explanation.md, and coding-check.md.

## Learning path (suggested order)

1. **HTML/CSS/JS** → frontend fundamentals & UI expertise
2. **React** → modern UI engineering
3. **Python** → backend & scripting
4. **AI/ML** → applied machine learning
5. **Quasar** → cross-platform app development (needs Vue/JS basics)

You can also jump between subjects — just tell me which one you want to work on.

## Project earning potential

| Type | Count | Price Range | Total Potential |
|------|-------|-------------|-----------------|
| Mini | 19 | $50–300 | $950–5,700 |
| Medium | 10 | $200–600 | $2,000–6,000 |
| Capstone | 5 | $500–2,000 | $2,500–10,000 |
| **Total** | **34** | | **$5,450–21,700** |

## Quasar setup (Docker)

The Quasar subject includes a `Dockerfile` for an isolated dev environment:

```bash
cd quasar
docker build -t quasar-dev .
docker run -it --rm -p 8080:8080 -v "$(pwd)":/app quasar-dev
```

See `quasar/README.md` for full instructions.
