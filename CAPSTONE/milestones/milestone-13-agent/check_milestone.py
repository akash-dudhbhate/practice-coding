"""Milestone 13 Check — Agent (the complete DataMind)"""

import importlib.util
import os
import sys


def check():
    path = os.path.join(os.path.dirname(__file__), "datamind.py")
    spec = importlib.util.spec_from_file_location("datamind", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)

    if not hasattr(mod, 'predict') or mod.predict([10, 20, 30]) is None:
        print("FAIL — predict() missing or still a TODO")
        return False
    pred = mod.predict([10, 20, 30]) if hasattr(mod, 'predict') else None
    if pred is None:
        print("FAIL — predict() missing or still a TODO")
        return False
    if abs(mod.predict([10, 20, 30]) - 17.1) > 0.01:
        print("FAIL — predict() broken")
        return False

    r = mod.run("load and summarize the data")
    if not isinstance(r, dict):
        print(f"FAIL — run() should return dict, got {type(r)}")
        return False
    for key in ["goal", "steps_run", "result"]:
        if key not in r:
            print(f"FAIL — missing key '{key}' in result")
            return False
    if len(r["steps_run"]) < 2:
        print(f"FAIL — 'load and summarize' should run ≥2 steps, got {r['steps_run']}")
        return False
    if len(mod.MEMORY) < 2:
        print("FAIL — MEMORY should log observations")
        return False

    r2 = mod.run("predict score for 10 20 30")
    if "predict" not in str(r2["steps_run"]).lower():
        print(f"FAIL — predict goal should run predict step, got {r2['steps_run']}")
        return False

    print("PASS — Milestone 13 complete!")
    print("  DataMind is complete — a full AI system you built yourself.")
    return True


if __name__ == "__main__":
    sys.exit(0 if check() else 1)
