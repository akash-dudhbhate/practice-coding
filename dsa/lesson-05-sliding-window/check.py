"""
Auto-Check System — Lesson 05 (Sliding Window)
=========================================================
Usage:
    python3 check.py easy/p01        # check one of YOUR files
    python3 check.py all             # check all 9 of YOUR files
    python3 check.py solutions       # run all 9 reference solutions
    python3 check.py verify          # solutions must pass AND stubs must fail
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


def _find_file(level_dir, level, num, solutions=False):
    num_clean = num.lstrip("p")
    if solutions:
        filepath = os.path.join(level_dir, level, "solutions", f"p{num_clean}-solution.py")
        if os.path.exists(filepath):
            return filepath
        pattern = os.path.join(level_dir, level, "solutions", f"p{num_clean}-*.py")
        matches = glob.glob(pattern)
        return matches[0] if matches else filepath
    filepath = os.path.join(level_dir, level, f"p{num_clean}-solve.py")
    if not os.path.exists(filepath):
        pattern = os.path.join(level_dir, level, f"p{num_clean}-*.py")
        matches = [f for f in glob.glob(pattern) if "solutions" not in f]
        if matches:
            filepath = matches[0]
    return filepath


def _is_stub(filepath):
    """True if the learner file still has the TODO marker (unwritten)."""
    try:
        with open(filepath) as f:
            return "# TODO" in f.read()
    except OSError:
        return False


def check_easy_p01(module):
    if not hasattr(module, 'max_sum_k'):
        return False, "Function 'max_sum_k' not found"
    if module.max_sum_k([2, 1, 5, 1, 3, 2], 3) != 9:
        return False, "max_sum_k([2,1,5,1,3,2], 3) should be 9"
    if module.max_sum_k([1, 2, 3, 4, 5], 2) != 9:
        return False, "max_sum_k([1,2,3,4,5], 2) should be 9"
    if module.max_sum_k([5], 1) != 5:
        return False, "max_sum_k([5], 1) should be 5"
    if module.max_sum_k([-1, -2, -3], 2) != -3:
        return False, "max_sum_k([-1,-2,-3], 2) should be -3"
    return True, "All tests passed!"


def check_easy_p02(module):
    if not hasattr(module, 'window_averages'):
        return False, "Function 'window_averages' not found"
    if module.window_averages([1, 2, 3, 4], 2) != [1.5, 2.5, 3.5]:
        return False, "window_averages([1,2,3,4], 2) should be [1.5, 2.5, 3.5]"
    if module.window_averages([5, 5, 5], 3) != [5.0]:
        return False, "window_averages([5,5,5], 3) should be [5.0]"
    if module.window_averages([1, 3, 5, 7, 9], 5) != [5.0]:
        return False, "window_averages([1,3,5,7,9], 5) should be [5.0]"
    if module.window_averages([1, 2], 3) != []:
        return False, "window_averages([1,2], 3) should be []"
    return True, "All tests passed!"


def check_easy_p03(module):
    if not hasattr(module, 'count_windows_at_least'):
        return False, "Function 'count_windows_at_least' not found"
    if module.count_windows_at_least([1, 4, 2, 10, 2, 3, 1, 0, 20], 4, 15) != 5:
        return False, "count_windows_at_least(...) should be 5"
    if module.count_windows_at_least([1, 1, 1], 2, 3) != 0:
        return False, "count_windows_at_least([1,1,1], 2, 3) should be 0"
    if module.count_windows_at_least([3, 3, 3], 2, 5) != 2:
        return False, "count_windows_at_least([3,3,3], 2, 5) should be 2"
    if module.count_windows_at_least([1, 2], 3, 0) != 0:
        return False, "count_windows_at_least([1,2], 3, 0) should be 0"
    return True, "All tests passed!"


def check_medium_p01(module):
    if not hasattr(module, 'length_of_longest_substring'):
        return False, "Function 'length_of_longest_substring' not found"
    if module.length_of_longest_substring("abcabcbb") != 3:
        return False, "length_of_longest_substring('abcabcbb') should be 3"
    if module.length_of_longest_substring("bbbbb") != 1:
        return False, "length_of_longest_substring('bbbbb') should be 1"
    if module.length_of_longest_substring("pwwkew") != 3:
        return False, "length_of_longest_substring('pwwkew') should be 3"
    if module.length_of_longest_substring("") != 0:
        return False, "length_of_longest_substring('') should be 0"
    if module.length_of_longest_substring("dvdf") != 3:
        return False, "length_of_longest_substring('dvdf') should be 3"
    if module.length_of_longest_substring("abba") != 2:
        return False, "length_of_longest_substring('abba') should be 2"
    return True, "All tests passed!"


def check_medium_p02(module):
    if not hasattr(module, 'longest_ones'):
        return False, "Function 'longest_ones' not found"
    if module.longest_ones([1,1,1,0,0,0,1,1,1,1,0], 2) != 6:
        return False, "longest_ones([1,1,1,0,0,0,1,1,1,1,0], 2) should be 6"
    if module.longest_ones([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3) != 10:
        return False, "longest_ones(...) should be 10"
    if module.longest_ones([1,1,1], 0) != 3:
        return False, "longest_ones([1,1,1], 0) should be 3"
    if module.longest_ones([0,0,0], 1) != 1:
        return False, "longest_ones([0,0,0], 1) should be 1"
    if module.longest_ones([1,0,1,0,1], 1) != 3:
        return False, "longest_ones([1,0,1,0,1], 1) should be 3"
    return True, "All tests passed!"


def check_medium_p03(module):
    if not hasattr(module, 'min_subarray_len'):
        return False, "Function 'min_subarray_len' not found"
    if module.min_subarray_len(7, [2, 3, 1, 2, 4, 3]) != 2:
        return False, "min_subarray_len(7, [2,3,1,2,4,3]) should be 2"
    if module.min_subarray_len(4, [1, 4, 4]) != 1:
        return False, "min_subarray_len(4, [1,4,4]) should be 1"
    if module.min_subarray_len(11, [1, 1, 1, 1, 1, 1, 1, 1]) != 0:
        return False, "min_subarray_len(11, [1x8]) should be 0"
    if module.min_subarray_len(15, [1, 2, 3, 4, 5]) != 5:
        return False, "min_subarray_len(15, [1,2,3,4,5]) should be 5"
    return True, "All tests passed!"


def check_hard_p01(module):
    if not hasattr(module, 'min_window'):
        return False, "Function 'min_window' not found"
    if module.min_window("ADOBECODEBANC", "ABC") != "BANC":
        return False, "min_window('ADOBECODEBANC','ABC') should be 'BANC'"
    if module.min_window("a", "a") != "a":
        return False, "min_window('a','a') should be 'a'"
    if module.min_window("a", "aa") != "":
        return False, "min_window('a','aa') should be ''"
    if module.min_window("ab", "b") != "b":
        return False, "min_window('ab','b') should be 'b'"
    if module.min_window("aa", "aa") != "aa":
        return False, "min_window('aa','aa') should be 'aa'"
    if module.min_window("bba", "ab") != "ba":
        return False, "min_window('bba','ab') should be 'ba'"
    return True, "All tests passed!"


def check_hard_p02(module):
    if not hasattr(module, 'length_of_longest_k_distinct'):
        return False, "Function 'length_of_longest_k_distinct' not found"
    if module.length_of_longest_k_distinct("eceba", 2) != 3:
        return False, "length_of_longest_k_distinct('eceba', 2) should be 3"
    if module.length_of_longest_k_distinct("aa", 1) != 2:
        return False, "length_of_longest_k_distinct('aa', 1) should be 2"
    if module.length_of_longest_k_distinct("abcadcacacaca", 3) != 11:
        return False, "length_of_longest_k_distinct('abcadcacacaca', 3) should be 11"
    if module.length_of_longest_k_distinct("aabbcc", 2) != 4:
        return False, "length_of_longest_k_distinct('aabbcc', 2) should be 4"
    if module.length_of_longest_k_distinct("", 2) != 0:
        return False, "length_of_longest_k_distinct('', 2) should be 0"
    if module.length_of_longest_k_distinct("abc", 0) != 0:
        return False, "length_of_longest_k_distinct('abc', 0) should be 0"
    return True, "All tests passed!"


def check_hard_p03(module):
    if not hasattr(module, 'total_fruit'):
        return False, "Function 'total_fruit' not found"
    if module.total_fruit([1, 2, 1]) != 3:
        return False, "total_fruit([1,2,1]) should be 3"
    if module.total_fruit([0, 1, 2, 2]) != 3:
        return False, "total_fruit([0,1,2,2]) should be 3"
    if module.total_fruit([1, 2, 3, 2, 2]) != 4:
        return False, "total_fruit([1,2,3,2,2]) should be 4"
    if module.total_fruit([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]) != 5:
        return False, "total_fruit([3,3,3,1,2,1,1,2,3,3,4]) should be 5"
    if module.total_fruit([1, 1, 1, 1]) != 4:
        return False, "total_fruit([1,1,1,1]) should be 4"
    if module.total_fruit([]) != 0:
        return False, "total_fruit([]) should be 0"
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


def _run_one(level_dir, check_id, solutions):
    level, num = check_id.split("/")
    filepath = _find_file(level_dir, level, num, solutions=solutions)
    if not os.path.exists(filepath):
        return check_id, "MISSING", "file not found", filepath
    module = load_module(filepath)
    passed, msg = CHECKS[check_id](module)
    return check_id, ("PASS" if passed else "FAIL"), msg, filepath


def _run_batch(level_dir, solutions, title):
    print("=" * 60)
    print(f"  {title}")
    print("=" * 60)
    n_pass = 0
    for check_id in CHECKS:
        try:
            cid, status, msg, fp = _run_one(level_dir, check_id, solutions)
        except Exception as e:
            cid, status, msg, fp = check_id, "ERROR", str(e), ""
            if "NoneType" in msg:
                msg = "a function returned None — write the body!"
        if status == "PASS":
            n_pass += 1
        if status == "FAIL" and not solutions and fp and _is_stub(fp):
            print(f"  {cid}: STUB — TODO still present, write your code first")
        else:
            print(f"  {cid}: {status} — {msg}")
    print("-" * 60)
    print(f"  {n_pass}/{len(CHECKS)} passed")
    print("=" * 60)
    return n_pass


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    target = sys.argv[1]
    level_dir = os.path.dirname(os.path.abspath(__file__))

    if target == "all":
        _run_batch(level_dir, solutions=False, title="LESSON 05 — CHECK YOUR FILES")
        return

    if target == "solutions":
        n = _run_batch(level_dir, solutions=True, title="LESSON 05 — REFERENCE SOLUTIONS")
        sys.exit(0 if n == len(CHECKS) else 1)

    if target == "verify":
        n_sol = _run_batch(level_dir, solutions=True, title="LESSON 05 — SOLUTIONS (must pass)")
        print()
        # stubs must NOT pass — they should be rejected
        n_stub = 0
        for check_id in CHECKS:
            level, num = check_id.split("/")
            fp = _find_file(level_dir, level, num)
            if _is_stub(fp):
                n_stub += 1
                print(f"  {check_id}: STUB correctly rejected (TODO present)")
            else:
                print(f"  {check_id}: WARNING — stub file has no TODO marker")
        print("-" * 60)
        print(f"  solutions: {n_sol}/{len(CHECKS)} pass · stubs rejected: {n_stub}/{len(CHECKS)}")
        print("=" * 60)
        sys.exit(0 if (n_sol == len(CHECKS) and n_stub == len(CHECKS)) else 1)

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
        print(f"STUB — {filepath} still has the TODO marker. Write your code first!")
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
