"""
Auto-Check System — Lesson 12 (Heaps)
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
from collections import Counter


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
    if not hasattr(module, 'run_heap_ops'):
        return False, "Function 'run_heap_ops' not found"
    if module.run_heap_ops([5, 1, 3], [("push", 0), ("pop",), ("peek",), ("pop",)]) != [0, 1, 1]:
        return False, "run_heap_ops([5,1,3], push0/pop/peek/pop) should be [0,1,1]"
    if module.run_heap_ops([4, 2, 7], [("pop",), ("pop",), ("peek",)]) != [2, 4, 7]:
        return False, "pops should come out ascending: [2,4,7]"
    if module.run_heap_ops([], [("push", 3), ("push", 1), ("pop",)]) != [1]:
        return False, "push 3, push 1, pop should be [1]"
    if module.run_heap_ops([9], [("peek",)]) != [9]:
        return False, "peek on [9] should be [9]"
    if module.run_heap_ops([3, 1, 2], [("peek",), ("peek",)]) != [1, 1]:
        return False, "peek must NOT remove — two peeks return 1 twice"
    return True, "All tests passed!"


def check_easy_p02(module):
    if not hasattr(module, 'kth_largest'):
        return False, "Function 'kth_largest' not found"
    if module.kth_largest([3, 2, 1, 5, 6, 4], 2) != 5:
        return False, "kth_largest([3,2,1,5,6,4], 2) should be 5"
    if module.kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) != 4:
        return False, "kth_largest(...,4) should be 4 (duplicates count)"
    if module.kth_largest([1], 1) != 1:
        return False, "kth_largest([1], 1) should be 1"
    if module.kth_largest([7, 7, 7], 2) != 7:
        return False, "kth_largest([7,7,7], 2) should be 7"
    if module.kth_largest([2, 1], 1) != 2 or module.kth_largest([2, 1], 2) != 1:
        return False, "kth_largest([2,1]): k=1 -> 2, k=2 -> 1"
    if module.kth_largest([-1, -5, -3], 2) != -3:
        return False, "kth_largest([-1,-5,-3], 2) should be -3 (negatives)"
    return True, "All tests passed!"


def check_easy_p03(module):
    if not hasattr(module, 'top_k_frequent_words'):
        return False, "Function 'top_k_frequent_words' not found"
    words = ["i", "love", "leetcode", "i", "love", "coding"]
    if module.top_k_frequent_words(words, 2) != ["i", "love"]:
        return False, "top2 should be ['i','love']"
    if module.top_k_frequent_words(words, 3) != ["i", "love", "coding"]:
        return False, "freq tie: 'coding' < 'leetcode' alphabetically -> ['i','love','coding']"
    w2 = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
    if module.top_k_frequent_words(w2, 4) != ["the", "is", "sunny", "day"]:
        return False, "top4 should be ['the','is','sunny','day']"
    if module.top_k_frequent_words(["a", "b", "a"], 1) != ["a"]:
        return False, "k=1 on ['a','b','a'] should be ['a']"
    return True, "All tests passed!"


def check_medium_p01(module):
    if not hasattr(module, 'k_closest'):
        return False, "Function 'k_closest' not found"
    if module.k_closest([[1, 3], [-2, 2]], 1) != [[-2, 2]]:
        return False, "k_closest([[1,3],[-2,2]], 1) should be [[-2,2]]"
    if module.k_closest([[3, 3], [5, -1], [-2, 4]], 2) != [[3, 3], [-2, 4]]:
        return False, "k_closest(..., 2) should be [[3,3],[-2,4]]"
    if module.k_closest([[0, 0], [1, 0], [0, 1]], 2) != [[0, 0], [0, 1]]:
        return False, "dist tie between [1,0] and [0,1] breaks by x then y"
    if module.k_closest([[1, 1], [2, 2]], 2) != [[1, 1], [2, 2]]:
        return False, "k == len returns all points sorted by distance"
    if module.k_closest([[-5, -5]], 1) != [[-5, -5]]:
        return False, "single point should return [[-5,-5]]"
    return True, "All tests passed!"


def check_medium_p02(module):
    if not hasattr(module, 'merge_k_sorted'):
        return False, "Function 'merge_k_sorted' not found"
    if module.merge_k_sorted([[1, 4, 5], [1, 3, 4], [2, 6]]) != [1, 1, 2, 3, 4, 4, 5, 6]:
        return False, "merge_k_sorted([[1,4,5],[1,3,4],[2,6]]) wrong"
    if module.merge_k_sorted([]) != []:
        return False, "merge_k_sorted([]) should be []"
    if module.merge_k_sorted([[], [], [1]]) != [1]:
        return False, "empty lists must be handled -> [1]"
    if module.merge_k_sorted([[-2, -1, 0], [1], [0, 2]]) != [-2, -1, 0, 0, 1, 2]:
        return False, "merge with negatives should be [-2,-1,0,0,1,2]"
    if module.merge_k_sorted([[1, 1, 1], [1, 1]]) != [1, 1, 1, 1, 1]:
        return False, "duplicates across lists must all survive"
    return True, "All tests passed!"


def check_medium_p03(module):
    if not hasattr(module, 'last_stone_weight'):
        return False, "Function 'last_stone_weight' not found"
    if module.last_stone_weight([2, 7, 4, 1, 8, 1]) != 1:
        return False, "last_stone_weight([2,7,4,1,8,1]) should be 1"
    if module.last_stone_weight([1]) != 1:
        return False, "single stone returns its weight"
    if module.last_stone_weight([1, 1]) != 0:
        return False, "[1,1] smash to nothing -> 0"
    if module.last_stone_weight([2, 2]) != 0:
        return False, "[2,2] -> 0"
    if module.last_stone_weight([10, 4, 2, 10]) != 2:
        return False, "last_stone_weight([10,4,2,10]) should be 2"
    if module.last_stone_weight([3, 7, 2]) != 2:
        return False, "[3,7,2]: 7&3 -> 4, 4&2 -> 2"
    return True, "All tests passed!"


def check_hard_p01(module):
    if not hasattr(module, 'running_medians'):
        return False, "Function 'running_medians' not found"
    if module.running_medians([1, 2, 3]) != [1.0, 1.5, 2.0]:
        return False, "running_medians([1,2,3]) should be [1.0, 1.5, 2.0]"
    if module.running_medians([5, 1, 4, 2, 3]) != [5.0, 3.0, 4.0, 3.0, 3.0]:
        return False, "running_medians([5,1,4,2,3]) should be [5.0,3.0,4.0,3.0,3.0]"
    if module.running_medians([]) != []:
        return False, "empty input -> []"
    if module.running_medians([2]) != [2.0]:
        return False, "single element -> [2.0]"
    if module.running_medians([4, 1]) != [4.0, 2.5]:
        return False, "running_medians([4,1]) should be [4.0, 2.5]"
    if module.running_medians([3, 3, 3]) != [3.0, 3.0, 3.0]:
        return False, "all-equal stream -> [3.0, 3.0, 3.0]"
    if module.running_medians([-1, -2]) != [-1.0, -1.5]:
        return False, "negatives: [-1,-2] -> [-1.0, -1.5]"
    return True, "All tests passed!"


def check_hard_p02(module):
    if not hasattr(module, 'least_interval'):
        return False, "Function 'least_interval' not found"
    if module.least_interval(['A', 'A', 'A', 'B', 'B', 'B'], 2) != 8:
        return False, "AAABBB n=2 should be 8 (A B _ A B _ A B)"
    if module.least_interval(['A', 'A', 'A', 'B', 'B', 'B'], 0) != 6:
        return False, "n=0 -> just len(tasks) = 6"
    if module.least_interval(['A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'C'], 2) != 9:
        return False, "AAABBBCCC n=2 -> 9 (no idle needed)"
    if module.least_interval(['A', 'A', 'A', 'A', 'A', 'A',
                              'B', 'C', 'D', 'E', 'F', 'G'], 2) != 16:
        return False, "AAAAAA+BCDEFG n=2 should be 16"
    if module.least_interval(['A'], 5) != 1:
        return False, "single task -> 1 regardless of cooldown"
    if module.least_interval([], 3) != 0:
        return False, "empty -> 0"
    if module.least_interval(['A', 'B'], 10) != 2:
        return False, "two different tasks need no cooldown -> 2"
    return True, "All tests passed!"


def _reorg_ok(orig, res):
    """Valid rearrangement = same multiset + no adjacent equal;
    "" is acceptable only when separation is provably impossible."""
    if not isinstance(res, str):
        return False
    if res == "":
        if orig == "":
            return True
        c = Counter(orig)
        return c.most_common(1)[0][1] > (len(orig) + 1) // 2
    return (sorted(res) == sorted(orig)
            and all(res[i] != res[i + 1] for i in range(len(res) - 1)))


def check_hard_p03(module):
    if not hasattr(module, 'reorganize_string'):
        return False, "Function 'reorganize_string' not found"
    if not _reorg_ok("aab", module.reorganize_string("aab")):
        return False, "reorganize_string('aab') — need valid arrangement like 'aba'"
    if module.reorganize_string("aaab") != "":
        return False, "'aaab' is impossible (3 a's > ceil(4/2)) — return ''"
    if not _reorg_ok("aaabbc", module.reorganize_string("aaabbc")):
        return False, "'aaabbc' has a valid arrangement"
    if module.reorganize_string("") != "":
        return False, "empty string -> ''"
    if not _reorg_ok("vvvlo", module.reorganize_string("vvvlo")):
        return False, "'vvvlo' has a valid arrangement"
    if module.reorganize_string("aaaa") != "":
        return False, "'aaaa' impossible -> ''"
    if not _reorg_ok("aabbcc", module.reorganize_string("aabbcc")):
        return False, "'aabbcc' has a valid arrangement"
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
        _run_batch(level_dir, solutions=False, title="LESSON 12 — CHECK YOUR FILES")
        return

    if target == "solutions":
        n = _run_batch(level_dir, solutions=True, title="LESSON 12 — REFERENCE SOLUTIONS")
        sys.exit(0 if n == len(CHECKS) else 1)

    if target == "verify":
        n_sol = _run_batch(level_dir, solutions=True, title="LESSON 12 — SOLUTIONS (must pass)")
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
