"""
Auto-Check — Lesson 01: HTML Structure & Semantic Tags
======================================================
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


def strip_comments(src):
    """Remove HTML/CSS/JS comments so TODO instructions can't satisfy checks."""
    src = re.sub(r"<!--.*?-->", "", src, flags=re.DOTALL)
    src = re.sub(r"/\*.*?\*/", "", src, flags=re.DOTALL)
    return src


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
    c = strip_comments(read_file(path))
    ok, msg = require_all(c, [
        (r"<table", "Missing <table> element"),
        (r"<thead", "Missing <thead> for the header row"),
        (r"<tbody", "Missing <tbody> for the data rows"),
        (r"<th", "Missing <th> header cells"),
    ])
    if not ok:
        return ok, msg
    if count(c, r"<th") < 3:
        return False, "Need 3 header cells (<th>) — Name/Age/City or similar"
    if count(c, r"<tr") < 4:
        return False, "Need 4 <tr> rows total (1 header + 3 data rows)"
    if count(c, r"<td") < 9:
        return False, "Need 9 data cells (<td>) — 3 rows x 3 columns"
    return True, "All tests passed!"


def check_easy_p02(path):
    c = strip_comments(read_file(path))
    ok, msg = require_all(c, [
        (r"<form", "Missing <form> element"),
        (r"<label[^>]*for\s*=", "Missing <label for=\"...\"> paired with an input"),
        (r'type\s*=\s*"email"', 'Missing <input type="email">'),
        (r'type\s*=\s*"submit"', "Missing a submit button/input"),
    ])
    if not ok:
        return ok, msg
    if count(c, r"<label") < 2:
        return False, "Need 2 <label> elements (name + email)"
    if count(c, r"<input") < 2:
        return False, "Need at least 2 <input> fields (text + email)"
    return True, "All tests passed!"


def check_easy_p03(path):
    c = strip_comments(read_file(path))
    ok, msg = require_all(c, [
        (r"<nav", "Missing <nav> element"),
        (r"<ul", "Missing <ul> unordered list inside <nav>"),
        (r"<a\s+[^>]*href\s*=", "Missing <a href=\"...\"> links"),
    ])
    if not ok:
        return ok, msg
    if count(c, r"<li") < 4:
        return False, "Need 4 <li> items (Home/About/Services/Contact or similar)"
    if count(c, r"<a\s") < 4:
        return False, "Need 4 <a> links"
    return True, "All tests passed!"


# ---------- medium ----------

def check_medium_p01(path):
    c = strip_comments(read_file(path))
    return require_all(c, [
        (r"<article", "Missing <article> wrapper"),
        (r"<header", "Missing <header> inside the article"),
        (r"<h1", "Missing <h1> post title"),
        (r"<time[^>]*datetime\s*=", 'Missing <time datetime="...">'),
        (r"<section", "Missing <section> for the post body"),
        (r"<footer", "Missing <footer> inside the article"),
        (r"<h2", "Missing <h2> section headings"),
    ])


def check_medium_p02(path):
    c = strip_comments(read_file(path))
    ok, msg = require_all(c, [
        (r"<figure", "Missing <figure> elements"),
        (r"<img[^>]*alt\s*=", 'Missing <img ... alt="...">'),
        (r"<figcaption", "Missing <figcaption> captions"),
    ])
    if not ok:
        return ok, msg
    if count(c, r"<figure") < 3:
        return False, "Need 3 <figure> elements"
    if count(c, r"<figcaption") < 3:
        return False, "Need 3 <figcaption> elements (one per figure)"
    if count(c, r"<img") < 3:
        return False, "Need 3 <img> elements"
    return True, "All tests passed!"


def check_medium_p03(path):
    c = strip_comments(read_file(path))
    ok, msg = require_all(c, [
        (r"<dl", "Missing <dl> definition list"),
        (r"<dt", "Missing <dt> definition terms"),
        (r"<dd", "Missing <dd> definition descriptions"),
    ])
    if not ok:
        return ok, msg
    if count(c, r"<dt") < 4:
        return False, "Need at least 4 <dt> terms"
    if count(c, r"<dd") < 4:
        return False, "Need at least 4 <dd> descriptions"
    return True, "All tests passed!"


# ---------- hard ----------

def check_hard_p01(path):
    c = strip_comments(read_file(path))
    return require_all(c, [
        (r'href\s*=\s*"#main"|class\s*=\s*"[^"]*skip-link',
         'Missing skip link (<a href="#main" class="skip-link">)'),
        (r"<header", "Missing <header> landmark"),
        (r"<nav[^>]*aria-label\s*=", 'Missing <nav aria-label="...">'),
        (r'<main[^>]*id\s*=\s*"main"|<main', 'Missing <main id="main"> landmark'),
        (r"<footer", "Missing <footer> landmark"),
        (r"<h1", "Missing exactly one <h1>"),
        (r"<img[^>]*alt\s*=", "Every <img> needs an alt attribute"),
    ])


def check_hard_p02(path):
    c = strip_comments(read_file(path))
    ok, msg = require_all(c, [
        (r"<article", "Missing <article> elements"),
        (r"<section", "Missing <section> wrapping the comments"),
        (r"<time[^>]*datetime\s*=", 'Missing <time datetime="...">'),
        (r"<h1", "Missing <h1> post title"),
    ])
    if not ok:
        return ok, msg
    if count(c, r"<article") < 4:
        return False, ("Need nested <article>s: 1 post + 2 comments + "
                       "1 comment nested inside a comment")
    return True, "All tests passed!"


def check_hard_p03(path):
    c = strip_comments(read_file(path))
    ok, msg = require_all(c, [
        (r"<table", "Missing <table> element"),
        (r"<caption", "Missing <caption> describing the table"),
        (r"<colgroup", "Missing <colgroup> with <col> elements"),
        (r"<thead", "Missing <thead>"),
        (r"<tbody", "Missing <tbody>"),
        (r"<tfoot", "Missing <tfoot> totals row"),
        (r'scope\s*=\s*"col"', 'Missing scope="col" on column headers'),
        (r'scope\s*=\s*"row"', 'Missing scope="row" on row headers'),
    ])
    if not ok:
        return ok, msg
    if count(c, r"<col[\s>]") < 4:
        return False, "Need several <col> elements inside <colgroup>"
    return True, "All tests passed!"


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
        print("  LESSON 01 — HTML STRUCTURE: AUTO-CHECK ALL")
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
