"""Milestone 11 Check — Explainer"""

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

    p = mod.explain_prompt([10, 20, 30], 17.1, ["age", "income_k", "spend"])
    if not isinstance(p, str):
        print(f"FAIL — explain_prompt should return str, got {type(p)}")
        return False
    for required in ["age", "income_k", "spend", "17.1"]:
        if required not in p:
            print(f"FAIL — prompt should include '{required}'")
            return False
    if "2 sentences" not in p and "two sentences" not in p.lower():
        print("FAIL — prompt should ask for 2 sentences")
        return False

    r = mod.parse_explanation("  padded text  \n")
    if r != "padded text":
        print(f"FAIL — parse should strip whitespace, got '{r}'")
        return False

    print("PASS — Milestone 11 complete!")
    print("  DataMind can explain itself. Move to level-12.")
    return True


if __name__ == "__main__":
    sys.exit(0 if check() else 1)
