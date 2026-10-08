"""
Auto-Check System — DSA Lesson 02 (Arrays & Strings)
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
    filepath = os.path.join(level_dir, level, f"p{num_clean}-solve.py")
    if not os.path.exists(filepath):
        pattern = os.path.join(level_dir, level, f"p{num_clean}-*.py")
        matches = [f for f in glob.glob(pattern) if "solutions" not in f]
        if matches:
            filepath = matches[0]
    return filepath


def _stub_check(filepath):
    """Reject unwritten stubs before running any function checks."""
    with open(filepath, "r") as f:
        content = f.read()
    if "TODO" in content:
        return False, "stub still contains TODO — write your solution!"
    return True, ""


def check_easy_p01(module):
    if not hasattr(module, 'running_sum'):
        return False, "Function 'running_sum' not found"
    if module.running_sum([1, 2, 3, 4]) != [1, 3, 6, 10]:
        return False, "running_sum([1,2,3,4]) should be [1,3,6,10]"
    if module.running_sum([5]) != [5]:
        return False, "running_sum([5]) should be [5]"
    if module.running_sum([]) != []:
        return False, "running_sum([]) should be []"
    if module.running_sum([1, -1, 1, -1]) != [1, 0, 1, 0]:
        return False, "running_sum([1,-1,1,-1]) should be [1,0,1,0]"
    return True, "All tests passed!"


def check_easy_p02(module):
    if not hasattr(module, 'max_min'):
        return False, "Function 'max_min' not found"
    if module.max_min([3, 1, 4, 1, 5]) != (5, 1):
        return False, "max_min([3,1,4,1,5]) should be (5, 1)"
    if module.max_min([7]) != (7, 7):
        return False, "max_min([7]) should be (7, 7)"
    if module.max_min([-2, -9, -4]) != (-2, -9):
        return False, "max_min([-2,-9,-4]) should be (-2, -9)"
    return True, "All tests passed!"


def check_easy_p03(module):
    if not hasattr(module, 'char_freq'):
        return False, "Function 'char_freq' not found"
    if module.char_freq("aab") != {"a": 2, "b": 1}:
        return False, "char_freq('aab') should be {'a': 2, 'b': 1}"
    if module.char_freq("hello") != {"h": 1, "e": 1, "l": 2, "o": 1}:
        return False, "char_freq('hello') should be {'h':1,'e':1,'l':2,'o':1}"
    if module.char_freq("") != {}:
        return False, "char_freq('') should be {}"
    if module.char_freq("Aa") != {"A": 1, "a": 1}:
        return False, "char_freq('Aa') should be {'A':1,'a':1} (case-sensitive)"
    return True, "All tests passed!"


def check_medium_p01(module):
    if not hasattr(module, 'answer_queries'):
        return False, "Function 'answer_queries' not found"
    if module.answer_queries([1, 2, 3, 4, 5], [(0, 2)]) != [6]:
        return False, "answer_queries([1,2,3,4,5],[(0,2)]) should be [6]"
    if module.answer_queries([1, 2, 3, 4, 5], [(0, 2), (1, 4), (2, 2)]) != [6, 14, 3]:
        return False, "answer_queries(...,[(0,2),(1,4),(2,2)]) should be [6,14,3]"
    if module.answer_queries([1, 2, 3, 4, 5], [(0, 4)]) != [15]:
        return False, "answer_queries([1,2,3,4,5],[(0,4)]) should be [15]"
    return True, "All tests passed!"


def check_medium_p02(module):
    if not hasattr(module, 'move_zeros'):
        return False, "Function 'move_zeros' not found"
    a = [0, 1, 0, 3, 12]
    module.move_zeros(a)
    if a != [1, 3, 12, 0, 0]:
        return False, "move_zeros must MUTATE the list to [1,3,12,0,0]"
    b = [0, 0, 1]
    module.move_zeros(b)
    if b != [1, 0, 0]:
        return False, "move_zeros([0,0,1]) should leave [1,0,0]"
    c = [1, 2, 3]
    module.move_zeros(c)
    if c != [1, 2, 3]:
        return False, "move_zeros([1,2,3]) should leave [1,2,3]"
    d = []
    module.move_zeros(d)
    if d != []:
        return False, "move_zeros([]) should leave []"
    return True, "All tests passed!"


def check_medium_p03(module):
    if not hasattr(module, 'product_except_self'):
        return False, "Function 'product_except_self' not found"
    if module.product_except_self([1, 2, 3, 4]) != [24, 12, 8, 6]:
        return False, "product_except_self([1,2,3,4]) should be [24,12,8,6]"
    if module.product_except_self([2, 3, 4]) != [12, 8, 6]:
        return False, "product_except_self([2,3,4]) should be [12,8,6]"
    if module.product_except_self([-1, 1, 0, -3, 3]) != [0, 0, 9, 0, 0]:
        return False, "product_except_self([-1,1,0,-3,3]) should be [0,0,9,0,0]"
    return True, "All tests passed!"


def check_hard_p01(module):
    if not hasattr(module, 'count_subarray_sum'):
        return False, "Function 'count_subarray_sum' not found"
    if module.count_subarray_sum([1, 1, 1], 2) != 2:
        return False, "count_subarray_sum([1,1,1],2) should be 2"
    if module.count_subarray_sum([1, 2, 3], 3) != 2:
        return False, "count_subarray_sum([1,2,3],3) should be 2"
    if module.count_subarray_sum([1, -1, 0], 0) != 3:
        return False, "count_subarray_sum([1,-1,0],0) should be 3"
    if module.count_subarray_sum([1], 1) != 1:
        return False, "count_subarray_sum([1],1) should be 1"
    return True, "All tests passed!"


def check_hard_p02(module):
    if not hasattr(module, 'max_subarray'):
        return False, "Function 'max_subarray' not found"
    if module.max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) != 6:
        return False, "max_subarray([-2,1,-3,4,-1,2,1,-5,4]) should be 6"
    if module.max_subarray([5, 4, -1, 7, 8]) != 23:
        return False, "max_subarray([5,4,-1,7,8]) should be 23"
    if module.max_subarray([-3, -1, -2]) != -1:
        return False, "max_subarray([-3,-1,-2]) should be -1 (all negative)"
    if module.max_subarray([7]) != 7:
        return False, "max_subarray([7]) should be 7"
    return True, "All tests passed!"


def check_hard_p03(module):
    if not hasattr(module, 'encode_with_freq'):
        return False, "Function 'encode_with_freq' not found"
    if module.encode_with_freq("aabca") != "a3b1c1":
        return False, "encode_with_freq('aabca') should be 'a3b1c1'"
    if module.encode_with_freq("zzz") != "z3":
        return False, "encode_with_freq('zzz') should be 'z3'"
    if module.encode_with_freq("ab") != "a1b1":
        return False, "encode_with_freq('ab') should be 'a1b1'"
    if module.encode_with_freq("") != "":
        return False, "encode_with_freq('') should be ''"
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
        print("  DSA LESSON 02 — AUTO-CHECK ALL")
        print("=" * 60)
        for check_id, check_func in CHECKS.items():
            level, num = check_id.split("/")
            filepath = _find_file(level_dir, level, num)
            if not os.path.exists(filepath):
                print(f"  {check_id}: FILE NOT FOUND")
                continue
            ok, msg = _stub_check(filepath)
            if not ok:
                print(f"  {check_id}: FAIL — {msg}")
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

    ok, msg = _stub_check(filepath)
    if not ok:
        print(f"FAIL — {msg}")
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
