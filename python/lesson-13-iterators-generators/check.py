"""
Auto-Check System — Lesson 13 (Iterators & Generators)
=====================================================
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
    if not hasattr(module, 'count_up_to'):
        return False, "Function 'count_up_to' not found"
    result = module.count_up_to(5)
    if not hasattr(result, '__next__'):
        return False, "count_up_to should be a generator (use yield)"
    if list(result) != [1, 2, 3, 4, 5]:
        return False, "count_up_to(5) should yield 1..5"
    if list(module.count_up_to(0)) != []:
        return False, "count_up_to(0) should yield nothing"
    return True, "All tests passed!"


def check_easy_p02(module):
    if not hasattr(module, 'even_squares'):
        return False, "Generator 'even_squares' not found"
    expected = [0, 4, 16, 36, 64, 100, 144, 196, 256, 324, 400]
    result = list(module.even_squares)
    if result != expected:
        return False, f"Expected {expected}, got {result}"
    return True, "All tests passed!"


def check_easy_p03(module):
    if not hasattr(module, 'CountDown'):
        return False, "Class 'CountDown' not found"
    if list(module.CountDown(3)) != [3, 2, 1]:
        return False, "list(CountDown(3)) should be [3, 2, 1]"
    if list(module.CountDown(0)) != []:
        return False, "list(CountDown(0)) should be []"
    it = iter(module.CountDown(2))
    if next(it) != 2 or next(it) != 1:
        return False, "next() should count down"
    try:
        next(it)
        return False, "Should raise StopIteration when done"
    except StopIteration:
        pass
    return True, "All tests passed!"


def check_medium_p01(module):
    if not hasattr(module, 'fibonacci'):
        return False, "Function 'fibonacci' not found"
    from itertools import islice
    result = list(islice(module.fibonacci(), 10))
    expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    if result != expected:
        return False, f"Expected {expected}, got {result}"
    return True, "All tests passed!"


def check_medium_p02(module):
    if not hasattr(module, 'flatten'):
        return False, "Function 'flatten' not found"
    if list(module.flatten([1, [2, [3, [4]]], 5])) != [1, 2, 3, 4, 5]:
        return False, "flatten([1,[2,[3,[4]]],5]) should be [1,2,3,4,5]"
    if list(module.flatten([])) != []:
        return False, "flatten([]) should be []"
    if list(module.flatten([[1, 2], [3], [[4, 5], 6]])) != [1, 2, 3, 4, 5, 6]:
        return False, "Deep nesting failed"
    return True, "All tests passed!"


def check_medium_p03(module):
    for fname in ['generate_nums', 'filter_multiples_of_3', 'square_them', 'take_first']:
        if not hasattr(module, fname):
            return False, f"Function '{fname}' not found"
    pipeline = module.take_first(
        module.square_them(
            module.filter_multiples_of_3(module.generate_nums(100))), 5)
    result = list(pipeline)
    if result != [9, 36, 81, 144, 225]:
        return False, f"Expected [9, 36, 81, 144, 225], got {result}"
    return True, "All tests passed!"


def check_hard_p01(module):
    if not hasattr(module, 'read_lines'):
        return False, "Function 'read_lines' not found"
    import tempfile
    path = os.path.join(tempfile.mkdtemp(), "t.txt")
    with open(path, "w") as f:
        f.write("line1\nline2\nline3\n")
    if list(module.read_lines(path)) != ["line1", "line2", "line3"]:
        return False, "read_lines should yield stripped lines"
    if list(module.read_lines("/nonexistent_path_xyz.txt")) != []:
        return False, "Missing file should yield nothing (no crash)"
    return True, "All tests passed!"


def check_hard_p02(module):
    if not hasattr(module, 'chunked'):
        return False, "Function 'chunked' not found"
    if list(module.chunked([1, 2, 3, 4, 5], 2)) != [[1, 2], [3, 4], [5]]:
        return False, "chunked([1..5], 2) failed"
    if list(module.chunked([], 3)) != []:
        return False, "chunked([], 3) should be []"
    if list(module.chunked([1, 2, 3], 5)) != [[1, 2, 3]]:
        return False, "chunked([1,2,3], 5) should be [[1,2,3]]"
    if list(module.chunked(iter([1, 2, 3, 4]), 3)) != [[1, 2, 3], [4]]:
        return False, "Should work on any iterable, not just lists"
    return True, "All tests passed!"


def check_hard_p03(module):
    if not hasattr(module, 'cycle_forever'):
        return False, "Function 'cycle_forever' not found"
    from itertools import islice
    result = list(islice(module.cycle_forever(["a", "b", "c"]), 7))
    if result != ["a", "b", "c", "a", "b", "c", "a"]:
        return False, f"Expected a,b,c,a,b,c,a — got {result}"
    if list(islice(module.cycle_forever([]), 5)) != []:
        return False, "Empty iterable should yield nothing"
    result2 = list(islice(module.cycle_forever(iter([1, 2]), ), 5))
    if result2 != [1, 2, 1, 2, 1]:
        return False, "Should work on one-shot iterators too"
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


def run_one(level_dir, check_id):
    check_func = CHECKS[check_id]
    level, num = check_id.split("/")
    filepath = _find_file(level_dir, level, num)
    if not os.path.exists(filepath):
        print(f"Error: file not found: {filepath}")
        sys.exit(1)
    try:
        module = load_module(filepath)
        passed, msg = check_func(module)
        if passed:
            print(f"PASS — {msg}")
            try:
                with open(filepath) as f:
                    if "# DONE" not in f.readline():
                        print(f"  Add '# DONE' to the first line of {filepath}")
            except OSError:
                pass
        else:
            print(f"FAIL — {msg}")
    except Exception as e:
        print(f"ERROR — {e}")
        import traceback
        traceback.print_exc()


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 check.py <level>/<problem>")
        sys.exit(1)

    target = sys.argv[1]
    level_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(level_dir)

    if target == "all":
        print("=" * 60)
        print("  LESSON 13 — AUTO-CHECK ALL")
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

    if "/" not in target or target not in CHECKS:
        print(f"Error: unknown problem '{target}'")
        sys.exit(1)

    run_one(level_dir, target)


if __name__ == "__main__":
    main()
