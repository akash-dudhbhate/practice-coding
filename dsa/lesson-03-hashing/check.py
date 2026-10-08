"""
Auto-Check System — Lesson 03 (Hashing: Dict & Set Patterns)
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
    if not hasattr(module, 'count_frequencies'):
        return False, "Function 'count_frequencies' not found"
    if module.count_frequencies(["a", "b", "a", "c", "b", "a"]) != {"a": 3, "b": 2, "c": 1}:
        return False, 'count_frequencies(["a","b","a","c","b","a"]) should be {"a":3,"b":2,"c":1}'
    if module.count_frequencies([7, 7, 7]) != {7: 3}:
        return False, "count_frequencies([7,7,7]) should be {7:3}"
    if module.count_frequencies([]) != {}:
        return False, "count_frequencies([]) should be {}"
    return True, "All tests passed!"


def check_easy_p02(module):
    if not hasattr(module, 'find_duplicates'):
        return False, "Function 'find_duplicates' not found"
    if module.find_duplicates([4, 3, 2, 4, 3, 5]) != [3, 4]:
        return False, "find_duplicates([4,3,2,4,3,5]) should be [3,4]"
    if module.find_duplicates([1, 2, 3]) != []:
        return False, "find_duplicates([1,2,3]) should be []"
    if module.find_duplicates([5, 5, 5, 5]) != [5]:
        return False, "find_duplicates([5,5,5,5]) should be [5]"
    return True, "All tests passed!"


def check_easy_p03(module):
    if not hasattr(module, 'first_unique_char'):
        return False, "Function 'first_unique_char' not found"
    if module.first_unique_char("leetcode") != 0:
        return False, "first_unique_char('leetcode') should be 0"
    if module.first_unique_char("loveleetcode") != 2:
        return False, "first_unique_char('loveleetcode') should be 2"
    if module.first_unique_char("aabb") != -1:
        return False, "first_unique_char('aabb') should be -1"
    if module.first_unique_char("") != -1:
        return False, "first_unique_char('') should be -1"
    return True, "All tests passed!"


def check_medium_p01(module):
    if not hasattr(module, 'two_sum'):
        return False, "Function 'two_sum' not found"
    if module.two_sum([2, 7, 11, 15], 9) != [0, 1]:
        return False, "two_sum([2,7,11,15], 9) should be [0,1]"
    if module.two_sum([3, 2, 4], 6) != [1, 2]:
        return False, "two_sum([3,2,4], 6) should be [1,2]"
    if module.two_sum([3, 3], 6) != [0, 1]:
        return False, "two_sum([3,3], 6) should be [0,1]"
    if module.two_sum([1, 5, 9], 20) != []:
        return False, "two_sum([1,5,9], 20) should be []"
    return True, "All tests passed!"


def check_medium_p02(module):
    if not hasattr(module, 'group_anagrams'):
        return False, "Function 'group_anagrams' not found"
    res = module.group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    if sorted(map(sorted, res)) != sorted([["ate", "eat", "tea"], ["bat"], ["nat", "tan"]]):
        return False, "group_anagrams should group [eat,tea,ate], [tan,nat], [bat]"
    if sorted(map(sorted, module.group_anagrams(["a"]))) != [["a"]]:
        return False, "group_anagrams(['a']) should be [['a']]"
    if module.group_anagrams([]) != []:
        return False, "group_anagrams([]) should be []"
    return True, "All tests passed!"


def check_medium_p03(module):
    if not hasattr(module, 'intersection'):
        return False, "Function 'intersection' not found"
    if module.intersection([1, 2, 2, 1], [2, 2]) != [2]:
        return False, "intersection([1,2,2,1],[2,2]) should be [2]"
    if module.intersection([4, 9, 5], [9, 4, 9, 8, 4]) != [4, 9]:
        return False, "intersection([4,9,5],[9,4,9,8,4]) should be [4,9]"
    if module.intersection([1, 2], [3, 4]) != []:
        return False, "intersection([1,2],[3,4]) should be []"
    return True, "All tests passed!"


def check_hard_p01(module):
    if not hasattr(module, 'longest_consecutive'):
        return False, "Function 'longest_consecutive' not found"
    if module.longest_consecutive([100, 4, 200, 1, 3, 2]) != 4:
        return False, "longest_consecutive([100,4,200,1,3,2]) should be 4"
    if module.longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) != 9:
        return False, "longest_consecutive([0,3,7,2,5,8,4,6,0,1]) should be 9"
    if module.longest_consecutive([]) != 0:
        return False, "longest_consecutive([]) should be 0"
    if module.longest_consecutive([1, 2, 0, 1]) != 3:
        return False, "longest_consecutive([1,2,0,1]) should be 3"
    return True, "All tests passed!"


def check_hard_p02(module):
    if not hasattr(module, 'subarray_sum'):
        return False, "Function 'subarray_sum' not found"
    if module.subarray_sum([1, 1, 1], 2) != 2:
        return False, "subarray_sum([1,1,1], 2) should be 2"
    if module.subarray_sum([1, 2, 3], 3) != 2:
        return False, "subarray_sum([1,2,3], 3) should be 2"
    if module.subarray_sum([1, -1, 0], 0) != 3:
        return False, "subarray_sum([1,-1,0], 0) should be 3"
    if module.subarray_sum([0, 0, 0], 0) != 6:
        return False, "subarray_sum([0,0,0], 0) should be 6"
    return True, "All tests passed!"


def check_hard_p03(module):
    if not hasattr(module, 'LRUCache'):
        return False, "Class 'LRUCache' not found"
    c = module.LRUCache(2)
    c.put(1, 1)
    c.put(2, 2)
    if c.get(1) != 1:
        return False, "get(1) should be 1"
    c.put(3, 3)                     # evicts 2
    if c.get(2) != -1:
        return False, "get(2) should be -1 (evicted)"
    c.put(4, 4)                     # evicts 1
    if c.get(1) != -1:
        return False, "get(1) should be -1 (evicted)"
    if c.get(3) != 3:
        return False, "get(3) should be 3"
    if c.get(4) != 4:
        return False, "get(4) should be 4"
    c2 = module.LRUCache(1)
    c2.put(1, 1)
    c2.put(1, 2)                    # update existing key
    if c2.get(1) != 2:
        return False, "get(1) should be 2 after update"
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


def _run_one(level_dir, check_id, filepath):
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
        print("  LESSON 03 — SOLUTION CHECK (all 9 must pass)")
        print("=" * 60)
        passed = 0
        for check_id in CHECKS:
            level, num = check_id.split("/")
            filepath = _find_solution(level_dir, level, num)
            if _run_one(level_dir, check_id, filepath):
                passed += 1
        print(f"  {passed}/9 solutions pass")
        print("=" * 60)
        return

    if target == "all":
        print("=" * 60)
        print("  LESSON 03 — AUTO-CHECK ALL")
        print("=" * 60)
        for check_id in CHECKS:
            level, num = check_id.split("/")
            filepath = _find_file(level_dir, level, num)
            _run_one(level_dir, check_id, filepath)
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
