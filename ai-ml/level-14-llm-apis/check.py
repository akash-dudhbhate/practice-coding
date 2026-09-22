"""
Level 14 Checker — Real LLM APIs
==================================
Runs each check function against your work file.
Usage:
    python3 check.py easy/p01
    python3 check.py all
"""

import importlib.util
import os
import sys
import json


def load_mod(filepath):
    spec = importlib.util.spec_from_file_location("work", filepath)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def check_easy_p01(mod):
    if not hasattr(mod, 'ask_llm'):
        return False, "Function 'ask_llm' not found"
    r = mod.ask_llm("What is 2+2?")
    if not isinstance(r, str) or len(r) == 0:
        return False, f"Expected non-empty string, got {r!r}"
    return True, "All tests passed!"


def check_easy_p02(mod):
    if not hasattr(mod, 'ask_with_persona'):
        return False, "Function 'ask_with_persona' not found"
    r = mod.ask_with_persona("Explain recursion", "You are a teacher")
    if not isinstance(r, str) or len(r) == 0:
        return False, f"Expected non-empty string, got {r!r}"
    return True, "All tests passed!"


def check_easy_p03(mod):
    if not hasattr(mod, 'creative_vs_precise'):
        return False, "Function 'creative_vs_precise' not found"
    p, c = mod.creative_vs_precise("Write a tagline")
    if not isinstance(p, str) or not isinstance(c, str):
        return False, "Should return (precise_str, creative_str)"
    return True, "All tests passed!"


def check_medium_p01(mod):
    if not hasattr(mod, 'extract'):
        return False, "Function 'extract' not found"
    d = mod.extract("My name is Alice, I'm 30, from Paris")
    if not isinstance(d, dict):
        return False, f"Expected dict, got {type(d)}"
    for key in ["name", "age", "city"]:
        if key not in d:
            return False, f"Missing key '{key}'"
    return True, "All tests passed!"


def check_medium_p02(mod):
    if not hasattr(mod, 'parse_or_retry'):
        return False, "Function 'parse_or_retry' not found"
    d = mod.parse_or_retry("Alice is 30")
    if not isinstance(d, dict):
        return False, f"Expected dict, got {type(d)}"
    return True, "All tests passed!"


def check_medium_p03(mod):
    if not hasattr(mod, 'classify_batch'):
        return False, "Function 'classify_batch' not found"
    texts = ["I love this", "terrible product", "it's ok"]
    labels = mod.classify_batch(texts, ["positive", "negative", "neutral"])
    if not isinstance(labels, list) or len(labels) != 3:
        return False, f"Expected list of 3 labels, got {labels}"
    return True, "All tests passed!"


def check_hard_p01(mod):
    if not hasattr(mod, 'stream'):
        return False, "Function 'stream' not found"
    chunks = list(mod.stream("Tell me a joke"))
    if len(chunks) < 2:
        return False, f"Expected multiple chunks, got {len(chunks)}"
    if not all(isinstance(c, str) for c in chunks):
        return False, "All chunks should be strings"
    return True, "All tests passed!"


def check_hard_p02(mod):
    if not hasattr(mod, 'agent_decide'):
        return False, "Function 'agent_decide' not found"
    d = mod.agent_decide("what is 6 * 7?")
    if not isinstance(d, dict) or "tool" not in d:
        return False, f"Expected dict with 'tool', got {d}"
    if d["tool"] not in ["calc", "search", "weather", "unknown"]:
        return False, f"Unknown tool '{d['tool']}'"
    return True, "All tests passed!"


def check_hard_p03(mod):
    if not hasattr(mod, 'TrackedLLM'):
        return False, "Class 'TrackedLLM' not found"
    llm = mod.TrackedLLM()
    llm.call("hello")
    llm.call("test")
    s = llm.stats()
    if s["calls"] != 2:
        return False, f"Expected 2 calls, got {s['calls']}"
    if "est_tokens" not in s or "est_cost_usd" not in s:
        return False, "stats() missing keys"
    return True, "All tests passed!"


CHECKS = {
    "easy/p01": check_easy_p01,   "easy/p02": check_easy_p02,
    "easy/p03": check_easy_p03,
    "medium/p01": check_medium_p01, "medium/p02": check_medium_p02,
    "medium/p03": check_medium_p03,
    "hard/p01": check_hard_p01,   "hard/p02": check_hard_p02,
    "hard/p03": check_hard_p03,
}


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 check.py <difficulty/pXX> or 'all'")
        return
    target = sys.argv[1]
    if target == "all":
        for check_id in sorted(CHECKS):
            run_one(check_id)
        return
    run_one(target)


def run_one(check_id):
    if check_id not in CHECKS:
        print(f"Unknown: {check_id}")
        return
    diff, num = check_id.split("/")
    num_clean = num.lstrip("p")
    work = None
    d = os.path.join(os.path.dirname(__file__), diff)
    exact = os.path.join(d, f"p{num_clean}-solve.py")
    if os.path.exists(exact):
        work = exact
    else:
        import glob
        matches = [f for f in glob.glob(os.path.join(d, f"p{num_clean}-*.py"))
                   if "solutions" not in f]
        work = matches[0] if matches else None
    if not work:
        print(f"{check_id}: FILE NOT FOUND")
        return
    try:
        mod = load_mod(work)
        passed, msg = CHECKS[check_id](mod)
        status = "PASS" if passed else "FAIL"
        print(f"{check_id}: {status} — {msg}")
        if passed:
            with open(work) as f:
                first = f.readline().strip()
            if "DONE" not in first:
                print("  → add '# DONE' to the first line to mark complete")
    except Exception as e:
        if "NoneType" in str(e):
            print(f"  {check_id}: FAIL — a function returned None — write the body!")
        else:
            print(f"{check_id}: ERROR — {e}")


if __name__ == "__main__":
    main()
