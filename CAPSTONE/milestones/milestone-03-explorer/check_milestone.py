"""Milestone 03 Check — Auto-Explorer"""

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

    rows = [{"age": 28.0, "income": 52000.0},
            {"age": 31.5, "income": 61500.0},
            {"age": 35.0, "income": None}]
    s = mod.summarize(rows)
    if not isinstance(s, dict) or "age" not in s:
        print(f"FAIL — summarize should return dict with 'age', got {s}")
        return False
    if abs(s["age"]["mean"] - 31.5) > 0.01:
        print(f"FAIL — age mean should be 31.5, got {s['age']['mean']}")
        return False
    if s["age"]["min"] != 28.0 or s["age"]["max"] != 35.0:
        print("FAIL — age min/max wrong")
        return False
    # income should skip the None and use only 2 values
    if abs(s["income"]["mean"] - 56750.0) > 0.01:
        print(f"FAIL — income mean should be 56750.0, got {s['income']['mean']}")
        return False

    mod.auto_chart(rows, "test_chart.png")
    if not os.path.exists(os.path.join(os.path.dirname(__file__), "test_chart.png")) \
       and not os.path.exists("test_chart.png"):
        print("FAIL — auto_chart didn't save a file")
        return False
    if os.path.exists("test_chart.png"):
        os.remove("test_chart.png")

    print("PASS — Milestone 03 complete!")
    print("  DataMind can explore data. Move to level-04.")
    return True


if __name__ == "__main__":
    sys.exit(0 if check() else 1)
