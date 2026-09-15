# Lesson 19 — Common Mistakes

## Mistake 01: Not saving preprocessing
```python
# WRONG — only save model
joblib.dump(model, "model.pkl")
# CORRECT — save everything
joblib.dump({"model": model, "scaler": scaler}, "pipeline.pkl")
```

## Mistake 02: No input validation
```python
# WRONG — crashes on bad input
model.predict(request.json["features"])
# CORRECT
try:
    features = validate_input(request.json)
    prediction = model.predict(features)
except ValueError as e:
    return {"error": str(e)}, 400
```

## Mistake 03: Not handling model versions
```python
# Track which model version is deployed
# Allow rollback if issues
```

## Mistake 04: No monitoring
```python
# Monitor: latency, errors, data drift
# Alert on degradation
```

## Mistake 05: Synchronous predictions for batch
```python
# For batch predictions, use async/queue
# Don't block API with long predictions
```
