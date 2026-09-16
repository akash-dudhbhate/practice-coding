"""
Auto-Check System — Lesson 18: Quasar SSR
==========================================
.vue files can't execute without a Quasar build step; .js files get a
parse-only syntax check via `node --check` when available. Everything is
then verified STRUCTURALLY.

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
    """SSR config: ssr enabled, componentCache, middlewares, comments."""
    return require_all(path, [
        ("ssr section", r"ssr\s*[:{]"),
        ("ssr enabled", r"ssr:\s*true|ssr\s*=\s*true"),
        ("componentCache", r"componentCache"),
        ("cache max", r"max\s*:|1000"),
        ("cache maxAge", r"maxAge|60\s*\*\s*15|15\s*min"),
        ("middlewares list", r"middlewares|compression"),
        ("render middleware", r"render"),
        ("comments/docs", r"//|/\*"),
        ("export/module", r"module\.exports|export"),
    ])


def check_easy_p02(path):
    """SSR-aware component: SERVER/CLIENT flags, window only in mounted."""
    return require_all(path, [
        ("<template> block", r"<template>"),
        ("<script setup> block", r"<script\s+setup>"),
        ("SERVER flag", r"process\.env\.SERVER|SERVER"),
        ("CLIENT flag", r"process\.env\.CLIENT|CLIENT"),
        ("onMounted", r"onMounted|mounted"),
        ("window access", r"window\."),
        ("environment message", r"isServer|server|client"),
        ("client-only data", r"clientInfo|viewport|userAgent|navigator"),
    ])


def check_easy_p03(path):
    """SEO meta tags: useHead/useMeta with OG + Twitter + canonical."""
    return require_all(path, [
        ("<template> block", r"<template>"),
        ("<script setup> block", r"<script\s+setup>"),
        ("head composable", r"useHead|useMeta|createHead"),
        ("title", r"title"),
        ("description meta", r"description"),
        ("og: tags", r"og:title|og:description|og:"),
        ("twitter tags", r"twitter:card|twitter:"),
        ("canonical/link", r"canonical|link:"),
        ("meta array", r"meta\s*[:=]"),
    ])


def check_medium_p01(path):
    """preFetch product page: fetch, store, render, error handling."""
    return require_all(path, [
        ("<template> block", r"<template>"),
        ("<script", r"<script"),
        ("preFetch defined", r"preFetch"),
        ("preFetch exported", r"export.*preFetch|preFetch.*export"),
        ("route params", r"currentRoute|params\.id|params"),
        ("store usage", r"store"),
        ("fetch/promise", r"fetch|Promise|await"),
        ("product render", r"product"),
        ("loading state", r"loading|q-linear-progress|q-spinner"),
        ("error handling", r"error|catch|reject"),
    ])


def check_medium_p02(path):
    """Blog list: preFetch all posts, links, unique SEO meta."""
    return require_all(path, [
        ("<template> block", r"<template>"),
        ("<script", r"<script"),
        ("preFetch defined", r"preFetch"),
        ("preFetch exported", r"export.*preFetch|preFetch.*export"),
        ("posts list", r"posts|v-for"),
        ("list links", r":to=|to=\"|/posts/|clickable|router-link"),
        ("store usage", r"store"),
        ("title export", r"title"),
        ("meta tags", r"meta|description|og:"),
        ("unique per page", r"export.*meta|export.*title|useHead|useMeta"),
    ])


def check_medium_p03(path):
    """SSR middleware: logging, X-App-Version header, 404 redirect."""
    return require_all(path, [
        ("middleware signature", r"\(req,\s*res,\s*next\)|req,\s*res,\s*next"),
        ("logging", r"console\.log|log"),
        ("timestamp", r"Date|toISOString|timestamp"),
        ("user agent", r"user-agent|userAgent|headers"),
        ("X-App-Version header", r"X-App-Version|setHeader"),
        ("404 handling", r"404|not[Ff]ound|not-found"),
        ("redirect", r"writeHead|redirect|Location"),
        ("next() calls", r"next\(\)"),
        ("order docs", r"//|/\*|order"),
        ("export", r"export|module\.exports"),
    ])


def check_hard_p01(path):
    """SSR blog post: preFetch + redirect 404, breadcrumbs, related."""
    return require_all(path, [
        ("<template> block", r"<template>"),
        ("<script", r"<script"),
        ("preFetch defined", r"preFetch"),
        ("preFetch exported", r"export.*preFetch|preFetch.*export"),
        ("route params", r"currentRoute|params"),
        ("404 redirect", r"redirect|/404"),
        ("breadcrumbs", r"q-breadcrumbs|breadcrumb|Breadcrumb"),
        ("post render", r"post"),
        ("related posts", r"related|relatedPosts"),
        ("loading state", r"loading|q-linear-progress|q-spinner"),
        ("error state", r"error|catch"),
        ("SEO meta", r"title|meta|useHead|useMeta"),
        ("store usage", r"store"),
    ])


def check_hard_p02(path):
    """SSR product page: prefetch product+reviews+related, JSON-LD schema."""
    return require_all(path, [
        ("<template> block", r"<template>"),
        ("<script", r"<script"),
        ("preFetch defined", r"preFetch"),
        ("preFetch exported", r"export.*preFetch|preFetch.*export"),
        ("parallel fetch", r"Promise\.all|fetchReviews|fetchRelated"),
        ("404 redirect", r"redirect|/404"),
        ("reviews render", r"reviews|review"),
        ("related products", r"related|relatedProducts"),
        ("OG meta", r"og:title|og:type|og:"),
        ("twitter meta", r"twitter:"),
        ("JSON-LD schema", r"ld\+json|schema\.org|@type|application/ld"),
        ("loading state", r"loading|q-linear-progress|q-spinner"),
        ("error state", r"error|catch"),
        ("store usage", r"store"),
    ])


def check_hard_p03(path):
    """Middleware stack: log, compress, proxy, cache, error pages."""
    return require_all(path, [
        ("middleware signature", r"req,\s*res|req,\s*res,\s*next"),
        ("logging middleware", r"logging|console\.log|log"),
        ("compression", r"compress"),
        ("API proxy", r"/api|proxy|Proxy"),
        ("cache store", r"cache|Map|Cache"),
        ("TTL expiry", r"TTL|5\s*\*\s*60|timestamp|Date\.now"),
        ("cache hit/miss", r"HIT|MISS|X-Cache"),
        ("error handler", r"err|error|500"),
        ("error page redirects", r"400|404|500|Location|writeHead"),
        ("order docs", r"//|/\*|order"),
        ("export", r"export|module\.exports"),
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
    Matches easy/p01-*.*, excluding solutions/."""
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
        print("  LESSON 18 — AUTO-CHECK ALL")
        print("=" * 60)
        for check_id in CHECKS:
            run_one(check_id)
        print("=" * 60)
        return

    run_one(target)


if __name__ == "__main__":
    main()
