"""Milestone 10 Check — API"""

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

    try:
        app = mod.make_app()
    except Exception as e:
        print(f"FAIL — make_app() raised {e}")
        return False
    if app is None:
        print("FAIL — make_app() returned None")
        return False

    from fastapi.testclient import TestClient
    c = TestClient(app)
    h = c.get("/health").json()
    if h.get("status") != "ok":
        print(f"FAIL — /health should return status ok, got {h}")
        return False
    p = c.post("/predict", json={"features": [10, 20, 30]}).json()
    if abs(p.get("prediction", 0) - 17.1) > 0.01:
        print(f"FAIL — /predict should return ~17.1, got {p}")
        return False

    print("PASS — Milestone 10 complete!")
    print("  DataMind is a live API. Move to level-11.")
    return True


if __name__ == "__main__":
    sys.exit(0 if check() else 1)
