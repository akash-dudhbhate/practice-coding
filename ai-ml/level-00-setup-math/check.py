"""
Auto-Check System — Level 00 (Setup & Math)
=============================================
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


def _find_file(level_dir, level, num):
    num_clean = num.lstrip("p")
    filepath = os.path.join(level_dir, level, f"p{num_clean}-solve.py")
    if not os.path.exists(filepath):
        pattern = os.path.join(level_dir, level, f"p{num_clean}-*.py")
        matches = [f for f in glob.glob(pattern) if "solutions" not in f]
        if matches:
            filepath = matches[0]
    return filepath


def check_easy_p01(module):
    if not hasattr(module, 'check_env'):
        return False, "Function 'check_env' not found"
    env = module.check_env()
    for key in ['numpy', 'pandas', 'sklearn']:
        if key not in env:
            return False, f"Missing key: {key}"
        if not isinstance(env[key], str):
            return False, f"{key} version should be a string"
    return True, "All tests passed!"


def check_easy_p02(module):
    if not hasattr(module, 'dot'):
        return False, "Function 'dot' not found"
    if module.dot([1, 2, 3], [4, 5, 6]) != 32:
        return False, "dot([1,2,3],[4,5,6]) should be 32"
    if module.dot([0, 1], [5, 5]) != 5:
        return False, "dot([0,1],[5,5]) should be 5"
    if module.dot([2, 0, 2], [1, 1, 1]) != 4:
        return False, "dot([2,0,2],[1,1,1]) should be 4"
    return True, "All tests passed!"


def check_easy_p03(module):
    if not hasattr(module, 'stats'):
        return False, "Function 'stats' not found"
    m, v, s = module.stats([2, 4, 6])
    if abs(m - 4.0) > 0.01:
        return False, f"Mean should be 4.0, got {m}"
    if abs(v - 2.667) > 0.01:
        return False, f"Variance should be ~2.67, got {v}"
    if abs(s - 1.633) > 0.01:
        return False, f"Std should be ~1.63, got {s}"
    return True, "All tests passed!"


def check_medium_p01(module):
    if not hasattr(module, 'weighted_sum'):
        return False, "Function 'weighted_sum' not found"
    if abs(module.weighted_sum([2, 3], [0.5, 1.5], 1) - 6.5) > 0.01:
        return False, "weighted_sum([2,3],[0.5,1.5],1) should be 6.5"
    if abs(module.weighted_sum([1, 1], [2, 2], 0) - 4.0) > 0.01:
        return False, "weighted_sum([1,1],[2,2],0) should be 4.0"
    return True, "All tests passed!"


def check_medium_p02(module):
    if not hasattr(module, 'normalize'):
        return False, "Function 'normalize' not found"
    result = module.normalize([10, 20, 30])
    if result != [0.0, 0.5, 1.0]:
        return False, f"Expected [0.0, 0.5, 1.0], got {result}"
    edge = module.normalize([5, 5, 5])
    if edge != [0.0, 0.0, 0.0]:
        return False, f"Edge case (all same) should return zeros, got {edge}"
    return True, "All tests passed!"


def check_medium_p03(module):
    if not hasattr(module, 'euclidean'):
        return False, "Function 'euclidean' not found"
    if abs(module.euclidean([0, 0], [3, 4]) - 5.0) > 0.001:
        return False, "euclidean([0,0],[3,4]) should be 5.0"
    if module.euclidean([1, 1, 1], [1, 1, 1]) != 0.0:
        return False, "Distance between identical points should be 0"
    return True, "All tests passed!"


def check_hard_p01(module):
    if not hasattr(module, 'descend'):
        return False, "Function 'descend' not found"
    path = module.descend(5.0, 0.1, 20)
    if path[0] != 5.0:
        return False, f"Path should start at 5.0, got {path[0]}"
    if not abs(path[-1] - 0.0576) < 0.001:
        return False, f"Path should end at ~0.0576, got {path[-1]}"
    if len(path) != 21:
        return False, f"Path should have 21 points (x0 + 20 steps), got {len(path)}"
    return True, "All tests passed!"


def check_hard_p02(module):
    if not hasattr(module, 'bayes'):
        return False, "Function 'bayes' not found"
    p = module.bayes(0.01, 0.95, 0.10)
    if not abs(p - 0.0876) < 0.001:
        return False, f"P(sick|+) should be ~0.0876, got {p}"
    return True, "All tests passed!"


def check_hard_p03(module):
    if not hasattr(module, 'matmul'):
        return False, "Function 'matmul' not found"
    result = module.matmul([[1, 2], [3, 4]], [[5, 6], [7, 8]])
    if result != [[19, 22], [43, 50]]:
        return False, f"Expected [[19,22],[43,50]], got {result}"
    return True, "All tests passed!"


CHECKS = {
    "easy/p01": check_easy_p01,
    "easy/p02": check_easy_p02,
    "easy/p03": check_easy_p03,
    "medium/p01": check_medium_p01,
    "medium/p02": check_medium_p02,
    "medium/p03": check_medium_p03,
    "hard/p01": check_hard_p01,
    "hard/p02": check_hard_p02,
    "hard/p03": check_hard_p03,
}


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 check.py <level>/<problem>")
        sys.exit(1)

    target = sys.argv[1]
    level_dir = os.path.dirname(os.path.abspath(__file__))

    if target == "all":
        print("=" * 60)
        print("  LEVEL 00 — AUTO-CHECK ALL")
        print("=" * 60)
        for check_id, check_func in CHECKS.items():
            level, num = check_id.split("/")
            filepath = _find_file(level_dir, level, num)
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

    filepath = _find_file(level_dir, level, num)
    if not os.path.exists(filepath):
        print(f"Error: file not found: {filepath}")
        sys.exit(1)

    try:
        module = load_module(filepath)
        passed, msg = CHECKS[check_id](module)
        if passed:
            print(f"PASS — {msg}")
            print(f"  Add '# DONE' to the first line of {filepath}")
        else:
            print(f"FAIL — {msg}")
    except Exception as e:
        print(f"ERROR — {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
