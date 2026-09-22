"""Milestone 05 Check — Evaluator"""

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
    from sklearn.model_selection import train_test_split
    X, y = load_iris(return_X_y=True)
    X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2,
                                            random_state=42, stratify=y)
    model = mod.train(X_tr, y_tr)
    m = mod.evaluate(model, X_te, y_te)
    for key in ["accuracy", "precision", "recall", "f1", "confusion"]:
        if key not in m:
            print(f"FAIL — missing metric '{key}'")
            return False
    if m["accuracy"] < 0.9:
        print(f"FAIL — iris accuracy should be >0.9, got {m['accuracy']}")
        return False
    if len(m["confusion"]) != 3:
        print("FAIL — confusion should be 3×3")
        return False

    print("PASS — Milestone 05 complete!")
    print("  DataMind can prove its quality. Move to level-06.")
    return True


if __name__ == "__main__":
    sys.exit(0 if check() else 1)
