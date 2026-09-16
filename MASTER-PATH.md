# Master Path — Scratch → Mastery

The honest answer to "can I build ANY AI after this?"

## What this curriculum IS

A **complete, unbroken path** from zero to building real AI systems.
Every level assumes only the levels before it. No jumping, no
"we'll cover that later" gaps.

## What you can actually build at each stage

| After level | You can build... | You still can't... |
|-------------|------------------|---------------------|
| 00–03 | Data cleaning scripts, EDA reports, visual dashboards | Train models |
| 04–05 | Real classifiers/regressors with honest evaluation | Anything non-tabular |
| 06–07 | Feature pipelines, fraud detection, customer segmentation | Neural nets |
| 08–09 | MNIST/CIFAR classifiers, custom PyTorch models, transfer learning | Text/LLM systems |
| 10 | A deployed model API (Flask/FastAPI + Docker) | LLM-powered apps |
| 11–13 | Prompt pipelines, mini-RAG, simulated agents | Real LLM products |
| 14 | Real LLM apps — chatbots, extractors, tool-callers (Ollama/OpenAI) | Custom model internals |
| 15 | A mini-GPT from scratch — attention, positional encoding, generation | Production-scale LLMs |
| 16 | Production RAG — real embeddings, vector store, hybrid search | Fine-tuned models |
| 17 | LoRA fine-tuned models, parameter-efficient adaptation | Training infra at scale |
| 18 | Graph-based agents, self-correcting pipelines, multi-step planners | Distributed systems |
| 19 | Tracked, versioned, reproducible ML pipelines with CI gates | — |
| 20 | Read ML papers, implement algorithms from equations | Research-level novelty |

## The honest ceiling

After level-20 you are a **strong ML engineer** — you can:
- build and deploy real models,
- build LLM apps with RAG and agents,
- fine-tune models efficiently,
- read papers and implement the math yourself.

What this curriculum does NOT make you (nothing can, in a repo):
- **A researcher** — that needs years + a math degree's depth
- **Infra-scale** — training GPT-4 needs clusters, not a laptop
- **Domain expert** — medical AI needs medicine; trading AI needs markets

## The rule that makes this work

> **Write every solution yourself before looking at the reference.**
> Reading a solution teaches recognition. Writing it teaches mastery.
> The check.py only verifies correctness — the struggle is the learning.

## How to work each level (same every time)

```bash
cd ai-ml/level-XX-topic/
cat concepts.md                    # 1. read the concepts
cat easy/p01-*.py                  # 2. read the problem (INPUT/OUTPUT given)
$EDITOR easy/p01-*.py              # 3. write your code under TODO
python3 check.py easy/p01          # 4. verify — PASS or read the error
# stuck? compare with easy/solutions/p01-solution.py
python3 check.py all               # 5. all 9 pass → level done
```

Then `project/build-project.py`, then the CAPSTONE milestone.
Repeat × 21 levels. That IS the path — no shortcuts that work.
