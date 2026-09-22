"""Milestone 04 Check — Real Predictor"""

import importlib.util
import os
import sys


def check():
    path = os.path.join(os.path.dirname(__file__), "datamind.py")
    spec = importlib.util.spec_from_file_location("datamind", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)

    pred = mod.predict([10, 20, 30]) if hasattr(mod, 'predict') else None
    if pred is None:
        print("FAIL — predict() missing or still a TODO")
        return False
    if abs(mod.predict([10, 20, 30]) - 17.1) > 0.01:
        print("FAIL — predict() baseline broken")
        return False

    from sklearn.datasets import load_iris
    X, y = load_iris(return_X_y=True)
    model = mod.train(X, y)
    if model is None:
        print("FAIL — train() returned None")
        return False
    pred = mod.model_predict(model, [5.1, 3.5, 1.4, 0.2])
    if pred != 0:
        print(f"FAIL — iris setosa should predict 0, got {pred}")
        return False

    print("PASS — Milestone 04 complete!")
    print("  DataMind has a learned model. Move to level-05.")
    return True


if __name__ == "__main__":
    sys.exit(0 if check() else 1)
