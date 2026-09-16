"""Milestone 01 Check — Design Doc"""

import importlib.util
import os
import sys


def check():
    path = os.path.join(os.path.dirname(__file__), "datamind.py")
    spec = importlib.util.spec_from_file_location("datamind", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)

    if not hasattr(mod, 'predict'):
        print("FAIL — predict() missing (did you break milestone-00?)")
        return False
    r = mod.predict([10, 20, 30])
    if r is None or abs(r - 17.1) > 0.01:
        print(f"FAIL — predict([10,20,30]) = {r}, expected ~17.1")
        return False

    if not hasattr(mod, 'describe'):
        print("FAIL — describe() not found")
        return False
    d = mod.describe()
    if not isinstance(d, dict):
        print(f"FAIL — describe() should return dict, got {type(d)}")
        return False
    for key in ["name", "problem_type", "tasks", "users", "v1_scope"]:
        if key not in d:
            print(f"FAIL — describe() missing key '{key}'")
            return False
    if d["name"] != "DataMind":
        print(f"FAIL — name should be 'DataMind', got '{d['name']}'")
        return False
    if len(d["tasks"]) < 3:
        print("FAIL — tasks should list ≥3 capabilities")
        return False

    print("PASS — Milestone 01 complete!")
    print("  DataMind has a design. Move to level-02.")
    return True


if __name__ == "__main__":
    sys.exit(0 if check() else 1)
