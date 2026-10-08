"""
Auto-Check System — Lesson 15 (1D Dynamic Programming)
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
    if not hasattr(module, 'fib'):
        return False, "Function 'fib' not found"
    if module.fib(0) != 0:
        return False, "fib(0) should be 0"
    if module.fib(1) != 1:
        return False, "fib(1) should be 1"
    if module.fib(2) != 1:
        return False, "fib(2) should be 1"
    if module.fib(10) != 55:
        return False, "fib(10) should be 55"
    if module.fib(30) != 832040:
        return False, "fib(30) should be 832040"
    if module.fib(50) != 12586269025:
        return False, "fib(50) should be 12586269025 — if this hangs, you forgot to memoize"
    return True, "All tests passed!"


def check_easy_p02(module):
    if not hasattr(module, 'climb_stairs'):
        return False, "Function 'climb_stairs' not found"
    if module.climb_stairs(1) != 1:
        return False, "climb_stairs(1) should be 1"
    if module.climb_stairs(2) != 2:
        return False, "climb_stairs(2) should be 2"
    if module.climb_stairs(3) != 3:
        return False, "climb_stairs(3) should be 3"
    if module.climb_stairs(5) != 8:
        return False, "climb_stairs(5) should be 8"
    if module.climb_stairs(10) != 89:
        return False, "climb_stairs(10) should be 89"
    if module.climb_stairs(45) != 1836311903:
        return False, "climb_stairs(45) should be 1836311903"
    return True, "All tests passed!"


def check_easy_p03(module):
    if not hasattr(module, 'tribonacci'):
        return False, "Function 'tribonacci' not found"
    if module.tribonacci(0) != 0:
        return False, "tribonacci(0) should be 0"
    if module.tribonacci(1) != 1 or module.tribonacci(2) != 1:
        return False, "tribonacci(1) and tribonacci(2) should both be 1"
    if module.tribonacci(4) != 4:
        return False, "tribonacci(4) should be 4"
    if module.tribonacci(10) != 149:
        return False, "tribonacci(10) should be 149"
    if module.tribonacci(25) != 1389537:
        return False, "tribonacci(25) should be 1389537"
    if module.tribonacci(37) != 2082876103:
        return False, "tribonacci(37) should be 2082876103"
    return True, "All tests passed!"


def check_medium_p01(module):
    if not hasattr(module, 'rob'):
        return False, "Function 'rob' not found"
    if module.rob([1, 2, 3, 1]) != 4:
        return False, "rob([1,2,3,1]) should be 4"
    if module.rob([2, 7, 9, 3, 1]) != 12:
        return False, "rob([2,7,9,3,1]) should be 12"
    if module.rob([2, 1, 1, 2]) != 4:
        return False, "rob([2,1,1,2]) should be 4"
    if module.rob([]) != 0:
        return False, "rob([]) should be 0"
    if module.rob([5]) != 5:
        return False, "rob([5]) should be 5"
    if module.rob([6, 6, 6, 6]) != 12:
        return False, "rob([6,6,6,6]) should be 12"
    return True, "All tests passed!"


def check_medium_p02(module):
    if not hasattr(module, 'min_cost'):
        return False, "Function 'min_cost' not found"
    if module.min_cost([10, 15, 20]) != 15:
        return False, "min_cost([10,15,20]) should be 15"
    if module.min_cost([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) != 6:
        return False, "min_cost([1,100,1,1,1,100,1,1,100,1]) should be 6"
    if module.min_cost([0, 0, 1]) != 0:
        return False, "min_cost([0,0,1]) should be 0"
    if module.min_cost([1, 2]) != 1:
        return False, "min_cost([1,2]) should be 1"
    if module.min_cost([0, 2, 2, 1]) != 2:
        return False, "min_cost([0,2,2,1]) should be 2"
    return True, "All tests passed!"


def check_medium_p03(module):
    if not hasattr(module, 'coin_change'):
        return False, "Function 'coin_change' not found"
    if module.coin_change([1, 2, 5], 11) != 3:
        return False, "coin_change([1,2,5], 11) should be 3"
    if module.coin_change([2], 3) != -1:
        return False, "coin_change([2], 3) should be -1"
    if module.coin_change([1], 0) != 0:
        return False, "coin_change([1], 0) should be 0"
    if module.coin_change([1, 3, 4], 6) != 2:
        return False, "coin_change([1,3,4], 6) should be 2 (greedy 4+1+1 fails)"
    if module.coin_change([186, 419, 83, 408], 6249) != 20:
        return False, "coin_change([186,419,83,408], 6249) should be 20"
    return True, "All tests passed!"


def check_hard_p01(module):
    if not hasattr(module, 'word_break'):
        return False, "Function 'word_break' not found"
    if module.word_break("leetcode", ["leet", "code"]) is not True:
        return False, "word_break('leetcode', ['leet','code']) should be True"
    if module.word_break("applepenapple", ["apple", "pen"]) is not True:
        return False, "word_break('applepenapple', ['apple','pen']) should be True"
    if module.word_break("catsandog", ["cats", "dog", "sand", "and", "cat"]) is not False:
        return False, "word_break('catsandog', ...) should be False"
    if module.word_break("cars", ["car", "ca", "rs"]) is not True:
        return False, "word_break('cars', ['car','ca','rs']) should be True"
    if module.word_break("aaaaaaa", ["aaaa", "aaa"]) is not True:
        return False, "word_break('aaaaaaa', ['aaaa','aaa']) should be True"
    if module.word_break("a" * 35 + "b", ["a", "aa", "aaa", "aaaa"]) is not False:
        return False, "word_break('a'*35+'b', ...) should be False — and fast (memoize!)"
    return True, "All tests passed!"


def check_hard_p02(module):
    if not hasattr(module, 'length_of_lis'):
        return False, "Function 'length_of_lis' not found"
    if module.length_of_lis([10, 9, 2, 5, 3, 7, 101, 18]) != 4:
        return False, "length_of_lis([10,9,2,5,3,7,101,18]) should be 4"
    if module.length_of_lis([0, 1, 0, 3, 2, 3]) != 4:
        return False, "length_of_lis([0,1,0,3,2,3]) should be 4"
    if module.length_of_lis([7, 7, 7, 7]) != 1:
        return False, "length_of_lis([7,7,7,7]) should be 1 (strictly increasing)"
    if module.length_of_lis([]) != 0:
        return False, "length_of_lis([]) should be 0"
    if module.length_of_lis([3, 2, 1]) != 1:
        return False, "length_of_lis([3,2,1]) should be 1"
    if module.length_of_lis([1, 2, 8, 3]) != 3:
        return False, "length_of_lis([1,2,8,3]) should be 3 — answer is max(dp), not dp[-1]"
    return True, "All tests passed!"


def check_hard_p03(module):
    if not hasattr(module, 'can_partition'):
        return False, "Function 'can_partition' not found"
    if module.can_partition([1, 5, 11, 5]) is not True:
        return False, "can_partition([1,5,11,5]) should be True"
    if module.can_partition([1, 2, 3, 5]) is not False:
        return False, "can_partition([1,2,3,5]) should be False (odd total)"
    if module.can_partition([1, 2, 5]) is not False:
        return False, "can_partition([1,2,5]) should be False"
    if module.can_partition([1, 1]) is not True:
        return False, "can_partition([1,1]) should be True"
    if module.can_partition([100]) is not False:
        return False, "can_partition([100]) should be False"
    if module.can_partition([3, 3, 3, 4, 5]) is not True:
        return False, "can_partition([3,3,3,4,5]) should be True"
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
        _run_batch(level_dir, solutions=False, title="LESSON 15 — CHECK YOUR FILES")
        return

    if target == "solutions":
        n = _run_batch(level_dir, solutions=True, title="LESSON 15 — REFERENCE SOLUTIONS")
        sys.exit(0 if n == len(CHECKS) else 1)

    if target == "verify":
        n_sol = _run_batch(level_dir, solutions=True, title="LESSON 15 — SOLUTIONS (must pass)")
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
