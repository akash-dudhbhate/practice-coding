"""
Auto-Check System — Lesson 05 (Control Flow & Loops)
=========================================================
Usage:
    python3 check.py easy/p01
    python3 check.py all
"""

import os
import sys
import glob
import io
import contextlib
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
    if not hasattr(module, 'classify_number'):
        return False, "Function 'classify_number' not found"
    if module.classify_number(5) != "positive":
        return False, "classify_number(5) should be 'positive'"
    if module.classify_number(-3) != "negative":
        return False, "classify_number(-3) should be 'negative'"
    if module.classify_number(0) != "zero":
        return False, "classify_number(0) should be 'zero'"
    return True, "All tests passed!"


def check_easy_p02(module):
    if not hasattr(module, 'sum_range'):
        return False, "Function 'sum_range' not found"
    if module.sum_range(1, 5) != 15:
        return False, "sum_range(1, 5) should be 15"
    if module.sum_range(0, 0) != 0:
        return False, "sum_range(0, 0) should be 0"
    if module.sum_range(-2, 2) != 0:
        return False, "sum_range(-2, 2) should be 0"
    return True, "All tests passed!"


def check_easy_p03(module):
    if not hasattr(module, 'count_down'):
        return False, "Function 'count_down' not found"
    if module.count_down(3) != [3, 2, 1]:
        return False, "count_down(3) should be [3, 2, 1]"
    if module.count_down(1) != [1]:
        return False, "count_down(1) should be [1]"
    if module.count_down(0) != []:
        return False, "count_down(0) should be []"
    return True, "All tests passed!"


def check_medium_p01(module):
    if not hasattr(module, 'first_even'):
        return False, "Function 'first_even' not found"
    if module.first_even([1, 3, 4, 5]) != 4:
        return False, "first_even([1, 3, 4, 5]) should be 4"
    if module.first_even([1, 3, 5]) is not None:
        return False, "first_even([1, 3, 5]) should be None"
    if module.first_even([]) is not None:
        return False, "first_even([]) should be None"
    return True, "All tests passed!"


def check_medium_p02(module):
    if not hasattr(module, 'skip_negatives'):
        return False, "Function 'skip_negatives' not found"
    if module.skip_negatives([1, -2, 3, -4, 5]) != [1, 3, 5]:
        return False, "skip_negatives([1, -2, 3, -4, 5]) should be [1, 3, 5]"
    if module.skip_negatives([-1, -2]) != []:
        return False, "skip_negatives([-1, -2]) should be []"
    if module.skip_negatives([]) != []:
        return False, "skip_negatives([]) should be []"
    return True, "All tests passed!"


def check_medium_p03(module):
    if not hasattr(module, 'multiplication_table'):
        return False, "Function 'multiplication_table' not found"
    if module.multiplication_table(3) != [[1, 2, 3], [2, 4, 6], [3, 6, 9]]:
        return False, "multiplication_table(3) should be [[1, 2, 3], [2, 4, 6], [3, 6, 9]]"
    if module.multiplication_table(1) != [[1]]:
        return False, "multiplication_table(1) should be [[1]]"
    return True, "All tests passed!"


def check_hard_p01(module):
    if not hasattr(module, 'is_palindrome'):
        return False, "Function 'is_palindrome' not found"
    if module.is_palindrome("racecar") is not True:
        return False, "is_palindrome('racecar') should be True"
    if module.is_palindrome("hello") is not False:
        return False, "is_palindrome('hello') should be False"
    if module.is_palindrome("") is not True:
        return False, "is_palindrome('') should be True"
    return True, "All tests passed!"


def check_hard_p02(module):
    if not hasattr(module, 'find_pair'):
        return False, "Function 'find_pair' not found"
    if module.find_pair([2, 7, 11, 15], 9) != (0, 1):
        return False, "find_pair([2, 7, 11, 15], 9) should be (0, 1)"
    if module.find_pair([1, 2, 3], 10) is not None:
        return False, "find_pair([1, 2, 3], 10) should be None"
    return True, "All tests passed!"


def check_hard_p03(module):
    if not hasattr(module, 'print_multiplication_table'):
        return False, "Function 'print_multiplication_table' not found"
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        module.print_multiplication_table(3)
    lines = buf.getvalue().splitlines()
    if len(lines) != 3:
        return False, f"print_multiplication_table(3) should print 3 lines, got {len(lines)}"
    for i, line in enumerate(lines, start=1):
        vals = [int(x) for x in line.split()]
        if vals != [i * j for j in range(1, 4)]:
            return False, f"row {i} should be {[i * j for j in range(1, 4)]}, got {vals}"
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
        print("  LESSON 05 — AUTO-CHECK ALL")
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
