"""
Auto-Check System — Lesson 07 (File I/O & Error Handling)
=========================================================
Usage:
    python3 check.py easy/p01
    python3 check.py all
"""

import os
import sys
import glob
import json
import tempfile
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


def _tmpfile(contents):
    fd, path = tempfile.mkstemp()
    with os.fdopen(fd, "w") as f:
        f.write(contents)
    return path


MISSING = "/nonexistent_path_xyz_123"


def check_easy_p01(module):
    if not hasattr(module, 'read_file'):
        return False, "Function 'read_file' not found"
    p = _tmpfile("hello")
    try:
        if module.read_file(p) != "hello":
            return False, "read_file should return file contents 'hello'"
        if module.read_file(MISSING) is not None:
            return False, "read_file(missing) should return None"
    finally:
        os.remove(p)
    return True, "All tests passed!"


def check_easy_p02(module):
    if not hasattr(module, 'write_file'):
        return False, "Function 'write_file' not found"
    p = tempfile.mktemp()
    try:
        if module.write_file(p, "content") is not True:
            return False, "write_file should return True on success"
        with open(p) as f:
            if f.read() != "content":
                return False, "file should contain 'content'"
    finally:
        if os.path.exists(p):
            os.remove(p)
    return True, "All tests passed!"


def check_easy_p03(module):
    if not hasattr(module, 'safe_int'):
        return False, "Function 'safe_int' not found"
    if module.safe_int("42") != 42:
        return False, "safe_int('42') should be 42"
    if module.safe_int("abc") is not None:
        return False, "safe_int('abc') should be None"
    if module.safe_int("") is not None:
        return False, "safe_int('') should be None"
    return True, "All tests passed!"


def check_medium_p01(module):
    if not hasattr(module, 'count_lines'):
        return False, "Function 'count_lines' not found"
    p = _tmpfile("line1\nline2\nline3\n")
    try:
        if module.count_lines(p) != 3:
            return False, "count_lines should return 3 for a 3-line file"
        if module.count_lines(MISSING) != 0:
            return False, "count_lines(missing) should return 0"
    finally:
        os.remove(p)
    return True, "All tests passed!"


def check_medium_p02(module):
    if not hasattr(module, 'append_log'):
        return False, "Function 'append_log' not found"
    p = tempfile.mktemp()
    try:
        module.append_log(p, "First")
        module.append_log(p, "Second")
        with open(p) as f:
            content = f.read()
        if content != "First\nSecond\n":
            return False, f"file should contain 'First\\nSecond\\n', got {content!r}"
    finally:
        if os.path.exists(p):
            os.remove(p)
    return True, "All tests passed!"


def check_medium_p03(module):
    if not hasattr(module, 'read_json'):
        return False, "Function 'read_json' not found"
    good = _tmpfile('{"key": "val"}')
    bad = _tmpfile("not json")
    try:
        if module.read_json(good) != {"key": "val"}:
            return False, "read_json should return {'key': 'val'}"
        if module.read_json(MISSING) is not None:
            return False, "read_json(missing) should return None"
        if module.read_json(bad) is not None:
            return False, "read_json(bad json) should return None"
    finally:
        os.remove(good)
        os.remove(bad)
    return True, "All tests passed!"


def check_hard_p01(module):
    if not hasattr(module, 'DivideByZeroError'):
        return False, "Class 'DivideByZeroError' not found"
    if not hasattr(module, 'safe_divide'):
        return False, "Function 'safe_divide' not found"
    if module.safe_divide(10, 2) != 5.0:
        return False, "safe_divide(10, 2) should be 5.0"
    try:
        module.safe_divide(1, 0)
        return False, "safe_divide(1, 0) should raise DivideByZeroError"
    except module.DivideByZeroError:
        pass
    except Exception as e:
        if "NoneType" in str(e):
            print(f"FAIL — a function returned None — write the body!")
        else:
            return False, f"safe_divide(1, 0) raised {type(e).__name__}, expected DivideByZeroError"
    try:
        module.safe_divide("a", 1)
        return False, "safe_divide('a', 1) should raise TypeError"
    except TypeError:
        pass
    except Exception as e:
        if "NoneType" in str(e):
            print(f"FAIL — a function returned None — write the body!")
        else:
            return False, f"safe_divide('a', 1) raised {type(e).__name__}, expected TypeError"
    return True, "All tests passed!"


def check_hard_p02(module):
    if not hasattr(module, 'process_file'):
        return False, "Function 'process_file' not found"
    p = _tmpfile("10\n20\n\nabc\n30\n")
    try:
        if module.process_file(p) != 60:
            return False, "process_file should return 60 (10+20+30, skipping blank and 'abc')"
        try:
            module.process_file(MISSING)
            return False, "process_file(missing) should raise FileNotFoundError"
        except FileNotFoundError:
            pass
    finally:
        os.remove(p)
    return True, "All tests passed!"


def check_hard_p03(module):
    if not hasattr(module, 'ConfigError'):
        return False, "Class 'ConfigError' not found"
    if not hasattr(module, 'config_loader'):
        return False, "Function 'config_loader' not found"
    good = _tmpfile('{"host": "localhost", "port": 8080}')
    nohost = _tmpfile('{"port": 8080}')
    bad = _tmpfile("not json")
    try:
        cfg = module.config_loader(good)
        if not isinstance(cfg, dict) or cfg.get("host") != "localhost":
            return False, "config_loader should return the parsed dict"
        for path, desc in [(nohost, "missing 'host' key"),
                           (bad, "invalid JSON"),
                           (MISSING, "missing file")]:
            try:
                module.config_loader(path)
                return False, f"config_loader with {desc} should raise ConfigError"
            except module.ConfigError:
                pass
            except Exception as e:
                if "NoneType" in str(e):
                    print(f"FAIL — a function returned None — write the body!")
                else:
                    return False, f"config_loader with {desc} raised {type(e).__name__}, expected ConfigError"
    finally:
        os.remove(good)
        os.remove(nohost)
        os.remove(bad)
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
        print("  LESSON 07 — AUTO-CHECK ALL")
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
