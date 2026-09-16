"""
Auto-Check System — Lesson 06: Vue Router in Quasar
===================================================
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
    """Page reading route.params.id via useRoute, displayed as User ID."""
    return require_all(path, [
        ("<template> block", r"<template>"),
        ("<script setup> block", r"<script\s+setup>"),
        ("useRoute import/call", r"useRoute\s*\("),
        ("params access", r"\.params"),
        ("id param", r"params\.id|params\[['\"]id"),
        ("user id displayed", r"[Uu]ser\s*ID|userId|params\.id"),
        ("vue-router import", r"from\s+['\"]vue-router['\"]"),
    ])


def check_easy_p02(path):
    """Nav menu: 3 q-items with to prop + active class highlighting."""
    return require_all(path, [
        ("<template> block", r"<template>"),
        ("<script setup> block", r"<script\s+setup>"),
        ("q-item components", r"<q-item"),
        ("to prop for routing", r":to=|\bto="),
        ("Home link", r"[Hh]ome"),
        ("About link", r"[Aa]bout"),
        ("Contact link", r"[Cc]ontact"),
        ("active class highlight", r"active-class|exact-active-class|exact"),
    ])


def check_easy_p03(path):
    """Query params (q, page) + Next Page button via router.push."""
    return require_all(path, [
        ("<template> block", r"<template>"),
        ("<script setup> block", r"<script\s+setup>"),
        ("useRoute call", r"useRoute\s*\("),
        ("useRouter call", r"useRouter\s*\("),
        ("query param read", r"\.query"),
        ("page param", r"page"),
        ("router.push navigation", r"router\.push|\.push\s*\("),
        ("next-page button", r"[Nn]ext"),
    ])


def check_medium_p01(path):
    """Routes array: Home, About, catch-all 404, lazy imports, meta titles."""
    return require_all(path, [
        ("<template> block", r"<template>"),
        ("<script setup> block", r"<script\s+setup>"),
        ("routes array", r"routes\s*=\s*\["),
        ("lazy import", r"\(\)\s*=>\s*import\s*\("),
        ("home path", r"path:\s*['\"]/['\"]"),
        ("about path", r"['\"]/about['\"]"),
        ("catch-all 404", r"catchAll|\(\.\*\)\*|404|[Nn]ot[Ff]ound"),
        ("meta title", r"meta:\s*\{[^}]*title"),
    ])


def check_medium_p02(path):
    """onBeforeRouteLeave guard with window.confirm + next(false) cancel."""
    return require_all(path, [
        ("<template> block", r"<template>"),
        ("<script setup> block", r"<script\s+setup>"),
        ("onBeforeRouteLeave", r"onBeforeRouteLeave"),
        ("unsaved changes flag", r"unsaved|Unsaved|dirty|modified"),
        ("confirm dialog", r"confirm\s*\("),
        ("next(false) cancel", r"next\s*\(\s*false\s*\)"),
        ("next() allow", r"next\s*\(\s*\)"),
        ("form input", r"<q-input|<input"),
        ("save function/button", r"[Ss]ave"),
    ])


def check_medium_p03(path):
    """User list with 5 users, q-btn :to named route + params."""
    return require_all(path, [
        ("<template> block", r"<template>"),
        ("<script setup> block", r"<script\s+setup>"),
        ("users array", r"users"),
        ("5 users", r"id:\s*5|id:\s*\d[\s\S]*id:\s*\d[\s\S]*id:\s*\d"),
        ("v-for over users", r"v-for"),
        ("named route", r"name:\s*['\"][^'\"]+['\"]"),
        ("params with id", r"params:\s*\{[^}]*id"),
        ("q-btn :to link", r":to="),
        ("q-item rows", r"<q-item|<q-list|<li"),
    ])


def check_hard_p01(path):
    """Nested routes: MainLayout (Home/Dashboard/Settings) + BlankLayout
    (Login/Register), requiresAuth meta."""
    return require_all(path, [
        ("<template> block", r"<template>"),
        ("<script setup> block", r"<script\s+setup>"),
        ("routes array", r"routes\s*=\s*\["),
        ("MainLayout", r"MainLayout"),
        ("BlankLayout", r"BlankLayout"),
        ("children arrays", r"children\s*:\s*\["),
        ("lazy imports", r"\(\)\s*=>\s*import\s*\("),
        ("dashboard child", r"[Dd]ashboard"),
        ("settings child", r"[Ss]ettings"),
        ("login child", r"[Ll]ogin"),
        ("register child", r"[Rr]egister"),
        ("requiresAuth meta", r"requiresAuth"),
    ])


def check_hard_p02(path):
    """beforeEach guard: token check, requiresAuth→/login+redirect,
    guestOnly→/dashboard."""
    return require_all(path, [
        ("<template> block", r"<template>"),
        ("guard function", r"beforeEach|Guard"),
        ("localStorage token", r"localStorage\.getItem\s*\(\s*['\"]token['\"]"),
        ("requiresAuth check", r"requiresAuth"),
        ("login redirect", r"['\"]/login['\"]"),
        ("redirect query with fullPath", r"redirect.*fullPath|fullPath.*redirect"),
        ("guestOnly check", r"guestOnly"),
        ("dashboard redirect", r"['\"]/dashboard['\"]"),
        ("next() call", r"next\s*\("),
    ])


def check_hard_p03(path):
    """Product detail: params.id watch (immediate), mock fetch, router.push."""
    return require_all(path, [
        ("<template> block", r"<template>"),
        ("<script setup> block", r"<script\s+setup>"),
        ("useRoute call", r"useRoute\s*\("),
        ("useRouter call", r"useRouter\s*\("),
        ("params.id access", r"params\.id|params\[['\"]id"),
        ("mock products array", r"[Pp]roduct"),
        ("fetch/load function", r"fetch|load|setTimeout"),
        ("watch on param", r"watch\s*\("),
        ("immediate option", r"immediate\s*:\s*true"),
        ("loading state", r"loading"),
        ("router.push navigation", r"\.push\s*\("),
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
        print("  LESSON 06 — AUTO-CHECK ALL")
        print("=" * 60)
        for check_id in CHECKS:
            run_one(check_id)
        print("=" * 60)
        return

    run_one(target)


if __name__ == "__main__":
    main()
