"""
Auto-Check — Lesson 01: Variables, Types & Functions
====================================================
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
    pattern = os.path.join(level_dir, level, f"p{num_clean}-*.py")
    matches = [f for f in glob.glob(pattern) if "solutions" not in f]
    return matches[0] if matches else os.path.join(level_dir, level, f"p{num_clean}-solve.py")


def check_easy_p01(module):
    if not hasattr(module, 'max_of_two'):
        return False, "Function 'max_of_two' not found"
    if module.max_of_two(3, 7) is None:
        return False, "returned None — write the body!"
    if module.max_of_two(3, 7) != 7:
        return False, "max_of_two(3,7) should be 7"
    if module.max_of_two(10, 5) != 10:
        return False, "max_of_two(10,5) should be 10"
    if module.max_of_two(4, 4) != 4:
        return False, "max_of_two(4,4) should be 4"
    return True, "All tests passed!"


def check_easy_p02(module):
    if not hasattr(module, 'is_even'):
        return False, "Function 'is_even' not found"
    if module.is_even(4) is None:
        return False, "returned None — write the body!"
    if module.is_even(4) is not True:
        return False, "is_even(4) should be True"
    if module.is_even(7) is not False:
        return False, "is_even(7) should be False"
    return True, "All tests passed!"


def check_easy_p03(module):
    if not hasattr(module, 'celsius_to_fahrenheit'):
        return False, "Function 'celsius_to_fahrenheit' not found"
    r = module.celsius_to_fahrenheit(0)
    if r is None:
        return False, "returned None — write the body!"
    if abs(r - 32.0) > 0.01:
        return False, f"celsius_to_fahrenheit(0) should be 32.0, got {r}"
    if abs(module.celsius_to_fahrenheit(100) - 212.0) > 0.01:
        return False, "celsius_to_fahrenheit(100) should be 212.0"
    return True, "All tests passed!"


def check_medium_p01(module):
    if not hasattr(module, 'max_of_three'):
        return False, "Function 'max_of_three' not found"
    if module.max_of_three(1, 5, 3) is None:
        return False, "returned None — write the body!"
    if module.max_of_three(1, 5, 3) != 5:
        return False, "max_of_three(1,5,3) should be 5"
    if module.max_of_three(9, 2, 7) != 9:
        return False, "max_of_three(9,2,7) should be 9"
    return True, "All tests passed!"


def check_medium_p02(module):
    if not hasattr(module, 'is_leap_year'):
        return False, "Function 'is_leap_year' not found"
    if module.is_leap_year(2000) is None:
        return False, "returned None — write the body!"
    cases = [(2000, True), (1900, False), (2024, True), (2023, False)]
    for year, exp in cases:
        if module.is_leap_year(year) != exp:
            return False, f"is_leap_year({year}) should be {exp}"
    return True, "All tests passed!"


def check_medium_p03(module):
    if not hasattr(module, 'count_vowels'):
        return False, "Function 'count_vowels' not found"
    if module.count_vowels("hello") is None:
        return False, "returned None — write the body!"
    if module.count_vowels("hello") != 2:
        return False, "count_vowels('hello') should be 2"
    if module.count_vowels("xyz") != 0:
        return False, "count_vowels('xyz') should be 0"
    return True, "All tests passed!"


def check_hard_p01(module):
    if not hasattr(module, 'fizzbuzz'):
        return False, "Function 'fizzbuzz' not found"
    r = module.fizzbuzz(15)
    if r is None:
        return False, "returned None — write the body!"
    if r[0] != "1" or r[2] != "Fizz" or r[4] != "Buzz" or r[14] != "FizzBuzz":
        return False, "fizzbuzz(15) wrong — check 3/5/15 order"
    return True, "All tests passed!"


def check_hard_p02(module):
    if not hasattr(module, 'reverse_string'):
        return False, "Function 'reverse_string' not found"
    if module.reverse_string("hello") is None:
        return False, "returned None — write the body!"
    if module.reverse_string("hello") != "olleh":
        return False, "reverse_string('hello') should be 'olleh'"
    if module.reverse_string("") != "":
        return False, "reverse_string('') should be ''"
    return True, "All tests passed!"


def check_hard_p03(module):
    if not hasattr(module, 'is_prime'):
        return False, "Function 'is_prime' not found"
    if module.is_prime(7) is None:
        return False, "returned None — write the body!"
    cases = [(2, True), (7, True), (1, False), (4, False), (13, True)]
    for n, exp in cases:
        if module.is_prime(n) != exp:
            return False, f"is_prime({n}) should be {exp}"
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
        print("  LESSON 01 — AUTO-CHECK ALL")
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
