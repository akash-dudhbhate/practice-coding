"""
Auto-Check — Lesson 11: CSS Grid
=================================
Verifies your solutions structurally (HTML/CSS can't be executed, so we
check for the required tags, selectors, and properties).

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


def count(content, pattern):
    return len(re.findall(pattern, content, FLAGS))


def run_js(path, extra=""):
    """Run a .js file under Node (extra code is appended for testing)."""
    src = read_file(path) + "\n" + extra
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
    c = read_file(path)
    ok, msg = require_all(c, [
        (r"display\s*:\s*grid", "Missing 'display: grid'"),
        (r"grid-template-columns\s*:\s*(repeat\(\s*3|1fr\s+1fr\s+1fr)",
         "Need 3 equal columns — repeat(3, 1fr) or '1fr 1fr 1fr'"),
        (r"gap\s*:\s*20px", "Missing 'gap: 20px'"),
    ])
    if not ok:
        return ok, msg
    if count(c, r'class="item"') < 6:
        return False, 'Need at least 6 elements with class="item"'
    return True, "All tests passed!"


def check_easy_p02(path):
    c = read_file(path)
    ok, msg = require_all(c, [
        (r"display\s*:\s*grid", "Missing 'display: grid'"),
        (r"grid-template-columns\s*:\s*(repeat\(\s*2|1fr\s+1fr)",
         "Need 2 columns — repeat(2, 1fr) or '1fr 1fr'"),
        (r"grid-template-rows\s*:\s*100px\s+200px\s+100px",
         "Need grid-template-rows: 100px 200px 100px"),
    ])
    if not ok:
        return ok, msg
    if count(c, r'class="item"') < 6:
        return False, 'Need at least 6 elements with class="item"'
    return True, "All tests passed!"


def check_easy_p03(path):
    c = read_file(path)
    ok, msg = require_all(c, [
        (r"display\s*:\s*grid", "Missing 'display: grid'"),
        (r"repeat\(\s*auto-fit\s*,\s*minmax\(\s*250px",
         "Need grid-template-columns: repeat(auto-fit, minmax(250px, 1fr))"),
    ])
    if not ok:
        return ok, msg
    if count(c, r'class="card"') < 8:
        return False, 'Need at least 8 elements with class="card"'
    return True, "All tests passed!"


# ---------- medium ----------

def check_medium_p01(path):
    c = read_file(path)
    return require_all(c, [
        (r"display\s*:\s*grid", "Missing 'display: grid'"),
        (r"grid-template-areas", "Missing 'grid-template-areas'"),
        (r'"header\s+header"', "Header area should span full width"),
        (r'"footer\s+footer"', "Footer area should span full width"),
        (r"grid-area\s*:\s*header", "Missing 'grid-area: header'"),
        (r"grid-area\s*:\s*sidebar", "Missing 'grid-area: sidebar'"),
        (r"grid-area\s*:\s*content", "Missing 'grid-area: content'"),
        (r"grid-area\s*:\s*footer", "Missing 'grid-area: footer'"),
        (r"<header", "Missing <header> element"),
        (r"<aside", "Missing <aside> element"),
        (r"<main", "Missing <main> element"),
        (r"<footer", "Missing <footer> element"),
    ])


def check_medium_p02(path):
    c = read_file(path)
    ok, msg = require_all(c, [
        (r"display\s*:\s*grid", "Missing 'display: grid'"),
        (r"grid-template-columns", "Missing 'grid-template-columns'"),
        (r"grid-column\s*:\s*span\s*2",
         "Need a wide item using 'grid-column: span 2'"),
        (r"<img", "Need <img> photos in the gallery"),
    ])
    if not ok:
        return ok, msg
    if count(c, r"@media") < 2:
        return False, "Need at least 2 @media queries (tablet + desktop)"
    if count(c, r"<img") < 6:
        return False, "Need at least 6 photos"
    return True, "All tests passed!"


def check_medium_p03(path):
    c = read_file(path)
    ok, msg = require_all(c, [
        (r"grid-template-areas", "Missing 'grid-template-areas'"),
        (r"grid-area\s*:\s*header", "Missing 'grid-area: header'"),
        (r"grid-area\s*:\s*sidebar", "Missing 'grid-area: sidebar'"),
        (r"<header", "Missing <header> element"),
        (r"<aside", "Missing <aside> element"),
    ])
    if not ok:
        return ok, msg
    if count(c, r"display\s*:\s*grid") < 2:
        return False, "Need a nested grid (.widgets should also be display: grid)"
    if count(c, r'class="widget"') < 4:
        return False, 'Need at least 4 elements with class="widget"'
    return True, "All tests passed!"


# ---------- hard ----------

def check_hard_p01(path):
    c = read_file(path)
    ok, msg = require_all(c, [
        (r"display\s*:\s*grid", "Missing 'display: grid'"),
        (r"grid-column\s*:\s*span\s*2",
         "Featured article needs 'grid-column: span 2'"),
        (r"grid-row\s*:\s*span\s*2",
         "Featured article needs 'grid-row: span 2'"),
        (r'class="article\s+featured"|class="featured\s+article"',
         'Need a featured article (class="article featured")'),
    ])
    if not ok:
        return ok, msg
    if count(c, r'class="article') < 5:
        return False, "Need at least 5 articles (1 featured + 4 regular)"
    return True, "All tests passed!"


def check_hard_p02(path):
    c = read_file(path)
    ok, msg = require_all(c, [
        (r"grid-template-areas", "Missing 'grid-template-areas'"),
        (r"repeat\(\s*4", "Desktop content grid should use repeat(4, ...)"),
        (r"display\s*:\s*none", "Sidebar should collapse with display: none"),
        (r"grid-area\s*:\s*sidebar", "Missing 'grid-area: sidebar'"),
    ])
    if not ok:
        return ok, msg
    if count(c, r"@media") < 2:
        return False, "Need at least 2 @media queries (tablet + mobile)"
    if count(c, r'class="widget"') < 4:
        return False, 'Need at least 4 elements with class="widget"'
    return True, "All tests passed!"


def check_hard_p03(path):
    c = read_file(path)
    ok, msg = require_all(c, [
        (r"display\s*:\s*grid", "Missing 'display: grid'"),
        (r"repeat\(\s*7", "Calendar needs 7 columns — repeat(7, 1fr)"),
        (r"grid-column\s*:\s*span",
         "Need a multi-day event using 'grid-column: span N'"),
    ])
    if not ok:
        return ok, msg
    if count(c, r'class="day-name"') < 7:
        return False, 'Need 7 day-name headers (class="day-name")'
    if count(c, r'class="day[ "]') < 14:
        return False, 'Need at least 14 day cells (class="day")'
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
        print("  LESSON 11 — CSS GRID: AUTO-CHECK ALL")
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
