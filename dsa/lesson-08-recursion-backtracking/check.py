"""
Auto-Check System — DSA Lesson 08 (Recursion & Backtracking)
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


def _sorted_lists(res):
    """Order-insensitive compare for list-of-lists answers."""
    return sorted(map(sorted, res))


def _unique(res):
    """True if no two entries are equal regardless of order."""
    return len(set(map(tuple, res))) == len(res)


def check_easy_p01(module):
    if not hasattr(module, 'sum_digits'):
        return False, "Function 'sum_digits' not found"
    if module.sum_digits(1234) != 10:
        return False, "sum_digits(1234) should be 10"
    if module.sum_digits(0) != 0:
        return False, "sum_digits(0) should be 0"
    if module.sum_digits(999) != 27:
        return False, "sum_digits(999) should be 27"
    if module.sum_digits(7) != 7:
        return False, "sum_digits(7) should be 7"
    return True, "All tests passed!"


def check_easy_p02(module):
    if not hasattr(module, 'countdown'):
        return False, "Function 'countdown' not found"
    if module.countdown(5) != [5, 4, 3, 2, 1]:
        return False, "countdown(5) should be [5,4,3,2,1]"
    if module.countdown(1) != [1]:
        return False, "countdown(1) should be [1]"
    if module.countdown(0) != []:
        return False, "countdown(0) should be []"
    if module.countdown(3) != [3, 2, 1]:
        return False, "countdown(3) should be [3,2,1]"
    return True, "All tests passed!"


def check_easy_p03(module):
    if not hasattr(module, 'power'):
        return False, "Function 'power' not found"
    if module.power(2, 10) != 1024:
        return False, "power(2,10) should be 1024"
    if module.power(2, 0) != 1:
        return False, "power(2,0) should be 1"
    if module.power(3, 3) != 27:
        return False, "power(3,3) should be 27"
    if module.power(5, 1) != 5:
        return False, "power(5,1) should be 5"
    if module.power(7, 2) != 49:
        return False, "power(7,2) should be 49"
    return True, "All tests passed!"


def check_medium_p01(module):
    if not hasattr(module, 'subsets'):
        return False, "Function 'subsets' not found"
    if _sorted_lists(module.subsets([1, 2])) != [[], [1], [1, 2], [2]]:
        return False, "subsets([1,2]) should be the 4 subsets [[],[1],[2],[1,2]]"
    r = module.subsets([1, 2, 3])
    if len(r) != 8 or not _unique(r):
        return False, "subsets([1,2,3]) should be 8 unique subsets"
    if module.subsets([]) != [[]]:
        return False, "subsets([]) should be [[]]"
    if _sorted_lists(module.subsets([1, 2, 3])) != [
            [], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]:
        return False, "subsets([1,2,3]) contents are wrong"
    return True, "All tests passed!"


def check_medium_p02(module):
    if not hasattr(module, 'permutations'):
        return False, "Function 'permutations' not found"
    if sorted(map(tuple, module.permutations([1, 2, 3]))) != [
            (1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]:
        return False, "permutations([1,2,3]) should be all 6 orderings"
    if module.permutations([1]) != [[1]]:
        return False, "permutations([1]) should be [[1]]"
    r = module.permutations([1, 2, 3, 4])
    if len(r) != 24 or not _unique(r):
        return False, "permutations([1,2,3,4]) should be 24 unique orderings"
    return True, "All tests passed!"


def check_medium_p03(module):
    if not hasattr(module, 'letter_case_permutation'):
        return False, "Function 'letter_case_permutation' not found"
    if set(module.letter_case_permutation("a1b2")) != {"a1b2", "a1B2", "A1b2", "A1B2"}:
        return False, "letter_case_permutation('a1b2') should be the 4-case set"
    if set(module.letter_case_permutation("3z4")) != {"3z4", "3Z4"}:
        return False, "letter_case_permutation('3z4') should be {'3z4','3Z4'}"
    if module.letter_case_permutation("123") != ["123"]:
        return False, "letter_case_permutation('123') should be ['123']"
    if len(module.letter_case_permutation("abc")) != 8:
        return False, "letter_case_permutation('abc') should have 8 results"
    return True, "All tests passed!"


def check_hard_p01(module):
    if not hasattr(module, 'solve_n_queens'):
        return False, "Function 'solve_n_queens' not found"
    if {tuple(b) for b in module.solve_n_queens(4)} != {
            (".Q..", "...Q", "Q...", "..Q."),
            ("..Q.", "Q...", "...Q", ".Q..")}:
        return False, "solve_n_queens(4) should return exactly the 2 valid boards"
    if module.solve_n_queens(1) != [["Q"]]:
        return False, "solve_n_queens(1) should be [['Q']]"
    if module.solve_n_queens(2) != []:
        return False, "solve_n_queens(2) should be [] (impossible)"
    if len(module.solve_n_queens(5)) != 10:
        return False, "solve_n_queens(5) should find 10 boards"
    return True, "All tests passed!"


def check_hard_p02(module):
    if not hasattr(module, 'combination_sum'):
        return False, "Function 'combination_sum' not found"
    if _sorted_lists(module.combination_sum([2, 3, 6, 7], 7)) != [[2, 2, 3], [7]]:
        return False, "combination_sum([2,3,6,7],7) should be [[2,2,3],[7]]"
    if module.combination_sum([2], 1) != []:
        return False, "combination_sum([2],1) should be []"
    if _sorted_lists(module.combination_sum([2, 3, 5], 8)) != [[2, 2, 2, 2], [2, 3, 3], [3, 5]]:
        return False, "combination_sum([2,3,5],8) should be 3 combos"
    r = module.combination_sum([2, 3, 6, 7], 7)
    canonical = [tuple(sorted(x)) for x in r]
    if len(set(canonical)) != len(canonical):
        return False, "combination_sum returned permutation duplicates like [2,2,3] and [3,2,2]"
    return True, "All tests passed!"


def check_hard_p03(module):
    if not hasattr(module, 'exist'):
        return False, "Function 'exist' not found"
    b = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    if module.exist([row[:] for row in b], "ABCCED") is not True:
        return False, "exist(board,'ABCCED') should be True"
    if module.exist([row[:] for row in b], "SEE") is not True:
        return False, "exist(board,'SEE') should be True"
    if module.exist([row[:] for row in b], "ABCB") is not False:
        return False, "exist(board,'ABCB') should be False (cells can't repeat)"
    if module.exist([["a"]], "a") is not True:
        return False, "exist([['a']],'a') should be True"
    if module.exist([["a"]], "b") is not False:
        return False, "exist([['a']],'b') should be False"
    if module.exist([["a"]], "aa") is not False:
        return False, "exist([['a']],'aa') should be False (no reuse)"
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
        print("  DSA LESSON 08 — AUTO-CHECK ALL")
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
