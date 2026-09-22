"""
Auto-Check System — Lesson 10: API Integration in Quasar
========================================================
.vue files can't execute without a Quasar build step; .js files get a
parse-only syntax check via `node --check` when available. Everything is
then verified STRUCTURALLY for the required pieces.

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
    """fetch() users with loading/error/data states + list."""
    return require_all(path, [
        ("<template> block", r"<template>"),
        ("<script setup> block", r"<script\s+setup>"),
        ("fetch call", r"fetch\s*\("),
        ("API url", r"http|api\.|users"),
        ("res.ok check", r"\.ok|status"),
        ("json parse", r"\.json\s*\("),
        ("loading state", r"loading"),
        ("error state", r"error"),
        ("onMounted fetch", r"onMounted"),
        ("user list", r"<q-item|v-for|<li"),
        ("try/catch/finally", r"try|catch|finally"),
    ])


def check_easy_p02(path):
    """Axios instance: baseURL, timeout, auth interceptor, 401 handling."""
    return require_all(path, [
        ("axios import", r"import\s+axios|require.*axios"),
        ("axios.create", r"axios\.create"),
        ("baseURL", r"baseURL"),
        ("timeout", r"timeout"),
        ("request interceptor", r"interceptors\.request\.use"),
        ("token from localStorage", r"localStorage\.getItem"),
        ("Authorization Bearer", r"Authorization|Bearer"),
        ("response interceptor", r"interceptors\.response\.use"),
        ("401 handling", r"401"),
        ("export", r"export"),
    ])


def check_easy_p03(path):
    """userService CRUD object + component with loading/error list."""
    return require_all(path, [
        ("<template> block", r"<template>"),
        ("<script setup> block", r"<script\s+setup>"),
        ("userService object", r"userService"),
        ("getAll method", r"getAll"),
        ("getById method", r"getById"),
        ("create method (POST)", r"create|POST"),
        ("update method (PUT)", r"update|PUT"),
        ("delete/remove method", r"remove|delete|DELETE"),
        ("loading state", r"loading"),
        ("error state", r"error"),
        ("fetch on mount", r"onMounted"),
        ("user list", r"v-for|<q-item|<li"),
    ])


def check_medium_p01(path):
    """Paginated list: _page/_limit fetch, prev/next, total pages."""
    return require_all(path, [
        ("<template> block", r"<template>"),
        ("<script setup> block", r"<script\s+setup>"),
        ("page state", r"page"),
        ("per-page limit", r"_limit|PER_PAGE|perPage|per_page"),
        ("page param", r"_page|page="),
        ("prev function", r"prev|[Pp]revious"),
        ("next function", r"next"),
        ("total pages", r"totalPages|total|Math\.ceil"),
        ("fetch call", r"fetch\s*\(|\.get\s*\("),
        ("watch or refetch on page", r"watch\s*\(|fetchPage|loadPage"),
        ("list rendering", r"v-for|<q-item|<li"),
    ])


def check_medium_p02(path):
    """Debounced search with AbortController cancellation."""
    return require_all(path, [
        ("<template> block", r"<template>"),
        ("<script setup> block", r"<script\s+setup>"),
        ("search input", r"<q-input|<input"),
        ("debounce", r"debounce|setTimeout"),
        ("search state", r"search|query"),
        ("fetch/axios call", r"fetch\s*\(|\.get\s*\("),
        ("query param", r"name_like|q=|search=|encodeURIComponent|\?"),
        ("AbortController", r"AbortController|\.abort\s*\(|signal"),
        ("loading state", r"loading"),
        ("results list", r"results|v-for|<q-item|<li"),
    ])


def check_medium_p03(path):
    """q-infinite-scroll loading 10 at a time until empty."""
    return require_all(path, [
        ("<template> block", r"<template>"),
        ("<script setup> block", r"<script\s+setup>"),
        ("q-infinite-scroll", r"<q-infinite-scroll|q-infinite-scroll"),
        ("@load handler", r"@load|onLoad"),
        ("offset prop", r"offset|:offset"),
        ("items array", r"items"),
        ("page counter", r"page"),
        ("10 per load", r"10|_limit"),
        ("done/stop flag", r"done|stop|hasMore"),
        ("loading slot/spinner", r"#loading|q-spinner|loading"),
        ("fetch call", r"fetch\s*\(|\.get\s*\("),
    ])


def check_hard_p01(path):
    """Full API layer: interceptors, logging, services, 401 refresh."""
    return require_all(path, [
        ("axios import", r"axios"),
        ("axios.create", r"axios\.create"),
        ("baseURL", r"baseURL"),
        ("request interceptor", r"interceptors\.request\.use"),
        ("auth token", r"Authorization|Bearer|token"),
        ("response interceptor", r"interceptors\.response\.use"),
        ("request/response logging", r"console\.(log|warn|error)"),
        ("central error handler", r"handleError|errorHandler"),
        ("401 refresh logic", r"401"),
        ("retry flag", r"_retry|retry|isRefreshing|refresh"),
        ("userService", r"userService"),
        ("postService", r"postService"),
        ("service methods", r"getAll|getById|create|update|remove|delete"),
    ])


def check_hard_p02(path):
    """CRUD app: table, create/edit dialog, delete confirm, notify."""
    return require_all(path, [
        ("<template> block", r"<template>"),
        ("<script setup> block", r"<script\s+setup>"),
        ("user list/table", r"<q-table|<q-list|<table|v-for"),
        ("create dialog/flow", r"[Cc]reate|[Aa]dd|dialogOpen|<q-dialog"),
        ("edit flow", r"[Ee]dit|editing"),
        ("delete with confirm", r"[Dd]elete|\$q\.dialog|dialog\s*\("),
        ("POST request", r"POST|\.post\s*\("),
        ("PUT request", r"PUT|\.put\s*\("),
        ("DELETE request", r"DELETE|\.delete\s*\("),
        ("loading state", r"loading|saving"),
        ("notifications", r"notify"),
        ("form fields", r"<q-input|<input"),
    ])


def check_hard_p03(path):
    """useApi composable returning { data, loading, error, refetch }."""
    return require_all(path, [
        ("<template> block", r"<template>"),
        ("<script setup> block", r"<script\s+setup>"),
        ("useApi composable", r"useApi|useFetch|useAsyncData"),
        ("async fn param", r"async|=>|function"),
        ("data ref", r"data"),
        ("loading ref", r"loading"),
        ("error ref", r"error"),
        ("refetch function", r"refetch|reload|refresh"),
        ("auto-fetch on mount", r"onMounted"),
        ("focus/activation refetch", r"focus|onActivated|visibilitychange"),
        ("refetch button", r"<q-btn|<button"),
        ("list rendering", r"v-for|<q-item|<li"),
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
    Matches easy/p01-*.vue/.js (or other extensions), excluding solutions/."""
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
        print("  LESSON 10 — AUTO-CHECK ALL")
        print("=" * 60)
        for check_id in CHECKS:
            run_one(check_id)
        print("=" * 60)
        return

    run_one(target)


if __name__ == "__main__":
    main()
