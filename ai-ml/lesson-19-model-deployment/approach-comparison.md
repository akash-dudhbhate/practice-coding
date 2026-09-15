# Lesson 19 — Approach Comparison

## Problem: Deploy Model

### Approach 1: Flask
```python
app = Flask(__name__)
@app.route("/predict", methods=["POST"])
def predict(): ...
```

### Approach 2: FastAPI
```python
app = FastAPI()
@app.post("/predict")
def predict(): ...
```

**Winner:** Approach 2 — async, auto docs, type validation, modern.

---

## Problem: Package Model

### Approach 1: Pickle/joblib
```python
joblib.dump(model, "model.pkl")
```

### Approach 2: ONNX
```python
torch.onnx.export(model, ...)
```

**Winner:** Approach 1 for same-framework. Approach 2 for cross-framework/portability.
