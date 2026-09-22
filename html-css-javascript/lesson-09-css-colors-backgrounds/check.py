"""
Auto-Check — Lesson 09: CSS Colors & Backgrounds
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
        (r"#[0-9a-f]{3,6}\b", "Missing a hex color (e.g. #ff6600)"),
        (r"rgb\s*\(", "Missing an rgb() color"),
        (r"hsl\s*\(", "Missing an hsl() color"),
        (r"display\s*:\s*inline-block", "Boxes need display: inline-block"),
    ])
    if not ok:
        return ok, msg
    if count(c, r"background") < 3:
        return False, "Need 3 boxes each with a different background color"
    return True, "All tests passed!"


def check_easy_p02(path):
    c = strip_comments(read_file(path))
    return require_all(c, [
        (r"\.card\s*\{", "Missing '.card' rule"),
        (r"url\s*\(", "Missing a background url(...)"),
        (r"cover", "Need background-size: cover (or /cover shorthand)"),
        (r"::after|:after", "Missing a ::after overlay element"),
        (r"rgba\s*\(\s*0\s*,\s*0\s*,\s*0", "Overlay should be rgba black"),
        (r"position\s*:\s*absolute", "Overlay needs position: absolute"),
    ])


def check_easy_p03(path):
    c = strip_comments(read_file(path))
    ok, msg = require_all(c, [
        (r"\.btn\s*\{", "Missing shared '.btn' rule"),
        (r"\.btn\s*:hover[^}]*box-shadow", "Missing '.btn:hover' deeper shadow"),
        (r"\.subtle\s*\{[^}]*box-shadow", "Missing '.subtle' shadow"),
        (r"\.medium\s*\{[^}]*box-shadow", "Missing '.medium' shadow"),
        (r"\.strong\s*\{[^}]*box-shadow", "Missing '.strong' shadow"),
    ])
    if not ok:
        return ok, msg
    if count(c, r"<button") < 3:
        return False, "Need 3 <button> elements (subtle/medium/strong)"
    return True, "All tests passed!"


# ---------- medium ----------

def check_medium_p01(path):
    c = strip_comments(read_file(path))
    return require_all(c, [
        (r"\.hero\s*\{[^}]*linear-gradient",
         "Missing '.hero' with linear-gradient"),
        (r"linear-gradient\s*\([^)]*,[^)]*,[^)]*\)",
         "Gradient should have 3 colors"),
        (r"text-shadow", "Hero text needs text-shadow for readability"),
        (r"\.cta\s*\{", "Missing '.cta' button style"),
        (r"text-align\s*:\s*center", "Hero should be centered"),
    ])


def check_medium_p02(path):
    c = strip_comments(read_file(path))
    ok, msg = require_all(c, [
        (r"\.grid\s*\{[^}]*display\s*:\s*flex", "Missing '.grid' flex row"),
        (r"\.card\s*\{[^}]*border-radius", "Cards need border-radius"),
        (r"\.card\s*\{[^}]*box-shadow", "Cards need box-shadow"),
        (r"\.card-img\s*\{[^}]*url\s*\(", "Missing '.card-img' background url"),
        (r"::after|:after", "Missing ::after gradient overlay"),
        (r"\.card\s*:hover", "Missing .card:hover rule"),
        (r"transition", "Overlay needs a transition for the fade"),
    ])
    if not ok:
        return ok, msg
    if count(c, r'class="card"') < 3:
        return False, 'Need 3 elements with class="card"'
    return True, "All tests passed!"


def check_medium_p03(path):
    c = strip_comments(read_file(path))
    ok, msg = require_all(c, [
        (r":root\s*\{", "Missing :root variable block"),
        (r"--c1\s*:", "Missing --c1 color variable"),
        (r"var\(\s*--c", "Swatches should use var(--cN)"),
        (r"\.palette\s*\{[^}]*display\s*:\s*flex", "Missing '.palette' flex"),
        (r"\.swatch\s*\{", "Missing '.swatch' rule"),
    ])
    if not ok:
        return ok, msg
    if count(c, r'class="swatch') < 5:
        return False, 'Need 5 swatch elements (class="swatch sN")'
    if count(c, r"rgb\s*\(") < 5:
        return False, "Each swatch should label its rgb() value"
    return True, "All tests passed!"


# ---------- hard ----------

def check_hard_p01(path):
    c = strip_comments(read_file(path))
    return require_all(c, [
        (r"linear-gradient", "Page background needs a linear-gradient"),
        (r"\.glass\s*\{", "Missing '.glass' card rule"),
        (r"rgba\s*\(\s*255\s*,\s*255\s*,\s*255",
         "Glass needs a translucent white background"),
        (r"backdrop-filter\s*:\s*blur", "Missing backdrop-filter: blur()"),
        (r"border-radius", "Missing border-radius"),
        (r"box-shadow", "Missing box-shadow"),
    ])


def check_hard_p02(path):
    c = strip_comments(read_file(path))
    return require_all(c, [
        (r"\.profile\s*\{[^}]*box-shadow", "Profile card needs box-shadow"),
        (r"\.profile\s*:hover", "Missing .profile:hover lift"),
        (r"transition", "Need a transition for the hover effect"),
        (r"\.avatar\s*\{[^}]*radial-gradient",
         "Avatar needs a radial-gradient"),
        (r"border-radius\s*:\s*50%", "Avatar should be a circle (50%)"),
        (r"\.stats\s*\{[^}]*display\s*:\s*flex", "Stats row needs flex"),
        (r"\.follow\s*\{[^}]*linear-gradient",
         "Follow button needs a linear-gradient"),
    ])


def check_hard_p03(path):
    c = strip_comments(read_file(path))
    return require_all(c, [
        (r"@keyframes", "Missing @keyframes for the gradient animation"),
        (r"animation\s*:", "Missing 'animation' applying the keyframes"),
        (r"background-size\s*:\s*400%", "Need background-size: 400% 400%"),
        (r"background-clip\s*:\s*text|-webkit-background-clip\s*:\s*text",
         "Missing background-clip: text for the gradient headline"),
        (r"color\s*:\s*transparent",
         "Gradient text needs color: transparent"),
        (r"\.navbar\s*\{[^}]*backdrop-filter",
         "Navbar needs backdrop-filter (glassmorphism)"),
        (r"\.navbar\s*\{[^}]*position\s*:\s*fixed",
         "Navbar needs position: fixed"),
        (r"\.floating-card\s*\{[^}]*box-shadow",
         "Floating card needs box-shadow"),
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
        print("  LESSON 09 — CSS COLORS & BACKGROUNDS: AUTO-CHECK ALL")
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
