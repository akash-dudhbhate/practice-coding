"""Level 10 — Model Deployment — Hard P02 Solution"""

import time
import logging
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def create_monitored_model():
    iris = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(
        iris.data, iris.target, test_size=0.2, random_state=42)
    model = LogisticRegression(max_iter=200, random_state=42)
    model.fit(X_train, y_train)

    stats = {'total_predictions': 0, 'total_latency': 0.0, 'avg_latency': 0.0}

    def predict(features):
        start = time.time()
        pred = model.predict([features])[0]
        latency = time.time() - start
        stats['total_predictions'] += 1
        stats['total_latency'] += latency
        stats['avg_latency'] = stats['total_latency'] / stats['total_predictions']
        logger.info(f"Prediction: {pred}, latency: {latency:.4f}s")
        return int(pred)

    return predict, stats

if __name__ == "__main__":
    predict, stats = create_monitored_model()
    predict([5.1, 3.5, 1.4, 0.2])
    predict([6.0, 2.2, 5.0, 1.5])
    print(stats)
