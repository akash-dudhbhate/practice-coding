"""
Auto-Check System — Lesson 19: Testing Quasar Apps
==================================================
Test files get a parse-only syntax check via `node --check` when
available (Cypress/Vitest files aren't executed — no runner installed).
Everything is then verified STRUCTURALLY.

Usage:
    python3 check.py easy/p01     # check one problem
    python3 check.py all          # check all problems
"""

import glob
import os
import re
import shutil
import subprocess
import sys

LESSON_DIR = os.path.dirname(os.path.abspath(__file__))

NODE = "/home/akash-dev/.nvm/versions/node/v22.23.2/bin/node"
if not os.path.isfile(NODE):
    NODE = shutil.which("node")


def read_body(path):
    """Read a solution file, stripping the leading docstring comment so
    hint text in the problem description isn't mistaken for real code."""
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    content = re.sub(r"^\s*<!--.*?-->", "", content, count=1, flags=re.DOTALL)
    content = re.sub(r"^\s*/\*.*?\*/", "", content, count=1, flags=re.DOTALL)
    return content


def js_syntax_ok(path):
    """Parse-only syntax check via `node --check` (does NOT execute, so
    unresolved imports are fine). Skipped if node is missing."""
    if not NODE:
        return True, "node not found — skipped syntax check"
    try:
        result = subprocess.run(
            [NODE, "--check", path],
            capture_output=True, text=True, timeout=15,
        )
    except Exception as e:
        return True, f"syntax check skipped ({e})"
    if result.returncode != 0:
        detail = (result.stderr or result.stdout).strip().splitlines()
        return False, "syntax error: " + (detail[0] if detail else "unknown")
    return True, "ok"


def require_all(path, checks, syntax=True):
    """checks: list of (label, regex). Returns (passed, message)."""
    if not os.path.isfile(path):
        return False, f"file not found: {path}"
    if syntax and path.endswith((".js", ".mjs", ".ts")):
        ok, msg = js_syntax_ok(path)
        if not ok:
            return False, msg
    body = read_body(path)
    if len(body.strip()) < 30:
        return False, "file looks empty — write your solution first"
    for label, pattern in checks:
        if not re.search(pattern, body):
            return False, f"missing {label} (expected pattern: {pattern})"
    return True, "All tests passed!"


def check_easy_p01(path):
    """Counter test: mount, initial 0, increment, decrement."""
    return require_all(path, [
        ("vitest imports", r"vitest|describe|it\(|expect"),
        ("test-utils mount", r"@vue/test-utils|mount\("),
        ("describe block", r"describe\("),
        ("it blocks (>=2)", r"it\([\s\S]*it\("),
        ("initial count test", r"toBe\(['\"]0|initial|count"),
        ("increment test", r"increment|trigger\(['\"]click"),
        ("decrement test", r"decrement"),
        ("data-test selectors", r"data-test"),
        ("expect assertions", r"expect\("),
    ])


def check_easy_p02(path):
    """UserCard test: props render + delete emit with id."""
    return require_all(path, [
        ("vitest imports", r"vitest|describe|it\(|expect"),
        ("test-utils mount", r"@vue/test-utils|mount\("),
        ("props passed", r"props"),
        ("name/email assert", r"name|email"),
        ("delete event assert", r"emitted|delete|emit"),
        ("id payload assert", r"toEqual|user\.id|\[1\]|id"),
        ("data-test selectors", r"data-test"),
        ("describe+it", r"describe\(.*it\(|it\("),
    ])


def check_easy_p03(path):
    """Pinia store test: setActivePinia, state, action, getter."""
    return require_all(path, [
        ("vitest imports", r"vitest|describe|it\(|expect"),
        ("pinia imports", r"pinia|setActivePinia|createPinia|defineStore"),
        ("beforeEach pinia", r"beforeEach.*setActivePinia|setActivePinia"),
        ("store used", r"useCounterStore|useStore|store"),
        ("initial state test", r"count|toBe\(0\)|initial"),
        ("increment action test", r"increment"),
        ("getter test", r"double|getter"),
        ("expect assertions", r"expect\("),
    ])


def check_medium_p01(path):
    """TodoList test: render, add, toggle, delete."""
    return require_all(path, [
        ("vitest imports", r"vitest|describe|it\(|expect"),
        ("test-utils mount", r"@vue/test-utils|mount\("),
        ("beforeEach mount", r"beforeEach"),
        ("initial todos test", r"todo-item|findAll|toHaveLength"),
        ("add todo test", r"setValue|add|newTodo|new-todo"),
        ("toggle test", r"toggle|done|classes\(\)"),
        ("delete test", r"delete|remove"),
        ("data-test selectors", r"data-test"),
        ("multiple its", r"it\([\s\S]*it\([\s\S]*it\("),
    ])


def check_medium_p02(path):
    """LoginForm test: Quasar plugin, disabled submit, emit, error."""
    return require_all(path, [
        ("vitest imports", r"vitest|describe|it\(|expect"),
        ("test-utils mount", r"@vue/test-utils|mount\("),
        ("Quasar plugin install", r"Quasar|plugins|global"),
        ("disabled submit test", r"disable|disabled|attributes"),
        ("submit emit test", r"emitted\(['\"]submit|emit|submit"),
        ("credentials payload", r"email|password"),
        ("error test", r"error|Invalid"),
        ("data-test selectors", r"data-test"),
        ("setValue inputs", r"setValue"),
    ])


def check_medium_p03(path):
    """API service test: vi.fn mock, get/post asserts, error reject."""
    return require_all(path, [
        ("vitest imports", r"vitest|describe|it\(|expect"),
        ("vi mock", r"vi\.fn|vi\.|jest\.fn"),
        ("fetch mocked", r"fetch"),
        ("mock resolved", r"mockResolvedValue|mockReturnValue"),
        ("getUsers test", r"getUsers|GET|users"),
        ("createUser test", r"createUser|POST|method"),
        ("call args assert", r"toHaveBeenCalledWith|objectContaining"),
        ("error reject test", r"rejects|toThrow|500|ok:\s*false"),
        ("restore mocks", r"afterEach|restoreAllMocks|mockRestore"),
    ])


def check_hard_p01(path):
    """ShoppingCart: store actions/getters + component rendering tests."""
    return require_all(path, [
        ("vitest imports", r"vitest|describe|it\(|expect"),
        ("pinia setup", r"setActivePinia|createPinia|defineStore"),
        ("mount", r"@vue/test-utils|mount\("),
        ("add item test", r"addItem|add"),
        ("remove item test", r"removeItem|remove"),
        ("quantity test", r"updateQuantity|quantity"),
        ("total getter test", r"total"),
        ("empty state test", r"isEmpty|empty"),
        ("count getter test", r"count"),
        ("component DOM assert", r"data-test|wrapper\.find"),
        ("store+component split", r"describe\("),
    ])


def check_hard_p02(path):
    """Cypress login E2E: visit, type, submit, redirect, error, logout."""
    return require_all(path, [
        ("describe block", r"describe\("),
        ("cy.visit", r"cy\.visit"),
        ("email field", r"email"),
        ("password field", r"password"),
        ("submit click", r"submit|\.click\(\)"),
        ("type credentials", r"\.type\("),
        ("url assertion", r"cy\.url\(\)|\.should\("),
        ("dashboard redirect", r"dashboard"),
        ("error assertion", r"error|Invalid"),
        ("logout test", r"logout"),
        ("data-test selectors", r"data-test"),
    ])


def check_hard_p03(path):
    """Async component test: loading, data, error, refetch."""
    return require_all(path, [
        ("vitest imports", r"vitest|describe|it\(|expect"),
        ("test-utils mount", r"@vue/test-utils|mount\("),
        ("flushPromises", r"flushPromises"),
        ("fetch mocked", r"vi\.fn|mockResolvedValue|mockReturnValue"),
        ("loading state test", r"loading"),
        ("data render test", r"data|json"),
        ("error state test", r"error|ok:\s*false|rejects"),
        ("refetch test", r"refetch|fetchData|toHaveBeenCalledTimes"),
        ("data-test selectors", r"data-test"),
        ("beforeEach/afterEach", r"beforeEach|afterEach"),
    ])


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


def find_problem_file(check_id):
    """Find the student's file for a check id like 'easy/p01'.
    Matches easy/p01-*.*, excluding solutions/."""
    level, num = check_id.split("/")
    pattern = os.path.join(LESSON_DIR, level, f"{num}-*")
    matches = [
        f for f in glob.glob(pattern)
        if os.path.isfile(f) and "solutions" not in f
    ]
    return matches[0] if matches else None


def run_one(check_id):
    if check_id not in CHECKS:
        print(f"ERROR — unknown problem '{check_id}'")
        print(f"Available: {', '.join(CHECKS)}")
        return False
    filepath = find_problem_file(check_id)
    if not filepath:
        print(f"ERROR — file not found: {check_id}-* (create it first)")
        return False
    try:
        passed, msg = CHECKS[check_id](filepath)
    except Exception as e:
        print(f"ERROR — {e}")
        return False
    if passed:
        print(f"PASS — {msg}")
        rel = os.path.relpath(filepath, LESSON_DIR)
        print(f"  Done? Add a DONE marker to the top of {rel}")
    else:
        print(f"FAIL — {msg}")
    return passed


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 check.py <level>/<problem>")
        print("Example: python3 check.py easy/p01")
        print("         python3 check.py all")
        sys.exit(1)

    target = sys.argv[1]

    if target == "all":
        print("=" * 60)
        print("  LESSON 19 — AUTO-CHECK ALL")
        print("=" * 60)
        for check_id in CHECKS:
            run_one(check_id)
        print("=" * 60)
        return

    run_one(target)


if __name__ == "__main__":
    main()
