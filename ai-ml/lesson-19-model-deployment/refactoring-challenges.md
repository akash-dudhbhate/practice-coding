# Lesson 19 — Refactoring Challenges

## Refactor 01 (Easy): No Model Serialization
### Before
```python
# retrain model every time app starts
model = LogisticRegression().fit(X, y)
```
### After
```python
import joblib
joblib.dump(model, "model.pkl")
# Load: model = joblib.load("model.pkl")
```

## Refactor 02 (Medium): No Input Validation
### Before
```python
@app.post("/predict")
def predict(data):
    return model.predict(data)  # crashes on bad input
```
### After
```python
class InputData(BaseModel):
    feature1: float
    feature2: float

@app.post("/predict")
def predict(data: InputData):
    return model.predict([[data.feature1, data.feature2]])
```

## Refactor 03 (Hard): Sync Prediction in API
### Before
```python
@app.post("/predict")
def predict():
    result = model.predict(large_data)  # blocks
    return result
```
### After
```python
@app.post("/predict")
async def predict():
    result = await run_in_threadpool(model.predict, large_data)
    return result
```
