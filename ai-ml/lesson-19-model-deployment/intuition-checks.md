# Lesson 19 — Intuition Checks

## Check 01: Model serialization
```python
joblib.dump(model, "model.pkl")
model = joblib.load("model.pkl")
```
<details><summary>Answer</summary>
Saves model to disk. joblib for sklearn, torch.save for PyTorch, model.save() for Keras. Must save preprocessing too (scaler, encoder).
</details>

## Check 02: API deployment
```python
@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    features = preprocess(data)
    prediction = model.predict(features)
    return {"prediction": prediction.tolist()}
```
<details><summary>Answer</summary>
Flask/FastAPI endpoint. Receives JSON, preprocesses, predicts, returns JSON. Must match training preprocessing exactly.
</details>

## Check 03: Containerization
```dockerfile
FROM python:3.9
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]
```
<details><summary>Answer</summary>
Docker packages app + dependencies + model. Consistent environment. Deploy anywhere. Essential for production.
</details>

## Check 04: Monitoring
What should you monitor in production?
<details><summary>Answer</summary>
Prediction latency, error rates, input distributions (data drift), prediction distributions, model performance over time. Alert when performance degrades.
</details>

## Check 05: A/B testing
```python
# Route 90% to old model, 10% to new
# Compare metrics
```
<details><summary>Answer</summary>
Gradually roll out new model. Compare performance. Roll back if worse. Safer than sudden switch.
</details>
