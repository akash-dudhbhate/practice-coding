"""
Auto-Check System — Lesson 10 (Sorting)
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
    if not hasattr(module, 'insertion_sort'):
        return False, "Function 'insertion_sort' not found"
    a = [5, 2, 4, 1, 3]
    if module.insertion_sort(a) != [1, 2, 3, 4, 5] or a != [1, 2, 3, 4, 5]:
        return False, "insertion_sort([5,2,4,1,3]) should mutate to [1,2,3,4,5] and return it"
    if module.insertion_sort([]) != []:
        return False, "insertion_sort([]) should be []"
    if module.insertion_sort([1]) != [1]:
        return False, "insertion_sort([1]) should be [1]"
    if module.insertion_sort([1, 2, 3]) != [1, 2, 3]:
        return False, "insertion_sort([1,2,3]) should stay [1,2,3]"
    if module.insertion_sort([3, -1, 0]) != [-1, 0, 3]:
        return False, "insertion_sort([3,-1,0]) should be [-1,0,3]"
    return True, "All tests passed!"


def check_easy_p02(module):
    if not hasattr(module, 'sort_by_length'):
        return False, "Function 'sort_by_length' not found"
    if module.sort_by_length(["banana", "kiwi", "apple", "fig", "cherry"]) != \
            ["fig", "kiwi", "apple", "banana", "cherry"]:
        return False, ("sort_by_length(['banana','kiwi','apple','fig','cherry']) should be "
                       "['fig','kiwi','apple','banana','cherry']")
    if module.sort_by_length(["bb", "aa", "c"]) != ["c", "aa", "bb"]:
        return False, "sort_by_length(['bb','aa','c']) should be ['c','aa','bb']"
    if module.sort_by_length([]) != []:
        return False, "sort_by_length([]) should be []"
    if module.sort_by_length(["same", "size"]) != ["same", "size"]:
        return False, "sort_by_length(['same','size']) should be ['same','size'] (alpha tiebreak)"
    return True, "All tests passed!"


def check_easy_p03(module):
    if not hasattr(module, 'merge_two_sorted'):
        return False, "Function 'merge_two_sorted' not found"
    if module.merge_two_sorted([1, 3, 5], [2, 4, 6]) != [1, 2, 3, 4, 5, 6]:
        return False, "merge_two_sorted([1,3,5],[2,4,6]) should be [1,2,3,4,5,6]"
    if module.merge_two_sorted([], [1]) != [1]:
        return False, "merge_two_sorted([],[1]) should be [1]"
    if module.merge_two_sorted([1, 2], []) != [1, 2]:
        return False, "merge_two_sorted([1,2],[]) should be [1,2]"
    if module.merge_two_sorted([1, 4], [2, 3]) != [1, 2, 3, 4]:
        return False, "merge_two_sorted([1,4],[2,3]) should be [1,2,3,4]"
    if module.merge_two_sorted([1, 1], [1]) != [1, 1, 1]:
        return False, "merge_two_sorted([1,1],[1]) should be [1,1,1]"
    return True, "All tests passed!"


def check_medium_p01(module):
    if not hasattr(module, 'merge_sort'):
        return False, "Function 'merge_sort' not found"
    if module.merge_sort([5, 2, 4, 1, 3]) != [1, 2, 3, 4, 5]:
        return False, "merge_sort([5,2,4,1,3]) should be [1,2,3,4,5]"
    if module.merge_sort([]) != []:
        return False, "merge_sort([]) should be []"
    if module.merge_sort([1]) != [1]:
        return False, "merge_sort([1]) should be [1]"
    if module.merge_sort([3, -1, 0, -7]) != [-7, -1, 0, 3]:
        return False, "merge_sort([3,-1,0,-7]) should be [-7,-1,0,3]"
    if module.merge_sort([2, 1]) != [1, 2]:
        return False, "merge_sort([2,1]) should be [1,2]"
    return True, "All tests passed!"


def _check_partition(arr_after, lo, hi, p, pivot_val):
    """Verify index p is a valid partition position."""
    if not (lo <= p <= hi):
        return False
    if arr_after[p] != pivot_val:
        return False
    for i in range(lo, p):
        if arr_after[i] > pivot_val:
            return False
    for i in range(p + 1, hi + 1):
        if arr_after[i] < pivot_val:
            return False
    return True


def check_medium_p02(module):
    if not hasattr(module, 'lomuto_partition'):
        return False, "Function 'lomuto_partition' not found"
    a = [4, 1, 3, 9, 7]
    p = module.lomuto_partition(a, 0, 4)
    if not _check_partition(a, 0, 4, p, 7):
        return False, ("lomuto_partition([4,1,3,9,7], 0, 4): pivot 7 must end at an index "
                       "with all-left <= 7 <= all-right")
    b = [3, 1, 2]
    p = module.lomuto_partition(b, 0, 2)
    if not _check_partition(b, 0, 2, p, 2):
        return False, "lomuto_partition([3,1,2], 0, 2): pivot 2 must end in sorted position"
    c = [5]
    p = module.lomuto_partition(c, 0, 0)
    if p != 0 or c != [5]:
        return False, "lomuto_partition([5], 0, 0) should return 0"
    d = [2, 8, 7, 1]
    p = module.lomuto_partition(d, 0, 3)
    if not _check_partition(d, 0, 3, p, 1):
        return False, "lomuto_partition([2,8,7,1], 0, 3): pivot 1 should land at index 0"
    e = [9, 7, 5, 3, 1, 8, 4, 6, 2]
    p = module.lomuto_partition(e, 2, 7)
    if not _check_partition(e, 2, 7, p, 6):
        return False, "lomuto_partition on subrange [2,7] with pivot 6 failed"
    return True, "All tests passed!"


def check_medium_p03(module):
    if not hasattr(module, 'sort_students'):
        return False, "Function 'sort_students' not found"
    got = module.sort_students([("bob", 75), ("amy", 90), ("cal", 90), ("dan", 60)])
    if got != [("amy", 90), ("cal", 90), ("bob", 75), ("dan", 60)]:
        return False, ("sort_students should sort by score DESC then name ASC: "
                       "[('amy',90),('cal',90),('bob',75),('dan',60)]")
    if module.sort_students([]) != []:
        return False, "sort_students([]) should be []"
    got = module.sort_students([("zed", 50), ("ann", 50)])
    if got != [("ann", 50), ("zed", 50)]:
        return False, "equal scores must sort by name ascending"
    got = module.sort_students([("moe", 70), ("leo", 80), ("kim", 80), ("abe", 60)])
    if got != [("kim", 80), ("leo", 80), ("moe", 70), ("abe", 60)]:
        return False, "sort_students([(moe,70),(leo,80),(kim,80),(abe,60)]) wrong"
    return True, "All tests passed!"


def check_hard_p01(module):
    if not hasattr(module, 'counting_sort'):
        return False, "Function 'counting_sort' not found"
    if module.counting_sort([4, 2, 2, 8, 3, 3, 1]) != [1, 2, 2, 3, 3, 4, 8]:
        return False, "counting_sort([4,2,2,8,3,3,1]) should be [1,2,2,3,3,4,8]"
    if module.counting_sort([-3, 1, -1, 2]) != [-3, -1, 1, 2]:
        return False, "counting_sort([-3,1,-1,2]) should be [-3,-1,1,2] (offset for negatives!)"
    if module.counting_sort([]) != []:
        return False, "counting_sort([]) should be []"
    if module.counting_sort([5]) != [5]:
        return False, "counting_sort([5]) should be [5]"
    if module.counting_sort([-5, -5, -5]) != [-5, -5, -5]:
        return False, "counting_sort([-5,-5,-5]) should be [-5,-5,-5]"
    return True, "All tests passed!"


def check_hard_p02(module):
    if not hasattr(module, 'count_inversions'):
        return False, "Function 'count_inversions' not found"
    if module.count_inversions([2, 4, 1, 3, 5]) != 3:
        return False, "count_inversions([2,4,1,3,5]) should be 3"
    if module.count_inversions([1, 2, 3]) != 0:
        return False, "count_inversions([1,2,3]) should be 0"
    if module.count_inversions([3, 2, 1]) != 3:
        return False, "count_inversions([3,2,1]) should be 3"
    if module.count_inversions([]) != 0:
        return False, "count_inversions([]) should be 0"
    if module.count_inversions([5, 4, 3, 2, 1]) != 10:
        return False, "count_inversions([5,4,3,2,1]) should be 10"
    if module.count_inversions([1, 1, 1]) != 0:
        return False, "count_inversions([1,1,1]) should be 0 (equal is not inverted)"
    return True, "All tests passed!"


def check_hard_p03(module):
    if not hasattr(module, 'sort_nearly_sorted'):
        return False, "Function 'sort_nearly_sorted' not found"
    if module.sort_nearly_sorted([6, 5, 3, 2, 8, 10, 9], 3) != [2, 3, 5, 6, 8, 9, 10]:
        return False, "sort_nearly_sorted([6,5,3,2,8,10,9], 3) should be [2,3,5,6,8,9,10]"
    if module.sort_nearly_sorted([2, 1, 3], 1) != [1, 2, 3]:
        return False, "sort_nearly_sorted([2,1,3], 1) should be [1,2,3]"
    if module.sort_nearly_sorted([], 3) != []:
        return False, "sort_nearly_sorted([], 3) should be []"
    if module.sort_nearly_sorted([1], 1) != [1]:
        return False, "sort_nearly_sorted([1], 1) should be [1]"
    if module.sort_nearly_sorted([10, 9, 8, 7, 6], 4) != [6, 7, 8, 9, 10]:
        return False, "sort_nearly_sorted([10,9,8,7,6], 4) should be [6,7,8,9,10]"
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
        print("  LESSON 10 — SOLUTION CHECK (all 9 must pass)")
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
        print("  LESSON 10 — AUTO-CHECK ALL")
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
