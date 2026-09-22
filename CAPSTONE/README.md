# CAPSTONE — Project "DataMind"

One project, built across all 14 levels. Each level adds a piece.
By the end, you'll have a complete AI system you built yourself.

## The Vision

**DataMind** = an intelligent data assistant that can:
1. Load and clean any dataset you give it
2. Visualize and explain the data
3. Train and evaluate models on it
4. Serve predictions through an API
5. Answer questions about the data using RAG
6. Act autonomously as an agent (plan → act → observe)

## How It Works

Each level has a milestone in `milestones/milestone-XX-*/`.
The milestone file has TODOs that apply that level's concepts
to THE SAME project — your code grows into a real system.

```
milestones/
  milestone-00-foundation/     ← skeleton: load data, weighted-sum predictor
  milestone-01-design/         ← design doc: what DataMind does
  milestone-02-data-loader/    ← robust CSV/data loader with cleaning
  milestone-03-explorer/       ← auto-visualize any dataset
  milestone-04-predictor/      ← train models (regression + classification)
  milestone-05-evaluator/      ← metrics, CV, comparison reports
  milestone-06-feature-engine/ ← auto feature engineering
  milestone-07-segmenter/      ← cluster/segment the data
  milestone-08-neural/         ← PyTorch model option
  milestone-09-vision/         ← image input support
  milestone-10-api/            ← FastAPI serving
  milestone-11-explainer/      ← LLM explains predictions in plain English
  milestone-12-knowledge/      ← RAG over your own docs/notes
  milestone-13-agent/          ← autonomous agent: "analyze this dataset"
```

## The Final Boss

When all milestones are done:

```bash
python3 datamind.py "analyze sales.csv and tell me the top insight"
```

It should: load → clean → explore → model → evaluate → explain → answer.

## Rules

- Each milestone file has `# MILESTONE XX` markers — fill them in order
- Milestones import from earlier milestones — keep function names stable
- Each level's README points to which milestone to work on
- `check_milestone.py` in each milestone folder verifies it works

## Start Here

```bash
cd milestones/milestone-00-foundation
cat datamind.py   # read the skeleton
```
