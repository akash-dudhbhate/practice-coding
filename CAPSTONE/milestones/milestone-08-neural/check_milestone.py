"""Milestone 08 Check — Neural Mode"""

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
        print("FAIL — predict() broken")
        return False

    from sklearn.datasets import load_iris
    X, y = load_iris(return_X_y=True)
    model, acc = mod.neural_fit(X, y)
    if model is None or acc is None:
        print("FAIL — neural_fit should return (model, accuracy)")
        return False
    if acc < 0.85:
        print(f"FAIL — iris MLP should hit >0.85 train acc, got {acc:.4f}")
        return False

    print("PASS — Milestone 08 complete!")
    print("  DataMind has a neural option. Move to level-09.")
    return True


if __name__ == "__main__":
    sys.exit(0 if check() else 1)
