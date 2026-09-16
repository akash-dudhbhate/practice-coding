"""Milestone 06 Check — Feature Engine"""

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

    rows = [{"age": 30, "income": 50000, "spend": 60},
            {"age": 45, "income": 80000, "spend": 30},
            {"age": 25, "income": 35000, "spend": 80}]
    out = mod.add_features(rows)
    if out is None:
        print("FAIL — add_features returned None")
        return False
    r = out[0]
    for key in ["income_per_age", "high_earner", "spend_ratio"]:
        if key not in r:
            print(f"FAIL — missing derived feature '{key}'")
            return False
    if abs(r["income_per_age"] - 50000/30) > 0.01:
        print(f"FAIL — income_per_age wrong: {r['income_per_age']}")
        return False
    if r["spend_ratio"] != 0.6:
        print(f"FAIL — spend_ratio should be 0.6, got {r['spend_ratio']}")
        return False
    if out[2]["high_earner"] != 0 or out[1]["high_earner"] != 1:
        print("FAIL — high_earner logic wrong (median=50000)")
        return False

    print("PASS — Milestone 06 complete!")
    print("  DataMind engineers features. Move to level-07.")
    return True


if __name__ == "__main__":
    sys.exit(0 if check() else 1)
