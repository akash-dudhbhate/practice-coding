"""
Auto-Check System — Lesson 15 (Testing with pytest)
=========================================================
Usage:
    python3 check.py easy/p01
    python3 check.py all
"""

import os
import sys
import glob
import subprocess
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


def _run_pytest(module):
    """Run pytest on the learner's file; return (ok, message)."""
    path = getattr(module, "__file__", None)
    if not path or not os.path.exists(path):
        return False, "cannot locate learner file to run pytest"
    try:
        proc = subprocess.run(
            [sys.executable, "-m", "pytest", path, "-q", "--no-header"],
            capture_output=True, text=True, timeout=60,
        )
    except FileNotFoundError:
        return False, "pytest is not installed (pip install pytest)"
    except subprocess.TimeoutExpired:
        return False, "pytest run timed out"
    if proc.returncode != 0:
        tail = (proc.stdout + proc.stderr).strip().splitlines()
        return False, "pytest failed: " + (tail[-1] if tail else "unknown")
    return True, "pytest passed"


def _has_tests(module):
    return any(name.startswith("test_") and callable(getattr(module, name))
               for name in dir(module))


def check_easy_p01(module):
    if not hasattr(module, 'is_palindrome'):
        return False, "Function 'is_palindrome' not found"
    if module.is_palindrome("racecar") is not True:
        return False, "is_palindrome('racecar') should be True"
    if module.is_palindrome("hello") is not False:
        return False, "is_palindrome('hello') should be False"
    if not _has_tests(module):
        return False, "No test_* functions found — write pytest tests too"
    return _run_pytest(module)


def check_easy_p02(module):
    if not hasattr(module, 'factorial'):
        return False, "Function 'factorial' not found"
    if module.factorial(5) != 120:
        return False, "factorial(5) should be 120"
    try:
        module.factorial(-1)
        return False, "factorial(-1) should raise ValueError"
    except ValueError:
        pass
    if not _has_tests(module):
        return False, "No test_* functions found — write pytest tests too"
    return _run_pytest(module)


def check_easy_p03(module):
    if not hasattr(module, 'sample_list'):
        return False, "Fixture 'sample_list' not found"
    if not _has_tests(module):
        return False, "No test_* functions found — write pytest tests too"
    return _run_pytest(module)


def check_medium_p01(module):
    if not hasattr(module, 'divide'):
        return False, "Function 'divide' not found"
    if module.divide(10, 2) != 5.0:
        return False, "divide(10, 2) should be 5.0"
    try:
        module.divide(1, 0)
        return False, "divide(1, 0) should raise ZeroDivisionError"
    except ZeroDivisionError:
        pass
    if not _has_tests(module):
        return False, "No test_* functions found — write pytest tests too"
    return _run_pytest(module)


def check_medium_p02(module):
    if not hasattr(module, 'temp_file'):
        return False, "Fixture 'temp_file' not found"
    if not _has_tests(module):
        return False, "No test_* functions found — write pytest tests too"
    return _run_pytest(module)


def check_medium_p03(module):
    if not hasattr(module, 'fetch_user'):
        return False, "Function 'fetch_user' not found"
    if not _has_tests(module):
        return False, "No test_* functions found — write pytest tests too"
    return _run_pytest(module)


def check_hard_p01(module):
    if not hasattr(module, 'BankAccount'):
        return False, "Class 'BankAccount' not found"
    acc = module.BankAccount("T", 100)
    acc.deposit(50)
    if acc.balance != 150:
        return False, "after deposit(50) balance should be 150"
    try:
        acc.withdraw(500)
        return False, "withdraw beyond balance should raise ValueError"
    except ValueError:
        pass
    if not _has_tests(module):
        return False, "No test_* functions found — write pytest tests too"
    return _run_pytest(module)


def check_hard_p02(module):
    if not hasattr(module, 'Stack'):
        return False, "Class 'Stack' not found"
    s = module.Stack()
    s.push(1)
    s.push(2)
    if s.pop() != 2:
        return False, "pop() should return 2"
    try:
        module.Stack().pop()
        return False, "pop() on empty stack should raise IndexError"
    except IndexError:
        pass
    if not _has_tests(module):
        return False, "No test_* functions found — write pytest tests too"
    return _run_pytest(module)


def check_hard_p03(module):
    if not hasattr(module, 'process_csv'):
        return False, "Function 'process_csv' not found"
    if not _has_tests(module):
        return False, "No test_* functions found — write pytest tests too"
    return _run_pytest(module)


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
        print("  LESSON 15 — AUTO-CHECK ALL")
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
