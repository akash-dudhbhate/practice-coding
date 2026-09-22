"""Milestone 12 Check — Knowledge Base"""

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

    docs = [
        "To reset your API key, visit settings and click regenerate.",
        "Model predictions return a score between 0 and 100.",
        "Upload CSV files via the /upload endpoint with POST.",
        "Accuracy above 0.9 is considered production-ready.",
    ]
    r = mod.retrieve("How do I reset my API key?", docs)
    if "API key" not in r:
        print(f"FAIL — should retrieve API key doc, got '{r}'")
        return False
    r2 = mod.retrieve("what is a good accuracy?", docs)
    if "0.9" not in r2 and "Accuracy" not in r2:
        print(f"FAIL — should retrieve accuracy doc, got '{r2}'")
        return False

    a = mod.answer("How do I reset my API key?", docs)
    if "API key" not in a:
        print(f"FAIL — answer should include doc, got '{a}'")
        return False
    a2 = mod.answer("quantum entanglement theory", docs)
    if "don't have" not in a2.lower() and "no information" not in a2.lower():
        print(f"FAIL — low-similarity query should get fallback, got '{a2}'")
        return False

    print("PASS — Milestone 12 complete!")
    print("  DataMind answers from its docs. Move to level-13.")
    return True


if __name__ == "__main__":
    sys.exit(0 if check() else 1)
