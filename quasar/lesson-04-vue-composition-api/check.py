"""
Auto-Check System — Lesson 04: Vue Composition API
==================================================
.vue files can't execute without a Quasar build step, so these checks are
STRUCTURAL: they verify the required components, props, directives, and
hooks are present in your solution file.

Usage:
    python3 check.py easy/p01     # check one problem
    python3 check.py all          # check all problems
"""

import glob
import os
import re
import sys

LESSON_DIR = os.path.dirname(os.path.abspath(__file__))


def read_body(path):
    """Read a solution file, stripping the leading docstring comment so
    hint text in the problem description isn't mistaken for real code."""
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    content = re.sub(r"^\s*<!--.*?-->", "", content, count=1, flags=re.DOTALL)
    content = re.sub(r"^\s*/\*.*?\*/", "", content, count=1, flags=re.DOTALL)
    return content


def require_all(path, checks):
    """checks: list of (label, regex). Returns (passed, message)."""
    if not os.path.isfile(path):
        return False, f"file not found: {path}"
    body = read_body(path)
    if len(body.strip()) < 30:
        return False, "file looks empty — write your solution first"
    for label, pattern in checks:
        if not re.search(pattern, body):
            return False, f"missing {label} (expected pattern: {pattern})"
    return True, "All tests passed!"


def check_easy_p01(path):
    """Counter using ref(0) with increment/decrement buttons."""
    return require_all(path, [
        ("<template> block", r"<template>"),
        ("<script setup> block", r"<script\s+setup>"),
        ("ref import/usage", r"ref\s*\("),
        ("count ref", r"count"),
        ("increment control", r"increment|\+\+|\+=\s*1"),
        ("decrement control", r"decrement|--|-=\s*1"),
        ("button component", r"<q-btn|<button"),
    ])


def check_easy_p02(path):
    """Reactive user object with name/email/role + change-name button."""
    return require_all(path, [
        ("<template> block", r"<template>"),
        ("<script setup> block", r"<script\s+setup>"),
        ("reactive() usage", r"reactive\s*\("),
        ("name property", r"name"),
        ("email property", r"email"),
        ("role property", r"role"),
        ("change-name button", r"<q-btn|<button"),
    ])


def check_easy_p03(path):
    """Computed fullName from firstName/lastName refs + two inputs."""
    return require_all(path, [
        ("<template> block", r"<template>"),
        ("<script setup> block", r"<script\s+setup>"),
        ("firstName ref", r"firstName"),
        ("lastName ref", r"lastName"),
        ("computed() fullName", r"computed\s*\("),
        ("fullName displayed", r"fullName"),
        ("v-model inputs", r"v-model"),
        ("<q-input> fields", r"<q-input|<input"),
    ])


def check_medium_p01(path):
    """Shopping cart: items ref, computed totalPrice, add/remove."""
    return require_all(path, [
        ("<template> block", r"<template>"),
        ("<script setup> block", r"<script\s+setup>"),
        ("items ref", r"items"),
        ("name+price item shape", r"price"),
        ("computed total", r"computed\s*\("),
        ("reduce for sum", r"reduce\s*\("),
        ("add item function", r"add"),
        ("remove item function", r"remove|splice"),
        ("v-for list", r"v-for"),
    ])


def check_medium_p02(path):
    """Search filter: searchQuery ref, computed filteredItems, watch log."""
    return require_all(path, [
        ("<template> block", r"<template>"),
        ("<script setup> block", r"<script\s+setup>"),
        ("searchQuery ref", r"search"),
        ("items ref", r"items"),
        ("computed filter", r"computed\s*\("),
        (".filter() usage", r"\.filter\s*\("),
        ("watch() on query", r"watch\s*\("),
        ("console.log in watcher", r"console\.log"),
        ("v-model on search input", r"v-model"),
    ])


def check_medium_p03(path):
    """Timer: setInterval in onMounted, clearInterval in onUnmounted."""
    return require_all(path, [
        ("<template> block", r"<template>"),
        ("<script setup> block", r"<script\s+setup>"),
        ("elapsed ref", r"elapsed|seconds|time"),
        ("setInterval", r"setInterval\s*\("),
        ("clearInterval", r"clearInterval\s*\("),
        ("onMounted hook", r"onMounted"),
        ("onUnmounted hook", r"onUnmounted"),
        ("start control", r"[Ss]tart"),
        ("stop control", r"[Ss]top"),
    ])


def check_hard_p01(path):
    """Inline useCounter composable returning count/double/inc/dec/reset."""
    return require_all(path, [
        ("<template> block", r"<template>"),
        ("<script setup> block", r"<script\s+setup>"),
        ("useCounter function", r"function\s+useCounter|const\s+useCounter"),
        ("returns count", r"count"),
        ("computed double", r"computed\s*\("),
        ("increment fn", r"increment"),
        ("decrement fn", r"decrement"),
        ("reset fn", r"reset"),
        ("composable invoked", r"useCounter\s*\("),
        ("double displayed", r"double"),
    ])


def check_hard_p02(path):
    """Reactive form {name,email,age,agree} + computed isValid + watch."""
    return require_all(path, [
        ("<template> block", r"<template>"),
        ("<script setup> block", r"<script\s+setup>"),
        ("reactive() form", r"reactive\s*\("),
        ("name field", r"name"),
        ("email field", r"email"),
        ("age field", r"age"),
        ("agree field", r"agree"),
        ("computed isValid", r"computed\s*\("),
        ("isValid usage", r"isValid"),
        ("@ check on email", r"includes\s*\(\s*['\"]@"),
        ("disable binding", r":disable|disabled"),
        ("watch() on isValid", r"watch\s*\("),
        ("toggle/checkbox for agree", r"<q-toggle|<q-checkbox|<input"),
    ])


def check_hard_p03(path):
    """Mouse tracker: mousemove listener + template ref div."""
    return require_all(path, [
        ("<template> block", r"<template>"),
        ("<script setup> block", r"<script\s+setup>"),
        ("x coordinate ref", r"[Xx]\b"),
        ("y coordinate ref", r"[Yy]\b"),
        ("mousemove listener", r"mousemove"),
        ("addEventListener", r"addEventListener"),
        ("removeEventListener", r"removeEventListener"),
        ("onMounted hook", r"onMounted"),
        ("onUnmounted hook", r"onUnmounted"),
        ("template ref on element", r"ref=\"|ref='"),
        ("ref(null) for element", r"ref\s*\(\s*null\s*\)"),
        ("offsetWidth logged", r"offsetWidth|clientWidth|getBoundingClientRect"),
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
    Matches easy/p01-*.vue (or other extensions), excluding solutions/."""
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
        print("  LESSON 04 — AUTO-CHECK ALL")
        print("=" * 60)
        for check_id in CHECKS:
            run_one(check_id)
        print("=" * 60)
        return

    run_one(target)


if __name__ == "__main__":
    main()
