"""
Auto-Check System — Lesson 06 (Functions Deep Dive)
=========================================================
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
    if module.greet("Akash") != "Hello, Akash!":
        return False, "greet('Akash') should be 'Hello, Akash!'"
    if module.greet("Dev", "Hi") != "Hi, Dev!":
        return False, "greet('Dev', 'Hi') should be 'Hi, Dev!'"
    return True, "All tests passed!"


def check_easy_p02(module):
    if not hasattr(module, 'sum_all'):
        return False, "Function 'sum_all' not found"
    if module.sum_all(1, 2, 3) != 6:
        return False, "sum_all(1, 2, 3) should be 6"
    if module.sum_all() != 0:
        return False, "sum_all() should be 0"
    if module.sum_all(10) != 10:
        return False, "sum_all(10) should be 10"
    return True, "All tests passed!"


def check_easy_p03(module):
    if not hasattr(module, 'square'):
        return False, "Variable 'square' (lambda) not found"
    if module.square(5) != 25:
        return False, "square(5) should be 25"
    if module.square(0) != 0:
        return False, "square(0) should be 0"
    if module.square(-3) != 9:
        return False, "square(-3) should be 9"
    return True, "All tests passed!"


def check_medium_p01(module):
    if not hasattr(module, 'make_tag'):
        return False, "Function 'make_tag' not found"
    if module.make_tag("a", "link", href="x.com") != '<a href="x.com">link</a>':
        return False, "make_tag('a', 'link', href='x.com') should be '<a href=\"x.com\">link</a>'"
    if module.make_tag("p", "hi") != "<p>hi</p>":
        return False, "make_tag('p', 'hi') should be '<p>hi</p>'"
    return True, "All tests passed!"


def check_medium_p02(module):
    if not hasattr(module, 'safe_append'):
        return False, "Function 'safe_append' not found"
    if module.safe_append(1) != [1]:
        return False, "safe_append(1) should be [1]"
    if module.safe_append(2) != [2]:
        return False, "safe_append(2) should be [2] (mutable default bug?)"
    if module.safe_append(1, [0]) != [0, 1]:
        return False, "safe_append(1, [0]) should be [0, 1]"
    return True, "All tests passed!"


def check_medium_p03(module):
    if not hasattr(module, 'apply_func'):
        return False, "Function 'apply_func' not found"
    if module.apply_func(lambda x: x * 2, [1, 2, 3]) != [2, 4, 6]:
        return False, "apply_func(lambda x: x*2, [1,2,3]) should be [2, 4, 6]"
    if module.apply_func(str, [1, 2]) != ["1", "2"]:
        return False, "apply_func(str, [1, 2]) should be ['1', '2']"
    return True, "All tests passed!"


def check_hard_p01(module):
    if not hasattr(module, 'make_counter'):
        return False, "Function 'make_counter' not found"
    c = module.make_counter()
    if c() != 1:
        return False, "make_counter() first call should return 1"
    if c() != 2:
        return False, "make_counter() second call should return 2"
    c2 = module.make_counter(10)
    if c2() != 11:
        return False, "make_counter(10) first call should return 11"
    return True, "All tests passed!"


def check_hard_p02(module):
    if not hasattr(module, 'compose'):
        return False, "Function 'compose' not found"
    h = module.compose(lambda x: x + 1, lambda x: x * 2)
    if h(3) != 7:
        return False, "compose(+1, *2)(3) should be 7"
    h2 = module.compose(str, lambda x: x + 1)
    if h2(4) != "5":
        return False, "compose(str, +1)(4) should be '5'"
    return True, "All tests passed!"


def check_hard_p03(module):
    if not hasattr(module, 'build_profile'):
        return False, "Function 'build_profile' not found"
    if not hasattr(module, 'format_profile'):
        return False, "Function 'format_profile' not found"
    p = module.build_profile("Akash", role="dev", level=5)
    if p.get("name") != "Akash" or p.get("role") != "dev" or p.get("level") != 5:
        return False, f"build_profile returned unexpected dict: {p}"
    f = module.format_profile(p)
    if "Akash" not in f or "role=dev" not in f or "level=5" not in f:
        return False, f"format_profile output missing expected parts: {f!r}"
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
        print("  LESSON 06 — AUTO-CHECK ALL")
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
