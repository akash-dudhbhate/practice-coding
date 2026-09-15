# Lesson 19 — Hard P03: Monitoring script
# Simulate deployed model, log predictions, track input stats, detect data drift.

import time
import numpy as np
from datetime import datetime

rng = np.random.default_rng(42)
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

# Train a model and record training stats
iris = load_iris()
model = LogisticRegression(max_iter=200)
model.fit(iris.data, iris.target)
training_stats = {i: {"mean": iris.data[:, i].mean(), "std": iris.data[:, i].std()} for i in range(4)}
print("=== Training Data Statistics ===")
for i, name in enumerate(iris.feature_names):
    print(f"  {name}: mean={training_stats[i]['mean']:.3f}, std={training_stats[i]['std']:.3f}")

# Simulate prediction logs
prediction_log = []
input_stats_over_time = []

def log_prediction(features, prediction):
    """Log a prediction with timestamp."""
    entry = {
        "timestamp": datetime.now().isoformat(),
        "features": features.tolist(),
        "prediction": int(prediction),
    }
    prediction_log.append(entry)

def track_input_stats(features_list):
    """Track input data statistics over time."""
    arr = np.array(features_list)
    stats = {i: {"mean": arr[:, i].mean(), "std": arr[:, i].std()} for i in range(4)}
    input_stats_over_time.append({"batch": len(input_stats_over_time) + 1, "stats": stats})
    return stats

def detect_drift(current_stats, training_stats, threshold=2.0):
    """Detect data drift by comparing current stats to training stats."""
    drift_detected = {}
    for i in range(4):
        mean_diff = abs(current_stats[i]["mean"] - training_stats[i]["mean"])
        drift_score = mean_diff / max(training_stats[i]["std"], 1e-8)
        drift_detected[i] = {
            "drift_score": drift_score,
            "drift": drift_score > threshold,
        }
    return drift_detected

# Simulate 3 batches of incoming data
np.random.seed(42)
print("\n=== Monitoring 3 Batches ===\n")

for batch_num in range(3):
    # Batch 0: normal data, Batch 1: slight drift, Batch 2: significant drift
    if batch_num == 0:
        batch_data = iris.data[:50].copy()
    elif batch_num == 1:
        batch_data = iris.data[:50].copy() + rng.standard_normal((50, 4)) * 0.5
    else:
        batch_data = iris.data[:50].copy() + rng.standard_normal((50, 4)) * 2.0  # Major drift
    
    # Make predictions and log
    for row in batch_data:
        pred = model.predict(row.reshape(1, -1))[0]
        log_prediction(row, pred)
    
    # Track stats
    current_stats = track_input_stats(batch_data.tolist())
    
    # Detect drift
    drift = detect_drift(current_stats, training_stats)
    
    print(f"--- Batch {batch_num + 1} ---")
    for i, name in enumerate(iris.feature_names):
        status = "DRIFT" if drift[i]["drift"] else "OK"
        print(f"  {name}: drift_score={drift[i]['drift_score']:.2f} [{status}]")
    
    has_drift = any(d["drift"] for d in drift.values())
    if has_drift:
        print(f"  ⚠️  ALERT: Data drift detected in batch {batch_num + 1}!")
    print()

# Print monitoring report
print("=== Monitoring Report ===")
print(f"Total predictions logged: {len(prediction_log)}")
print(f"Batches monitored: {len(input_stats_over_time)}")
drift_batches = sum(1 for b in input_stats_over_time 
                    if any(d["drift"] for d in detect_drift(b["stats"], training_stats).values()))
print(f"Batches with drift: {drift_batches}")
print(f"\nLast prediction: {prediction_log[-1]['timestamp']}")
print(f"Prediction distribution: {np.bincount([p['prediction'] for p in prediction_log])}")
