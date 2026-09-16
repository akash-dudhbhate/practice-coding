"""
Auto-Check — Lesson 12: CSS Responsive Design
==============================================
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


VIEWPORT = (r'name="viewport"', "Missing viewport meta tag")


# ---------- easy ----------

def check_easy_p01(path):
    c = read_file(path)
    return require_all(c, [
        VIEWPORT,
        (r"font-size\s*:\s*16px", "Missing base 'font-size: 16px'"),
        (r"@media[^{]*min-width\s*:\s*768px",
         "Missing @media (min-width: 768px) breakpoint"),
        (r"font-size\s*:\s*18px", "Missing 'font-size: 18px' for desktop"),
    ])


def check_easy_p02(path):
    c = read_file(path)
    return require_all(c, [
        VIEWPORT,
        (r'class="container"', 'Need an element with class="container"'),
        (r"max-width\s*:\s*1200px", "Missing 'max-width: 1200px'"),
        (r"margin\s*:\s*0\s+auto", "Missing 'margin: 0 auto' to center"),
        (r"@media", "Need a media query for the desktop breakpoint"),
    ])


def check_easy_p03(path):
    c = read_file(path)
    return require_all(c, [
        VIEWPORT,
        (r"<h1", "Missing <h1> heading"),
        (r"clamp\(\s*1\.5rem\s*,\s*5vw\s*,\s*3rem\s*\)",
         "Need font-size: clamp(1.5rem, 5vw, 3rem)"),
    ])


# ---------- medium ----------

def check_medium_p01(path):
    c = read_file(path)
    ok, msg = require_all(c, [
        VIEWPORT,
        (r"display\s*:\s*grid", "Missing 'display: grid'"),
        (r"@media[^{]*min-width\s*:\s*768px",
         "Missing @media (min-width: 768px) for 2 columns"),
        (r"@media[^{]*min-width\s*:\s*1024px",
         "Missing @media (min-width: 1024px) for 3 columns"),
        (r"repeat\(\s*2", "Need repeat(2, ...) for tablet"),
        (r"repeat\(\s*3", "Need repeat(3, ...) for desktop"),
    ])
    if not ok:
        return ok, msg
    if count(c, r'class="card"') < 6:
        return False, 'Need at least 6 elements with class="card"'
    return True, "All tests passed!"


def check_medium_p02(path):
    c = read_file(path)
    return require_all(c, [
        (r"<nav", "Missing <nav> element"),
        (r'class="hamburger"', 'Need a hamburger label (class="hamburger")'),
        (r'type="checkbox"', "Need a checkbox input for the toggle"),
        (r'class="nav-toggle"', 'Need class="nav-toggle" on the checkbox'),
        (r'class="nav-links"', 'Need a <ul> with class="nav-links"'),
        (r":checked", "Missing :checked selector for the toggle"),
        (r"@media[^{]*max-width\s*:\s*768px",
         "Missing @media (max-width: 768px) mobile block"),
    ])


def check_medium_p03(path):
    c = read_file(path)
    return require_all(c, [
        (r'class="hero"', 'Need a section with class="hero"'),
        (r"100vh", "Hero should fill the viewport (min-height/height: 100vh)"),
        (r"background[^}]*cover|background-size\s*:\s*cover",
         "Missing background-size: cover"),
        (r"clamp\(", "Hero title should use clamp() for fluid sizing"),
        (r'class="cta"', 'Need a CTA button (class="cta")'),
        (r"@media[^{]*max-width\s*:\s*768px",
         "Missing mobile @media (max-width: 768px)"),
        (r"width\s*:\s*100%", "CTA should be width: 100% on mobile"),
    ])


# ---------- hard ----------

def check_hard_p01(path):
    c = read_file(path)
    ok, msg = require_all(c, [
        VIEWPORT,
        (r"<header", "Missing <header>"),
        (r"<nav", "Missing <nav> inside the header"),
        (r'class="hero"', 'Need a hero section (class="hero")'),
        (r"clamp\(", "Hero title should use clamp()"),
        (r'class="features"', 'Need a features section (class="features")'),
        (r'class="testimonials"',
         'Need a testimonials section (class="testimonials")'),
        (r"<footer", "Missing <footer>"),
    ])
    if not ok:
        return ok, msg
    if count(c, r"@media") < 2:
        return False, "Need at least 2 @media breakpoints for the features grid"
    if count(c, r'class="feature"') < 3:
        return False, 'Need at least 3 elements with class="feature"'
    return True, "All tests passed!"


def check_hard_p02(path):
    c = read_file(path)
    ok, msg = require_all(c, [
        (r'class="dashboard"', 'Need a container with class="dashboard"'),
        (r'class="sidebar"', 'Need a sidebar (class="sidebar")'),
        (r'class="content"', 'Need a content area (class="content")'),
        (r'class="icon"', 'Need icon elements (class="icon") in the sidebar'),
        (r"transition", "Missing CSS transition for smooth changes"),
        (r"display\s*:\s*none", "Sidebar should be hidden on mobile"),
    ])
    if not ok:
        return ok, msg
    if count(c, r"@media") < 2:
        return False, "Need at least 2 @media breakpoints (tablet + mobile)"
    if count(c, r'class="widget"') < 4:
        return False, 'Need at least 4 elements with class="widget"'
    return True, "All tests passed!"


def check_hard_p03(path):
    c = read_file(path)
    ok, msg = require_all(c, [
        (r"repeat\(\s*auto-fit\s*,\s*minmax\(\s*250px",
         "Gallery needs repeat(auto-fit, minmax(250px, 1fr))"),
        (r'class="gallery"', 'Need a grid with class="gallery"'),
        (r'loading="lazy"|loading=lazy', 'Images need loading="lazy"'),
        (r":target", "Need a :target rule for the lightbox"),
        (r'class="lightbox"', 'Need overlay divs (class="lightbox")'),
        (r'class="close"', 'Need a close link (class="close")'),
    ])
    if not ok:
        return ok, msg
    if count(c, r"<img") < 4:
        return False, "Need at least 4 gallery images"
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
        print("  LESSON 12 — CSS RESPONSIVE: AUTO-CHECK ALL")
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
