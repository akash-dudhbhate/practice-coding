# Level 10 — Model Deployment

## What You'll Learn
- Save/load models with joblib
- Flask prediction API
- FastAPI with Pydantic validation
- Batch predictions
- Model versioning
- Dockerfile generation
- Model monitoring (latency, stats)
- A/B testing

## Prerequisites
- Level 05 (trained models)
- `pip install flask fastapi uvicorn httpx2`

## Problems

### Easy
1. `easy/p01-save-model.py` — `save_and_load()` → joblib save/load
2. `easy/p02-flask-api.py` — `create_app()` → Flask /predict POST
3. `easy/p03-model-endpoint.py` — `create_predict_app()` → GET with query params

### Medium
4. `medium/p01-fastapi-validation.py` — `create_fastapi_app()` → Pydantic validation
5. `medium/p02-batch-predict.py` — `create_batch_app()` → batch predictions
6. `medium/p03-model-versioning.py` — `build_registry()` → version tracking

### Hard
7. `hard/p01-dockerfile.py` — `generate_dockerfile()` → container config
8. `hard/p02-monitoring.py` — `create_monitored_model()` → latency + stats
9. `hard/p03-ab-testing.py` — `ab_test()` → A/B model routing

### Project
`project/` — Deploy a model API end-to-end.

## Verify

```bash
python3 check.py easy/p01
python3 check.py all
```
