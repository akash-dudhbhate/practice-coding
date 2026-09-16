#!/usr/bin/env python3
"""
Lesson 19 — Testing React — structural checker.

.test.jsx files can't be imported or run directly (they need a JSX transform
and a test runner), so these checks inspect your SOURCE text instead: render
calls, queries, events, mocks, and assertions.

Usage:
    python3 check.py easy/p01      # check one problem
    python3 check.py all           # check all 9
"""
import glob
import os
import re
import sys

BASE = os.path.dirname(os.path.abspath(__file__))


def make_check(component=None, required=(), any_of=(), min_occurrences=None, jsx=True, export_required=False):
    """Build a structural check: file path -> (passed: bool, message: str)."""

    def check(path):
        try:
            with open(path, encoding="utf-8") as f:
                code = f.read()
        except OSError as exc:
            return False, f"could not read file: {exc}"

        if export_required and "export" not in code:
            return False, "no 'export' found — file still looks like a stub"
        if "test(" not in code and "it(" not in code:
            return False, "no test()/it() blocks found — file still looks like a stub"
        if "expect(" not in code:
            return False, "no expect() assertions found — tests must assert something"
        if not re.search(r"\bfunction\b|=>|\bclass\b", code):
            return False, "no function/test definition found"
        if jsx and not re.search(r"<[A-Za-z]", code):
            return False, "no JSX tags found — render() should mount a component"
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
    "easy/p01": make_check(component="Greeting", required=("render(", "screen", "getByText", "toBeInTheDocument", "name=")),
    "easy/p02": make_check(component="Counter", required=("render(", "getByRole", "fireEvent.click", "toBeInTheDocument"), min_occurrences={"test(": 2, "it(": 0}),
    "easy/p03": make_check(component="Button", required=("render(", "getByRole", "label", "name:"), min_occurrences={"test(": 2}),
    "medium/p01": make_check(component="TodoList", required=("render(", "getByText", "fireEvent.change", "fireEvent.click", "toBeInTheDocument", "toHaveClass"), min_occurrences={"test(": 3}),
    "medium/p02": make_check(component="LoginForm", required=("jest.fn", "onSubmit", "fireEvent.change", "toBeDisabled", "toHaveBeenCalledWith", "invalid email"), min_occurrences={"test(": 3}),
    "medium/p03": make_check(component="UserProfile", required=("jest.spyOn", "mockResolvedValue", "mockRejectedValue", "waitFor", "loading", "async", "restoreAllMocks"), min_occurrences={"test(": 3}),
    "hard/p01": make_check(component="Modal", required=("open", "onClose", "jest.fn", "queryByText", "fireEvent", "Escape", "overflow", "getByTestId"), min_occurrences={"test(": 6}),
    "hard/p02": make_check(component="useFetch", required=("renderHook", "result.current", "waitFor", "jest.spyOn", "mockResolvedValue", "mockRejectedValue", "loading", "rerender"), min_occurrences={"test(": 4}, jsx=False),
    "hard/p03": make_check(component="CartProvider", required=("useCart", "addItem", "removeItem", "updateQty", "total", "fireEvent.click", "getByTestId", "Cart is empty"), min_occurrences={"test(": 5}),
}


def find_file(check_id):
    diff, num = check_id.split("/")
    for ext in ("jsx", "js"):
        pattern = os.path.join(BASE, diff, num + "-*." + ext)
        hits = [
            p for p in glob.glob(pattern)
            if os.sep + "solutions" + os.sep not in p
        ]
        if hits:
            return hits[0]
    return None


def run_one(check_id):
    path = find_file(check_id)
    if path is None:
        print(f"ERROR — no problem file found for {check_id} "
              f"(expected {check_id.split('/')[0]}/{check_id.split('/')[1]}-*.jsx)")
        return False
    try:
        passed, msg = CHECKS[check_id](path)
    except Exception as exc:  # never crash on a learner's file
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
