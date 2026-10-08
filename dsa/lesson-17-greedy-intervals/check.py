"""
Auto-Check System — Lesson 17 (Greedy & Intervals)
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
    if not hasattr(module, 'merge'):
        return False, "Function 'merge' not found"
    if module.merge([[1,3],[2,6],[8,10],[15,18]]) != [[1,6],[8,10],[15,18]]:
        return False, "merge([[1,3],[2,6],[8,10],[15,18]]) should be [[1,6],[8,10],[15,18]]"
    if module.merge([[1,4],[4,5]]) != [[1,5]]:
        return False, "merge([[1,4],[4,5]]) should be [[1,5]] — touching intervals merge (use <=)"
    if module.merge([[1,4],[2,3]]) != [[1,4]]:
        return False, "merge([[1,4],[2,3]]) should be [[1,4]] — take max of ends, don't shrink"
    if module.merge([[2,6],[1,3]]) != [[1,6]]:
        return False, "merge([[2,6],[1,3]]) should be [[1,6]] — did you sort first?"
    if module.merge([[5,7]]) != [[5,7]]:
        return False, "merge([[5,7]]) should be [[5,7]]"
    if module.merge([[1,2],[3,4],[5,6]]) != [[1,2],[3,4],[5,6]]:
        return False, "merge([[1,2],[3,4],[5,6]]) should stay unchanged"
    return True, "All tests passed!"


def check_easy_p02(module):
    if not hasattr(module, 'can_attend_all'):
        return False, "Function 'can_attend_all' not found"
    if module.can_attend_all([[0,30],[5,10],[15,20]]) != False:
        return False, "can_attend_all([[0,30],[5,10],[15,20]]) should be False"
    if module.can_attend_all([[7,10],[2,4]]) != True:
        return False, "can_attend_all([[7,10],[2,4]]) should be True — sort first"
    if module.can_attend_all([[1,5],[5,8],[8,10]]) != True:
        return False, "can_attend_all([[1,5],[5,8],[8,10]]) should be True — touching is OK"
    if module.can_attend_all([]) != True:
        return False, "can_attend_all([]) should be True"
    if module.can_attend_all([[1,2]]) != True:
        return False, "can_attend_all([[1,2]]) should be True"
    if module.can_attend_all([[1,10],[2,3],[4,5]]) != False:
        return False, "can_attend_all([[1,10],[2,3],[4,5]]) should be False"
    return True, "All tests passed!"


def check_easy_p03(module):
    if not hasattr(module, 'find_content_children'):
        return False, "Function 'find_content_children' not found"
    if module.find_content_children([1,2,3], [1,1]) != 1:
        return False, "find_content_children([1,2,3], [1,1]) should be 1"
    if module.find_content_children([1,2], [1,2,3]) != 2:
        return False, "find_content_children([1,2], [1,2,3]) should be 2"
    if module.find_content_children([10,9,8,7], [5,6,7,8]) != 2:
        return False, "find_content_children([10,9,8,7], [5,6,7,8]) should be 2"
    if module.find_content_children([], [1,2]) != 0:
        return False, "find_content_children([], [1,2]) should be 0"
    if module.find_content_children([1,2,3], []) != 0:
        return False, "find_content_children([1,2,3], []) should be 0"
    if module.find_content_children([1,2,3], [3]) != 1:
        return False, "find_content_children([1,2,3], [3]) should be 1"
    return True, "All tests passed!"


def check_medium_p01(module):
    if not hasattr(module, 'erase_overlap_intervals'):
        return False, "Function 'erase_overlap_intervals' not found"
    if module.erase_overlap_intervals([[1,2],[2,3],[3,4],[1,3]]) != 1:
        return False, "erase_overlap_intervals([[1,2],[2,3],[3,4],[1,3]]) should be 1"
    if module.erase_overlap_intervals([[1,2],[1,2],[1,2]]) != 2:
        return False, "erase_overlap_intervals([[1,2]x3]) should be 2"
    if module.erase_overlap_intervals([[1,2],[2,3]]) != 0:
        return False, "erase_overlap_intervals([[1,2],[2,3]]) should be 0 — touching is fine"
    if module.erase_overlap_intervals([[0,2],[1,3],[2,4],[3,5],[4,6]]) != 2:
        return False, "erase_overlap_intervals([[0,2],[1,3],[2,4],[3,5],[4,6]]) should be 2"
    if module.erase_overlap_intervals([[1,10],[2,3],[4,5]]) != 1:
        return False, "erase_overlap_intervals([[1,10],[2,3],[4,5]]) should be 1 — sort by END, not start"
    if module.erase_overlap_intervals([[-52,31],[-73,-26],[82,97],[-65,-11],
                                       [-62,-49],[95,99],[58,95],[-31,49],
                                       [66,98],[-63,2],[30,47],[-40,-26]]) != 7:
        return False, "erase_overlap_intervals(12-interval case) should be 7"
    if module.erase_overlap_intervals([]) != 0:
        return False, "erase_overlap_intervals([]) should be 0"
    return True, "All tests passed!"


def check_medium_p02(module):
    if not hasattr(module, 'insert'):
        return False, "Function 'insert' not found"
    if module.insert([[1,3],[6,9]], [2,5]) != [[1,5],[6,9]]:
        return False, "insert([[1,3],[6,9]], [2,5]) should be [[1,5],[6,9]]"
    if module.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]) != [[1,2],[3,10],[12,16]]:
        return False, "insert(..., [4,8]) should be [[1,2],[3,10],[12,16]]"
    if module.insert([], [5,7]) != [[5,7]]:
        return False, "insert([], [5,7]) should be [[5,7]]"
    if module.insert([[1,5]], [2,7]) != [[1,7]]:
        return False, "insert([[1,5]], [2,7]) should be [[1,7]]"
    if module.insert([[1,5]], [2,3]) != [[1,5]]:
        return False, "insert([[1,5]], [2,3]) should be [[1,5]]"
    if module.insert([[5,8]], [1,3]) != [[1,3],[5,8]]:
        return False, "insert([[5,8]], [1,3]) should be [[1,3],[5,8]] — insert before everything"
    if module.insert([[1,3]], [4,6]) != [[1,3],[4,6]]:
        return False, "insert([[1,3]], [4,6]) should be [[1,3],[4,6]]"
    return True, "All tests passed!"


def check_medium_p03(module):
    if not hasattr(module, 'can_jump'):
        return False, "Function 'can_jump' not found"
    if module.can_jump([2,3,1,1,4]) != True:
        return False, "can_jump([2,3,1,1,4]) should be True"
    if module.can_jump([3,2,1,0,4]) != False:
        return False, "can_jump([3,2,1,0,4]) should be False — index 3 is a wall"
    if module.can_jump([0]) != True:
        return False, "can_jump([0]) should be True"
    if module.can_jump([2,0,0]) != True:
        return False, "can_jump([2,0,0]) should be True — can jump over zeros"
    if module.can_jump([1,1,0,1]) != False:
        return False, "can_jump([1,1,0,1]) should be False"
    if module.can_jump([1,0,1,0]) != False:
        return False, "can_jump([1,0,1,0]) should be False — check i <= reach BEFORE extending"
    if module.can_jump([4,0,0,0,0]) != True:
        return False, "can_jump([4,0,0,0,0]) should be True"
    return True, "All tests passed!"


def check_hard_p01(module):
    if not hasattr(module, 'jump'):
        return False, "Function 'jump' not found"
    if module.jump([2,3,1,1,4]) != 2:
        return False, "jump([2,3,1,1,4]) should be 2"
    if module.jump([2,3,0,1,4]) != 2:
        return False, "jump([2,3,0,1,4]) should be 2"
    if module.jump([1,1,1,1]) != 3:
        return False, "jump([1,1,1,1]) should be 3"
    if module.jump([0]) != 0:
        return False, "jump([0]) should be 0"
    if module.jump([1,2,3]) != 2:
        return False, "jump([1,2,3]) should be 2"
    if module.jump([4,1,1,1,1,1]) != 2:
        return False, "jump([4,1,1,1,1,1]) should be 2 — landing on max-reach still needs a jump"
    if module.jump([7,0,9,6,9,6,1,7,9,0,1,2,9]) != 2:
        return False, "jump(13-element case) should be 2"
    return True, "All tests passed!"


def check_hard_p02(module):
    if not hasattr(module, 'can_complete_circuit'):
        return False, "Function 'can_complete_circuit' not found"
    if module.can_complete_circuit([1,2,3,4,5], [3,4,5,1,2]) != 3:
        return False, "can_complete_circuit([1,2,3,4,5],[3,4,5,1,2]) should be 3"
    if module.can_complete_circuit([2,3,4], [3,4,3]) != -1:
        return False, "can_complete_circuit([2,3,4],[3,4,3]) should be -1"
    if module.can_complete_circuit([5,1,2,3,4], [4,4,1,5,1]) != 4:
        return False, "can_complete_circuit([5,1,2,3,4],[4,4,1,5,1]) should be 4"
    if module.can_complete_circuit([3,1,1], [1,2,2]) != 0:
        return False, "can_complete_circuit([3,1,1],[1,2,2]) should be 0"
    if module.can_complete_circuit([2], [2]) != 0:
        return False, "can_complete_circuit([2],[2]) should be 0"
    if module.can_complete_circuit([1], [2]) != -1:
        return False, "can_complete_circuit([1],[2]) should be -1"
    return True, "All tests passed!"


def check_hard_p03(module):
    if not hasattr(module, 'partition_labels'):
        return False, "Function 'partition_labels' not found"
    if module.partition_labels("ababcbacadefegdehijhklij") != [9,7,8]:
        return False, "partition_labels('ababcbacadefegdehijhklij') should be [9,7,8]"
    if module.partition_labels("eccbbbbdec") != [10]:
        return False, "partition_labels('eccbbbbdec') should be [10]"
    if module.partition_labels("a") != [1]:
        return False, "partition_labels('a') should be [1]"
    if module.partition_labels("abac") != [3,1]:
        return False, "partition_labels('abac') should be [3,1]"
    if module.partition_labels("ababcbaca") != [9]:
        return False, "partition_labels('ababcbaca') should be [9]"
    if module.partition_labels("abcd") != [1,1,1,1]:
        return False, "partition_labels('abcd') should be [1,1,1,1]"
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
        _run_batch(level_dir, solutions=False, title="LESSON 17 — CHECK YOUR FILES")
        return

    if target == "solutions":
        n = _run_batch(level_dir, solutions=True, title="LESSON 17 — REFERENCE SOLUTIONS")
        sys.exit(0 if n == len(CHECKS) else 1)

    if target == "verify":
        n_sol = _run_batch(level_dir, solutions=True, title="LESSON 17 — SOLUTIONS (must pass)")
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
