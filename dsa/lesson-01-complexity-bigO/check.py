"""
Auto-Check System — DSA Lesson 01 (Time/Space Complexity & Big-O)
=================================================================
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


def check_easy_p01(module):
    if not hasattr(module, 'count_ops'):
        return False, "Function 'count_ops' not found"
    if module.count_ops(10) != 10:
        return False, "count_ops(10) should be 10"
    if module.count_ops(0) != 0:
        return False, "count_ops(0) should be 0"
    if module.count_ops(1000) != 1000:
        return False, "count_ops(1000) should be 1000"
    return True, "All tests passed!"


def check_easy_p02(module):
    if not hasattr(module, 'classify_growth'):
        return False, "Function 'classify_growth' not found"
    if module.classify_growth(7, 7, 7) != "O(1)":
        return False, "classify_growth(7,7,7) should be 'O(1)'"
    if module.classify_growth(10, 11, 12) != "O(log n)":
        return False, "classify_growth(10,11,12) should be 'O(log n)'"
    if module.classify_growth(50, 100, 200) != "O(n)":
        return False, "classify_growth(50,100,200) should be 'O(n)'"
    if module.classify_growth(25, 100, 400) != "O(n^2)":
        return False, "classify_growth(25,100,400) should be 'O(n^2)'"
    if module.classify_growth(8, 64, 4096) != "O(2^n)":
        return False, "classify_growth(8,64,4096) should be 'O(2^n)'"
    return True, "All tests passed!"


def check_easy_p03(module):
    if not hasattr(module, 'growth_values'):
        return False, "Function 'growth_values' not found"
    expected = {"O(1)": 1, "O(log n)": 3, "O(n)": 8,
                "O(n log n)": 24, "O(n^2)": 64, "O(2^n)": 256}
    if module.growth_values(8) != expected:
        return False, f"growth_values(8) should be {expected}"
    if module.growth_values(16)["O(n^2)"] != 256:
        return False, "growth_values(16)['O(n^2)'] should be 256"
    if module.growth_values(16)["O(2^n)"] != 65536:
        return False, "growth_values(16)['O(2^n)'] should be 65536"
    return True, "All tests passed!"


def check_medium_p01(module):
    if not hasattr(module, 'count_pair_ops'):
        return False, "Function 'count_pair_ops' not found"
    if module.count_pair_ops(5) != 10:
        return False, "count_pair_ops(5) should be 10"
    if module.count_pair_ops(4) != 6:
        return False, "count_pair_ops(4) should be 6"
    if module.count_pair_ops(1) != 0:
        return False, "count_pair_ops(1) should be 0"
    if module.count_pair_ops(10) != 45:
        return False, "count_pair_ops(10) should be 45"
    return True, "All tests passed!"


def check_medium_p02(module):
    if not hasattr(module, 'phase_ops'):
        return False, "Function 'phase_ops' not found"
    if not hasattr(module, 'bottleneck_phase'):
        return False, "Function 'bottleneck_phase' not found"
    if module.phase_ops(8) != {"linear": 8, "nlogn": 24, "quadratic": 64}:
        return False, "phase_ops(8) should be {'linear': 8, 'nlogn': 24, 'quadratic': 64}"
    if module.bottleneck_phase(8) != "quadratic":
        return False, "bottleneck_phase(8) should be 'quadratic'"
    if module.bottleneck_phase(2) != "quadratic":
        return False, "bottleneck_phase(2) should be 'quadratic'"
    return True, "All tests passed!"


def check_medium_p03(module):
    if not hasattr(module, 'count_comparisons'):
        return False, "Function 'count_comparisons' not found"
    if module.count_comparisons([5, 9, 2, 7], 5) != 1:
        return False, "count_comparisons([5,9,2,7],5) should be 1 (best case)"
    if module.count_comparisons([5, 9, 2, 7], 7) != 4:
        return False, "count_comparisons([5,9,2,7],7) should be 4"
    if module.count_comparisons([5, 9, 2, 7], 99) != 4:
        return False, "count_comparisons([5,9,2,7],99) should be 4 (worst case)"
    if module.count_comparisons([], 1) != 0:
        return False, "count_comparisons([],1) should be 0"
    return True, "All tests passed!"


def check_hard_p01(module):
    if not hasattr(module, 'dedup_naive'):
        return False, "Function 'dedup_naive' not found"
    if not hasattr(module, 'dedup_set'):
        return False, "Function 'dedup_set' not found"
    if module.dedup_naive([1, 2, 2, 3]) != ([1, 2, 3], 5):
        return False, "dedup_naive([1,2,2,3]) should be ([1,2,3], 5)"
    if module.dedup_set([1, 2, 2, 3]) != ([1, 2, 3], 4):
        return False, "dedup_set([1,2,2,3]) should be ([1,2,3], 4)"
    if module.dedup_naive([1, 2, 3, 4, 5]) != ([1, 2, 3, 4, 5], 10):
        return False, "dedup_naive([1,2,3,4,5]) should be ([1,2,3,4,5], 10)"
    return True, "All tests passed!"


def check_hard_p02(module):
    if not hasattr(module, 'fib_with_count'):
        return False, "Function 'fib_with_count' not found"
    if module.fib_with_count(0) != (0, 1):
        return False, "fib_with_count(0) should be (0, 1)"
    if module.fib_with_count(1) != (1, 1):
        return False, "fib_with_count(1) should be (1, 1)"
    if module.fib_with_count(5) != (5, 15):
        return False, "fib_with_count(5) should be (5, 15)"
    if module.fib_with_count(10) != (55, 177):
        return False, "fib_with_count(10) should be (55, 177)"
    return True, "All tests passed!"


def check_hard_p03(module):
    if not hasattr(module, 'pair_sum_slow'):
        return False, "Function 'pair_sum_slow' not found"
    if not hasattr(module, 'pair_sum_fast'):
        return False, "Function 'pair_sum_fast' not found"
    if module.pair_sum_slow([1, 4, 7, 2, 9], 11) != (True, 5):
        return False, "pair_sum_slow([1,4,7,2,9],11) should be (True, 5)"
    if module.pair_sum_fast([1, 4, 7, 2, 9], 11) != (True, 3):
        return False, "pair_sum_fast([1,4,7,2,9],11) should be (True, 3)"
    if module.pair_sum_slow([1, 2, 3], 10) != (False, 3):
        return False, "pair_sum_slow([1,2,3],10) should be (False, 3)"
    if module.pair_sum_fast([1, 2, 3], 10) != (False, 3):
        return False, "pair_sum_fast([1,2,3],10) should be (False, 3)"
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
        print("  DSA LESSON 01 — AUTO-CHECK ALL")
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
