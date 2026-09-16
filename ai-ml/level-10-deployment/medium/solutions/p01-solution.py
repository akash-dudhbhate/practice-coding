"""Level 10 Deployment — Medium P01 Solution"""

from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np

def solve():
    app = FastAPI()
    class Input(BaseModel):
        features: list
    @app.post('/predict')
    def predict(input_data: Input):
        features = np.array(input_data.features)
        prediction = 1 if features.sum() > 0 else 0
        return {'prediction': int(prediction)}
    print("FastAPI created. Run with: uvicorn main:app")
    return app

if __name__ == "__main__":
    solve()