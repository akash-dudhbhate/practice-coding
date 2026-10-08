"""
Auto-Check System — Lesson 16 (2D DP & Knapsack)
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
    if not hasattr(module, 'unique_paths'):
        return False, "Function 'unique_paths' not found"
    if module.unique_paths(3, 2) != 3:
        return False, "unique_paths(3, 2) should be 3"
    if module.unique_paths(3, 7) != 28:
        return False, "unique_paths(3, 7) should be 28"
    if module.unique_paths(7, 3) != 28:
        return False, "unique_paths(7, 3) should be 28"
    if module.unique_paths(1, 1) != 1:
        return False, "unique_paths(1, 1) should be 1"
    if module.unique_paths(1, 10) != 1 or module.unique_paths(10, 1) != 1:
        return False, "unique_paths on a line grid should be 1"
    return True, "All tests passed!"


def check_easy_p02(module):
    if not hasattr(module, 'min_path_sum'):
        return False, "Function 'min_path_sum' not found"
    if module.min_path_sum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]) != 7:
        return False, "min_path_sum([[1,3,1],[1,5,1],[4,2,1]]) should be 7"
    if module.min_path_sum([[1, 2, 3], [4, 5, 6]]) != 12:
        return False, "min_path_sum([[1,2,3],[4,5,6]]) should be 12"
    if module.min_path_sum([[7]]) != 7:
        return False, "min_path_sum([[7]]) should be 7"
    if module.min_path_sum([[1, 2], [1, 1]]) != 3:
        return False, "min_path_sum([[1,2],[1,1]]) should be 3"
    return True, "All tests passed!"


def check_easy_p03(module):
    if not hasattr(module, 'unique_paths_with_obstacles'):
        return False, "Function 'unique_paths_with_obstacles' not found"
    if module.unique_paths_with_obstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]) != 2:
        return False, "obstacle grid should give 2"
    if module.unique_paths_with_obstacles([[0, 1], [0, 0]]) != 1:
        return False, "[[0,1],[0,0]] should give 1"
    if module.unique_paths_with_obstacles([[1]]) != 0:
        return False, "blocked start should give 0"
    if module.unique_paths_with_obstacles([[0]]) != 1:
        return False, "single open cell should give 1"
    if module.unique_paths_with_obstacles([[0, 1, 0]]) != 0:
        return False, "wall in row 0 blocks the rest — should be 0"
    if module.unique_paths_with_obstacles([[0, 0], [1, 1], [0, 0]]) != 0:
        return False, "wall row blocks all paths — should be 0"
    return True, "All tests passed!"


def check_medium_p01(module):
    if not hasattr(module, 'knapsack'):
        return False, "Function 'knapsack' not found"
    if module.knapsack([1, 3, 4, 5], [1, 4, 5, 7], 7) != 9:
        return False, "knapsack([1,3,4,5],[1,4,5,7],7) should be 9"
    if module.knapsack([2, 3, 4, 5], [3, 4, 5, 6], 5) != 7:
        return False, "knapsack([2,3,4,5],[3,4,5,6],5) should be 7"
    if module.knapsack([4, 5, 6], [1, 2, 3], 3) != 0:
        return False, "knapsack([4,5,6],[1,2,3],3) should be 0"
    if module.knapsack([1, 2, 3], [6, 10, 12], 5) != 22:
        return False, "knapsack([1,2,3],[6,10,12],5) should be 22"
    if module.knapsack([1], [1], 0) != 0:
        return False, "capacity 0 should give 0"
    if module.knapsack([], [], 10) != 0:
        return False, "no items should give 0"
    return True, "All tests passed!"


def check_medium_p02(module):
    if not hasattr(module, 'longest_common_subsequence'):
        return False, "Function 'longest_common_subsequence' not found"
    if module.longest_common_subsequence("abcde", "ace") != 3:
        return False, "lcs('abcde','ace') should be 3"
    if module.longest_common_subsequence("abc", "abc") != 3:
        return False, "lcs('abc','abc') should be 3"
    if module.longest_common_subsequence("abc", "def") != 0:
        return False, "lcs('abc','def') should be 0"
    if module.longest_common_subsequence("", "abc") != 0:
        return False, "lcs('','abc') should be 0"
    if module.longest_common_subsequence("bsbininm", "jmjkbkjkv") != 1:
        return False, "lcs('bsbininm','jmjkbkjkv') should be 1"
    if module.longest_common_subsequence("abcba", "babcab") != 4:
        return False, "lcs('abcba','babcab') should be 4"
    return True, "All tests passed!"


def check_medium_p03(module):
    if not hasattr(module, 'coin_change_count'):
        return False, "Function 'coin_change_count' not found"
    if module.coin_change_count(5, [1, 2, 5]) != 4:
        return False, "coin_change_count(5, [1,2,5]) should be 4 — if you got 9, you counted permutations (coins must be the OUTER loop)"
    if module.coin_change_count(3, [2]) != 0:
        return False, "coin_change_count(3, [2]) should be 0"
    if module.coin_change_count(10, [10]) != 1:
        return False, "coin_change_count(10, [10]) should be 1"
    if module.coin_change_count(0, [1, 2]) != 1:
        return False, "coin_change_count(0, [1,2]) should be 1"
    if module.coin_change_count(4, [1, 2, 3]) != 4:
        return False, "coin_change_count(4, [1,2,3]) should be 4"
    if module.coin_change_count(7, [2, 3]) != 1:
        return False, "coin_change_count(7, [2,3]) should be 1"
    return True, "All tests passed!"


def check_hard_p01(module):
    if not hasattr(module, 'min_distance'):
        return False, "Function 'min_distance' not found"
    if module.min_distance("horse", "ros") != 3:
        return False, "min_distance('horse','ros') should be 3"
    if module.min_distance("intention", "execution") != 5:
        return False, "min_distance('intention','execution') should be 5"
    if module.min_distance("", "") != 0:
        return False, "min_distance('','') should be 0"
    if module.min_distance("a", "ab") != 1:
        return False, "min_distance('a','ab') should be 1"
    if module.min_distance("abc", "") != 3:
        return False, "min_distance('abc','') should be 3 — borders are delete/insert costs, not 0"
    if module.min_distance("kitten", "sitting") != 3:
        return False, "min_distance('kitten','sitting') should be 3"
    return True, "All tests passed!"


def check_hard_p02(module):
    if not hasattr(module, 'is_match_wildcard'):
        return False, "Function 'is_match_wildcard' not found"
    if module.is_match_wildcard("aa", "a") is not False:
        return False, "is_match_wildcard('aa','a') should be False"
    if module.is_match_wildcard("aa", "*") is not True:
        return False, "is_match_wildcard('aa','*') should be True"
    if module.is_match_wildcard("cb", "?a") is not False:
        return False, "is_match_wildcard('cb','?a') should be False"
    if module.is_match_wildcard("adceb", "*a*b") is not True:
        return False, "is_match_wildcard('adceb','*a*b') should be True"
    if module.is_match_wildcard("acdcb", "a*c?b") is not False:
        return False, "is_match_wildcard('acdcb','a*c?b') should be False"
    if module.is_match_wildcard("", "*") is not True:
        return False, "is_match_wildcard('','*') should be True — '*' matches empty"
    if module.is_match_wildcard("abc", "***") is not True:
        return False, "is_match_wildcard('abc','***') should be True"
    return True, "All tests passed!"


def check_hard_p03(module):
    if not hasattr(module, 'max_coins'):
        return False, "Function 'max_coins' not found"
    if module.max_coins([3, 1, 5, 8]) != 167:
        return False, "max_coins([3,1,5,8]) should be 167"
    if module.max_coins([1, 5]) != 10:
        return False, "max_coins([1,5]) should be 10"
    if module.max_coins([9]) != 9:
        return False, "max_coins([9]) should be 9"
    if module.max_coins([]) != 0:
        return False, "max_coins([]) should be 0"
    if module.max_coins([1, 2, 3]) != 12:
        return False, "max_coins([1,2,3]) should be 12"
    if module.max_coins([7, 9]) != 72:
        return False, "max_coins([7,9]) should be 72"
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
        _run_batch(level_dir, solutions=False, title="LESSON 16 — CHECK YOUR FILES")
        return

    if target == "solutions":
        n = _run_batch(level_dir, solutions=True, title="LESSON 16 — REFERENCE SOLUTIONS")
        sys.exit(0 if n == len(CHECKS) else 1)

    if target == "verify":
        n_sol = _run_batch(level_dir, solutions=True, title="LESSON 16 — SOLUTIONS (must pass)")
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
