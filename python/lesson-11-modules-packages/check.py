"""
Auto-Check System — Lesson 11 (Modules & Packages)
==================================================
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
    if not hasattr(module, 'greet'):
        return False, "Function 'greet' not found"
    if not hasattr(module, 'PI'):
        return False, "Constant 'PI' not found"
    if module.greet("World") != "Hello, World!":
        return False, f"greet('World') should return 'Hello, World!', got {module.greet('World')!r}"
    if module.PI != 3.14159:
        return False, f"PI should be 3.14159, got {module.PI}"
    return True, "All tests passed!"


def check_easy_p02(module):
    if not hasattr(module, 'math'):
        return False, "Module 'math' not imported at top level"
    if not hasattr(module, 'random'):
        return False, "Module 'random' not imported at top level"
    if module.math.sqrt(16) != 4.0:
        return False, "math.sqrt should be usable via the imported module"
    r = module.random.randint(1, 100)
    if not isinstance(r, int) or not (1 <= r <= 100):
        return False, f"random.randint(1, 100) gave unexpected {r!r}"
    return True, "All tests passed!"


def check_easy_p03(module):
    if not hasattr(module, 'reverse_string'):
        return False, "Function 'reverse_string' not found"
    if not hasattr(module, 'count_vowels'):
        return False, "Function 'count_vowels' not found"
    if module.reverse_string("hello") != "olleh":
        return False, "reverse_string('hello') should be 'olleh'"
    if module.count_vowels("hello") != 2:
        return False, "count_vowels('hello') should be 2"
    if module.count_vowels("AEiou") != 5:
        return False, "count_vowels should be case-insensitive"
    return True, "All tests passed!"


def check_medium_p01(module):
    if not hasattr(module, 'format_date'):
        return False, "Function 'format_date' not found"
    if not hasattr(module, 'User'):
        return False, "Class 'User' not found"
    from datetime import datetime
    if module.format_date(datetime(2024, 1, 15)) != "2024-01-15":
        return False, "format_date(datetime(2024,1,15)) should be '2024-01-15'"
    u = module.User("Akash", "akash@test.com")
    if u.name != "Akash" or u.email != "akash@test.com":
        return False, "User should store name and email attributes"
    if "Akash" not in str(u) or "akash@test.com" not in str(u):
        return False, "str(User) should contain name and email"
    return True, "All tests passed!"


def check_medium_p02(module):
    if not hasattr(module, 'celsius_to_fahrenheit'):
        return False, "Function 'celsius_to_fahrenheit' not found"
    if not hasattr(module, 'fahrenheit_to_celsius'):
        return False, "Function 'fahrenheit_to_celsius' not found"
    if module.celsius_to_fahrenheit(100) != 212.0:
        return False, "celsius_to_fahrenheit(100) should be 212.0"
    if module.fahrenheit_to_celsius(32) != 0.0:
        return False, "fahrenheit_to_celsius(32) should be 0.0"
    if abs(module.celsius_to_fahrenheit(37) - 98.6) > 0.01:
        return False, "celsius_to_fahrenheit(37) should be ~98.6"
    return True, "All tests passed!"


def check_medium_p03(module):
    if not hasattr(module, 'list_py_files'):
        return False, "Function 'list_py_files' not found"
    import tempfile
    d = tempfile.mkdtemp()
    with open(os.path.join(d, "a.py"), "w") as f:
        f.write("x = 1\n")
    with open(os.path.join(d, "b.py"), "w") as f:
        f.write("y = 22\n")
    with open(os.path.join(d, "c.txt"), "w") as f:
        f.write("not python\n")
    result = module.list_py_files(d)
    names = sorted(os.path.basename(n) for n, s in result)
    if names != ["a.py", "b.py"]:
        return False, f"Expected a.py and b.py, got {names}"
    for n, s in result:
        if not isinstance(s, int) or s <= 0:
            return False, f"Size for {n} should be a positive int, got {s!r}"
    return True, "All tests passed!"


def check_hard_p01(module):
    for fname in ['add', 'sub', 'mul', 'div', 'power', 'sqrt', 'factorial']:
        if not hasattr(module, fname):
            return False, f"Function '{fname}' not found"
    if module.add(2, 3) != 5 or module.sub(5, 2) != 3 or module.mul(3, 4) != 12:
        return False, "Basic ops failed"
    if module.div(10, 2) != 5.0:
        return False, "div(10, 2) should be 5.0"
    try:
        module.div(1, 0)
        return False, "div(1, 0) should raise ZeroDivisionError"
    except ZeroDivisionError:
        pass
    if module.power(2, 3) != 8 or module.sqrt(16) != 4.0 or module.factorial(5) != 120:
        return False, "Advanced ops failed"
    return True, "All tests passed!"


def check_hard_p02(module):
    if not hasattr(module, 'extract_imports'):
        return False, "Function 'extract_imports' not found"
    import tempfile
    d = tempfile.mkdtemp()
    path = os.path.join(d, "sample.py")
    with open(path, "w") as f:
        f.write("import os\nimport requests\nfrom flask import Flask\nimport sys\n")
    result = module.extract_imports(path)
    if result != ["flask", "requests"]:
        return False, f"Expected ['flask', 'requests'], got {result}"
    path2 = os.path.join(d, "stdlib_only.py")
    with open(path2, "w") as f:
        f.write("import os\nimport json\nfrom pathlib import Path\n")
    if module.extract_imports(path2) != []:
        return False, "Stdlib-only file should return []"
    return True, "All tests passed!"


def check_hard_p03(module):
    if not hasattr(module, 'load_plugins'):
        return False, "Function 'load_plugins' not found"
    import tempfile
    d = tempfile.mkdtemp()
    with open(os.path.join(d, "hello.py"), "w") as f:
        f.write("def run():\n    return 'hi'\n")
    with open(os.path.join(d, "_skip.py"), "w") as f:
        f.write("def run():\n    return 'should not load'\n")
    plugins = module.load_plugins(d)
    if len(plugins) != 1:
        return False, f"Expected 1 plugin, got {len(plugins)}"
    if plugins[0].run() != "hi":
        return False, f"plugin.run() should return 'hi', got {plugins[0].run()!r}"
    if module.load_plugins("/nonexistent_dir_xyz") != []:
        return False, "Missing directory should return []"
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
        print("  LESSON 11 — AUTO-CHECK ALL")
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
