"""
Auto-Check — Lesson 08: CSS Text & Typography
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
        (r"body\s*\{[^}]*font-family\s*:[^}]*sans-serif",
         "Missing 'body' font stack ending in sans-serif"),
        (r"h1\s*\{[^}]*font-family\s*:[^}]*serif",
         "Missing 'h1' serif font stack"),
        (r"code\s*\{[^}]*font-family\s*:[^}]*monospace",
         "Missing 'code' monospace font stack"),
    ])


def check_easy_p02(path):
    c = strip_comments(read_file(path))
    return require_all(c, [
        (r"html\s*\{[^}]*font-size\s*:\s*16px",
         "Missing 'html { font-size: 16px }' root size"),
        (r"body\s*\{[^}]*font-size\s*:\s*1rem",
         "Missing 'body { font-size: 1rem }'"),
        (r"h1\s*\{[^}]*font-size\s*:\s*2rem",
         "Missing 'h1 { font-size: 2rem }'"),
        (r"h2\s*\{[^}]*font-size\s*:\s*1\.5rem",
         "Missing 'h2 { font-size: 1.5rem }'"),
        (r"\.small\s*\{[^}]*font-size", "Missing '.small' size class"),
    ])


def check_easy_p03(path):
    c = strip_comments(read_file(path))
    return require_all(c, [
        (r"\bp\s*\{[^}]*line-height\s*:\s*1\.5",
         "Missing 'p { line-height: 1.5 }'"),
        (r"h1\s*\{[^}]*line-height\s*:\s*1\.2",
         "Missing 'h1 { line-height: 1.2 }'"),
        (r"h1\s*\{[^}]*text-align\s*:\s*center",
         "Missing 'h1 { text-align: center }'"),
        (r"\.date\s*\{[^}]*text-align\s*:\s*right",
         "Missing '.date { text-align: right }'"),
    ])


# ---------- medium ----------

def check_medium_p01(path):
    c = strip_comments(read_file(path))
    return require_all(c, [
        (r"h1\s*\{[^}]*font-weight\s*:\s*700",
         "Missing 'h1 { font-weight: 700 }'"),
        (r"strong\s*\{[^}]*font-weight\s*:\s*700",
         "Missing 'strong { font-weight: 700 }'"),
        (r"em\s*\{[^}]*font-style\s*:\s*italic",
         "Missing 'em { font-style: italic }'"),
        (r"\.caption\s*\{[^}]*font-style\s*:\s*italic",
         "Missing '.caption' italic style"),
        (r"\.caption\s*\{[^}]*font-weight\s*:\s*300",
         "Missing '.caption' light weight (300)"),
    ])


def check_medium_p02(path):
    c = strip_comments(read_file(path))
    return require_all(c, [
        (r"\ba\s*\{[^}]*text-decoration\s*:\s*underline",
         "Missing 'a { text-decoration: underline }'"),
        (r"a\s*:hover[^}]*text-decoration\s*:\s*none",
         "Missing 'a:hover { text-decoration: none }'"),
        (r"nav\s+a\s*\{[^}]*text-decoration\s*:\s*none",
         "Missing 'nav a { text-decoration: none }'"),
        (r"\.done\s*\{[^}]*text-decoration\s*:\s*line-through",
         "Missing '.done { text-decoration: line-through }'"),
    ])


def check_medium_p03(path):
    c = strip_comments(read_file(path))
    return require_all(c, [
        (r"h1\s*\{[^}]*letter-spacing\s*:\s*2px",
         "Missing 'h1 { letter-spacing: 2px }'"),
        (r"h1\s*\{[^}]*text-transform\s*:\s*uppercase",
         "Missing 'h1 { text-transform: uppercase }'"),
        (r"\.btn\s*\{[^}]*text-transform\s*:\s*uppercase",
         "Missing '.btn' uppercase"),
        (r"\.label\s*\{[^}]*text-transform\s*:\s*capitalize",
         "Missing '.label { text-transform: capitalize }'"),
        (r"\.lower\s*\{[^}]*text-transform\s*:\s*lowercase",
         "Missing '.lower { text-transform: lowercase }'"),
    ])


# ---------- hard ----------

def check_hard_p01(path):
    c = strip_comments(read_file(path))
    return require_all(c, [
        (r"html\s*\{[^}]*font-size\s*:\s*16px",
         "Missing 'html { font-size: 16px }'"),
        (r"body\s*\{[^}]*font-family", "Missing body font-family"),
        (r"body\s*\{[^}]*line-height", "Missing body line-height"),
        (r"h1\s*,\s*h2\s*,\s*h3\s*\{[^}]*font-weight",
         "Missing grouped 'h1, h2, h3' heading rule"),
        (r"h1\s*\{[^}]*font-size\s*:\s*2\.5rem",
         "Missing 'h1 { font-size: 2.5rem }'"),
        (r"a\s*:hover[^}]*text-decoration\s*:\s*underline",
         "Missing 'a:hover { text-decoration: underline }'"),
        (r"\.small\s*\{", "Missing '.small' utility class"),
        (r"\.caption\s*\{", "Missing '.caption' utility class"),
    ])


def check_hard_p02(path):
    c = strip_comments(read_file(path))
    return require_all(c, [
        (r"\.hero\s+h1\s*\{[^}]*text-shadow",
         "Missing '.hero h1' with text-shadow"),
        (r"\.hero\s+h1\s*\{[^}]*color\s*:\s*#fff|\.hero\s+h1\s*\{[^}]*color\s*:\s*white",
         "Missing '.hero h1' white color"),
        (r"\.hero\s+p\s*\{[^}]*text-shadow",
         "Missing '.hero p' with text-shadow"),
        (r"\.glow\s*\{[^}]*text-shadow",
         "Missing '.glow' glow text-shadow"),
        (r"rgba\s*\(", "Shadows should use rgba() for transparency"),
    ])


def check_hard_p03(path):
    c = strip_comments(read_file(path))
    return require_all(c, [
        (r":root\s*\{[^}]*--font-body", "Missing --font-body variable in :root"),
        (r":root\s*\{[^}]*--font-heading",
         "Missing --font-heading variable in :root"),
        (r":root\s*\{[^}]*--color-text", "Missing --color-text variable"),
        (r":root\s*\{[^}]*--color-link", "Missing --color-link variable"),
        (r"font-family\s*:\s*var\(\s*--font-body",
         "body should use var(--font-body)"),
        (r"font-family\s*:\s*var\(\s*--font-heading",
         "headings should use var(--font-heading)"),
        (r"color\s*:\s*var\(\s*--color-link",
         "links should use var(--color-link)"),
        (r"\.lead\s*\{", "Missing '.lead' class"),
        (r"\.caption\s*\{", "Missing '.caption' class"),
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
        print("  LESSON 08 — CSS TEXT & TYPOGRAPHY: AUTO-CHECK ALL")
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
