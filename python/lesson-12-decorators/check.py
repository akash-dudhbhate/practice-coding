"""
Auto-Check System — Lesson 12 (Decorators)
==========================================
Usage:
    python3 check.py easy/p01
    python3 check.py all
"""

import os
import sys
import glob
import io
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


def check_easy_p01(module):
    if not hasattr(module, 'shout'):
        return False, "Decorator 'shout' not found"
    wrapped = module.shout(lambda name: f"hello {name}")
    if wrapped("world") != "HELLO WORLD":
        return False, "shout should uppercase the string return value"
    wrapped2 = module.shout(lambda: 42)
    if wrapped2() != 42:
        return False, "shout should pass non-string results through unchanged"
    return True, "All tests passed!"


def check_easy_p02(module):
    if not hasattr(module, 'timer'):
        return False, "Decorator 'timer' not found"
    wrapped = module.timer(lambda: "done")
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        result = wrapped()
    if result != "done":
        return False, "timer should return the function's result unchanged"
    out = buf.getvalue()
    if "took" not in out:
        return False, f"timer should print elapsed time, got: {out!r}"
    return True, "All tests passed!"


def check_easy_p03(module):
    if not hasattr(module, 'log_call'):
        return False, "Decorator 'log_call' not found"
    def sample(a, b):
        return a + b
    wrapped = module.log_call(sample)
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        result = wrapped(2, 3)
    if result != 5:
        return False, "log_call should return the function's result"
    out = buf.getvalue()
    if "sample" not in out:
        return False, "log_call should print the function name before calling"
    if "5" not in out:
        return False, "log_call should print the return value after calling"
    return True, "All tests passed!"


def check_medium_p01(module):
    if not hasattr(module, 'repeat'):
        return False, "Decorator factory 'repeat' not found"
    calls = {"n": 0}
    @module.repeat(3)
    def counter():
        calls["n"] += 1
        return calls["n"]
    result = counter()
    if calls["n"] != 3:
        return False, f"Expected 3 calls, got {calls['n']}"
    if result != 3:
        return False, f"Should return last result (3), got {result}"
    return True, "All tests passed!"


def check_medium_p02(module):
    if not hasattr(module, 'cache'):
        return False, "Decorator 'cache' not found"
    calls = {"n": 0}
    @module.cache
    def square(x):
        calls["n"] += 1
        return x * x
    if square(4) != 16:
        return False, "First call should return 16"
    if square(4) != 16:
        return False, "Cached call should still return 16"
    if calls["n"] != 1:
        return False, f"Function should run once for same args, ran {calls['n']} times"
    square(5)
    if calls["n"] != 2:
        return False, "New args should trigger a new computation"
    return True, "All tests passed!"


def check_medium_p03(module):
    if not hasattr(module, 'validate_positive'):
        return False, "Decorator 'validate_positive' not found"
    @module.validate_positive
    def area(w, h):
        return w * h
    if area(4, 5) != 20:
        return False, "Positive args should work normally"
    try:
        area(-1, 5)
        return False, "Should raise ValueError for negative arg"
    except ValueError:
        pass
    try:
        area(4, 0)
        return False, "Should raise ValueError for zero arg"
    except ValueError:
        pass
    return True, "All tests passed!"


def check_hard_p01(module):
    if not hasattr(module, 'CountCalls'):
        return False, "Class 'CountCalls' not found"
    @module.CountCalls
    def ping():
        return "pong"
    if ping() != "pong":
        return False, "Decorated function should still return its result"
    ping(); ping()
    if ping.count != 3:
        return False, f"Expected count=3, got {ping.count}"
    return True, "All tests passed!"


def check_hard_p02(module):
    if not hasattr(module, 'retry'):
        return False, "Decorator factory 'retry' not found"
    calls = {"n": 0}
    @module.retry(times=3, delay=0)
    def flaky():
        calls["n"] += 1
        if calls["n"] < 3:
            raise ValueError("boom")
        return "success"
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        result = flaky()
    if result != "success":
        return False, f"Expected 'success' on 3rd try, got {result!r}"
    if calls["n"] != 3:
        return False, f"Expected 3 attempts, got {calls['n']}"
    calls2 = {"n": 0}
    @module.retry(times=2, delay=0)
    def always_fail():
        calls2["n"] += 1
        raise RuntimeError("nope")
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            always_fail()
        return False, "Should re-raise after all attempts fail"
    except RuntimeError:
        pass
    if calls2["n"] != 2:
        return False, f"Expected exactly 2 attempts, got {calls2['n']}"
    return True, "All tests passed!"


def check_hard_p03(module):
    if not hasattr(module, 'log'):
        return False, "Decorator 'log' not found"
    if not hasattr(module, 'timer'):
        return False, "Decorator 'timer' not found"
    def sample(n):
        return n * 2
    wrapped = module.log(module.timer(sample))
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        result = wrapped(5)
    if result != 10:
        return False, f"Expected 10, got {result!r}"
    lines = [l for l in buf.getvalue().strip().splitlines() if l.strip()]
    if len(lines) < 2:
        return False, f"Expected both log and timer output, got: {lines}"
    if "sample" not in buf.getvalue():
        return False, "Output should mention the function name"
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
        if "NoneType" in str(e):
            print(f"FAIL — a function returned None — write the body!")
        else:
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
        print("  LESSON 12 — AUTO-CHECK ALL")
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

    if "/" not in target or target not in CHECKS:
        print(f"Error: unknown problem '{target}'")
        sys.exit(1)

    run_one(level_dir, target)


if __name__ == "__main__":
    main()
