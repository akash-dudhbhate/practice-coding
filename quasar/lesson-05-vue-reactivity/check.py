"""
Auto-Check System — Lesson 05: Vue Reactivity System
====================================================
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
    """ref (title) + reactive ({author, year}) side by side + update button."""
    return require_all(path, [
        ("<template> block", r"<template>"),
        ("<script setup> block", r"<script\s+setup>"),
        ("ref() for a string", r"ref\s*\("),
        ("reactive() for object", r"reactive\s*\("),
        ("author property", r"author"),
        ("year property", r"year"),
        ("update function/button", r"[Uu]pdate"),
        ("button component", r"<q-btn|<button"),
    ])


def check_easy_p02(path):
    """3-level nested reactive object: user.profile.settings.theme toggle."""
    return require_all(path, [
        ("<template> block", r"<template>"),
        ("<script setup> block", r"<script\s+setup>"),
        ("reactive() usage", r"reactive\s*\("),
        ("profile level", r"profile"),
        ("settings level", r"settings"),
        ("theme property", r"theme"),
        ("nested access chain", r"profile\.settings\.theme|settings:\s*\{"),
        ("toggle button", r"<q-btn|<button"),
    ])


def check_easy_p03(path):
    """Computed fullName rendered twice + console.log proving caching."""
    return require_all(path, [
        ("<template> block", r"<template>"),
        ("<script setup> block", r"<script\s+setup>"),
        ("firstName ref", r"firstName"),
        ("lastName ref", r"lastName"),
        ("computed() fullName", r"computed\s*\("),
        ("console.log inside computed", r"console\.log"),
        ("v-model inputs", r"v-model"),
        ("change-name trigger", r"<q-btn|<button|@click"),
    ])


def check_medium_p01(path):
    """watchEffect sets document.title from firstName + lastName."""
    return require_all(path, [
        ("<template> block", r"<template>"),
        ("<script setup> block", r"<script\s+setup>"),
        ("watchEffect import/usage", r"watchEffect\s*\("),
        ("document.title assignment", r"document\.title"),
        ("firstName ref", r"firstName"),
        ("lastName ref", r"lastName"),
        ("v-model inputs", r"v-model"),
    ])


def check_medium_p02(path):
    """watch on reactive property via getter + watch multiple sources."""
    return require_all(path, [
        ("<template> block", r"<template>"),
        ("<script setup> block", r"<script\s+setup>"),
        ("reactive() state", r"reactive\s*\("),
        ("count property", r"count"),
        ("name property", r"name"),
        ("watch() call", r"watch\s*\("),
        ("getter function source", r"\(\)\s*=>"),
        ("console.log old/new", r"console\.log"),
        ("buttons to mutate", r"<q-btn|<button"),
    ])


def check_medium_p03(path):
    """reactive form destructured via toRefs + watch on destructured ref."""
    return require_all(path, [
        ("<template> block", r"<template>"),
        ("<script setup> block", r"<script\s+setup>"),
        ("reactive() form", r"reactive\s*\("),
        ("toRefs destructure", r"toRefs\s*\("),
        ("name field", r"name"),
        ("email field", r"email"),
        ("watch() on ref", r"watch\s*\("),
        ("console.log", r"console\.log"),
        ("v-model bindings", r"v-model"),
    ])


def check_hard_p01(path):
    """computed vs function filtered list with call counters."""
    return require_all(path, [
        ("<template> block", r"<template>"),
        ("<script setup> block", r"<script\s+setup>"),
        ("filter input", r"filter"),
        ("computed version", r"computed\s*\("),
        ("computed call counter", r"computedCalls|computedCount"),
        ("function call counter", r"functionCalls|functionCount|methodCalls"),
        (".filter() on items", r"\.filter\s*\("),
        ("v-for list(s)", r"v-for"),
        ("counters displayed", r"\{\{[^}]*[Cc]alls"),
    ])


def check_hard_p02(path):
    """nextTick: v-if toggled input focused after DOM update."""
    return require_all(path, [
        ("<template> block", r"<template>"),
        ("<script setup> block", r"<script\s+setup>"),
        ("showInput ref", r"showInput|show|visible"),
        ("v-if on input wrapper", r"v-if"),
        ("template ref on input", r"ref=\"|ref='"),
        ("nextTick usage", r"nextTick"),
        ("await nextTick", r"await\s+nextTick"),
        ("focus() call", r"\.focus\s*\("),
        ("toggle function", r"[Tt]oggle"),
    ])


def check_hard_p03(path):
    """shallowRef 100 items: nested mutate no-ops, triggerRef/reassign work."""
    return require_all(path, [
        ("<template> block", r"<template>"),
        ("<script setup> block", r"<script\s+setup>"),
        ("shallowRef usage", r"shallowRef\s*\("),
        ("100 generated items", r"\b100\b"),
        ("nested mutation fn", r"[Mm]utate|items\.value\[0\]"),
        ("triggerRef call", r"triggerRef\s*\("),
        ("reassign .value fn", r"\.value\s*=\s*\["),
        ("three buttons", r"<q-btn|<button"),
        ("first item displayed", r"\[0\]|first"),
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
        print("  LESSON 05 — AUTO-CHECK ALL")
        print("=" * 60)
        for check_id in CHECKS:
            run_one(check_id)
        print("=" * 60)
        return

    run_one(target)


if __name__ == "__main__":
    main()
