"""
Auto-Check — Lesson 05: HTML Accessibility
=====================
Verifies your solutions structurally (files can't be imported directly,
so we check for the required tags, selectors, properties, and — for
pure JS — run the file under Node).

Usage:
    python3 check.py easy/p01
    python3 check.py medium/p02
    python3 check.py hard/p03
    python3 check.py all
"""

import glob
import os
import re
import subprocess
import sys

LESSON_DIR = os.path.dirname(os.path.abspath(__file__))
NODE = "/home/akash-dev/.nvm/versions/node/v22.23.2/bin/node"
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


def strip_comments(src):
    """Remove HTML/CSS/JS comments so TODO instructions can't satisfy checks."""
    src = re.sub(r"<!--.*?-->", "", src, flags=re.DOTALL)
    src = re.sub(r"/\*.*?\*/", "", src, flags=re.DOTALL)
    return src


def count(content, pattern):
    return len(re.findall(pattern, content, FLAGS))


def run_js(path, extra=""):
    """Run a .js file under Node (extra code is appended for testing).

    Assertions run inside a block so their locals can't collide with
    the learner's top-level names.
    """
    src = read_file(path) + "\n{\n" + extra + "\n}\n"
    return subprocess.run([NODE, "-e", src],
                          capture_output=True, text=True, timeout=10)


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
    c = strip_comments(read_file(path))
    ok, msg = require_all(c, [
        (r"<img", "Missing <img> elements"),
        (r'alt\s*=\s*""', 'Decorative image needs an empty alt=""'),
        (r'alt\s*=\s*"[^"]+"', "Meaningful image needs descriptive alt text"),
        (r"<a\s+[^>]*href[^>]*>\s*<img|<a[^>]*>[^<]*<img",
         "One image should be wrapped in an <a> link"),
    ])
    if not ok:
        return ok, msg
    if count(c, r"<img") < 3:
        return False, "Need 3 images: meaningful, decorative, linked"
    return True, "All tests passed!"


def check_easy_p02(path):
    c = strip_comments(read_file(path))
    ok, msg = require_all(c, [
        (r"<form", "Missing <form>"),
        (r"<label[^>]*for\s*=", "Missing <label for=\"...\">"),
        (r"aria-describedby\s*=", "Inputs need aria-describedby hints"),
        (r'id\s*=\s*"[^"]*-hint"|id\s*=\s*"\w*hint',
         "Hint elements need ids matching aria-describedby"),
        (r'type\s*=\s*"submit"', "Missing submit button"),
    ])
    if not ok:
        return ok, msg
    if count(c, r"aria-describedby") < 3:
        return False, "Need aria-describedby on all 3 inputs"
    if count(c, r"<label") < 3:
        return False, "Need 3 labeled inputs"
    return True, "All tests passed!"


def check_easy_p03(path):
    c = strip_comments(read_file(path))
    return require_all(c, [
        (r'<html[^>]*lang\s*=\s*"en"|<html[^>]*lang',
         'Missing lang attribute on <html>'),
        (r"<header", "Missing <header> landmark"),
        (r"<nav", "Missing <nav> landmark"),
        (r"<main", "Missing <main> landmark"),
        (r"<footer", "Missing <footer> landmark"),
        (r"<h1", "Missing <h1> in the header"),
    ])


# ---------- medium ----------

def check_medium_p01(path):
    c = strip_comments(read_file(path))
    return require_all(c, [
        (r'href\s*=\s*"#main"', 'Missing skip link to #main'),
        (r"position\s*:\s*absolute|left\s*:\s*-9999",
         "Skip link should be hidden off-screen until focus"),
        (r":focus", "Skip link needs a :focus style"),
        (r'<main[^>]*id\s*=\s*"main"', 'Missing <main id="main">'),
        (r"<nav[^>]*aria-label", "Nav needs an aria-label"),
        (r"<h1", "Missing h1"),
        (r"<h2", "Missing h2"),
        (r"<h3", "Missing h3 (no skipped heading levels)"),
        (r"<header", "Missing <header>"),
        (r"<footer", "Missing <footer>"),
    ])


def check_medium_p02(path):
    c = strip_comments(read_file(path))
    ok, msg = require_all(c, [
        (r"<form", "Missing <form>"),
        (r"<fieldset", "Missing <fieldset>"),
        (r"<legend", "Missing <legend>"),
        (r"<label[^>]*for\s*=", "Missing paired <label for>"),
        (r"required", "Fields should be required"),
        (r"aria-describedby", "Missing aria-describedby hints"),
        (r'role\s*=\s*"alert"', 'Error messages need role="alert"'),
    ])
    if not ok:
        return ok, msg
    if count(c, r'role\s*=\s*"alert"') < 2:
        return False, 'Need role="alert" on each error message'
    return True, "All tests passed!"


def check_medium_p03(path):
    c = strip_comments(read_file(path))
    return require_all(c, [
        (r"<table", "Missing <table>"),
        (r"<caption", "Missing <caption>"),
        (r"<thead", "Missing <thead>"),
        (r"<tbody", "Missing <tbody>"),
        (r'scope\s*=\s*"col"', 'Column headers need scope="col"'),
        (r'scope\s*=\s*"row"', 'Row headers need scope="row"'),
    ])


# ---------- hard ----------

def check_hard_p01(path):
    c = strip_comments(read_file(path))
    return require_all(c, [
        (r'<html[^>]*lang', "Missing lang on <html>"),
        (r'href\s*=\s*"#main"', "Missing skip link"),
        (r"<nav[^>]*aria-label", "Nav needs an aria-label"),
        (r'aria-current\s*=\s*"page"', 'Missing aria-current="page"'),
        (r'<main[^>]*id\s*=\s*"main"', 'Missing <main id="main">'),
        (r"<h1", "Missing h1"), (r"<h2", "Missing h2"),
        (r"<h3", "Missing h3"),
        (r'<img[^>]*alt\s*=\s*"[^"]+"', "Image needs real alt text"),
        (r"<label[^>]*for\s*=", "Form field needs a label"),
        (r":focus-visible|:focus", "Missing visible focus styles"),
        (r"aria-describedby", "Form field needs a hint"),
        (r"<footer", "Missing <footer>"),
    ])


def check_hard_p02(path):
    c = strip_comments(read_file(path))
    return require_all(c, [
        (r"<button[^>]*aria-expanded", "Toggle needs aria-expanded"),
        (r"aria-controls", "Toggle needs aria-controls pointing at the panel"),
        (r'id\s*=\s*"panel"|id\s*=\s*"\w*panel', "Missing the panel element"),
        (r"hidden", "Panel should start hidden"),
        (r'aria-live\s*=\s*"polite"|role\s*=\s*"status"',
         "Missing a live region for status"),
        (r"addEventListener\s*\(\s*.click", "Missing click handler"),
        (r"setAttribute\s*\(\s*.aria-expanded",
         "Update aria-expanded on toggle"),
        (r"textContent|innerHTML", "Update the status text"),
    ])


def check_hard_p03(path):
    c = strip_comments(read_file(path))
    return require_all(c, [
        (r'href\s*=\s*"#main"', "Missing skip link"),
        (r"<nav[^>]*aria-label", "Missing labeled <nav>"),
        (r'aria-current\s*=\s*"page"', 'Missing aria-current="page"'),
        (r":focus-visible|:focus", "Missing keyboard focus styles"),
        (r"outline", "Focus style should use outline"),
        (r'<main[^>]*id\s*=\s*"main"', 'Missing <main id="main">'),
        (r"<ul", "Nav links should be a <ul> list"),
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
        if "NoneType" in str(e):
            print(f"  {check_id}: FAIL — a function returned None — write the body!")
        else:
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
        print("  LESSON 05 — HTML ACCESSIBILITY: AUTO-CHECK ALL")
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
