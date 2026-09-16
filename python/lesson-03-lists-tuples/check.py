"""
Auto-Check System — Lesson 03 (Lists & Tuples)
===============================================
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
    if not hasattr(module, 'sum_list'):
        return False, "Function 'sum_list' not found"
    if module.sum_list([1, 2, 3]) != 6:
        return False, "sum_list([1,2,3]) should be 6"
    if module.sum_list([]) != 0:
        return False, "sum_list([]) should be 0"
    if module.sum_list([-1, 1]) != 0:
        return False, "sum_list([-1,1]) should be 0"
    return True, "All tests passed!"


def check_easy_p02(module):
    if not hasattr(module, 'reverse_list'):
        return False, "Function 'reverse_list' not found"
    if module.reverse_list([1, 2, 3]) != [3, 2, 1]:
        return False, "reverse_list([1,2,3]) should be [3,2,1]"
    if module.reverse_list([]) != []:
        return False, "reverse_list([]) should be []"
    original = [1, 2, 3]
    module.reverse_list(original)
    if original != [1, 2, 3]:
        return False, "reverse_list must NOT mutate the input list"
    return True, "All tests passed!"


def check_easy_p03(module):
    if not hasattr(module, 'contains'):
        return False, "Function 'contains' not found"
    if module.contains([1, 2, 3], 2) != True:
        return False, "contains([1,2,3], 2) should be True"
    if module.contains([1, 2, 3], 5) != False:
        return False, "contains([1,2,3], 5) should be False"
    if module.contains([], 1) != False:
        return False, "contains([], 1) should be False"
    return True, "All tests passed!"


def check_medium_p01(module):
    if not hasattr(module, 'remove_duplicates'):
        return False, "Function 'remove_duplicates' not found"
    if module.remove_duplicates([1, 2, 2, 3, 3, 3]) != [1, 2, 3]:
        return False, "remove_duplicates([1,2,2,3,3,3]) should be [1,2,3]"
    if module.remove_duplicates(["a", "b", "a"]) != ["a", "b"]:
        return False, "remove_duplicates(['a','b','a']) should be ['a','b']"
    if module.remove_duplicates([]) != []:
        return False, "remove_duplicates([]) should be []"
    return True, "All tests passed!"


def check_medium_p02(module):
    if not hasattr(module, 'sort_by_length'):
        return False, "Function 'sort_by_length' not found"
    if module.sort_by_length(["apple", "hi", "cat"]) != ["hi", "cat", "apple"]:
        return False, "sort_by_length(['apple','hi','cat']) should be ['hi','cat','apple']"
    if module.sort_by_length(["same", "four"]) != ["same", "four"]:
        return False, "Equal lengths should keep original order"
    if module.sort_by_length([]) != []:
        return False, "sort_by_length([]) should be []"
    return True, "All tests passed!"


def check_medium_p03(module):
    if not hasattr(module, 'swap_pairs'):
        return False, "Function 'swap_pairs' not found"
    if module.swap_pairs([1, 2, 3, 4, 5]) != [2, 1, 4, 3, 5]:
        return False, "swap_pairs([1,2,3,4,5]) should be [2,1,4,3,5]"
    if module.swap_pairs([1, 2]) != [2, 1]:
        return False, "swap_pairs([1,2]) should be [2,1]"
    if module.swap_pairs([1]) != [1]:
        return False, "swap_pairs([1]) should be [1]"
    if module.swap_pairs([]) != []:
        return False, "swap_pairs([]) should be []"
    return True, "All tests passed!"


def check_hard_p01(module):
    if not hasattr(module, 'flatten'):
        return False, "Function 'flatten' not found"
    if module.flatten([[1, 2], [3], [4, 5]]) != [1, 2, 3, 4, 5]:
        return False, "flatten([[1,2],[3],[4,5]]) should be [1,2,3,4,5]"
    if module.flatten([1, [2], 3]) != [1, 2, 3]:
        return False, "flatten([1,[2],3]) should be [1,2,3]"
    if module.flatten([]) != []:
        return False, "flatten([]) should be []"
    return True, "All tests passed!"


def check_hard_p02(module):
    if not hasattr(module, 'second_largest'):
        return False, "Function 'second_largest' not found"
    if module.second_largest([5, 1, 4, 4, 3]) != 4:
        return False, "second_largest([5,1,4,4,3]) should be 4"
    if module.second_largest([1, 1, 1]) is not None:
        return False, "second_largest([1,1,1]) should be None"
    if module.second_largest([3, 1]) != 1:
        return False, "second_largest([3,1]) should be 1"
    return True, "All tests passed!"


def check_hard_p03(module):
    if not hasattr(module, 'tuple_stats'):
        return False, "Function 'tuple_stats' not found"
    if module.tuple_stats((1, 2, 3)) != (1, 3, 2.0):
        return False, "tuple_stats((1,2,3)) should be (1, 3, 2.0)"
    if module.tuple_stats(()) != (None, None, 0.0):
        return False, "tuple_stats(()) should be (None, None, 0.0)"
    if module.tuple_stats((5,)) != (5, 5, 5.0):
        return False, "tuple_stats((5,)) should be (5, 5, 5.0)"
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
        print("  LESSON 03 — AUTO-CHECK ALL")
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
