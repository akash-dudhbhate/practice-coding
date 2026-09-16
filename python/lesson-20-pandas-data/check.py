"""
Auto-Check System — Lesson 20 (Pandas & Data)
=========================================================
Usage:
    python3 check.py easy/p01
    python3 check.py all
"""

import os
import sys
import glob
import io
import tempfile
import contextlib
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


def _run_main(module):
    """Run module.main() inside a temp dir; return (stdout, tmpdir)."""
    if not hasattr(module, 'main'):
        return None, None
    tmpdir = tempfile.mkdtemp()
    old_cwd = os.getcwd()
    buf = io.StringIO()
    try:
        os.chdir(tmpdir)
        with contextlib.redirect_stdout(buf):
            module.main()
    finally:
        os.chdir(old_cwd)
    return buf.getvalue(), tmpdir


def check_easy_p01(module):
    if not hasattr(module, 'main'):
        return False, "Function 'main' not found"
    out, _ = _run_main(module)
    if "(5, 3)" not in out:
        return False, f"output should show shape (5, 3): {out[:200]!r}"
    for col in ("name", "age", "city"):
        if col not in out:
            return False, f"output should list column '{col}'"
    return True, "All tests passed!"


def check_easy_p02(module):
    if not hasattr(module, 'main'):
        return False, "Function 'main' not found"
    out, _ = _run_main(module)
    if "Diana" not in out or "28" not in out or "Mumbai" not in out:
        return False, f"filtered output should contain Diana/28/Mumbai: {out[:300]!r}"
    if "Bob" in out or "Alice" in out.split("Diana")[0][-200:]:
        # crude check that non-matching rows were filtered out
        lines = [l for l in out.splitlines() if "Bob" in l or "Alice" in l]
        if lines:
            return False, f"filtered output should exclude Bob/Alice rows: {lines!r}"
    return True, "All tests passed!"


def check_easy_p03(module):
    if not hasattr(module, 'main'):
        return False, "Function 'main' not found"
    out, _ = _run_main(module)
    if "Unknown" not in out:
        return False, f"output should show 'Unknown' for filled cities: {out[:300]!r}"
    if "30" not in out:
        return False, f"output should show mean-filled age 30.0: {out[:300]!r}"
    after = out.split("After")[-1]
    if "NaN" in after:
        return False, "after fillna there should be no NaN values"
    return True, "All tests passed!"


def check_medium_p01(module):
    if not hasattr(module, 'main'):
        return False, "Function 'main' not found"
    out, _ = _run_main(module)
    if "region" not in out.lower():
        return False, "output should include groupby by region"
    for region in ("North", "South", "East"):
        if region not in out:
            return False, f"output missing region '{region}'"
    if "430" not in out or "640" not in out:
        return False, "expected totals 430 (North) and 640 (East) in output"
    return True, "All tests passed!"


def check_medium_p02(module):
    if not hasattr(module, 'main'):
        return False, "Function 'main' not found"
    out, _ = _run_main(module)
    if "Alice" not in out or "1200" not in out:
        return False, "top user should be Alice with 1200 total"
    if "Bob" not in out or "900" not in out:
        return False, "second user should be Bob with 900 total"
    return True, "All tests passed!"


def check_medium_p03(module):
    if not hasattr(module, 'categorize'):
        return False, "Function 'categorize' not found"
    if module.categorize(18) != "teen":
        return False, "categorize(18) should be 'teen'"
    if module.categorize(35) != "adult":
        return False, "categorize(35) should be 'adult'"
    if module.categorize(70) != "senior":
        return False, "categorize(70) should be 'senior'"
    if not hasattr(module, 'main'):
        return False, "Function 'main' not found"
    out, tmpdir = _run_main(module)
    if "category" not in out:
        return False, "printed DataFrame should include a 'category' column"
    if not os.path.exists(os.path.join(tmpdir, "people_categorized.csv")):
        return False, "should export people_categorized.csv"
    return True, "All tests passed!"


def check_hard_p01(module):
    if not hasattr(module, 'get_grade'):
        return False, "Function 'get_grade' not found"
    if module.get_grade(95) != "A" or module.get_grade(65) != "D" or module.get_grade(50) != "F":
        return False, "get_grade boundaries wrong (95->A, 65->D, 50->F)"
    if not hasattr(module, 'main'):
        return False, "Function 'main' not found"
    out, tmpdir = _run_main(module)
    if "Pass" not in out or "Fail" not in out:
        return False, "output should report Pass/Fail counts"
    if not os.path.exists(os.path.join(tmpdir, "student_results.csv")):
        return False, "should export student_results.csv"
    return True, "All tests passed!"


def check_hard_p02(module):
    if not hasattr(module, 'main'):
        return False, "Function 'main' not found"
    out, tmpdir = _run_main(module)
    clean = os.path.join(tmpdir, "clean_data.csv")
    if not os.path.exists(clean):
        return False, "should export clean_data.csv"
    import pandas as pd
    df = pd.read_csv(clean)
    if df.isnull().any().any():
        return False, f"clean_data.csv still has NaN values:\n{df}"
    names = df["name"].astype(str)
    if any(n != n.strip() for n in names):
        return False, "names should be whitespace-stripped"
    if len(df) != len(df.drop_duplicates()):
        return False, "duplicates should be removed"
    return True, "All tests passed!"


def check_hard_p03(module):
    if not hasattr(module, 'main'):
        return False, "Function 'main' not found"
    out, _ = _run_main(module)
    low = out.lower()
    if "pivot" not in low:
        return False, "output should include a pivot table"
    if "trending" not in low:
        return False, "output should report trending products"
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
        print("  LESSON 20 — AUTO-CHECK ALL")
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
