"""
Auto-Check System — Lesson 08: Quasar Plugins
=============================================
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
    """4 buttons, each firing $q.notify with a different type."""
    return require_all(path, [
        ("<template> block", r"<template>"),
        ("<script setup> block", r"<script\s+setup>"),
        ("useQuasar", r"useQuasar"),
        ("$q.notify calls", r"\$q\.notify|notify\s*\("),
        ("positive type", r"['\"]positive['\"]"),
        ("negative type", r"['\"]negative['\"]"),
        ("warning type", r"['\"]warning['\"]"),
        ("info type", r"['\"]info['\"]"),
        ("buttons", r"<q-btn|<button"),
    ])


def check_easy_p02(path):
    """Dark mode toggle: $q.dark.toggle + isActive displayed."""
    return require_all(path, [
        ("<template> block", r"<template>"),
        ("<script setup> block", r"<script\s+setup>"),
        ("useQuasar", r"useQuasar"),
        ("dark toggle", r"\$q\.dark\.toggle|dark\.toggle"),
        ("dark state read", r"\$q\.dark\.isActive|dark\.isActive"),
        ("toggle button", r"<q-btn|<button|<q-toggle"),
        ("state displayed", r"dark|Dark|[Ll]ight"),
    ])


def check_easy_p03(path):
    """Platform detection: mobile/desktop, ios/android, browser name."""
    return require_all(path, [
        ("<template> block", r"<template>"),
        ("<script setup> block", r"<script\s+setup>"),
        ("useQuasar", r"useQuasar"),
        ("platform access", r"\$q\.platform|platform\.is"),
        ("mobile check", r"mobile"),
        ("desktop/other", r"desktop|Desktop"),
        ("ios check", r"ios|iOS"),
        ("android check", r"android|Android"),
        ("browser detection", r"chrome|firefox|safari|edge|browser|Browser"),
    ])


def check_medium_p01(path):
    """$q.dialog confirm → deleted notify; cancel → cancelled notify."""
    return require_all(path, [
        ("<template> block", r"<template>"),
        ("<script setup> block", r"<script\s+setup>"),
        ("useQuasar", r"useQuasar"),
        ("$q.dialog call", r"\$q\.dialog|dialog\s*\("),
        ("cancel option", r"cancel"),
        ("onOk handler", r"onOk"),
        ("onCancel handler", r"onCancel"),
        ("notify on result", r"notify"),
        ("delete button", r"[Dd]elete"),
    ])


def check_medium_p02(path):
    """Responsive grid: $q.screen breakpoint + col-* classes + q-cards."""
    return require_all(path, [
        ("<template> block", r"<template>"),
        ("<script setup> block", r"<script\s+setup>"),
        ("useQuasar", r"useQuasar"),
        ("$q.screen usage", r"\$q\.screen|screen\."),
        ("breakpoint name display", r"xs|sm|md|breakpoint|screen\.name"),
        ("grid column classes", r"col-"),
        ("q-card items", r"<q-card"),
        ("v-for grid", r"v-for"),
    ])


def check_medium_p03(path):
    """$q.loading.show during save + hide in finally + notify result."""
    return require_all(path, [
        ("<template> block", r"<template>"),
        ("<script setup> block", r"<script\s+setup>"),
        ("useQuasar", r"useQuasar"),
        ("loading.show", r"loading\.show|\$q\.loading"),
        ("loading.hide", r"loading\.hide|\.hide\s*\("),
        ("finally block", r"finally"),
        ("simulated async", r"setTimeout|Promise|await"),
        ("q-form submit", r"<q-form|@submit|handleSubmit|onSubmit"),
        ("success notify", r"notify"),
        ("form inputs", r"<q-input|<input"),
    ])


def check_hard_p01(path):
    """useNotifications composable with presets + Undo action."""
    return require_all(path, [
        ("<template> block", r"<template>"),
        ("<script setup> block", r"<script\s+setup>"),
        ("useQuasar", r"useQuasar"),
        ("composable function", r"useNotifications|useNotify"),
        ("presets map", r"presets|success.*type|type.*positive"),
        ("success preset", r"success"),
        ("error preset", r"error"),
        ("warning preset", r"warning"),
        ("info preset", r"info"),
        ("undo action", r"[Uu]ndo"),
        ("actions array", r"actions"),
        ("icon per preset", r"icon"),
        ("timeout per preset", r"timeout"),
    ])


def check_hard_p02(path):
    """Platform-aware: q-menu on desktop, $q.bottomSheet on mobile, 4+ items."""
    return require_all(path, [
        ("<template> block", r"<template>"),
        ("<script setup> block", r"<script\s+setup>"),
        ("useQuasar", r"useQuasar"),
        ("platform check", r"\$q\.platform|platform\.is"),
        ("screen check", r"\$q\.screen|screen\."),
        ("mobile detection", r"mobile|isMobile|xs"),
        ("q-menu dropdown", r"<q-menu"),
        ("bottom sheet", r"bottomSheet|bottom-sheet|BottomSheet"),
        ("menu items array", r"menuItems|items"),
        ("v-for over items", r"v-for"),
        ("item icons", r"icon"),
    ])


def check_hard_p03(path):
    """Settings panel: dark toggle, notify position, persisted to storage."""
    return require_all(path, [
        ("<template> block", r"<template>"),
        ("<script setup> block", r"<script\s+setup>"),
        ("useQuasar", r"useQuasar"),
        ("dark mode toggle", r"<q-toggle|darkMode|dark\.set|\$q\.dark"),
        ("notification position", r"position|notifyPosition"),
        ("localStorage save", r"localStorage\.setItem"),
        ("localStorage load", r"localStorage\.getItem"),
        ("JSON serialize", r"JSON\.(stringify|parse)"),
        ("load on mount", r"onMounted|loadSettings|created\s*\("),
        ("apply dark setting", r"dark\.set|applyDark"),
        ("test notification", r"notify|notification"),
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
        print("  LESSON 08 — AUTO-CHECK ALL")
        print("=" * 60)
        for check_id in CHECKS:
            run_one(check_id)
        print("=" * 60)
        return

    run_one(target)


if __name__ == "__main__":
    main()
