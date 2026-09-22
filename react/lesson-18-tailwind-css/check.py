#!/usr/bin/env python3
"""
Lesson 18 — Tailwind CSS — structural checker.

.jsx files can't be imported or run directly (they need a JSX transform and a
React runtime), so these checks inspect your SOURCE text instead: component
name, hooks used, props, and JSX structure.

Usage:
    python3 check.py easy/p01      # check one problem
    python3 check.py all           # check all 9
"""
import glob
import os
import re
import sys

BASE = os.path.dirname(os.path.abspath(__file__))


def make_check(component=None, required=(), any_of=(), min_occurrences=None, jsx=True):
    """Build a structural check: file path -> (passed: bool, message: str)."""

    def check(path):
        try:
            with open(path, encoding="utf-8") as f:
                code = f.read()
        except OSError as exc:
            return False, f"could not read file: {exc}"

        if "export" not in code:
            return False, "no 'export' found — file still looks like a stub"
        if not re.search(r"\bfunction\b|=>|\bclass\b", code):
            return False, "no function/class component definition found"
        if jsx and not re.search(r"<[A-Za-z]", code):
            return False, "no JSX tags found — component should render JSX"
        if component and not re.search(r"\b" + re.escape(component) + r"\b", code):
            return False, f"component '{component}' not found"
        for token in required:
            if token not in code:
                return False, f"missing '{token}'"
        for group in any_of:
            if not any(t in code for t in group):
                return False, "missing one of: " + " | ".join(group)
        for token, count in (min_occurrences or {}).items():
            if code.count(token) < count:
                return False, f"expected at least {count}x '{token}'"
        return True, "looks good"

    return check


CHECKS = {
    "easy/p01": make_check(component="Card", required=("className", "bg-white", "rounded", "shadow", "p-6", "<h3", "<button", "hover:")),
    "easy/p02": make_check(component="ResponsiveGrid", required=("grid", "grid-cols-1", "md:grid-cols-2", "lg:grid-cols-3", "gap", "map", "key=")),
    "easy/p03": make_check(component="StyledButton", required=("<button", "className", "hover:", "focus:", "active:", "transition")),
    "medium/p01": make_check(component="Button", required=("variants", "sizes", "className", "variant", "size", "primary", "secondary", "danger"), any_of=(("clsx", "cn(", "classnames"),)),
    "medium/p02": make_check(component="Navbar", required=("hidden md:flex", "md:hidden", "useState", "className", "<nav", "open")),
    "medium/p03": make_check(component="StyledForm", required=("useState", "onChange", "label", "border-red-500", "focus:ring", "checkbox", "<select", "errors")),
    "hard/p01": make_check(component="Dashboard", required=("useState", "collapsed", "<aside", "<header", "<main", "grid", "<table", "className", "transition")),
    "hard/p02": make_check(component="DarkModeApp", required=("dark:", "localStorage", "useEffect", "useState", "classList", "documentElement", "dark")),
    "hard/p03": make_check(component="UIKitDemo", required=("Button", "Input", "Select", "Card", "Badge", "Alert", "Modal", "Tabs", "Accordion", "className"), min_occurrences={"function": 9}),
}


def find_file(check_id):
    diff, num = check_id.split("/")
    pattern = os.path.join(BASE, diff, num + "-*.jsx")
    hits = [
        p for p in glob.glob(pattern)
        if os.sep + "solutions" + os.sep not in p
    ]
    return hits[0] if hits else None


def run_one(check_id):
    path = find_file(check_id)
    if path is None:
        print(f"ERROR — no problem file found for {check_id} "
              f"(expected {check_id.split('/')[0]}/{check_id.split('/')[1]}-*.jsx)")
        return False
    try:
        passed, msg = CHECKS[check_id](path)
    except Exception as exc:  # never crash on a learner's file
        if "NoneType" in str(exc):
            print(f"FAIL — a function returned None — write the body!")
        else:
            print(f"ERROR — {exc}")
            return False
    rel = os.path.relpath(path, BASE)
    if passed:
        print(f"PASS — All tests passed! ({rel})")
        print("       Add '// DONE' at the top of the file to mark it complete.")
        return True
    print(f"FAIL — {msg} ({rel})")
    return False


def main(argv):
    if len(argv) != 2 or argv[1] in ("-h", "--help"):
        print(__doc__)
        return 2
    target = argv[1]
    if target == "all":
        ok = True
        for cid in CHECKS:
            ok = run_one(cid) and ok
        return 0 if ok else 1
    if target not in CHECKS:
        print(f"ERROR — unknown problem '{target}'. "
              f"Choose from: {', '.join(CHECKS)} or 'all'")
        return 2
    return 0 if run_one(target) else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
