"""
Auto-Check — Lesson 07: CSS Box Model
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
        (r"\.box\s*\{", "Missing '.box' rule"),
        (r"\.box\s*\{[^}]*width\s*:", ".box needs a width"),
        (r"\.box\s*\{[^}]*padding\s*:", ".box needs padding"),
        (r"\.box\s*\{[^}]*border\s*:", ".box needs a border"),
        (r"\.box\s*\{[^}]*margin\s*:", ".box needs margin"),
        (r"\.box\s*\{[^}]*background", ".box needs a background to show padding"),
    ])


def check_easy_p02(path):
    c = strip_comments(read_file(path))
    return require_all(c, [
        (r"\*\s*\{[^}]*box-sizing\s*:\s*border-box",
         "Missing '* { box-sizing: border-box }' reset"),
        (r"\.box1\s*,\s*\.box2|\.box2\s*,\s*\.box1",
         "Missing grouped '.box1, .box2' rule"),
        (r"width\s*:\s*50%", "Boxes should each be width: 50%"),
        (r"display\s*:\s*inline-block",
         "Boxes need 'display: inline-block' to sit side by side"),
    ])


def check_easy_p03(path):
    c = strip_comments(read_file(path))
    return require_all(c, [
        (r"\.button\s*\{", "Missing '.button' rule"),
        (r"padding\s*:\s*10px\s+20px", "Need 'padding: 10px 20px'"),
        (r"border\s*:", "Missing border"),
        (r"border-radius\s*:", "Missing border-radius"),
        (r"margin\s*:", "Missing margin between buttons"),
    ])


# ---------- medium ----------

def check_medium_p01(path):
    c = strip_comments(read_file(path))
    return require_all(c, [
        (r"\.card\s*\{", "Missing '.card' rule"),
        (r"\.card\s*\{[^}]*padding\s*:", ".card needs padding (internal space)"),
        (r"\.card\s*\{[^}]*margin\s*:", ".card needs margin (external space)"),
        (r"\.card\s*\{[^}]*background", ".card needs a background color"),
        (r"\.card\s*\{[^}]*border", ".card needs a border"),
    ])


def check_medium_p02(path):
    c = strip_comments(read_file(path))
    return require_all(c, [
        (r"\.box-a\s*\{[^}]*margin-bottom\s*:\s*30px",
         "Need '.box-a { margin-bottom: 30px }'"),
        (r"\.box-b\s*\{[^}]*margin-top\s*:\s*20px",
         "Need '.box-b { margin-top: 20px }'"),
        (r"30\s*px", "Comment should state the collapsed gap (30px)"),
    ])


def check_medium_p03(path):
    c = strip_comments(read_file(path))
    return require_all(c, [
        (r"\.block\s*\{[^}]*display\s*:\s*block",
         "Missing '.block { display: block }'"),
        (r"\.inline-block\s*\{[^}]*display\s*:\s*inline-block",
         "Missing '.inline-block { display: inline-block }'"),
        (r"\.inline\s*\{[^}]*display\s*:\s*inline",
         "Missing '.inline { display: inline }'"),
        (r"width\s*:", "Give the elements a width to compare"),
        (r"height\s*:", "Give the elements a height to compare"),
    ])


# ---------- hard ----------

def check_hard_p01(path):
    c = strip_comments(read_file(path))
    return require_all(c, [
        (r"\*\s*\{[^}]*box-sizing\s*:\s*border-box",
         "Missing '* { box-sizing: border-box }' reset"),
        (r"\.container\s*\{[^}]*max-width",
         "Missing '.container' with max-width"),
        (r"margin\s*:\s*0\s+auto", "Center with 'margin: 0 auto'"),
        (r"\.card\s*\{[^}]*padding", ".card needs padding"),
        (r"\.card\s+img\s*\{[^}]*max-width\s*:\s*100%",
         "Need '.card img { max-width: 100% }' responsive images"),
    ])


def check_hard_p02(path):
    c = strip_comments(read_file(path))
    ok, msg = require_all(c, [
        (r"\.btn-group\s+\.btn\s*\{[^}]*display\s*:\s*inline-block",
         "Missing '.btn-group .btn { display: inline-block }'"),
        (r"border-radius", "Missing border-radius"),
        (r"\.btn\s*:hover|\.btn-group\s+\.btn:hover", "Missing .btn:hover state"),
        (r":first-child", "Missing :first-child for the left corners"),
        (r":last-child", "Missing :last-child for the right corners"),
        (r"margin-right\s*:\s*-1px",
         "Need 'margin-right: -1px' so borders overlap"),
    ])
    if not ok:
        return ok, msg
    code = re.sub(r"/\*.*?\*/", "", c, flags=re.DOTALL)
    if re.search(r"display\s*:\s*(flex|grid)", code, FLAGS):
        return False, "No flexbox/grid — use box model + inline-block only"
    return True, "All tests passed!"


def check_hard_p03(path):
    c = strip_comments(read_file(path))
    return require_all(c, [
        (r"\*\s*\{[^}]*box-sizing\s*:\s*border-box",
         "Missing box-sizing reset"),
        (r"header\s*\{[^}]*border-bottom", "Missing header border-bottom"),
        (r"\.sidebar\s*\{[^}]*float\s*:\s*left",
         "Missing '.sidebar { float: left }'"),
        (r"\.sidebar\s*\{[^}]*min-height", ".sidebar needs min-height"),
        (r"\.content\s*\{[^}]*margin-left\s*:\s*250px",
         "'.content' needs margin-left: 250px to clear the sidebar"),
        (r"\.content\s*\{[^}]*max-width", ".content needs max-width"),
        (r"footer\s*\{[^}]*clear\s*:\s*both",
         "Missing 'footer { clear: both }'"),
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
        print("  LESSON 07 — CSS BOX MODEL: AUTO-CHECK ALL")
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
