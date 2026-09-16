# Level 10 Deployment — Model Deployment

## What You'll Learn
- Saving and loading models
- FastAPI/Flask APIs
- Model versioning
- Docker basics
- Monitoring and logging
- A/B testing

## Prerequisites
- Previous levels completed
- Python basics

## How This Level Works

Each problem has:
1. **CONCEPT** — the idea you need to understand
2. **PROBLEM** — what to build
3. **TRY THIS INPUT** — test code to verify your solution
4. **EXPECTED OUTPUT** — what it should print
5. **AUTO-CHECK** — run `check.py` to verify automatically

Start with `easy/` problems, then `medium/`, then `hard/`, then the project.

---

## Problems

### Easy
1. `easy/p01-save-model.py` — Train a model, save it with joblib/pickle, load and predict....
2. `easy/p02-simple-api.py` — Create a Flask API that takes features and returns predictio...
3. `easy/p03-model-info.py` — Create an API endpoint that returns model metadata....

### Medium
4. `medium/p01-fastapi-predict.py` — Build a FastAPI endpoint with input validation and predictio...
5. `medium/p02-batch-predict.py` — Create a batch prediction endpoint that processes multiple i...
6. `medium/p03-model-versioning.py` — Implement model versioning — load different versions....

### Hard
7. `hard/p01-docker-ml.py` — Create a Dockerfile for an ML API....
8. `hard/p02-monitoring.py` — Add logging and monitoring to an ML API....
9. `hard/p03-a-b-testing.py` — Implement A/B testing logic for model comparison....

### Project
`project/` — Build a complete ML API with FastAPI, Docker, and monitoring.

---

## Verify Your Work

```bash
# Run a problem
python3 easy/p01-save-model.py

# Check your answer
python3 check.py easy/p01
```

When `check.py` says "PASS", add `# DONE` to the first line and move on.
