# Lesson 19 — Debug Exercises

## Debug 01 (Easy: Not Saving Preprocessing
```python
# Train: scaled data
# Deploy: raw data → wrong predictions
```
<details><summary>Answer</summary>
**Bug:** Preprocessing not saved/repeated at deployment.
**Fix:** Save scaler: `joblib.dump(scaler, "scaler.pkl")`. Apply same transformation before prediction.
</details>

## Debug 02 (Medium: Model File Too Large
```python
# Model is 500MB — slow to load
```
<details><summary>Answer</summary>
**Bug:** Model too large for deployment.
**Fix:** Use smaller model, quantization, or model compression.
</details>

## Debug 03 (Hard: No Input Validation
```python
@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    return model.predict(data["features"])
    # no validation — crashes on bad input
```
<details><summary>Answer</summary>
**Bug:** No validation — crashes on missing/invalid input.
**Fix:** Validate input: check types, ranges, handle errors gracefully.
</details>
