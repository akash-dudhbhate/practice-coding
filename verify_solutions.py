"""
Verify All Solutions — AI/ML Track
====================================
Runs every level's check functions against the reference solutions.
This is for curriculum maintainers — learners should use check.py
inside each level to test THEIR OWN work files.

Usage:
    python3 verify_solutions.py            # all levels
    python3 verify_solutions.py 07         # one level
"""

import os
import sys
import glob
import io
import contextlib
import importlib.util


AI_ML_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ai-ml")


def load_module(filepath, name="mod"):
    spec = importlib.util.spec_from_file_location(name, filepath)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def verify_level(level_path):
    """Run a level's checks against its solutions. Returns list of results."""
    results = []
    check_file = os.path.join(level_path, "check.py")
    if not os.path.exists(check_file):
        return [("—", "SKIP", "no check.py")]

    # Load check.py BEFORE chdir so the path resolves correctly
    check = load_module(check_file, "check")
    cwd = os.getcwd()
    os.chdir(level_path)
    sys.path.insert(0, level_path)
    try:
        for check_id, func in check.CHECKS.items():
            diff, num = check_id.split("/")
            sol = os.path.join(level_path, diff, "solutions", f"{num}-solution.py")
            if not os.path.exists(sol):
                results.append((check_id, "MISS", "no solution file"))
                continue
            buf = io.StringIO()
            try:
                with contextlib.redirect_stdout(buf):
                    mod = load_module(sol, "sol")
                    passed, msg = func(mod)
                results.append((check_id, "PASS" if passed else "FAIL", msg))
            except Exception as e:
                results.append((check_id, "ERROR", str(e)[:80]))
    finally:
        os.chdir(cwd)
        sys.path.remove(level_path)
        # Clean cached module so next level's check.py loads fresh
        for m in ["check", "sol"]:
            sys.modules.pop(m, None)
    return results


def main():
    only = sys.argv[1] if len(sys.argv) > 1 else None
    levels = sorted(glob.glob(os.path.join(AI_ML_DIR, "level-*")))
    if only:
        levels = [l for l in levels if f"level-{only.zfill(2)}" in os.path.basename(l)]
        if not levels:
            print(f"No level matching '{only}'")
            sys.exit(1)

    total_pass = total_fail = 0
    for level_path in levels:
        name = os.path.basename(level_path)
        print(f"\n=== {name} ===")
        for check_id, status, msg in verify_level(level_path):
            print(f"  {check_id}: {status}" + (f" — {msg}" if status != "PASS" else ""))
            if status == "PASS":
                total_pass += 1
            else:
                total_fail += 1

    print(f"\n{'=' * 50}")
    print(f"  {total_pass} passed, {total_fail} failed")
    print(f"{'=' * 50}")
    sys.exit(0 if total_fail == 0 else 1)


if __name__ == "__main__":
    main()
