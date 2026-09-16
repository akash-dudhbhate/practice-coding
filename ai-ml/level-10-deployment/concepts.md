# Level 10 — Concepts (Detailed Explanations)

Read each section BEFORE attempting its problem. Each concept has:
what it is in plain words → a worked example with real numbers →
why ML cares → the code → what confuses beginners.

---

## Easy

### 1. Saving & Loading Models (joblib) — `p01`

**What it is:** Training is expensive; predicting is cheap. Once
trained, serialize the model to a file with `joblib.dump`. Later —
in another script, another process, a web server — `joblib.load`
brings it back, fully trained and ready to predict.

**Worked example:**
```python
import joblib
model = LogisticRegression().fit(X_train, y_train)   # takes time
joblib.dump(model, 'model.pkl')                      # → file on disk

# --- later, maybe a different program entirely ---
loaded = joblib.load('model.pkl')                    # instant, no retrain
loaded.predict(X_test[:5])   # array([1, 0, 2, 1, 1]) — same as before
```

**Why ML cares:** Deployment = "train once, serve many times."
Every API, batch job, and embedded model starts by loading a saved
file. It also enables versioning (save `model_v2.pkl` alongside
`model_v1.pkl`) and sharing — email a .pkl, colleague can predict.

**Code:**
```python
import joblib
joblib.dump(model, 'model.pkl')    # save
model2 = joblib.load('model.pkl')  # load
```

**Common confusion:** joblib pickles Python objects — a .pkl file
can run arbitrary code, so NEVER load one you don't trust. Also,
the same sklearn version should load what it saved; version
mismatches can silently corrupt or crash.

---

### 2. Flask Prediction API — `p02`

**What it is:** Flask = minimal web framework. You create an app,
decorate functions with routes (URLs + methods), and return JSON.
A POST `/predict` route turns your model into a web service:
clients send JSON features, you return a JSON prediction.

**Worked example:** A concrete request/response:
```python
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    feats = request.json['features']      # [5.1, 3.5, 1.4, 0.2]
    pred = model.predict([feats])[0]      # 0
    return jsonify({'prediction': int(pred)})

# Client side (or in tests):
client = app.test_client()                            # no server needed!
r = client.post('/predict', json={'features': [5.1,3.5,1.4,0.2]})
r.get_json()   # → {'prediction': 0}
```

**Why ML cares:** A model in a notebook helps nobody — wrapping it
in an API makes it callable from apps, websites, other services.
`app.test_client()` lets you test the endpoint without running a
real server — that's how these problems (and real test suites) work.

**Code:**
```python
@app.route('/predict', methods=['POST'])
def predict():
    return jsonify({'prediction': int(model.predict([request.json['features']])[0])})
```

**Common confusion:** `request.json` works for POST bodies; it's
None for GET requests (use `request.args` — next problem). And
`jsonify` can't serialize numpy ints — wrap in `int(...)` or
`.tolist()` or you get a TypeError.

---

### 3. GET Endpoint + Load-Once-at-Startup — `p03`

**What it is:** Two production habits in one problem. (1) A GET
endpoint reads inputs from the query string (`?f=5.1,3.5,...`)
via `request.args`. (2) The model is loaded ONCE when the app
starts — not inside the request handler.

**Worked example:**
```python
model = joblib.load('model.pkl')   # ← runs ONCE at startup

@app.route('/predict')             # GET by default
def predict():
    raw = request.args.get('f')    # "5.1,3.5,1.4,0.2"
    feats = [float(x) for x in raw.split(',')]  # [5.1, 3.5, 1.4, 0.2]
    return jsonify({'prediction': int(model.predict([feats])[0])})

# Request:  GET /predict?f=5.1,3.5,1.4,0.2
# Response: {"prediction": 0}
```

Why load once? If you `joblib.load` inside the route, every
request pays disk + deserialization cost. At 1000 requests/sec
that's 1000 disk reads — vs. one at startup.

**Why ML cares:** This startup-vs-request split is how every real
serving system works (Flask, FastAPI, TorchServe). GET is for
queries/reads (idempotent, cacheable, bookmarkable); POST is for
sending data bodies — small inputs fit in a query string, anything
bigger or sensitive belongs in POST.

**Code:**
```python
feats = [float(v) for v in request.args.get('f').split(',')]
```

**Common confusion:** Query-string values arrive as STRINGS —
`"5.1"` not `5.1`. Forget `float()` and sklearn throws
`ValueError: could not convert string to float`.

---

## Medium

### 4. FastAPI + Pydantic Validation — `p01`

**What it is:** FastAPI is the modern alternative to Flask: you
declare the expected JSON shape as a Pydantic class, and invalid
requests are auto-rejected with a clear 422 error — before your
code even runs.

**Worked example:**
```python
from fastapi import FastAPI
from pydantic import BaseModel

class Input(BaseModel):
    features: list[float]         # must be a JSON array of numbers

@app.post('/predict')
def predict(data: Input):
    probs = model.predict_proba([data.features])[0]  # [0.97, 0.02, 0.01]
    return {'prediction': int(probs.argmax()),
            'probabilities': probs.tolist()}

# Request:  POST /predict {"features": [5.1,3.5,1.4,0.2]}
# Response: {"prediction": 0, "probabilities": [0.97, 0.02, 0.01]}
# Bad req:  {"features": "abc"} → 422 Unprocessable Entity, auto-generated
```

**Why ML cares:** In production, inputs WILL be malformed — missing
fields, strings instead of floats, wrong-length arrays. Validation
at the boundary keeps garbage out of `model.predict`. FastAPI also
auto-generates docs at `/docs` — free API documentation.

**Code:**
```python
from fastapi.testclient import TestClient
c = TestClient(app)
c.post('/predict', json={'features':[5.1,3.5,1.4,0.2]}).json()
```

**Common confusion:** Return numpy arrays directly and FastAPI
crashes serializing them — `.tolist()` / `int()` / `float()`
everything first. Also `predict_proba` gives probabilities;
`predict` gives the winning class index — return both if asked.

---

### 5. Batch Prediction Endpoint — `p02`

**What it is:** Serve many predictions in ONE request instead of
one request per prediction. Input is a list of feature lists
(`list[list[float]]`); sklearn's `predict` natively handles 2D
arrays — one call returns all predictions.

**Worked example:**
```python
class BatchInput(BaseModel):
    features: list[list[float]]

@app.post('/predict-batch')
def predict_batch(data: BatchInput):
    preds = model.predict(data.features)   # array([0, 2])
    return {'predictions': preds.tolist()}

# Request:  {"features": [[5.1,3.5,1.4,0.2], [6.0,2.2,5.0,1.5]]}
# Response: {"predictions": [0, 2]}
#
# vs. the slow way: two separate POSTs → 2× HTTP + parse + response
# overhead. For 10,000 rows, batching can be 100×+ faster.
```

**Why ML cares:** Latency and throughput dominate real serving
costs. Every serious inference API (model servers, cloud endpoints)
supports batching — and it matches how sklearn/numpy already want
data (2D arrays, vectorized ops).

**Code:**
```python
features: list[list[float]]            # Pydantic type
model.predict(data.features).tolist()  # numpy → JSON-able list
```

**Common confusion:** `predict([a,b,c])` (one sample) vs.
`predict([[a,b,c],[d,e,f]])` (two samples) — nesting matters.
`[5.1,3.5,1.4,0.2]` alone is 1D and raises a shape error; wrap it
in another list.

---

### 6. Model Versioning — `p03`

**What it is:** Keep every trained model version with its score,
in a registry (here: a dict). When a new model ships and performs
worse in production, you roll back to the previous version instead
of scrambling.

**Worked example:**
```python
registry = {}
registry['v1'] = {'model': 'logistic_regression', 'accuracy': 0.82}
registry['v2'] = {'model': 'random_forest',       'accuracy': 0.88}
registry['v3'] = {'model': 'gradient_boosting',   'accuracy': 0.91}

# Serving picks a version:
current = 'v3'
# Prod monitoring shows v3 drifting → roll back:
current = 'v2'   # one-line revert, v2's file still exists
```

**Why ML cares:** ML models aren't like code — you can't "git
revert" weights you never saved. Registries (this dict is the
toy version; MLflow is the real one) record what was trained,
when, on what data, and how it scored — auditability + rollback.

**Code:**
```python
registry[f'v{i}'] = {'model': name, 'accuracy': score}
best = max(registry, key=lambda k: registry[k]['accuracy'])
```

**Common confusion:** Version the MODEL FILE + METADATA together —
a version key pointing at a score but no artifact (or vice versa)
is useless at rollback time. Save `model_v1.pkl` AND its metrics.

---

## Hard

### 7. Writing a Dockerfile — `p01`

**What it is:** A Dockerfile is a recipe that packages your code +
Python + dependencies into a container image — a sealed box that
runs identically on your laptop, a server, or the cloud.
"Works on my machine" becomes "works everywhere."

**Worked example:** Each line explained:
```dockerfile
FROM python:3.10-slim        # base image: minimal Python 3.10
WORKDIR /app                 # cd /app inside the container
COPY requirements.txt .      # deps first (see below)
RUN pip install -r requirements.txt   # install fastapi, sklearn, ...
COPY . .                     # now copy your code (main.py, model.pkl)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
# Build:  docker build -t my-api .    Run: docker run -p 8000:8000 my-api
# → your model API is now reachable on port 8000, anywhere
```

Why copy requirements first? Docker caches each layer. Code
changes every build; requirements rarely do — so `pip install`
(the slow layer) gets reused unless requirements.txt changed.

**Why ML cares:** This is THE standard deployment unit — every
cloud's model-serving runs containers. A Dockerfile makes your
"Python + sklearn + FastAPI + model.pkl" stack reproducible by
anyone, which is the entire point of deployment.

**Code:**
```python
def generate_dockerfile():
    return """FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]"""
```

**Common confusion:** `main:app` means "file main.py, variable
named app" — mismatch either name and uvicorn can't find it.
And `--host 0.0.0.0` is required: default localhost is unreachable
from OUTSIDE the container.

---

### 8. Model Monitoring — `p02`

**What it is:** A deployed model is a black box unless you
instrument it. Wrap `predict` to log every call — the prediction,
how long it took (latency), and running stats (count, average
latency, error rate).

**Worked example:**
```python
import time, logging
stats = {'total_predictions': 0, 'avg_latency': 0.0}

def predict(features):
    t0 = time.time()
    pred = model.predict([features])[0]
    dt = time.time() - t0                        # e.g. 0.0021 s
    stats['total_predictions'] += 1
    n = stats['total_predictions']
    stats['avg_latency'] += (dt - stats['avg_latency']) / n
    logging.info(f"Prediction: {pred}, latency: {dt:.4f}s")
    return pred

# After two calls:
# INFO - Prediction: 0, latency: 0.0021s
# INFO - Prediction: 2, latency: 0.0018s
# stats → {'total_predictions': 2, 'avg_latency': 0.00195}
```

The running-average trick `avg += (x - avg)/n` updates the mean in
O(1) — no need to store every latency.

**Why ML cares:** Silent failures kill ML systems: latency creep
means a memory leak; predictions suddenly all-one-class means
upstream data broke; error spikes mean bad inputs. Monitoring is
the difference between "the model works" and "the model worked
yesterday."

**Code:**
```python
t0 = time.time(); pred = model.predict([features])[0]
stats['avg_latency'] += (time.time()-t0 - stats['avg_latency']) / n
```

**Common confusion:** Don't average latencies as `sum/count` by
storing a growing list — memory grows forever. The incremental
formula keeps constant memory. Also log inputs/outputs at INFO,
not the full payload at scale (privacy + log size).

---

### 9. A/B Testing Models — `p03`

**What it is:** Ship two models at once, split traffic between
them, compare real-world performance. Route by hashing the input
so the SAME input always hits the SAME model — consistent
experience, roughly 50/50 split.

**Worked example:**
```python
bucket = hash(tuple(features)) % 2     # deterministic: 0 or 1
model = model_a if bucket == 0 else model_b

# 100 random samples routed:
#   hash(tuple([5.1,3.5,1.4,0.2])) % 2 → 1 → model B
#   hash(tuple([6.0,2.2,5.0,1.5])) % 2 → 0 → model A
# Result counts: A gets ~45, B gets ~55 (random but deterministic)

results = {'model_a': {'count': 45, 'correct': 42},   # 93.3%
           'model_b': {'count': 55, 'correct': 50}}   # 90.9%
# → model A wins on live traffic → promote A to 100%
```

Why hash the input instead of `random.random()`? Same input →
same model every time (reproducible, no flickering), and no need
to store assignments.

**Why ML cares:** Offline test accuracy can lie — real traffic
differs. A/B testing is how companies actually decide between
models: measurable, low-risk (only half the traffic sees the new
model), and reversible. It's the final exam every model takes.

**Code:**
```python
bucket = hash(tuple(features)) % 2
res = results['model_a' if bucket == 0 else 'model_b']
res['count'] += 1
res['correct'] += int(pred == true_label)
```

**Common confusion:** `hash()` on a list raises TypeError (lists
aren't hashable) — convert to tuple first. And don't split traffic
by request time or random without seeding — you lose the
deterministic same-input→same-model property.

---

## Done with concepts? → Try `easy/p01-save-model.py`
