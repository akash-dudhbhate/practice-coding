"""
Auto-Check — Lesson 13: CSS Transitions & Animations
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
        (r"\.btn\s*\{", "Missing '.btn' rule"),
        (r"transition\s*:", "Missing 'transition' for smooth hover"),
        (r"\.btn\s*:hover[^}]*background", ".btn:hover needs a new background"),
        (r"\.btn\s*:hover[^}]*transform\s*:\s*scale",
         ".btn:hover needs transform: scale()"),
    ])


def check_easy_p02(path):
    c = strip_comments(read_file(path))
    return require_all(c, [
        (r"@keyframes\s+spin", "Missing '@keyframes spin'"),
        (r"rotate\s*\(\s*360deg\s*\)", "Spin should rotate(360deg)"),
        (r"animation\s*:[^;]*spin[^;]*infinite",
         "Missing 'animation: spin ... infinite'"),
        (r"border-radius\s*:\s*50%", "Spinner needs border-radius: 50%"),
        (r"border-top-color", "Spinner needs a distinct border-top-color"),
    ])


def check_easy_p03(path):
    c = strip_comments(read_file(path))
    return require_all(c, [
        (r"\.card\s*\{", "Missing '.card' rule"),
        (r"transition\s*:", "Missing transition for the lift"),
        (r"\.card\s*:hover[^}]*translateY",
         ".card:hover needs transform: translateY()"),
        (r"\.card\s*:hover[^}]*box-shadow",
         ".card:hover needs a deeper box-shadow"),
        (r"box-shadow", "Card needs a resting box-shadow too"),
    ])


# ---------- medium ----------

def check_medium_p01(path):
    c = strip_comments(read_file(path))
    ok, msg = require_all(c, [
        (r"@keyframes\s+\w+", "Missing a @keyframes block"),
        (r"opacity\s*:\s*0", "Animation should start at opacity: 0"),
        (r"translateY\s*\(\s*50px\s*\)", "Start 50px below (translateY(50px))"),
        (r"animation\s*:", "Missing 'animation' applying the keyframes"),
        (r"forwards", "Use 'forwards' so items stay visible"),
        (r"animation-delay", "Stagger the items with animation-delay"),
        (r":nth-child", "Use :nth-child for the per-item delays"),
    ])
    if not ok:
        return ok, msg
    if count(c, r'class="item"') < 3:
        return False, 'Need 3 elements with class="item"'
    return True, "All tests passed!"


def check_medium_p02(path):
    c = strip_comments(read_file(path))
    ok, msg = require_all(c, [
        (r"@keyframes\s+bounce", "Missing '@keyframes bounce'"),
        (r"translateY\s*\(\s*-?100px\s*\)", "Ball should rise ~100px"),
        (r"animation-timing-function\s*:\s*ease-in",
         "Need ease-in timing on the way down"),
        (r"animation-timing-function\s*:\s*ease-out",
         "Need ease-out timing on the way up"),
        (r"\.ball\s*\{[^}]*animation\s*:[^;]*infinite",
         ".ball needs 'animation: bounce ... infinite'"),
        (r"border-radius\s*:\s*50%", "Ball should be a circle"),
        (r"\.shadow", "Missing a .shadow element animating with the ball"),
        (r"scaleX", "Shadow should scale with the bounce"),
    ])
    if not ok:
        return ok, msg
    if count(c, r"@keyframes") < 2:
        return False, "Need 2 @keyframes (bounce + shadow)"
    return True, "All tests passed!"


def check_medium_p03(path):
    c = strip_comments(read_file(path))
    return require_all(c, [
        (r"@keyframes\s+pulse", "Missing '@keyframes pulse'"),
        (r"scale\s*\(\s*1\.2\s*\)", "Pulse should scale up to 1.2"),
        (r"scale\s*\(\s*1\s*\)", "Pulse should return to scale(1)"),
        (r"box-shadow", "Pulse needs a glowing box-shadow ring"),
        (r"animation\s*:[^;]*pulse[^;]*infinite",
         "Missing 'animation: pulse ... infinite'"),
        (r"\.badge\s*\{", "Missing '.badge' rule"),
    ])


# ---------- hard ----------

def check_hard_p01(path):
    c = strip_comments(read_file(path))
    return require_all(c, [
        (r'type\s*=\s*"checkbox"', "Missing the checkbox (checkbox hack)"),
        (r"\.menu-toggle\s*\{[^}]*display\s*:\s*none|display\s*:\s*none",
         "Checkbox should be hidden"),
        (r"\.hamburger", "Missing '.hamburger' element/styles"),
        (r":nth-child\s*\(\s*1\s*\)", "Position bar 1 with :nth-child(1)"),
        (r":nth-child\s*\(\s*2\s*\)", "Position bar 2 with :nth-child(2)"),
        (r":nth-child\s*\(\s*3\s*\)", "Position bar 3 with :nth-child(3)"),
        (r":checked", "Missing :checked state for the toggle"),
        (r"rotate\s*\(\s*45deg\s*\)", "Bar 1 should rotate(45deg)"),
        (r"rotate\s*\(\s*-45deg\s*\)", "Bar 3 should rotate(-45deg)"),
        (r"opacity\s*:\s*0", "Middle bar should fade to opacity: 0"),
        (r"transition", "Bars need a transition"),
        (r"~", "Need the ~ sibling combinator (checkbox ~ .hamburger)"),
    ])


def check_hard_p02(path):
    c = strip_comments(read_file(path))
    return require_all(c, [
        (r"perspective\s*:", "Container needs perspective"),
        (r"transform-style\s*:\s*preserve-3d",
         "Need transform-style: preserve-3d"),
        (r"backface-visibility\s*:\s*hidden",
         "Faces need backface-visibility: hidden"),
        (r"rotateY\s*\(\s*180deg\s*\)", "Need rotateY(180deg) for the flip"),
        (r"\.card-inner", "Missing '.card-inner' wrapper"),
        (r"\.card-face|\.front|\.back", "Missing .card-face/.front/.back"),
        (r"transition", "Need a transition on the flip"),
        (r"flipped|onclick", "Need a click toggle ('flipped' class)"),
        (r"position\s*:\s*absolute", "Faces need position: absolute"),
    ])


def check_hard_p03(path):
    c = strip_comments(read_file(path))
    ok, msg = require_all(c, [
        (r"\.fade-in\s*\{[^}]*opacity\s*:\s*0",
         ".fade-in should start at opacity: 0"),
        (r"\.fade-in\s*\{[^}]*transform", ".fade-in should start translated"),
        (r"\.fade-in\.visible|\.visible\s*\{[^}]*opacity\s*:\s*1",
         "Need a .visible end state (opacity: 1)"),
        (r"transition", "Need a transition for the reveal"),
        (r"IntersectionObserver", "Missing IntersectionObserver"),
        (r"isIntersecting", "Check entry.isIntersecting"),
        (r"classList\.add\s*\(\s*['\"]visible", "Add 'visible' when shown"),
        (r"querySelectorAll", "Observe all .fade-in elements"),
    ])
    if not ok:
        return ok, msg
    if count(c, r'class="item\s+fade-in"|class="fade-in') < 4:
        return False, "Need at least 4 .fade-in items to scroll through"
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
        print("  LESSON 13 — CSS TRANSITIONS & ANIMATIONS: AUTO-CHECK ALL")
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
