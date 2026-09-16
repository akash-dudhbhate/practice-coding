"""
Auto-Check System — Lesson 07: Pinia State Management
=====================================================
These .js files import 'vue' and 'pinia', so they can't run without
dependencies — but we CAN syntax-check them with `node --check` (parse only,
no execution) and then run STRUCTURAL checks on the required store pieces.

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
    unresolved imports like 'vue'/'pinia' are fine). Skipped if node is
    missing."""
    if not NODE:
        return True, "node not found — skipped syntax check"
    try:
        result = subprocess.run(
            [NODE, "--check", path],
            capture_output=True, text=True, timeout=15,
        )
    except Exception as e:
        if "NoneType" in str(e):
            print(f"FAIL — a function returned None — write the body!")
        else:
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
    """useCounterStore: count ref, double computed, increment/decrement."""
    return require_all(path, [
        ("defineStore from pinia", r"defineStore"),
        ("useCounterStore export", r"useCounterStore"),
        ("store id 'counter'", r"['\"]counter['\"]"),
        ("count ref", r"count\s*=\s*ref|const\s+count"),
        ("double computed", r"computed\s*\("),
        ("increment action", r"increment"),
        ("decrement action", r"decrement"),
        ("return statement", r"return\s*\{"),
    ])


def check_easy_p02(path):
    """Component using useCounterStore with storeToRefs."""
    return require_all(path, [
        ("store import/usage", r"useCounterStore"),
        ("storeToRefs", r"storeToRefs"),
        ("count exposed", r"count"),
        ("double exposed", r"double"),
        ("increment exposed", r"increment"),
        ("decrement exposed", r"decrement"),
        ("component/template", r"setup\s*\(|template|<template>|export\s+default"),
    ])


def check_easy_p03(path):
    """useThemeStore: dark ref + toggle action (+ $q.dark usage shown)."""
    return require_all(path, [
        ("defineStore", r"defineStore"),
        ("useThemeStore export", r"useThemeStore"),
        ("store id 'theme'", r"['\"]theme['\"]"),
        ("dark ref", r"dark"),
        ("toggle action", r"toggle"),
        ("$q.dark.set usage or mention", r"\$q\.dark|q\.dark|useQuasar|dark\.set"),
    ])


def check_medium_p01(path):
    """useCartStore: items, totalItems/totalPrice getters, 3 actions."""
    return require_all(path, [
        ("defineStore", r"defineStore"),
        ("useCartStore export", r"useCartStore"),
        ("store id 'cart'", r"['\"]cart['\"]"),
        ("items ref", r"items\s*=\s*ref|const\s+items"),
        ("totalItems getter", r"totalItems"),
        ("totalPrice getter", r"totalPrice"),
        ("addItem action", r"addItem"),
        ("removeItem action", r"removeItem"),
        ("clearCart action", r"clearCart"),
        ("reduce for totals", r"reduce\s*\("),
    ])


def check_medium_p02(path):
    """Two stores: useUserStore (login/logout) + useProductStore (fetch)."""
    return require_all(path, [
        ("defineStore", r"defineStore"),
        ("useUserStore", r"useUserStore"),
        ("useProductStore", r"useProductStore"),
        ("user state", r"user\s*=\s*ref|const\s+user"),
        ("login action", r"login"),
        ("logout action", r"logout"),
        ("products state", r"products"),
        ("fetchProducts action", r"fetchProducts"),
        ("async mock fetch", r"async|setTimeout|Promise"),
    ])


def check_medium_p03(path):
    """Persistent useUserStore: localStorage load/save via watch."""
    return require_all(path, [
        ("defineStore", r"defineStore"),
        ("useUserStore", r"useUserStore"),
        ("localStorage read", r"localStorage\.getItem"),
        ("localStorage write", r"localStorage\.(setItem|removeItem)"),
        ("JSON parse/stringify", r"JSON\.(parse|stringify)"),
        ("watch for auto-save", r"watch\s*\("),
        ("deep option", r"deep\s*:\s*true|deep"),
        ("login action", r"login"),
        ("logout action", r"logout"),
    ])


def check_hard_p01(path):
    """useAuthStore: user/token/isAuthenticated, async login, persist."""
    return require_all(path, [
        ("defineStore", r"defineStore"),
        ("useAuthStore", r"useAuthStore"),
        ("user state", r"user"),
        ("token state", r"token"),
        ("loading state", r"loading"),
        ("error state", r"error"),
        ("isAuthenticated getter", r"isAuthenticated"),
        ("async login", r"async\s+function\s+login|login.*async|async"),
        ("try/catch handling", r"try\s*\{|catch"),
        ("logout action", r"logout"),
        ("localStorage persistence", r"localStorage\."),
        ("login form component shown", r"<q-form|q-input|template|handleLogin"),
    ])


def check_hard_p02(path):
    """Three stores: user, cart, order — cart items become orders."""
    return require_all(path, [
        ("useUserStore", r"useUserStore"),
        ("useCartStore", r"useCartStore"),
        ("useOrderStore", r"useOrderStore"),
        ("orders state", r"orders"),
        ("createOrder action", r"createOrder"),
        ("userId reference", r"userId|user\.id|userName"),
        ("total computed", r"total"),
        ("addItem action", r"addItem"),
        ("clearCart action", r"clearCart"),
        ("checkout flow shown", r"checkout|createOrder\s*\("),
    ])


def check_hard_p03(path):
    """Cross-store: cart uses auth store; visibleCart, login_required,
    watcher clears cart on logout."""
    return require_all(path, [
        ("useAuthStore", r"useAuthStore"),
        ("useCartStore", r"useCartStore"),
        ("auth used inside cart", r"useAuthStore\s*\(\s*\)"),
        ("isAuthenticated getter", r"isAuthenticated"),
        ("visibleCart computed", r"visibleCart"),
        ("login_required guard", r"login_required|login required|not authenticated|!authStore"),
        ("watch on auth state", r"watch\s*\("),
        ("clearCart on logout", r"clearCart"),
        ("addItem action", r"addItem"),
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
    Matches easy/p01-*.js (or other extensions), excluding solutions/."""
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
        if "NoneType" in str(e):
            print(f"FAIL — a function returned None — write the body!")
        else:
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
        print("  LESSON 07 — AUTO-CHECK ALL")
        print("=" * 60)
        for check_id in CHECKS:
            run_one(check_id)
        print("=" * 60)
        return

    run_one(target)


if __name__ == "__main__":
    main()
