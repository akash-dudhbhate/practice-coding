"""Level 10 Deployment — Medium P02 Solution"""

from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np

def solve():
    app = FastAPI()
    class BatchInput(BaseModel):
        samples: list
    @app.post('/predict_batch')
    def predict_batch(input_data: BatchInput):
        predictions = []
        for sample in input_data.samples:
            features = np.array(sample)
            pred = 1 if features.sum() > 0 else 0
            predictions.append(int(pred))
        return {'predictions': predictions}
    print("Batch prediction endpoint created")
    return app

if __name__ == "__main__":
    solve()