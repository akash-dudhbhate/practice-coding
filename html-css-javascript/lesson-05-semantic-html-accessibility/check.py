"""
Auto-Check — Lesson 05: Semantic HTML & Accessibility
=====================================================
Verifies your solutions structurally (HTML can't be executed, so we
check for the required tags and attributes).

Usage:
    python3 check.py easy/p01
    python3 check.py medium/p02
    python3 check.py hard/p03
    python3 check.py all
"""

import glob
import os
import re
import sys

LESSON_DIR = os.path.dirname(os.path.abspath(__file__))
FLAGS = re.IGNORECASE | re.DOTALL


# ---------- helpers ----------

def read_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def require_all(content, reqs):
    """Run (regex, reason) pairs; return (False, reason) on first miss."""
    for pattern, reason in reqs:
        if not re.search(pattern, content, FLAGS):
            return False, reason
    return True, "All tests passed!"


def count(content, pattern):
    return len(re.findall(pattern, content, FLAGS))


def find_file(level, num):
    """Locate e.g. easy/p01-*.* , skipping the solutions/ directory."""
    pattern = os.path.join(LESSON_DIR, level, num + "-*")
    matches = sorted(
        f for f in glob.glob(pattern)
        if os.path.isfile(f) and "solutions" not in f
    )
    return matches[0] if matches else None


# ---------- easy ----------

def check_easy_p01(path):
    c = read_file(path)
    return require_all(c, [
        (r"<header", "Missing <header> landmark"),
        (r"<h1", "Missing <h1> site title"),
        (r"<nav", "Missing <nav> element"),
        (r"<main", "Missing <main> landmark"),
        (r"<section", "Missing <section> inside <main>"),
        (r"<h2", "Missing <h2> section heading"),
        (r"<footer", "Missing <footer> landmark"),
    ])


def check_easy_p02(path):
    c = read_file(path)
    ok, msg = require_all(c, [
        (r"<article", "Missing <article> wrapper"),
        (r"<h1", "Missing <h1> article title"),
        (r"<h2", "Missing <h2> section headings"),
        (r"<section", "Missing <section> elements"),
    ])
    if not ok:
        return ok, msg
    if count(c, r"<section") < 2:
        return False, "Need at least 2 <section> elements inside the article"
    return True, "All tests passed!"


def check_easy_p03(path):
    c = read_file(path)
    ok, msg = require_all(c, [
        (r"<main", "Missing <main> wrapper"),
        (r"<article", "Missing <article> for the main content"),
        (r"<aside", "Missing <aside> for related content"),
        (r"<ul", "Missing <ul> link list inside <aside>"),
        (r"<a\s+[^>]*href\s*=", "Missing <a href=\"...\"> links"),
    ])
    if not ok:
        return ok, msg
    if count(c, r"<li") < 2:
        return False, "Need at least 2 related links in the <aside>"
    return True, "All tests passed!"


# ---------- medium ----------

def check_medium_p01(path):
    c = read_file(path)
    ok, msg = require_all(c, [
        (r"<form", "Missing <form> element"),
        (r"<fieldset", "Missing <fieldset> grouping"),
        (r"<legend", "Missing <legend> group title"),
        (r"<label[^>]*for\s*=", "Missing <label for=\"...\"> paired with inputs"),
        (r"required", "Missing required attributes on inputs"),
        (r'type\s*=\s*"submit"', "Missing a submit button"),
    ])
    if not ok:
        return ok, msg
    if count(c, r"<label") < 2:
        return False, "Need 2 <label> elements (email + password)"
    return True, "All tests passed!"


def check_medium_p02(path):
    c = read_file(path)
    ok, msg = require_all(c, [
        (r"<nav[^>]*aria-label\s*=", 'Missing <nav aria-label="...">'),
        (r'aria-current\s*=\s*"page"', 'Missing aria-current="page"'),
        (r"<ul", "Missing <ul> in the main nav"),
        (r"<ol", "Missing <ol> breadcrumb list"),
    ])
    if not ok:
        return ok, msg
    if count(c, r"<nav") < 2:
        return False, "Need 2 <nav> elements (main nav + breadcrumb)"
    return True, "All tests passed!"


def check_medium_p03(path):
    c = read_file(path)
    return require_all(c, [
        (r"<header", "Missing <header> landmark"),
        (r"<nav[^>]*aria-label\s*=", 'Missing labeled <nav aria-label="...">'),
        (r"<main", "Missing <main> landmark"),
        (r"<article", "Missing <article> for the post"),
        (r"<time[^>]*datetime\s*=", 'Missing <time datetime="...">'),
        (r"<aside", "Missing <aside> (About the Author)"),
        (r"<footer", "Missing <footer>"),
    ])


# ---------- hard ----------

def check_hard_p01(path):
    c = read_file(path)
    return require_all(c, [
        (r'href\s*=\s*"#main"', 'Missing skip link (<a href="#main">)'),
        (r"position\s*:\s*absolute", "Skip link should be positioned off-screen"),
        (r":focus", "Skip link should appear on :focus"),
        (r"<nav[^>]*aria-label\s*=", 'Missing <nav aria-label="Main">'),
        (r'aria-current\s*=\s*"page"', 'Missing aria-current="page"'),
        (r'<main[^>]*id\s*=\s*"main"', 'Missing <main id="main">'),
        (r"aria-labelledby", "Missing aria-labelledby on the <section>"),
        (r"<footer", "Missing <footer>"),
    ])


def check_hard_p02(path):
    c = read_file(path)
    return require_all(c, [
        (r'<form[^>]*id\s*=\s*"searchForm"|<form',
         'Missing <form id="searchForm">'),
        (r"<label[^>]*for\s*=", "Missing <label for=\"...\"> for the input"),
        (r'aria-live\s*=\s*"polite"', 'Missing aria-live="polite" region'),
        (r"<script", "Missing <script> for the submit handler"),
        (r"addEventListener\s*\(\s*['\"]submit", "Missing submit event listener"),
        (r"preventDefault", "Missing e.preventDefault()"),
        (r"innerHTML", "Should update the results via innerHTML"),
    ])


def check_hard_p03(path):
    c = read_file(path)
    return require_all(c, [
        (r'href\s*=\s*"#main"', 'Missing skip link (<a href="#main">)'),
        (r":focus", "Need :focus styles (skip link / outlines)"),
        (r"<nav[^>]*aria-label\s*=", 'Missing <nav aria-label="...">'),
        (r'aria-current\s*=\s*"page"', 'Missing aria-current="page"'),
        (r'<main[^>]*id\s*=\s*"main"', 'Missing <main id="main">'),
        (r"<article", "Missing <article> in <main>"),
        (r"<img[^>]*alt\s*=", "Missing <img> with alt text"),
        (r"aria-labelledby", "Missing aria-labelledby on a <section>"),
        (r"<aside[^>]*aria-label\s*=", 'Missing <aside aria-label="...">'),
        (r"<footer", "Missing <footer>"),
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


# ---------- runner ----------

def run_one(check_id):
    level, num = check_id.split("/")
    path = find_file(level, num)
    if not path:
        print(f"  {check_id}: ERROR — no file matching {level}/{num}-* "
              f"(create it next to the solutions/ folder)")
        return False
    try:
        passed, msg = CHECKS[check_id](path)
    except Exception as e:
        print(f"  {check_id}: ERROR — {e}")
        return False
    if passed:
        print(f"  {check_id}: PASS — {msg}")
        rel = os.path.relpath(path, LESSON_DIR)
        print(f'    Finished? Add a "# DONE" marker to the top of {rel}')
    else:
        print(f"  {check_id}: FAIL — {msg}")
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
        print("  LESSON 05 — SEMANTIC HTML & ACCESSIBILITY: AUTO-CHECK ALL")
        print("=" * 60)
        results = {cid: run_one(cid) for cid in CHECKS}
        print("=" * 60)
        passed = sum(results.values())
        print(f"  {passed}/{len(results)} passed")
        return

    if target not in CHECKS:
        print(f"ERROR — unknown problem '{target}'")
        print(f"Available: {', '.join(CHECKS)}")
        sys.exit(1)

    sys.exit(0 if run_one(target) else 1)


if __name__ == "__main__":
    main()
