"""
Auto-Check System — Lesson 13: Quasar Animations & Transitions
==============================================================
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
    """<Transition> + v-if toggle + fade CSS classes."""
    return require_all(path, [
        ("<template> block", r"<template>"),
        ("<script setup> block", r"<script\s+setup>"),
        ("Transition component", r"<[Tt]ransition"),
        ("v-if on content", r"v-if"),
        ("visible/show ref", r"visible|show"),
        ("toggle button", r"<q-btn|<button|@click"),
        ("enter-active CSS", r"enter-active"),
        ("leave-active CSS", r"leave-active"),
        ("enter-from CSS", r"enter-from|enter\b"),
        ("leave-to CSS", r"leave-to|leave\b"),
        ("opacity transition", r"opacity"),
        ("transition property", r"transition"),
    ])


def check_easy_p02(path):
    """q-slide-transition + v-show + Expand/Collapse button."""
    return require_all(path, [
        ("<template> block", r"<template>"),
        ("<script setup> block", r"<script\s+setup>"),
        ("q-slide-transition", r"q-slide-transition"),
        ("v-show (not v-if)", r"v-show"),
        ("expanded ref", r"expanded|expand"),
        ("toggle button", r"<q-btn|<button|@click"),
        ("expand/collapse label or icon", r"[Cc]ollapse|expand_more|expand_less"),
    ])


def check_easy_p03(path):
    """Skeleton card: q-skeleton during 2s load then real content."""
    return require_all(path, [
        ("<template> block", r"<template>"),
        ("<script setup> block", r"<script\s+setup>"),
        ("q-skeleton", r"<q-skeleton"),
        ("loading ref", r"loading"),
        ("setTimeout delay", r"setTimeout"),
        ("onMounted", r"onMounted"),
        ("v-if loading branch", r"v-if"),
        ("v-else content branch", r"v-else"),
        ("real image", r"<q-img|<img"),
        ("q-card", r"<q-card"),
        ("skeleton sizing", r"height|width|type="),
    ])


def check_medium_p01(path):
    """TransitionGroup list: add/remove items with slide animations."""
    return require_all(path, [
        ("<template> block", r"<template>"),
        ("<script setup> block", r"<script\s+setup>"),
        ("TransitionGroup", r"TransitionGroup|transition-group"),
        ("items array", r"items"),
        ("v-for keyed", r"v-for"),
        (":key binding", r":key"),
        ("add function", r"add|push"),
        ("remove function", r"remove|filter|splice"),
        ("enter CSS", r"enter-from|enter-active"),
        ("leave CSS", r"leave-to|leave-active"),
        ("translateX slide", r"translateX|translate"),
        ("move transition", r"-move|transition"),
    ])


def check_medium_p02(path):
    """v-intersection scroll-fade cards animating once."""
    return require_all(path, [
        ("<template> block", r"<template>"),
        ("<script setup> block", r"<script\s+setup>"),
        ("v-intersection directive", r"v-intersection|intersection"),
        ("once modifier", r"once"),
        ("5 cards", r"v-for|id:\s*5|length:\s*5|\{[^}]*title"),
        ("visible flag/class", r"visible|is-visible"),
        ("initial hidden style", r"opacity:\s*0|opacity\s*0"),
        ("translateY offset", r"translateY|translate"),
        ("transition style", r"transition"),
        ("icons", r"<q-icon|icon"),
    ])


def check_medium_p03(path):
    """Route transition: <Transition mode=out-in> around router-view."""
    return require_all(path, [
        ("<template> block", r"<template>"),
        ("router-view", r"router-view|router\s*view"),
        ("Transition wrapper", r"<[Tt]ransition"),
        ("mode out-in", r"out-in|mode="),
        ("named transition", r"name="),
        ("nav links/buttons", r"to=|<q-btn|router-link|href"),
        ("enter CSS", r"enter-active|enter-from"),
        ("leave CSS", r"leave-active|leave-to"),
        ("slide/fade", r"translate|opacity"),
    ])


def check_hard_p01(path):
    """FAQ accordion: q-expansion-item list, one open at a time."""
    return require_all(path, [
        ("<template> block", r"<template>"),
        ("<script setup> block", r"<script\s+setup>"),
        ("q-expansion-item or slide-transition", r"q-expansion-item|q-slide-transition|<q-item"),
        ("5 FAQs", r"v-for|question"),
        ("expanded state", r"expanded|v-model"),
        ("question labels", r"question|label"),
        ("answers", r"answer"),
        ("close-others logic", r"closeOthers|forEach|i\s*!==|!==\s*index|index\s*!=="),
        ("expand icon", r"expand|icon"),
        ("q-list wrapper", r"<q-list|bordered"),
    ])


def check_hard_p02(path):
    """Staggered entrance: 6 cards, index*100ms delay, hover scale."""
    return require_all(path, [
        ("<template> block", r"<template>"),
        ("<script setup> block", r"<script\s+setup>"),
        ("6 cards", r"v-for|id:\s*6|length:\s*6|\{[^}]*icon"),
        ("animation-delay binding", r"animationDelay|animation-delay|index\s*\*\s*100|\*\s*100"),
        ("@keyframes", r"@keyframes"),
        ("initial opacity 0", r"opacity:\s*0"),
        ("forwards fill", r"forwards"),
        ("transform translateY", r"translateY|translate"),
        ("hover scale", r":hover|scale"),
        ("grid columns", r"col-|row|gutter"),
        ("q-card", r"<q-card"),
        ("q-icon", r"<q-icon|icon"),
    ])


def check_hard_p03(path):
    """Loading experience: top bar + skeletons + fade-in content + notify."""
    return require_all(path, [
        ("<template> block", r"<template>"),
        ("<script setup> block", r"<script\s+setup>"),
        ("loading bar", r"q-linear-progress|q-ajax-bar|loading-bar|indeterminate"),
        ("loading ref", r"loading"),
        ("q-skeleton grid", r"<q-skeleton"),
        ("Transition(s)", r"<[Tt]ransition"),
        ("content after load", r"v-if|v-else"),
        ("setTimeout ~2s", r"setTimeout|2000"),
        ("onMounted initial load", r"onMounted"),
        ("success notify", r"notify"),
        ("reload button", r"[Rr]eload|[Rr]efresh|<q-btn"),
        ("GPU-friendly props", r"transform|opacity|will-change"),
        ("real content cards", r"<q-img|<img|<q-card"),
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
        print("  LESSON 13 — AUTO-CHECK ALL")
        print("=" * 60)
        for check_id in CHECKS:
            run_one(check_id)
        print("=" * 60)
        return

    run_one(target)


if __name__ == "__main__":
    main()
