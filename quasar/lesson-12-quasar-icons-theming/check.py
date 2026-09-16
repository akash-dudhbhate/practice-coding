"""
Auto-Check System — Lesson 12: Quasar Icons & Theming
=====================================================
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
    """5 icons (home/settings/user/bell/search), different sizes+colors, labels."""
    return require_all(path, [
        ("<template> block", r"<template>"),
        ("5 q-icon components", r"(<q-icon[\s\S]*){5,}|<q-icon"),
        ("home icon", r"home"),
        ("settings icon", r"settings"),
        ("user/person icon", r"person|account|user"),
        ("bell/notifications icon", r"notifications|bell"),
        ("search icon", r"search"),
        ("size prop", r"size="),
        ("color prop", r"color="),
        ("labels", r"<span|label|<div"),
        ("row layout", r"row"),
    ])


def check_easy_p02(path):
    """Typography classes (h4/subtitle1/body1/caption) + spacing utilities."""
    return require_all(path, [
        ("<template> block", r"<template>"),
        ("text-h4 title", r"text-h4"),
        ("text-subtitle1", r"text-subtitle1"),
        ("text-body1", r"text-body1"),
        ("text-caption", r"text-caption"),
        ("padding utility", r"q-pa-|q-p[xytblr]-"),
        ("margin utility", r"q-m[xytblr]-|q-mt-lg|q-mb-"),
    ])


def check_easy_p03(path):
    """Responsive grid: 3 cards with col-12 col-md-6 col-lg-4."""
    return require_all(path, [
        ("<template> block", r"<template>"),
        ("col-12 base", r"col-12"),
        ("col-md-6", r"col-md-6|col-sm-6"),
        ("col-lg-4", r"col-lg-4|col-md-4"),
        ("q-card components", r"<q-card"),
        ("icons in cards", r"<q-icon"),
        ("card titles", r"text-h6|title"),
        ("descriptions", r"description|text-body2|<p"),
        ("row + gutter", r"row|gutter"),
        ("v-for over cards", r"v-for"),
    ])


def check_medium_p01(path):
    """Brand colors: SCSS override shown + primary/secondary/accent usage."""
    return require_all(path, [
        ("<template> block", r"<template>"),
        ("primary color used", r"primary"),
        ("secondary color used", r"secondary"),
        ("accent color used", r"accent"),
        ("button(s) with color", r"<q-btn"),
        ("card", r"<q-card"),
        ("icon(s) with color", r"<q-icon"),
        ("bg- class usage", r"bg-"),
    ])


def check_medium_p02(path):
    """Dark mode: $q.dark toggle + .body--dark custom card styles."""
    return require_all(path, [
        ("<template> block", r"<template>"),
        ("<script setup> block", r"<script\s+setup>"),
        ("useQuasar", r"useQuasar|\$q"),
        ("dark toggle", r"dark\.set|dark\.toggle|darkMode|dark_mode"),
        ("toggle control", r"<q-toggle|<q-btn|<q-checkbox"),
        ("custom card class", r"custom|my-card|class="),
        ("body--dark styles", r"body--dark|body\.dark|dark.*\{|:global"),
        ("background override", r"background"),
        ("color override", r"color"),
        ("q-card present", r"<q-card"),
    ])


def check_medium_p03(path):
    """Theme switcher: 3 themes, --q-primary/--q-secondary, localStorage."""
    return require_all(path, [
        ("<template> block", r"<template>"),
        ("<script setup> block", r"<script\s+setup>"),
        ("themes array (3)", r"blue|green|purple|[Tt]heme"),
        ("theme buttons", r"<q-btn|v-for"),
        ("--q-primary set", r"--q-primary"),
        ("--q-secondary set", r"--q-secondary"),
        ("setProperty", r"setProperty|documentElement|style\."),
        ("localStorage save", r"localStorage\.setItem"),
        ("restore on mount", r"localStorage\.getItem|onMounted"),
        ("apply function", r"apply|setTheme|applyTheme"),
        ("preview shown", r"bg-primary|<q-card|preview|Preview"),
    ])


def check_hard_p01(path):
    """Themed dashboard: nav bar, stat grid, activity list, dark mode."""
    return require_all(path, [
        ("<template> block", r"<template>"),
        ("<script setup> block", r"<script\s+setup>"),
        ("nav bar/toolbar", r"<q-bar|<q-toolbar|<q-header"),
        ("dark mode toggle", r"dark_mode|dark\.toggle|\$q\.dark"),
        ("typography", r"text-h[456]|text-subtitle|text-caption"),
        ("responsive stat grid", r"col-12|col-sm|col-md|col-lg"),
        ("stat cards", r"<q-card"),
        ("stats data array", r"stats|stat"),
        ("icons", r"<q-icon"),
        ("activity list", r"<q-list|<q-item|activit"),
        ("action buttons", r"<q-btn"),
        ("spacing utilities", r"q-m[bt]|q-pa|q-gutter|q-col-gutter"),
        ("brand colors", r"bg-primary|color=\"primary\"|text-white"),
    ])


def check_hard_p02(path):
    """White-label theming: q-color pickers for 3 colors, persist, reset."""
    return require_all(path, [
        ("<template> block", r"<template>"),
        ("<script setup> block", r"<script\s+setup>"),
        ("theme object", r"theme|reactive|ref\s*\("),
        ("primary color", r"primary"),
        ("secondary color", r"secondary"),
        ("accent color", r"accent"),
        ("color picker", r"<q-color|type=\"color\"|color picker"),
        ("popup proxy", r"q-popup-proxy|<q-input|<q-menu"),
        ("CSS var set", r"--q-|setProperty"),
        ("localStorage persist", r"localStorage"),
        ("reset to default", r"[Rr]eset|default"),
        ("apply on mount", r"onMounted|getItem"),
        ("live preview", r"[Pp]review|:style|bg-"),
    ])


def check_hard_p03(path):
    """Responsive nav: q-layout, header tabs (gt-sm), footer tabs (lt-md)."""
    return require_all(path, [
        ("<template> block", r"<template>"),
        ("<script setup> block", r"<script\s+setup>"),
        ("q-layout", r"<q-layout"),
        ("view string", r"view="),
        ("q-header (desktop)", r"<q-header"),
        ("q-footer (mobile)", r"<q-footer"),
        ("q-tabs", r"<q-tabs"),
        ("q-tab entries", r"<q-tab"),
        ("gt-sm visibility class", r"gt-sm|gt-xs|gt-md"),
        ("lt-md visibility class", r"lt-md|lt-lg|lt-sm"),
        ("shared activeTab ref", r"activeTab|v-model"),
        ("tab icons", r"icon="),
        ("tab labels", r"label="),
        ("tab panels/content", r"q-tab-panels|q-tab-panel|q-page"),
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
        print("  LESSON 12 — AUTO-CHECK ALL")
        print("=" * 60)
        for check_id in CHECKS:
            run_one(check_id)
        print("=" * 60)
        return

    run_one(target)


if __name__ == "__main__":
    main()
