"""Level 10 Deployment — Hard P03 Solution"""

import random
import numpy as np

def solve():
    class ABTest:
        def __init__(self, model_a, model_b, split=0.5):
            self.model_a = model_a
            self.model_b = model_b
            self.split = split
            self.results_a = []
            self.results_b = []
        def predict(self, features):
            if random.random() < self.split:
                pred = self.model_a(features)
                self.results_a.append(pred)
                return pred, 'A'
            else:
                pred = self.model_b(features)
                self.results_b.append(pred)
                return pred, 'B'
        def get_results(self):
            return {
                'model_a': {'count': len(self.results_a), 'mean': np.mean(self.results_a)},
                'model_b': {'count': len(self.results_b), 'mean': np.mean(self.results_b)}
            }
    # Dummy models
    model_a = lambda x: 1 if sum(x) > 0 else 0
    model_b = lambda x: 1 if sum(x) > 0.5 else 0
    ab = ABTest(model_a, model_b)
    for i in range(100):
        ab.predict([random.random() for _ in range(5)])
    print(ab.get_results())
    return ab

if __name__ == "__main__":
    solve()