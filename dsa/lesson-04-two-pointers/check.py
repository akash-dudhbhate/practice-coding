"""
Auto-Check System — Lesson 04 (Two Pointers)
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
    if not hasattr(module, 'reverse_in_place'):
        return False, "Function 'reverse_in_place' not found"
    a = [1, 2, 3, 4]
    if module.reverse_in_place(a) != [4, 3, 2, 1] or a != [4, 3, 2, 1]:
        return False, "reverse_in_place([1,2,3,4]) should mutate to [4,3,2,1] and return it"
    b = [1, 2, 3]
    module.reverse_in_place(b)
    if b != [3, 2, 1]:
        return False, "reverse_in_place([1,2,3]) should mutate to [3,2,1]"
    if module.reverse_in_place([]) != []:
        return False, "reverse_in_place([]) should be []"
    return True, "All tests passed!"


def check_easy_p02(module):
    if not hasattr(module, 'is_palindrome'):
        return False, "Function 'is_palindrome' not found"
    if module.is_palindrome("A man, a plan, a canal: Panama") != True:
        return False, "is_palindrome('A man, a plan, a canal: Panama') should be True"
    if module.is_palindrome("race a car") != False:
        return False, "is_palindrome('race a car') should be False"
    if module.is_palindrome(" ") != True:
        return False, "is_palindrome(' ') should be True"
    if module.is_palindrome("0P") != False:
        return False, "is_palindrome('0P') should be False"
    return True, "All tests passed!"


def check_easy_p03(module):
    if not hasattr(module, 'pair_sum_sorted'):
        return False, "Function 'pair_sum_sorted' not found"
    if module.pair_sum_sorted([2, 7, 11, 15], 9) != [0, 1]:
        return False, "pair_sum_sorted([2,7,11,15], 9) should be [0,1]"
    if module.pair_sum_sorted([1, 2, 4, 7, 11], 9) != [1, 3]:
        return False, "pair_sum_sorted([1,2,4,7,11], 9) should be [1,3]"
    if module.pair_sum_sorted([1, 3, 5], 10) != []:
        return False, "pair_sum_sorted([1,3,5], 10) should be []"
    return True, "All tests passed!"


def check_medium_p01(module):
    if not hasattr(module, 'remove_duplicates'):
        return False, "Function 'remove_duplicates' not found"
    a = [1, 1, 2]
    if module.remove_duplicates(a) != 2 or a[:2] != [1, 2]:
        return False, "remove_duplicates([1,1,2]) -> k=2, prefix [1,2]"
    b = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    if module.remove_duplicates(b) != 5 or b[:5] != [0, 1, 2, 3, 4]:
        return False, "remove_duplicates([0,0,1,1,1,2,2,3,3,4]) -> k=5, prefix [0,1,2,3,4]"
    if module.remove_duplicates([]) != 0:
        return False, "remove_duplicates([]) should return 0"
    c = [1, 2, 3]
    if module.remove_duplicates(c) != 3 or c[:3] != [1, 2, 3]:
        return False, "remove_duplicates([1,2,3]) -> k=3"
    return True, "All tests passed!"


def check_medium_p02(module):
    if not hasattr(module, 'max_area'):
        return False, "Function 'max_area' not found"
    if module.max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]) != 49:
        return False, "max_area([1,8,6,2,5,4,8,3,7]) should be 49"
    if module.max_area([1, 1]) != 1:
        return False, "max_area([1,1]) should be 1"
    if module.max_area([4, 3, 2, 1, 4]) != 16:
        return False, "max_area([4,3,2,1,4]) should be 16"
    return True, "All tests passed!"


def check_medium_p03(module):
    if not hasattr(module, 'three_sum'):
        return False, "Function 'three_sum' not found"
    if module.three_sum([-1, 0, 1, 2, -1, -4]) != [[-1, -1, 2], [-1, 0, 1]]:
        return False, "three_sum([-1,0,1,2,-1,-4]) should be [[-1,-1,2],[-1,0,1]]"
    if module.three_sum([0, 1, 1]) != []:
        return False, "three_sum([0,1,1]) should be []"
    if module.three_sum([0, 0, 0]) != [[0, 0, 0]]:
        return False, "three_sum([0,0,0]) should be [[0,0,0]]"
    if module.three_sum([0, 0, 0, 0]) != [[0, 0, 0]]:
        return False, "three_sum([0,0,0,0]) should be [[0,0,0]] (no dupes)"
    return True, "All tests passed!"


def check_hard_p01(module):
    if not hasattr(module, 'trap'):
        return False, "Function 'trap' not found"
    if module.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) != 6:
        return False, "trap([0,1,0,2,1,0,1,3,2,1,2,1]) should be 6"
    if module.trap([4, 2, 0, 3, 2, 5]) != 9:
        return False, "trap([4,2,0,3,2,5]) should be 9"
    if module.trap([]) != 0:
        return False, "trap([]) should be 0"
    if module.trap([2, 0, 2]) != 2:
        return False, "trap([2,0,2]) should be 2"
    return True, "All tests passed!"


def check_hard_p02(module):
    if not hasattr(module, 'merge_sorted'):
        return False, "Function 'merge_sorted' not found"
    a = [1, 2, 3, 0, 0, 0]
    module.merge_sorted(a, 3, [2, 5, 6], 3)
    if a != [1, 2, 2, 3, 5, 6]:
        return False, "merge [1,2,3]+[2,5,6] should give [1,2,2,3,5,6]"
    b = [1]
    module.merge_sorted(b, 1, [], 0)
    if b != [1]:
        return False, "merge [1]+[] should give [1]"
    c = [0]
    module.merge_sorted(c, 0, [1], 1)
    if c != [1]:
        return False, "merge []+[1] should give [1]"
    d = [4, 5, 6, 0, 0, 0]
    module.merge_sorted(d, 3, [1, 2, 3], 3)
    if d != [1, 2, 3, 4, 5, 6]:
        return False, "merge [4,5,6]+[1,2,3] should give [1,2,3,4,5,6]"
    return True, "All tests passed!"


def check_hard_p03(module):
    if not hasattr(module, 'four_sum'):
        return False, "Function 'four_sum' not found"
    res = module.four_sum([1, 0, -1, 0, -2, 2], 0)
    if res != [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]:
        return False, "four_sum([1,0,-1,0,-2,2],0) should be [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]"
    if module.four_sum([2, 2, 2, 2, 2], 8) != [[2, 2, 2, 2]]:
        return False, "four_sum([2,2,2,2,2],8) should be [[2,2,2,2]]"
    if module.four_sum([], 0) != []:
        return False, "four_sum([],0) should be []"
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
        print("  LESSON 04 — SOLUTION CHECK (all 9 must pass)")
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
        print("  LESSON 04 — AUTO-CHECK ALL")
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
