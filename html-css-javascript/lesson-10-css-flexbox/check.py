"""
Auto-Check — Lesson 10: CSS Flexbox
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
        (r"display\s*:\s*flex", "Missing 'display: flex'"),
        (r"align-items\s*:\s*center", "Missing 'align-items: center'"),
        (r"justify-content\s*:\s*center",
         "Missing 'justify-content: center'"),
        (r"height\s*:\s*100vh", "Container needs height: 100vh"),
        (r"\.box\s*\{[^}]*width\s*:\s*200px", ".box needs width: 200px"),
        (r"\.box\s*\{[^}]*height\s*:\s*200px", ".box needs height: 200px"),
    ])


def check_easy_p02(path):
    c = strip_comments(read_file(path))
    return require_all(c, [
        (r"\.navbar\s*\{[^}]*display\s*:\s*flex",
         "Missing '.navbar { display: flex }'"),
        (r"justify-content\s*:\s*space-between",
         "Missing 'justify-content: space-between'"),
        (r"\.logo", "Missing '.logo' element/style"),
        (r"\.nav-links\s*\{[^}]*display\s*:\s*flex",
         "Missing '.nav-links' flex container"),
        (r"gap\s*:", "Links need a gap (or margins) between them"),
    ])


def check_easy_p03(path):
    c = strip_comments(read_file(path))
    ok, msg = require_all(c, [
        (r"display\s*:\s*flex", "Missing 'display: flex' on the row"),
        (r"gap\s*:\s*16px", "Missing 'gap: 16px'"),
        (r"\.card\s*\{[^}]*flex\s*:\s*1", "Cards need 'flex: 1'"),
    ])
    if not ok:
        return ok, msg
    if count(c, r'class="card"') < 4:
        return False, 'Need 4 elements with class="card"'
    return True, "All tests passed!"


# ---------- medium ----------

def check_medium_p01(path):
    c = strip_comments(read_file(path))
    return require_all(c, [
        (r"flex-direction\s*:\s*column",
         "body needs 'flex-direction: column'"),
        (r"height\s*:\s*100vh", "Layout needs height: 100vh"),
        (r"\.main\s*\{[^}]*display\s*:\s*flex",
         "Missing '.main { display: flex }' row"),
        (r"\.sidebar\s*\{[^}]*width\s*:\s*250px",
         "Sidebar needs width: 250px"),
        (r"\.content\s*\{[^}]*flex\s*:\s*1",
         "Content needs flex: 1 to fill remaining space"),
        (r"<header", "Missing <header> element"),
    ])


def check_medium_p02(path):
    c = strip_comments(read_file(path))
    ok, msg = require_all(c, [
        (r"\.grid\s*\{[^}]*display\s*:\s*flex", "Missing '.grid' flex"),
        (r"flex-wrap\s*:\s*wrap", "Missing 'flex-wrap: wrap'"),
        (r"gap\s*:\s*16px", "Missing 'gap: 16px'"),
        (r"\.card\s*\{[^}]*flex\s*:\s*1\s+1\s+300px|min-width\s*:\s*300px",
         "Cards need 'flex: 1 1 300px' (or min-width: 300px)"),
    ])
    if not ok:
        return ok, msg
    if count(c, r'class="card"') < 5:
        return False, 'Need at least 5 elements with class="card"'
    return True, "All tests passed!"


def check_medium_p03(path):
    c = strip_comments(read_file(path))
    return require_all(c, [
        (r"\.product\s*\{[^}]*display\s*:\s*flex",
         "Missing '.product { display: flex }'"),
        (r"\.details\s*\{[^}]*flex\s*:\s*1", ".details needs flex: 1"),
        (r"@media\s*\([^)]*max-width\s*:\s*600px",
         "Missing @media (max-width: 600px) breakpoint"),
        (r"flex-direction\s*:\s*column",
         "Mobile layout needs 'flex-direction: column'"),
        (r"<img", "Need a product <img>"),
    ])


# ---------- hard ----------

def check_hard_p01(path):
    c = strip_comments(read_file(path))
    return require_all(c, [
        (r"display\s*:\s*flex", "Missing 'display: flex'"),
        (r"flex-direction\s*:\s*column", "body needs column direction"),
        (r"header\s*\{[^}]*position\s*:\s*sticky",
         "Header needs position: sticky"),
        (r"footer\s*\{[^}]*position\s*:\s*sticky",
         "Footer needs position: sticky"),
        (r"overflow-y\s*:\s*auto",
         "Content/sidebar need overflow-y: auto to scroll independently"),
        (r"\.sidebar\s*\{[^}]*width\s*:\s*250px",
         "Sidebar needs width: 250px"),
        (r"\.content\s*\{[^}]*flex\s*:\s*1", "Content needs flex: 1"),
    ])


def check_hard_p02(path):
    c = strip_comments(read_file(path))
    ok, msg = require_all(c, [
        (r"\.features\s*\{[^}]*display\s*:\s*flex", "Missing '.features' flex"),
        (r"flex-wrap\s*:\s*wrap", "Missing 'flex-wrap: wrap'"),
        (r"\.feature\s*\{[^}]*flex\s*:\s*1\s+1",
         "Features need 'flex: 1 1 ...'"),
        (r"@media", "Missing @media breakpoints"),
        (r"flex-basis\s*:\s*45%", "Tablet needs flex-basis ~45% (2 cols)"),
        (r"flex-basis\s*:\s*100%", "Mobile needs flex-basis: 100% (1 col)"),
        (r"\.icon", "Each feature needs an .icon element"),
    ])
    if not ok:
        return ok, msg
    if count(c, r"@media") < 2:
        return False, "Need 2 @media queries (tablet + mobile)"
    if count(c, r'class="feature"') < 3:
        return False, 'Need 3 elements with class="feature"'
    return True, "All tests passed!"


def check_hard_p03(path):
    c = strip_comments(read_file(path))
    ok, msg = require_all(c, [
        (r"\.pricing\s*\{[^}]*display\s*:\s*flex",
         "Missing '.pricing { display: flex }'"),
        (r"align-items\s*:\s*stretch|align-items\s*:",
         "Pricing row needs align-items (stretch for equal heights)"),
        (r"\.tier\s*\{[^}]*flex\s*:\s*1", "Tiers need flex: 1"),
        (r"\.popular|\.tier\.popular", "Missing '.tier.popular' highlight"),
        (r"order\s*:\s*\d", "Missing 'order' rules to control visual order"),
        (r"scale\s*\(", "Popular tier should stand out via transform: scale()"),
        (r"\.badge", "Missing '.badge' element/style for 'Popular'"),
    ])
    if not ok:
        return ok, msg
    if count(c, r'class="tier') < 3:
        return False, 'Need 3 pricing tiers (class="tier ...")'
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
        print("  LESSON 10 — CSS FLEXBOX: AUTO-CHECK ALL")
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
