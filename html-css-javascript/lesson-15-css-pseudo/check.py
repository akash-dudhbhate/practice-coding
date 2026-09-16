"""
Auto-Check — Lesson 15: CSS Pseudo-Classes & Pseudo-Elements
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
        (r"transition", "Links need a transition"),
        (r"\.color\s*:hover[^}]*color", "Missing '.color:hover' color change"),
        (r"\.underline\s*:hover[^}]*text-decoration\s*:\s*underline",
         "Missing '.underline:hover' underline"),
        (r"\.scale\s*:hover[^}]*scale", "Missing '.scale:hover' scale()"),
    ])
    if not ok:
        return ok, msg
    if count(c, r"<a\s") < 3:
        return False, "Need 3 <a> links (one per effect class)"
    return True, "All tests passed!"


def check_easy_p02(path):
    c = strip_comments(read_file(path))
    ok, msg = require_all(c, [
        (r"li\s*:nth-child\s*\(\s*even\s*\)",
         "Missing 'li:nth-child(even)'"),
        (r"li\s*:nth-child\s*\(\s*odd\s*\)",
         "Missing 'li:nth-child(odd)'"),
        (r"li\s*:first-child", "Missing 'li:first-child' style"),
        (r"li\s*:last-child", "Missing 'li:last-child' style"),
    ])
    if not ok:
        return ok, msg
    if count(c, r"<li") < 5:
        return False, "Need at least 5 <li> items to show striping"
    return True, "All tests passed!"


def check_easy_p03(path):
    c = strip_comments(read_file(path))
    return require_all(c, [
        (r"list-style\s*:\s*none", "Remove default bullets (list-style: none)"),
        (r"li\s*::before|li:before", "Missing 'li::before' pseudo-element"),
        (r"content\s*:", "::before needs a content value (the arrow)"),
        (r"2192|→|->", "Content should be an arrow (→)"),
    ])


# ---------- medium ----------

def check_medium_p01(path):
    c = strip_comments(read_file(path))
    return require_all(c, [
        (r"data-tooltip\s*=", 'Missing data-tooltip="..." attribute'),
        (r"content\s*:\s*attr\(\s*data-tooltip\s*\)",
         "::after needs content: attr(data-tooltip)"),
        (r"\.tooltip\s*::after|\.tooltip:after", "Missing '.tooltip::after'"),
        (r"\.tooltip\s*:hover\s*::after|\.tooltip:hover:after",
         "Missing '.tooltip:hover::after' reveal"),
        (r"position\s*:\s*absolute", "Tooltip needs position: absolute"),
        (r"\.tooltip\s*\{[^}]*position\s*:\s*relative",
         ".tooltip needs position: relative"),
        (r"opacity", "Fade the tooltip with opacity"),
    ])


def check_medium_p02(path):
    c = strip_comments(read_file(path))
    return require_all(c, [
        (r"input\s*:focus", "Missing 'input:focus' style"),
        (r"input\s*:invalid|:invalid", "Missing ':invalid' style"),
        (r"input\s*:disabled|:disabled", "Missing ':disabled' style"),
        (r":checked", "Missing ':checked' style for the checkbox label"),
        (r'type\s*=\s*"email"', 'Need an <input type="email">'),
        (r"required", "Email input should be required (to show :invalid)"),
        (r"disabled", "Need a disabled input"),
        (r'type\s*=\s*"checkbox"', "Need a checkbox + label pair"),
    ])


def check_medium_p03(path):
    c = strip_comments(read_file(path))
    return require_all(c, [
        (r"::first-letter|:first-letter", "Missing ::first-letter drop cap"),
        (r"::first-line|:first-line", "Missing ::first-line styling"),
        (r"float\s*:\s*left", "Drop cap should float: left"),
        (r"font-size\s*:\s*[2-9]", "Drop cap needs a large font-size"),
        (r"text-transform\s*:\s*uppercase",
         "First line should be uppercase"),
        (r"<article", "Missing <article> element"),
    ])


# ---------- hard ----------

def check_hard_p01(path):
    c = strip_comments(read_file(path))
    ok, msg = require_all(c, [
        (r":target", "Missing ':target' selector"),
        (r'href\s*=\s*"#\w+"', 'Question links need href="#id"'),
        (r'id\s*=\s*"\w+"', "Answers need matching id attributes"),
        (r"max-height\s*:\s*0", "Collapse answers with max-height: 0"),
        (r"overflow\s*:\s*hidden", "Answers need overflow: hidden"),
        (r"transition", "Animate the expand with a transition"),
    ])
    if not ok:
        return ok, msg
    if count(c, r'class="faq-item"') < 2:
        return False, 'Need at least 2 FAQ items (class="faq-item")' 
    if re.search(r"addEventListener|onclick", c):
        pass  # JS allowed but not required
    return True, "All tests passed!"


def check_hard_p02(path):
    c = strip_comments(read_file(path))
    return require_all(c, [
        (r'type="checkbox"', "Need checkbox input(s)"),
        (r'type="radio"', "Need radio input(s)"),
        (r"display\s*:\s*none", "Hide the native inputs"),
        (r"::before|:before", "Draw the control with ::before"),
        (r":checked", "Show the selected state with :checked"),
        (r'input:checked\s*\+\s*\.?\w*-?label|:checked\s*\+',
         "Style the label via 'input:checked + label'"),
        (r"border-radius\s*:\s*50%", "Radio ::before should be a circle"),
        (r":hover", "Add hover states on the labels"),
        (r'for\s*=\s*"', "Labels need for= attributes"),
    ])


def check_hard_p03(path):
    c = strip_comments(read_file(path))
    return require_all(c, [
        (r"nav\s+a\s*::after|a::after", "Missing 'a::after' underline bar"),
        (r"transform\s*:\s*scaleX\s*\(\s*0\s*\)",
         "Underline starts at scaleX(0)"),
        (r"scaleX\s*\(\s*1\s*\)", "Underline grows to scaleX(1)"),
        (r":hover\s*::after|:hover:after",
         "Missing a:hover::after reveal"),
        (r":target", "Active item should use :target (or a class)"),
        (r'content\s*:\s*"3"|content\s*:\s*.\d',
         'Badge needs content: "3" (a number)'),
        (r"border-radius\s*:\s*10px|border-radius", "Badge should be a pill"),
        (r"display\s*:\s*flex", "Nav list should be a flex row"),
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
        print("  LESSON 15 — CSS PSEUDO-CLASSES & PSEUDO-ELEMENTS: AUTO-CHECK ALL")
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
