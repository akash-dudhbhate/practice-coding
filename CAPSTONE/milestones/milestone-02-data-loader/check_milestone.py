"""Milestone 02 Check — Data Loader"""

import importlib.util
import os
import sys


def check():
    path = os.path.join(os.path.dirname(__file__), "datamind.py")
    spec = importlib.util.spec_from_file_location("datamind", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)

    # Earlier milestones still work
    pred = mod.predict([10, 20, 30]) if hasattr(mod, 'predict') else None
    if pred is None:
        print("FAIL — predict() missing or still a TODO")
        return False
    if abs(mod.predict([10, 20, 30]) - 17.1) > 0.01:
        print("FAIL — predict() broken")
        return False
    if not isinstance(mod.describe(), dict):
        print("FAIL — describe() broken")
        return False

    raw = [
        {"name": "Ana", "age": "28", "country": "usa", "income": "$52,000"},
        {"name": "Ana", "age": "28", "country": "usa", "income": "$52,000"},
        {"name": "Ben", "age": "",   "country": "US",  "income": "$61,500"},
        {"name": "Cid", "age": "35", "country": "in",  "income": ""},
    ]
    cleaned = mod.load_records(raw)
    if len(cleaned) != 3:
        print(f"FAIL — expected 3 rows after dedup, got {len(cleaned)}")
        return False
    if not isinstance(cleaned[0]["age"], float):
        print(f"FAIL — age should be float, got {type(cleaned[0]['age'])}")
        return False
    if cleaned[1]["age"] != 31.5:  # median of 28, 35
        print(f"FAIL — Ben's age should be median 31.5, got {cleaned[1]['age']}")
        return False
    if cleaned[0]["country"] != "USA":
        print(f"FAIL — country should be USA, got {cleaned[0]['country']}")
        return False
    if cleaned[0]["income"] != 52000.0:
        print(f"FAIL — income should be 52000.0, got {cleaned[0]['income']}")
        return False
    if cleaned[2]["income"] is not None:
        print(f"FAIL — empty income should be None, got {cleaned[2]['income']}")
        return False

    print("PASS — Milestone 02 complete!")
    print("  DataMind can clean messy data. Move to level-03.")
    return True


if __name__ == "__main__":
    sys.exit(0 if check() else 1)
