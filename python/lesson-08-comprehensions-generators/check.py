"""
Auto-Check System — Lesson 08 (Comprehensions & Generators)
=========================================================
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
    if not hasattr(module, 'squares'):
        return False, "Function 'squares' not found"
    if module.squares(4) != [0, 1, 4, 9]:
        return False, "squares(4) should be [0, 1, 4, 9]"
    if module.squares(0) != []:
        return False, "squares(0) should be []"
    return True, "All tests passed!"


def check_easy_p02(module):
    if not hasattr(module, 'evens'):
        return False, "Function 'evens' not found"
    if module.evens([1, 2, 3, 4, 5, 6]) != [2, 4, 6]:
        return False, "evens([1,2,3,4,5,6]) should be [2, 4, 6]"
    if module.evens([1, 3, 5]) != []:
        return False, "evens([1,3,5]) should be []"
    return True, "All tests passed!"


def check_easy_p03(module):
    if not hasattr(module, 'lengths'):
        return False, "Function 'lengths' not found"
    if module.lengths(["hi", "hello"]) != {"hi": 2, "hello": 5}:
        return False, "lengths(['hi','hello']) should be {'hi': 2, 'hello': 5}"
    if module.lengths([]) != {}:
        return False, "lengths([]) should be {}"
    return True, "All tests passed!"


def check_medium_p01(module):
    if not hasattr(module, 'flatten'):
        return False, "Function 'flatten' not found"
    if module.flatten([[1, 2], [3, 4]]) != [1, 2, 3, 4]:
        return False, "flatten([[1,2],[3,4]]) should be [1, 2, 3, 4]"
    if module.flatten([]) != []:
        return False, "flatten([]) should be []"
    return True, "All tests passed!"


def check_medium_p02(module):
    if not hasattr(module, 'sum_squares'):
        return False, "Function 'sum_squares' not found"
    if module.sum_squares(4) != 14:
        return False, "sum_squares(4) should be 14 (0+1+4+9)"
    if module.sum_squares(0) != 0:
        return False, "sum_squares(0) should be 0"
    return True, "All tests passed!"


def check_medium_p03(module):
    if not hasattr(module, 'even_squares'):
        return False, "Function 'even_squares' not found"
    if module.even_squares(5) != [0, 4, 16]:
        return False, "even_squares(5) should be [0, 4, 16]"
    if module.even_squares(1) != [0]:
        return False, "even_squares(1) should be [0]"
    return True, "All tests passed!"


def check_hard_p01(module):
    if not hasattr(module, 'fibonacci_gen'):
        return False, "Function 'fibonacci_gen' not found"
    if list(module.fibonacci_gen(6)) != [0, 1, 1, 2, 3, 5]:
        return False, "list(fibonacci_gen(6)) should be [0, 1, 1, 2, 3, 5]"
    if list(module.fibonacci_gen(0)) != []:
        return False, "list(fibonacci_gen(0)) should be []"
    if list(module.fibonacci_gen(1)) != [0]:
        return False, "list(fibonacci_gen(1)) should be [0]"
    return True, "All tests passed!"


def check_hard_p02(module):
    if not hasattr(module, 'chunked'):
        return False, "Function 'chunked' not found"
    if list(module.chunked([1, 2, 3, 4, 5], 2)) != [[1, 2], [3, 4], [5]]:
        return False, "list(chunked([1..5], 2)) should be [[1, 2], [3, 4], [5]]"
    if list(module.chunked([], 3)) != []:
        return False, "list(chunked([], 3)) should be []"
    return True, "All tests passed!"


def check_hard_p03(module):
    for fn in ('filter_positive', 'double', 'to_strings', 'pipeline'):
        if not hasattr(module, fn):
            return False, f"Function '{fn}' not found"
    if module.pipeline([-1, 2, -3, 4]) != ["4", "8"]:
        return False, "pipeline([-1, 2, -3, 4]) should be ['4', '8']"
    if module.pipeline([]) != []:
        return False, "pipeline([]) should be []"
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
        print("  LESSON 08 — AUTO-CHECK ALL")
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
                if "NoneType" in str(e):
                    print(f"  {check_id}: FAIL — a function returned None — write the body!")
                else:
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
        if "NoneType" in str(e):
            print(f"FAIL — a function returned None — write the body!")
        else:
            print(f"ERROR — {e}")
            import traceback
            traceback.print_exc()


if __name__ == "__main__":
    main()
