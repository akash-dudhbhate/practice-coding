"""
Auto-Check System — Deep Learning
=============================
Run this to verify your solutions automatically.

Usage:
    python3 check.py easy/p01
    python3 check.py all
"""

import os
import sys
import glob
import importlib.util


def load_module(filepath):
    spec = importlib.util.spec_from_file_location("solution", filepath)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


# TODO: Add check functions for each problem
# def check_p01(module):
#     if not hasattr(module, 'solve'):
#         return False, "Function 'solve' not found"
#     result = module.solve(...)
#     if result != expected:
#         return False, f"Expected X, got Y"
#     return True, "All tests passed!"


CHECKS = {
    # Add checks here
}


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 check.py <level>/<problem>")
        sys.exit(1)

    target = sys.argv[1]
    level_dir = os.path.dirname(os.path.abspath(__file__))

    if target == "all":
        print("=" * 60)
        print(f"  DEEP LEARNING — AUTO-CHECK ALL")
        print("=" * 60)
        for check_id, check_func in CHECKS.items():
            level, num = check_id.split("/")
            num_clean = num.lstrip("p")
            filepath = os.path.join(level_dir, level, f"p{num_clean}-solve.py")
            if not os.path.exists(filepath):
                pattern = os.path.join(level_dir, level, f"p{num_clean}-*.py")
                matches = [f for f in glob.glob(pattern) if "solutions" not in f]
                if matches:
                    filepath = matches[0]
            if not os.path.exists(filepath):
                print(f"  {check_id}: FILE NOT FOUND")
                continue
            try:
                module = load_module(filepath)
                passed, msg = check_func(module)
                status = "PASS" if passed else "FAIL"
                print(f"  {check_id}: {status} — {msg}")
            except Exception as e:
                print(f"  {check_id}: ERROR — {e}")
        print("=" * 60)
        return

    level, num = target.split("/")
    check_id = f"{level}/{num}"
    if check_id not in CHECKS:
        print(f"Error: unknown problem '{check_id}'")
        sys.exit(1)

    num_clean = num.lstrip("p")
    filepath = os.path.join(level_dir, level, f"p{num_clean}-solve.py")
    if not os.path.exists(filepath):
        pattern = os.path.join(level_dir, level, f"p{num_clean}-*.py")
        matches = [f for f in glob.glob(pattern) if "solutions" not in f]
        if matches:
            filepath = matches[0]
    if not os.path.exists(filepath):
        print(f"Error: file not found: {filepath}")
        sys.exit(1)

    try:
        module = load_module(filepath)
        passed, msg = CHECKS[check_id](module)
        if passed:
            print(f"✓ PASS — {msg}")
            print(f"  Add '# DONE' to the first line of {filepath}")
        else:
            print(f"✗ FAIL — {msg}")
    except Exception as e:
        print(f"✗ ERROR — {e}")


if __name__ == "__main__":
    main()
