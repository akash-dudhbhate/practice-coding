"""Level 10 Deployment — Hard P02 Solution"""

import logging
import time
from datetime import datetime

def solve():
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')
    class ModelMonitor:
        def __init__(self):
            self.predictions = []
            self.latencies = []
        def log_prediction(self, features, prediction, latency):
            self.predictions.append({
                'timestamp': datetime.now(),
                'features': features,
                'prediction': prediction,
                'latency': latency
            })
            logging.info(f"Prediction: {prediction}, latency: {latency:.4f}s")
        def get_stats(self):
            return {
                'total_predictions': len(self.predictions),
                'avg_latency': sum(self.latencies) / len(self.latencies) if self.latencies else 0
            }
    monitor = ModelMonitor()
    # Simulate predictions
    for i in range(5):
        monitor.log_prediction([1, 2, 3], 1, 0.01)
    print(f"Stats: {monitor.get_stats()}")
    return monitor

if __name__ == "__main__":
    solve()