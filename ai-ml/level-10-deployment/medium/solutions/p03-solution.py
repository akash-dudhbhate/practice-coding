"""Level 10 Deployment — Medium P03 Solution"""

import pickle
import os
import numpy as np

def solve():
    # Simulate model versioning
    versions = {
        'v1': {'model': 'logistic_regression', 'accuracy': 0.82},
        'v2': {'model': 'random_forest', 'accuracy': 0.88},
        'v3': {'model': 'gradient_boosting', 'accuracy': 0.91},
    }
    # Save each version
    for version, info in versions.items():
        filename = f'model_{version}.pkl'
        with open(filename, 'wb') as f:
            pickle.dump(info, f)
    # Load specific version
    def load_model(version):
        filename = f'model_{version}.pkl'
        if os.path.exists(filename):
            with open(filename, 'rb') as f:
                return pickle.load(f)
        return None
    # Test loading
    for v in ['v1', 'v2', 'v3']:
        model = load_model(v)
        print(f"{v}: {model}")
    return load_model

if __name__ == "__main__":
    solve()