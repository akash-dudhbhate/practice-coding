"""
Milestone 00 Check — DataMind Foundation
"""

import importlib.util
import os
import sys


def check():
    path = os.path.join(os.path.dirname(__file__), "datamind.py")
    spec = importlib.util.spec_from_file_location("datamind", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)

    if not hasattr(mod, 'predict'):
        print("FAIL — 'predict' function not found")
        return False

    result = mod.predict([10, 20, 30])
    if result is None:
        print("FAIL — predict() returned None (still a TODO?)")
        return False

    expected = 10*0.5 + 20*0.3 + 30*0.2 + 0.1  # 17.1
    if abs(result - expected) > 0.01:
        print(f"FAIL — predict([10,20,30]) = {result}, expected ~{expected}")
        return False

    print("PASS — Milestone 00 complete!")
    print("  DataMind foundation works. Move to level-01.")
    return True


if __name__ == "__main__":
    ok = check()
    sys.exit(0 if ok else 1)
