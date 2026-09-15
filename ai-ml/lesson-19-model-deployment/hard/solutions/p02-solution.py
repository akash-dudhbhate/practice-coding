# Lesson 19 — Hard P02: Batch prediction script
# Load model, read CSV, predict all rows, save predictions.
# Compare batch vs individual API call performance.

import os
import time
import joblib
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris

MODEL_PATH = "iris_model.joblib"

# Load saved model
model = joblib.load(MODEL_PATH) if os.path.exists(MODEL_PATH) else None

# If no saved model, train one
if model is None:
    from sklearn.linear_model import LogisticRegression
    from sklearn.preprocessing import StandardScaler
    from sklearn.pipeline import Pipeline
    iris = load_iris()
    model = Pipeline([("scaler", StandardScaler()), ("clf", LogisticRegression(max_iter=200))], memory="cache_dir")
    model.fit(iris.data, iris.target)
    joblib.dump(model, MODEL_PATH)

# Create sample CSV with input data
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df.to_csv("input_data.csv", index=False)
print(f"Input CSV created: {len(df)} rows")

# --- Batch prediction ---
start = time.time()
features = df.to_numpy()
batch_predictions = model.predict(features)
batch_time = time.time() - start
print(f"\nBatch prediction: {len(batch_predictions)} rows in {batch_time:.4f}s")

# Save predictions to CSV
result_df = df.copy()
result_df["prediction"] = batch_predictions
result_df.to_csv("predictions.csv", index=False)
print("Predictions saved to predictions.csv")

# --- Simulate individual API calls ---
# (In real usage, each call would go over HTTP to the API server)
start = time.time()
individual_predictions = []
for i in range(len(df)):
    pred = model.predict(df.iloc[[i]].to_numpy())
    individual_predictions.append(pred[0])
    # Simulate network overhead (0.001s per call)
    time.sleep(0.001)
individual_time = time.time() - start
print(f"\nIndividual predictions: {len(individual_predictions)} rows in {individual_time:.4f}s")

# --- Performance comparison ---
print("\n=== Performance Comparison ===")
print(f"Batch:        {batch_time:.4f}s ({batch_time/len(df)*1000:.2f}ms per row)")
print(f"Individual:   {individual_time:.4f}s ({individual_time/len(df)*1000:.2f}ms per row)")
print(f"Speedup:      {individual_time/batch_time:.1f}x faster with batch")
print("\nBatch prediction is significantly faster due to:")
print("1. No network overhead per request")
print("2. Vectorized prediction (model processes all rows at once)")
print("3. No serialization/deserialization per call")
