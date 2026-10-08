"""
Auto-Check System — Lesson 18 (Advanced Mix: Tries, Bits, Monotonic Stack)
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
    if not hasattr(module, 'single_number'):
        return False, "Function 'single_number' not found"
    if module.single_number([2,2,1]) != 1:
        return False, "single_number([2,2,1]) should be 1"
    if module.single_number([4,1,2,1,2]) != 4:
        return False, "single_number([4,1,2,1,2]) should be 4"
    if module.single_number([1]) != 1:
        return False, "single_number([1]) should be 1"
    if module.single_number([-1,-1,-2]) != -2:
        return False, "single_number([-1,-1,-2]) should be -2 — XOR works on negatives"
    if module.single_number([7,3,5,3,5]) != 7:
        return False, "single_number([7,3,5,3,5]) should be 7"
    return True, "All tests passed!"


def check_easy_p02(module):
    if not hasattr(module, 'is_power_of_two'):
        return False, "Function 'is_power_of_two' not found"
    if module.is_power_of_two(1) != True:
        return False, "is_power_of_two(1) should be True"
    if module.is_power_of_two(16) != True:
        return False, "is_power_of_two(16) should be True"
    if module.is_power_of_two(3) != False:
        return False, "is_power_of_two(3) should be False"
    if module.is_power_of_two(0) != False:
        return False, "is_power_of_two(0) should be False — guard with n > 0"
    if module.is_power_of_two(-8) != False:
        return False, "is_power_of_two(-8) should be False"
    if module.is_power_of_two(1024) != True:
        return False, "is_power_of_two(1024) should be True"
    if module.is_power_of_two(6) != False:
        return False, "is_power_of_two(6) should be False — two set bits"
    return True, "All tests passed!"


def check_easy_p03(module):
    if not hasattr(module, 'hamming_weight'):
        return False, "Function 'hamming_weight' not found"
    if module.hamming_weight(11) != 3:
        return False, "hamming_weight(11) should be 3"
    if module.hamming_weight(128) != 1:
        return False, "hamming_weight(128) should be 1"
    if module.hamming_weight(0) != 0:
        return False, "hamming_weight(0) should be 0"
    if module.hamming_weight(255) != 8:
        return False, "hamming_weight(255) should be 8"
    if module.hamming_weight(2147483647) != 31:
        return False, "hamming_weight(2147483647) should be 31"
    if module.hamming_weight(-1) != 32:
        return False, "hamming_weight(-1) should be 32 — mask to 32 bits"
    return True, "All tests passed!"


def check_medium_p01(module):
    if not hasattr(module, 'Trie'):
        return False, "Class 'Trie' not found"
    try:
        trie = module.Trie()
        trie.insert("apple")
        if trie.search("apple") != True:
            return False, "search('apple') should be True after insert('apple')"
        if trie.search("app") != False:
            return False, "search('app') should be False — path exists but is_end is False"
        if trie.startsWith("app") != True:
            return False, "startsWith('app') should be True"
        trie.insert("app")
        if trie.search("app") != True:
            return False, "search('app') should be True after insert('app')"
        if trie.search("apples") != False:
            return False, "search('apples') should be False"
        if trie.startsWith("apples") != False:
            return False, "startsWith('apples') should be False — path dies at 's'"
        trie.insert("application")
        if trie.startsWith("appli") != True:
            return False, "startsWith('appli') should be True"
        if trie.search("appli") != False:
            return False, "search('appli') should be False — it's a prefix, not a word"
        if trie.search("application") != True:
            return False, "search('application') should be True"
    except AttributeError as e:
        return False, f"Trie missing a method: {e}"
    return True, "All tests passed!"


def check_medium_p02(module):
    if not hasattr(module, 'single_numbers'):
        return False, "Function 'single_numbers' not found"
    if sorted(module.single_numbers([1,2,1,3,2,5])) != [3,5]:
        return False, "single_numbers([1,2,1,3,2,5]) should be [3,5] (any order)"
    if sorted(module.single_numbers([-1,0])) != [-1,0]:
        return False, "single_numbers([-1,0]) should be [-1,0]"
    if sorted(module.single_numbers([0,1])) != [0,1]:
        return False, "single_numbers([0,1]) should be [0,1]"
    if sorted(module.single_numbers([1,2,3,4,1,2,3,7])) != [4,7]:
        return False, "single_numbers([1,2,3,4,1,2,3,7]) should be [4,7]"
    if sorted(module.single_numbers([4,4,7,7,3,1])) != [1,3]:
        return False, "single_numbers([4,4,7,7,3,1]) should be [1,3]"
    return True, "All tests passed!"


def check_medium_p03(module):
    if not hasattr(module, 'next_greater_elements'):
        return False, "Function 'next_greater_elements' not found"
    if module.next_greater_elements([1,2,1]) != [2,-1,2]:
        return False, "next_greater_elements([1,2,1]) should be [2,-1,2]"
    if module.next_greater_elements([1,2,3,4,3]) != [2,3,4,-1,4]:
        return False, "next_greater_elements([1,2,3,4,3]) should be [2,3,4,-1,4]"
    if module.next_greater_elements([5,4,3,2,1]) != [-1,5,5,5,5]:
        return False, "next_greater_elements([5,4,3,2,1]) should be [-1,5,5,5,5] — wraparound"
    if module.next_greater_elements([1,2,3,2,1]) != [2,3,-1,3,2]:
        return False, "next_greater_elements([1,2,3,2,1]) should be [2,3,-1,3,2]"
    if module.next_greater_elements([3]) != [-1]:
        return False, "next_greater_elements([3]) should be [-1]"
    if module.next_greater_elements([2,2,2]) != [-1,-1,-1]:
        return False, "next_greater_elements([2,2,2]) should be [-1,-1,-1] — strictly greater"
    return True, "All tests passed!"


def check_hard_p01(module):
    if not hasattr(module, 'find_words'):
        return False, "Function 'find_words' not found"
    board = [["o","a","a","n"],
             ["e","t","a","e"],
             ["i","h","k","r"],
             ["i","f","l","v"]]
    if module.find_words(board, ["oath","pea","eat","rain"]) != ["eat","oath"]:
        return False, "find_words(4x4 board, ['oath','pea','eat','rain']) should be ['eat','oath']"
    if module.find_words([["a","b"],["c","d"]], ["abcb"]) != []:
        return False, "find_words(2x2, ['abcb']) should be [] — cells can't be reused"
    if module.find_words([["a"]], ["a"]) != ["a"]:
        return False, "find_words([['a']], ['a']) should be ['a']"
    if module.find_words([["a","b"],["c","d"]], ["ab","ba","cd","abd"]) != ["ab","abd","ba","cd"]:
        return False, "find_words(2x2, ['ab','ba','cd','abd']) should be all four sorted"
    if module.find_words([["a","a"],["a","a"]], ["aaaa"]) != ["aaaa"]:
        return False, "find_words(2x2 all-a, ['aaaa']) should be ['aaaa']"
    return True, "All tests passed!"


def check_hard_p02(module):
    if not hasattr(module, 'find_maximum_xor'):
        return False, "Function 'find_maximum_xor' not found"
    if module.find_maximum_xor([3,10,5,25,2,8]) != 28:
        return False, "find_maximum_xor([3,10,5,25,2,8]) should be 28 (5^25)"
    if module.find_maximum_xor([0]) != 0:
        return False, "find_maximum_xor([0]) should be 0"
    if module.find_maximum_xor([5,5]) != 0:
        return False, "find_maximum_xor([5,5]) should be 0"
    if module.find_maximum_xor([2,4]) != 6:
        return False, "find_maximum_xor([2,4]) should be 6"
    if module.find_maximum_xor([8,10,2]) != 10:
        return False, "find_maximum_xor([8,10,2]) should be 10 (8^2)"
    if module.find_maximum_xor([14,70,53,83,49,91,36,80,92,51,66,70]) != 127:
        return False, "find_maximum_xor(12-element case) should be 127"
    return True, "All tests passed!"


def check_hard_p03(module):
    if not hasattr(module, 'largest_rectangle_area'):
        return False, "Function 'largest_rectangle_area' not found"
    if module.largest_rectangle_area([2,1,5,6,2,3]) != 10:
        return False, "largest_rectangle_area([2,1,5,6,2,3]) should be 10"
    if module.largest_rectangle_area([2,4]) != 4:
        return False, "largest_rectangle_area([2,4]) should be 4 — did you flush the stack?"
    if module.largest_rectangle_area([1]) != 1:
        return False, "largest_rectangle_area([1]) should be 1"
    if module.largest_rectangle_area([4,2,0,3,2,5]) != 6:
        return False, "largest_rectangle_area([4,2,0,3,2,5]) should be 6"
    if module.largest_rectangle_area([]) != 0:
        return False, "largest_rectangle_area([]) should be 0"
    if module.largest_rectangle_area([6,2,0,9,2,9]) != 9:
        return False, "largest_rectangle_area([6,2,0,9,2,9]) should be 9"
    if module.largest_rectangle_area([2,2,2,2]) != 8:
        return False, "largest_rectangle_area([2,2,2,2]) should be 8"
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
        _run_batch(level_dir, solutions=False, title="LESSON 18 — CHECK YOUR FILES")
        return

    if target == "solutions":
        n = _run_batch(level_dir, solutions=True, title="LESSON 18 — REFERENCE SOLUTIONS")
        sys.exit(0 if n == len(CHECKS) else 1)

    if target == "verify":
        n_sol = _run_batch(level_dir, solutions=True, title="LESSON 18 — SOLUTIONS (must pass)")
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
