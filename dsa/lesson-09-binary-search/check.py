"""
Auto-Check System — Lesson 09 (Binary Search)
=========================================================
Usage:
    python3 check.py easy/p01     # check one of YOUR files
    python3 check.py all          # check all 9 of YOUR files
    python3 check.py solutions    # check the reference solutions (9/9 must pass)
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


def _find_solution(level_dir, level, num):
    num_clean = num.lstrip("p")
    return os.path.join(level_dir, level, "solutions", f"p{num_clean}-solution.py")


def _is_stub(filepath):
    """A file that still contains the TODO marker has not been attempted."""
    try:
        with open(filepath) as f:
            return "# TODO" in f.read()
    except OSError:
        return False


def check_easy_p01(module):
    if not hasattr(module, 'binary_search'):
        return False, "Function 'binary_search' not found"
    if module.binary_search([-1, 0, 3, 5, 9, 12], 9) != 4:
        return False, "binary_search([-1,0,3,5,9,12], 9) should be 4"
    if module.binary_search([-1, 0, 3, 5, 9, 12], 2) != -1:
        return False, "binary_search([-1,0,3,5,9,12], 2) should be -1"
    if module.binary_search([5], 5) != 0:
        return False, "binary_search([5], 5) should be 0"
    if module.binary_search([], 1) != -1:
        return False, "binary_search([], 1) should be -1"
    if module.binary_search([1, 2, 3], 1) != 0:
        return False, "binary_search([1,2,3], 1) should be 0 (first element)"
    return True, "All tests passed!"


def check_easy_p02(module):
    if not hasattr(module, 'first_occurrence'):
        return False, "Function 'first_occurrence' not found"
    if module.first_occurrence([1, 2, 2, 2, 3, 4], 2) != 1:
        return False, "first_occurrence([1,2,2,2,3,4], 2) should be 1"
    if module.first_occurrence([1, 2, 2, 2, 3, 4], 4) != 5:
        return False, "first_occurrence([1,2,2,2,3,4], 4) should be 5"
    if module.first_occurrence([1, 2, 2, 2, 3, 4], 9) != -1:
        return False, "first_occurrence([1,2,2,2,3,4], 9) should be -1"
    if module.first_occurrence([2, 2, 2], 2) != 0:
        return False, "first_occurrence([2,2,2], 2) should be 0"
    if module.first_occurrence([], 3) != -1:
        return False, "first_occurrence([], 3) should be -1"
    return True, "All tests passed!"


def check_easy_p03(module):
    if not hasattr(module, 'search_insert'):
        return False, "Function 'search_insert' not found"
    if module.search_insert([1, 3, 5, 6], 5) != 2:
        return False, "search_insert([1,3,5,6], 5) should be 2"
    if module.search_insert([1, 3, 5, 6], 2) != 1:
        return False, "search_insert([1,3,5,6], 2) should be 1"
    if module.search_insert([1, 3, 5, 6], 7) != 4:
        return False, "search_insert([1,3,5,6], 7) should be 4"
    if module.search_insert([1, 3, 5, 6], 0) != 0:
        return False, "search_insert([1,3,5,6], 0) should be 0"
    if module.search_insert([1], 0) != 0:
        return False, "search_insert([1], 0) should be 0"
    return True, "All tests passed!"


def check_medium_p01(module):
    if not hasattr(module, 'my_sqrt'):
        return False, "Function 'my_sqrt' not found"
    if module.my_sqrt(4) != 2:
        return False, "my_sqrt(4) should be 2"
    if module.my_sqrt(8) != 2:
        return False, "my_sqrt(8) should be 2 (floor of 2.82...)"
    if module.my_sqrt(0) != 0:
        return False, "my_sqrt(0) should be 0"
    if module.my_sqrt(1) != 1:
        return False, "my_sqrt(1) should be 1"
    if module.my_sqrt(2147395599) != 46339:
        return False, "my_sqrt(2147395599) should be 46339"
    if module.my_sqrt(15) != 3:
        return False, "my_sqrt(15) should be 3"
    return True, "All tests passed!"


def check_medium_p02(module):
    if not hasattr(module, 'min_ship_capacity'):
        return False, "Function 'min_ship_capacity' not found"
    if module.min_ship_capacity([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5) != 15:
        return False, "min_ship_capacity([1..10], 5) should be 15"
    if module.min_ship_capacity([3, 2, 2, 4, 1, 4], 3) != 6:
        return False, "min_ship_capacity([3,2,2,4,1,4], 3) should be 6"
    if module.min_ship_capacity([1, 2, 3, 1, 1], 4) != 3:
        return False, "min_ship_capacity([1,2,3,1,1], 4) should be 3"
    if module.min_ship_capacity([5], 1) != 5:
        return False, "min_ship_capacity([5], 1) should be 5"
    return True, "All tests passed!"


def check_medium_p03(module):
    if not hasattr(module, 'min_eating_speed'):
        return False, "Function 'min_eating_speed' not found"
    if module.min_eating_speed([3, 6, 7, 11], 8) != 4:
        return False, "min_eating_speed([3,6,7,11], 8) should be 4"
    if module.min_eating_speed([30, 11, 23, 4, 20], 5) != 30:
        return False, "min_eating_speed([30,11,23,4,20], 5) should be 30"
    if module.min_eating_speed([30, 11, 23, 4, 20], 6) != 23:
        return False, "min_eating_speed([30,11,23,4,20], 6) should be 23"
    if module.min_eating_speed([1], 1) != 1:
        return False, "min_eating_speed([1], 1) should be 1"
    return True, "All tests passed!"


def check_hard_p01(module):
    if not hasattr(module, 'search_rotated'):
        return False, "Function 'search_rotated' not found"
    if module.search_rotated([4, 5, 6, 7, 0, 1, 2], 0) != 4:
        return False, "search_rotated([4,5,6,7,0,1,2], 0) should be 4"
    if module.search_rotated([4, 5, 6, 7, 0, 1, 2], 3) != -1:
        return False, "search_rotated([4,5,6,7,0,1,2], 3) should be -1"
    if module.search_rotated([1], 0) != -1:
        return False, "search_rotated([1], 0) should be -1"
    if module.search_rotated([1, 3], 3) != 1:
        return False, "search_rotated([1,3], 3) should be 1"
    if module.search_rotated([5, 1, 3], 5) != 0:
        return False, "search_rotated([5,1,3], 5) should be 0"
    return True, "All tests passed!"


def check_hard_p02(module):
    if not hasattr(module, 'find_min_rotated'):
        return False, "Function 'find_min_rotated' not found"
    if module.find_min_rotated([3, 4, 5, 1, 2]) != 1:
        return False, "find_min_rotated([3,4,5,1,2]) should be 1"
    if module.find_min_rotated([4, 5, 6, 7, 0, 1, 2]) != 0:
        return False, "find_min_rotated([4,5,6,7,0,1,2]) should be 0"
    if module.find_min_rotated([11, 13, 15, 17]) != 11:
        return False, "find_min_rotated([11,13,15,17]) should be 11 (no rotation)"
    if module.find_min_rotated([2, 1]) != 1:
        return False, "find_min_rotated([2,1]) should be 1"
    if module.find_min_rotated([1]) != 1:
        return False, "find_min_rotated([1]) should be 1"
    return True, "All tests passed!"


def check_hard_p03(module):
    if not hasattr(module, 'find_peak'):
        return False, "Function 'find_peak' not found"
    r = module.find_peak([1, 2, 3, 1])
    if r != 2:
        return False, "find_peak([1,2,3,1]) should be 2"
    r = module.find_peak([1, 2, 1, 3, 5, 6, 4])
    if r not in (1, 5):
        return False, "find_peak([1,2,1,3,5,6,4]) should be 1 or 5"
    if module.find_peak([1]) != 0:
        return False, "find_peak([1]) should be 0"
    r = module.find_peak([1, 2])
    if r != 1:
        return False, "find_peak([1,2]) should be 1"
    r = module.find_peak([3, 2, 1])
    if r != 0:
        return False, "find_peak([3,2,1]) should be 0"
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


def _run_one(check_id, filepath):
    check_func = CHECKS[check_id]
    if not os.path.exists(filepath):
        print(f"  {check_id}: FILE NOT FOUND — {filepath}")
        return False
    if _is_stub(filepath):
        print(f"  {check_id}: FAIL — still a stub (TODO present) — write your solution!")
        return False
    try:
        module = load_module(filepath)
        passed, msg = check_func(module)
        status = "PASS" if passed else "FAIL"
        print(f"  {check_id}: {status} — {msg}")
        return passed
    except Exception as e:
        if "NoneType" in str(e):
            print(f"  {check_id}: FAIL — a function returned None — write the body!")
        else:
            print(f"  {check_id}: ERROR — {e}")
        return False


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 check.py <level>/<problem> | all | solutions")
        sys.exit(1)

    target = sys.argv[1]
    level_dir = os.path.dirname(os.path.abspath(__file__))

    if target == "solutions":
        print("=" * 60)
        print("  LESSON 09 — SOLUTION CHECK (all 9 must pass)")
        print("=" * 60)
        passed = 0
        for check_id in CHECKS:
            level, num = check_id.split("/")
            filepath = _find_solution(level_dir, level, num)
            if _run_one(check_id, filepath):
                passed += 1
        print(f"  {passed}/9 solutions pass")
        print("=" * 60)
        return

    if target == "all":
        print("=" * 60)
        print("  LESSON 09 — AUTO-CHECK ALL")
        print("=" * 60)
        for check_id in CHECKS:
            level, num = check_id.split("/")
            filepath = _find_file(level_dir, level, num)
            _run_one(check_id, filepath)
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
    if _is_stub(filepath):
        print("FAIL — still a stub (TODO present) — write your solution!")
        sys.exit(0)

    try:
        module = load_module(filepath)
        passed, msg = CHECKS[check_id](module)
        if passed:
            print(f"PASS — {msg}")
            print(f"  Add '# DONE' to the first line of {filepath}")
        else:
            print(f"FAIL — {msg}")
    except Exception as e:
        if "NoneType" in str(e):
            print(f"FAIL — a function returned None — write the body!")
        else:
            print(f"ERROR — {e}")
            import traceback
            traceback.print_exc()


if __name__ == "__main__":
    main()
