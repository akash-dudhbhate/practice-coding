"""
Auto-Check System — Lesson 14: Quasar Notifications & Dialogs
=============================================================
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
    """4 notify types with custom message, icon, position."""
    return require_all(path, [
        ("<template> block", r"<template>"),
        ("<script setup> block", r"<script\s+setup>"),
        ("useQuasar", r"useQuasar"),
        ("$q.notify calls", r"\$q\.notify|notify\s*\("),
        ("positive type", r"positive"),
        ("negative type", r"negative"),
        ("warning type", r"warning"),
        ("info type", r"info"),
        ("custom messages", r"message"),
        ("icons", r"icon"),
        ("positions", r"position"),
        ("4 buttons", r"<q-btn|<button"),
    ])


def check_easy_p02(path):
    """Confirm dialog → deleted notify with Undo action; cancel → toast."""
    return require_all(path, [
        ("<template> block", r"<template>"),
        ("<script setup> block", r"<script\s+setup>"),
        ("useQuasar", r"useQuasar"),
        ("$q.dialog", r"\$q\.dialog|dialog\s*\("),
        ("cancel option", r"cancel"),
        ("onOk handler", r"onOk"),
        ("onCancel handler", r"onCancel"),
        ("deleted notification", r"notify"),
        ("Undo action", r"[Uu]ndo"),
        ("actions array", r"actions"),
        ("5s timeout", r"timeout"),
        ("undo handler notify", r"handler"),
    ])


def check_easy_p03(path):
    """Prompt dialog: text input validated non-empty, notify on OK."""
    return require_all(path, [
        ("<template> block", r"<template>"),
        ("<script setup> block", r"<script\s+setup>"),
        ("useQuasar", r"useQuasar"),
        ("$q.dialog", r"\$q\.dialog|dialog\s*\("),
        ("prompt option", r"prompt"),
        ("prompt model", r"model"),
        ("isValid validation", r"isValid|valid|length|trim"),
        ("cancel option", r"cancel"),
        ("onOk receives value", r"onOk"),
        ("notify with value", r"notify"),
        ("trigger button", r"<q-btn|<button|@click"),
    ])


def check_medium_p01(path):
    """Persistent loading notify (timeout:0) + dismiss + success toast."""
    return require_all(path, [
        ("<template> block", r"<template>"),
        ("<script setup> block", r"<script\s+setup>"),
        ("useQuasar", r"useQuasar"),
        ("loading notify", r"\$q\.notify|notify\s*\("),
        ("spinner option", r"spinner"),
        ("timeout: 0 persistent", r"timeout\s*:\s*0"),
        ("dismiss function used", r"dismiss\s*\(|dismiss\b"),
        ("simulated delay", r"setTimeout|await|Promise"),
        ("success notification", r"positive|success|completed|Success"),
        ("loading state/disable", r"loading|:disable|disabled"),
    ])


def check_medium_p02(path):
    """$q.bottomSheet with 4 actions; notify on select."""
    return require_all(path, [
        ("<template> block", r"<template>"),
        ("<script setup> block", r"<script\s+setup>"),
        ("useQuasar", r"useQuasar"),
        ("bottomSheet call", r"bottomSheet|bottom-sheet|BottomSheet"),
        ("actions array", r"actions"),
        ("Share action", r"[Ss]hare"),
        ("Copy action", r"[Cc]opy"),
        ("Edit action", r"[Ee]dit"),
        ("Delete action", r"[Dd]elete"),
        ("action icons", r"icon"),
        ("onOk handler", r"onOk"),
        ("notify on select", r"notify"),
        ("trigger button", r"<q-btn|<button|@click"),
    ])


def check_medium_p03(path):
    """Custom dialog component (name+email form) via $q.dialog component."""
    return require_all(path, [
        ("<template> block", r"<template>"),
        ("<script setup> block", r"<script\s+setup>"),
        ("useQuasar", r"useQuasar"),
        ("custom component", r"defineComponent|component\s*:|component:"),
        ("dialog call", r"\$q\.dialog|dialog\s*\("),
        ("name field", r"name"),
        ("email field", r"email"),
        ("emit/ok payload", r"emit|['\"]ok['\"]|onOk"),
        ("notify with data", r"notify"),
        ("dialog inputs", r"q-input|<input"),
        ("trigger button", r"<q-btn|<button|@click"),
    ])


def check_hard_p01(path):
    """useCrudNotifications: loading toast, success/error, delete+undo."""
    return require_all(path, [
        ("<template> block", r"<template>"),
        ("<script setup> block", r"<script\s+setup>"),
        ("useQuasar", r"useQuasar"),
        ("composable", r"useCrudNotifications|useCrud|useNotif"),
        ("create op", r"create|[Cc]reate"),
        ("update op", r"update|[Uu]pdate"),
        ("delete/remove op", r"remove|delete|[Dd]elete"),
        ("loading notify", r"spinner|timeout\s*:\s*0|loading|Loading"),
        ("success notify", r"positive|success|Success"),
        ("error notify", r"negative|error|Error"),
        ("dismiss used", r"dismiss"),
        ("undo action", r"[Uu]ndo"),
        ("actions array", r"actions"),
        ("3 trigger buttons", r"<q-btn|<button"),
    ])


def check_hard_p02(path):
    """Multi-step dialog wizard: 3 steps, per-step validation, emit data."""
    return require_all(path, [
        ("<template> block", r"<template>"),
        ("<script setup> block", r"<script\s+setup>"),
        ("useQuasar", r"useQuasar"),
        ("custom dialog component", r"defineComponent|component\s*:"),
        ("step state", r"step"),
        ("form data", r"form|name|email"),
        ("validation", r"validate|errors|error"),
        ("next navigation", r"next|step\s*\+"),
        ("back navigation", r"prev|back|step\s*-"),
        ("finish emits data", r"emit|['\"]ok['\"]"),
        ("progress indicator", r"q-linear-progress|step.*of|progress"),
        ("dialog call", r"\$q\.dialog|dialog\s*\("),
        ("onOk notify", r"onOk"),
        ("notify", r"notify"),
    ])


def check_hard_p03(path):
    """Notification center: bell + badge, dropdown list, read state, persist."""
    return require_all(path, [
        ("<template> block", r"<template>"),
        ("<script setup> block", r"<script\s+setup>"),
        ("bell icon button", r"notifications|<q-btn|bell"),
        ("unread badge", r"<q-badge|badge|unreadCount|unread"),
        ("dropdown menu", r"<q-menu|dropdown|<q-card"),
        ("notifications array", r"notifications"),
        ("notification types", r"info|warning|error"),
        ("mark as read", r"read|markAsRead|markAllRead"),
        ("unread count computed", r"computed|filter"),
        ("list rendering", r"v-for|<q-item|<q-list"),
        ("localStorage persist", r"localStorage"),
        ("watch for save", r"watch\s*\("),
        ("type→icon/color map", r"iconForType|colorForType|icon.*type|color.*type"),
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
        print("  LESSON 14 — AUTO-CHECK ALL")
        print("=" * 60)
        for check_id in CHECKS:
            run_one(check_id)
        print("=" * 60)
        return

    run_one(target)


if __name__ == "__main__":
    main()
