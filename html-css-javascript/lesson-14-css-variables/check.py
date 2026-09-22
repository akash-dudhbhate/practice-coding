"""
Auto-Check — Lesson 14: CSS Variables
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
    return require_all(c, [
        (r"--primary\s*:", "Missing --primary variable"),
        (r"--spacing\s*:", "Missing --spacing variable"),
        (r"--radius\s*:", "Missing --radius variable"),
        (r"\.btn\s*\{[^}]*var\(", ".btn should use var()"),
        (r"\.card\s*\{[^}]*var\(", ".card should use var()"),
        (r"input\s*\{[^}]*var\(|input\b[^}]*var\(",
         "input should use var()"),
    ])


def check_easy_p02(path):
    c = strip_comments(read_file(path))
    return require_all(c, [
        (r"var\(\s*--btn-bg\s*,\s*#ccc\s*\)",
         "Missing 'var(--btn-bg, #ccc)' fallback"),
        (r"--btn-bg\s*:", "Define --btn-bg so the custom color is used"),
        (r"\.btn\s*\{", "Missing '.btn' rule"),
    ])


def check_easy_p03(path):
    c = strip_comments(read_file(path))
    return require_all(c, [
        (r"\.card\s*\{[^}]*--card-color\s*:",
         "Define --card-color inside .card (not :root)"),
        (r"background\s*:\s*var\(\s*--card-color",
         "Use var(--card-color) for the background"),
        (r"border[^;]*var\(\s*--card-color",
         "Use var(--card-color) for the border"),
        (r"\.card\.alt|\.alt\s*\{[^}]*--card-color",
         "Missing .card.alt (or .alt) overriding the variable"),
    ])


# ---------- medium ----------

def check_medium_p01(path):
    c = strip_comments(read_file(path))
    return require_all(c, [
        (r":root\s*\{[^}]*--bg", "Missing light theme vars in :root"),
        (r'\[data-theme\s*=\s*"dark"\]',
         'Missing [data-theme="dark"] dark theme block'),
        (r"background\s*:\s*var\(\s*--bg", "body should use var(--bg)"),
        (r"color\s*:\s*var\(\s*--text", "body should use var(--text)"),
        (r"\.card\s*\{[^}]*var\(", ".card should use variables"),
        (r"dataset\.theme|setAttribute\s*\(\s*['\"]data-theme",
         "Missing JS toggling data-theme"),
        (r"transition", "Add a transition for smooth theme switching"),
    ])


def check_medium_p02(path):
    c = strip_comments(read_file(path))
    return require_all(c, [
        (r":root\s*\{[^}]*--bg", "Missing light theme vars in :root"),
        (r"@media\s*\(\s*prefers-color-scheme\s*:\s*dark\s*\)",
         "Missing @media (prefers-color-scheme: dark)"),
        (r"background\s*:\s*var\(\s*--bg", "body should use var(--bg)"),
        (r"color\s*:\s*var\(\s*--text", "body should use var(--text)"),
        (r"\.card\s*\{[^}]*var\(", ".card should use variables"),
    ])


def check_medium_p03(path):
    c = strip_comments(read_file(path))
    ok, msg = require_all(c, [
        (r":root\s*\{", "Missing :root token block"),
        (r"--color-\w+\s*:", "Missing --color-* palette variables"),
        (r"--space-\w+\s*:", "Missing --space-* spacing scale"),
        (r"--font-\w+\s*:", "Missing --font-* size scale"),
        (r"--radius-\w+\s*:", "Missing --radius-* scale"),
        (r"\.card\s*\{[^}]*var\(", ".card should use variables"),
        (r"\.btn\s*\{[^}]*var\(", ".btn should use variables"),
    ])
    if not ok:
        return ok, msg
    if count(c, r"--color-") < 5:
        return False, "Need at least 5 --color-* variables"
    if count(c, r"--space-") < 5:
        return False, "Need at least 5 --space-* variables"
    if count(c, r"--font-") < 4:
        return False, "Need at least 4 --font-* variables"
    if count(c, r"--radius-") < 3:
        return False, "Need at least 3 --radius-* variables"
    return True, "All tests passed!"


# ---------- hard ----------

def check_hard_p01(path):
    c = strip_comments(read_file(path))
    ok, msg = require_all(c, [
        (r"--primary\s*:", "Missing --primary variable"),
        (r"--secondary\s*:", "Missing --secondary variable"),
        (r"--accent\s*:", "Missing --accent variable"),
        (r'type\s*=\s*"color"', "Missing <input type=\"color\"> pickers"),
        (r"style\.setProperty", "Use style.setProperty to update vars"),
        (r"documentElement", "Set properties on documentElement (:root)"),
        (r"var\(\s*--primary", "Cards should use var(--primary)"),
    ])
    if not ok:
        return ok, msg
    if count(c, r'type\s*=\s*"color"') < 3:
        return False, 'Need 3 <input type="color"> pickers'
    if not re.search(r"reset", c, FLAGS):
        return False, "Missing a Reset button"
    return True, "All tests passed!"


def check_hard_p02(path):
    c = strip_comments(read_file(path))
    ok, msg = require_all(c, [
        (r":root\s*\{[^}]*--spacing", "Missing --spacing variable"),
        (r"--font-size", "Missing --font-size variable"),
        (r"--container-width", "Missing --container-width variable"),
        (r"@media\s*\(\s*min-width\s*:\s*768px",
         "Missing @media (min-width: 768px)"),
        (r"@media\s*\(\s*min-width\s*:\s*1024px",
         "Missing @media (min-width: 1024px)"),
        (r"var\(\s*--spacing", "Layout should use var(--spacing)"),
        (r"var\(\s*--container-width",
         "Container should use var(--container-width)"),
        (r"<header", "Missing <header>"),
        (r"<footer", "Missing <footer>"),
    ])
    if not ok:
        return ok, msg
    if count(c, r"@media") < 2:
        return False, "Need at least 2 breakpoints redefining the vars"
    return True, "All tests passed!"


def check_hard_p03(path):
    c = strip_comments(read_file(path))
    return require_all(c, [
        (r":root\s*\{[^}]*--bg", "Missing light theme in :root"),
        (r'\[data-theme\s*=\s*"dark"\]', 'Missing [data-theme="dark"]'),
        (r'\[data-theme\s*=\s*"contrast"\]|\[data-theme\s*=\s*"high-contrast"\]',
         'Missing a high-contrast theme block'),
        (r"localStorage\.setItem", "Persist the theme with setItem"),
        (r"localStorage\.getItem", "Restore the theme with getItem"),
        (r"dataset\.theme|setAttribute\s*\(\s*['\"]data-theme",
         "Set data-theme to switch themes"),
        (r"transition", "Add transitions between themes"),
        (r"function\s+setTheme|setTheme\s*=",
         "Missing a setTheme() function"),
        (r"--link", "Missing --link variable used for link color"),
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
        print("  LESSON 14 — CSS VARIABLES: AUTO-CHECK ALL")
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
