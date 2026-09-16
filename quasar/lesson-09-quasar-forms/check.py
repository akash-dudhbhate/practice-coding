"""
Auto-Check System — Lesson 09: Quasar Forms
===========================================
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
    """Login form: email+password rules, submit → notify."""
    return require_all(path, [
        ("<template> block", r"<template>"),
        ("<script setup> block", r"<script\s+setup>"),
        ("q-form", r"<q-form|<form"),
        ("email input", r"email"),
        ("password input", r"password"),
        ("validation rules", r":rules"),
        ("required rule", r"!!val|required"),
        ("submit button", r"type=\"submit\"|@submit"),
        ("notify on submit", r"notify|alert|console\.log"),
    ])


def check_easy_p02(path):
    """QSelect + QToggle + QCheckbox + QRadio with state display."""
    return require_all(path, [
        ("<template> block", r"<template>"),
        ("<script setup> block", r"<script\s+setup>"),
        ("q-select", r"<q-select"),
        ("options bound", r":options"),
        ("q-toggle", r"<q-toggle"),
        ("q-checkbox", r"<q-checkbox"),
        ("q-radio", r"<q-radio"),
        ("radio val prop", r"val="),
        ("form state shown", r"JSON\.stringify|\{\{\s*form"),
        ("v-model bindings", r"v-model"),
    ])


def check_easy_p03(path):
    """Submit + reset form using formRef.resetValidation()."""
    return require_all(path, [
        ("<template> block", r"<template>"),
        ("<script setup> block", r"<script\s+setup>"),
        ("q-form with ref", r"<q-form[^>]*ref=|<form[^>]*ref="),
        ("formRef in script", r"formRef|ref\s*\(\s*null\s*\)"),
        ("resetValidation call", r"resetValidation"),
        ("submit handler", r"@submit|type=\"submit\""),
        ("reset button", r"[Rr]eset"),
        ("rules present", r":rules"),
        ("fields cleared", r"name.*''|=\s*\{"),
    ])


def check_medium_p01(path):
    """Sectioned registration: personal/address/preferences, 2-col grid."""
    return require_all(path, [
        ("<template> block", r"<template>"),
        ("<script setup> block", r"<script\s+setup>"),
        ("q-form", r"<q-form|<form"),
        ("name field", r"name"),
        ("email field", r"email"),
        ("street field", r"street"),
        ("city field", r"city"),
        ("zip field", r"zip"),
        ("newsletter toggle", r"newsletter|<q-toggle"),
        ("theme select", r"theme|<q-select"),
        ("responsive columns", r"col-12|col-md|col-sm"),
        ("section separators", r"q-separator|text-h6|<h"),
        ("rules", r":rules"),
    ])


def check_medium_p02(path):
    """Async username availability: debounce, checking, taken/available."""
    return require_all(path, [
        ("<template> block", r"<template>"),
        ("<script setup> block", r"<script\s+setup>"),
        ("username input", r"username|[Uu]sername"),
        ("debounce", r"debounce"),
        ("checking state", r"checking"),
        ("status state", r"status|available|taken"),
        ("simulated async check", r"setTimeout|Promise|await"),
        ("watch on username", r"watch\s*\("),
        ("available result", r"available"),
        ("taken result", r"taken"),
        ("disable submit unless ok", r":disable|disabled"),
    ])


def check_medium_p03(path):
    """q-file multi-image upload: previews, max size, rejected notify."""
    return require_all(path, [
        ("<template> block", r"<template>"),
        ("<script setup> block", r"<script\s+setup>"),
        ("q-file component", r"<q-file|<input[^>]*file"),
        ("multiple flag", r"multiple"),
        ("accept images", r"accept|jpg|png|image"),
        ("max file size", r"max-file-size|5242880|5\s*\*\s*1024|size"),
        ("rejected handler", r"@rejected|onRejected|rejected"),
        ("previews generated", r"preview|createObjectURL|URL\."),
        ("q-img preview", r"<q-img|<img"),
        ("notify on reject", r"notify"),
    ])


def check_hard_p01(path):
    """Multi-step wizard: q-stepper 3 steps, per-step validation, nav."""
    return require_all(path, [
        ("<template> block", r"<template>"),
        ("<script setup> block", r"<script\s+setup>"),
        ("q-stepper", r"<q-stepper"),
        ("q-step entries", r"<q-step"),
        ("step model", r"v-model.*step|step\s*=\s*ref"),
        ("stepper ref", r"stepperRef|ref=\"stepper"),
        ("per-step q-form", r"<q-form"),
        ("validate before next", r"validate\s*\("),
        ("next navigation", r"\.next\s*\(|step\s*\+\+|step\s*\+="),
        ("back navigation", r"previous|\.previous|[Bb]ack"),
        ("review step content", r"[Rr]eview"),
        ("submit on last step", r"[Ss]ubmit"),
        ("navigation slot", r"navigation|q-stepper-navigation"),
    ])


def check_hard_p02(path):
    """Dynamic form: add/remove phone fields with validation + submit."""
    return require_all(path, [
        ("<template> block", r"<template>"),
        ("<script setup> block", r"<script\s+setup>"),
        ("dynamic array", r"phones|fields|items"),
        ("v-for over fields", r"v-for"),
        ("add function", r"[Aa]dd.*\(.*\)\s*\{|\.push\s*\("),
        ("remove function", r"\.splice\s*\(|remove"),
        ("per-field q-input", r"<q-input|<input"),
        ("per-field rules", r":rules"),
        ("submit collects values", r"@submit|onSubmit|\.map\s*\(|\.filter"),
        ("submitted data display", r"submitted|JSON\.stringify|<pre"),
        ("remove hidden when 1", r"length\s*>\s*1|v-if"),
    ])


def check_hard_p03(path):
    """q-editor + sanitized v-html preview + save/clear."""
    return require_all(path, [
        ("<template> block", r"<template>"),
        ("<script setup> block", r"<script\s+setup>"),
        ("q-editor component", r"<q-editor"),
        ("toolbar config", r":toolbar|toolbar"),
        ("content v-model", r"v-model"),
        ("v-html preview", r"v-html"),
        ("sanitize computed", r"computed|sanitize|replace"),
        ("script strip", r"script|on\\w|on\w"),
        ("save function", r"[Ss]ave"),
        ("clear function", r"[Cc]lear"),
        ("notify feedback", r"notify|q-banner|alert"),
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
        print("  LESSON 09 — AUTO-CHECK ALL")
        print("=" * 60)
        for check_id in CHECKS:
            run_one(check_id)
        print("=" * 60)
        return

    run_one(target)


if __name__ == "__main__":
    main()
