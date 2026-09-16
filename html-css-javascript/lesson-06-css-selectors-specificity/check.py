"""
Auto-Check — Lesson 06: CSS Selectors & Specificity
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
    return require_all(c, [
        (r"\bp\s*\{[^}]*color\s*:\s*gray", "Missing 'p { color: gray }'"),
        (r"\bh1\s*\{[^}]*color\s*:\s*blue", "Missing 'h1 { color: blue }'"),
        (r"\.highlight\s*\{[^}]*background\s*:\s*yellow",
         "Missing '.highlight { background: yellow }'"),
    ])


def check_easy_p02(path):
    c = read_file(path)
    return require_all(c, [
        (r"\ba\s*\{[^}]*color\s*:\s*blue", "Missing 'a { color: blue }'"),
        (r"a\s*:hover[^}]*color\s*:\s*red", "Missing 'a:hover { color: red }'"),
        (r"a\s*:focus[^}]*text-decoration\s*:\s*underline",
         "Missing 'a:focus { text-decoration: underline }'"),
        (r"\.btn\s*\{[^}]*padding", "Missing '.btn' rule with padding"),
    ])


def check_easy_p03(path):
    c = read_file(path)
    return require_all(c, [
        (r"h1\s*,\s*h2\s*,\s*h3\s*\{",
         "Missing grouped selector 'h1, h2, h3 { ... }'"),
        (r"h1\s*,\s*h2\s*,\s*h3\s*\{[^}]*font-family",
         "The h1,h2,h3 group needs font-family"),
        (r"#main-title\s*\{", "Missing '#main-title' ID rule"),
        (r"#main-title\s*\{[^}]*color",
         "#main-title should override the group color"),
    ])


# ---------- medium ----------

def check_medium_p01(path):
    c = read_file(path)
    return require_all(c, [
        (r"article\s+p\s*\{", "Missing descendant selector 'article p'"),
        (r"ul\s*>\s*li\s*\{", "Missing child selector 'ul > li'"),
        (r"h2\s*\+\s*p\s*\{", "Missing adjacent sibling 'h2 + p'"),
    ])


def check_medium_p02(path):
    c = read_file(path)
    ok, msg = require_all(c, [
        (r"\bp\s*\{[^}]*color", "Missing element-level 'p { color: ... }'"),
        (r"\.text|p\.text", "Missing class-level rule (p.text / .text)"),
        (r"#important|p#important", "Missing ID-level rule (p#important / #important)"),
    ])
    if not ok:
        return ok, msg
    if count(c, r"color\s*:") < 3:
        return False, "Need 3 escalating color rules (element, class, ID)"
    return True, "All tests passed!"


def check_medium_p03(path):
    c = read_file(path)
    return require_all(c, [
        (r"li\s*:first-child", "Missing 'li:first-child'"),
        (r"li\s*:last-child", "Missing 'li:last-child'"),
        (r"li\s*:nth-child\s*\(\s*odd\s*\)", "Missing 'li:nth-child(odd)'"),
        (r"li\s*:not\s*\(\s*\.active\s*\)", "Missing 'li:not(.active)'"),
    ])


# ---------- hard ----------

def check_hard_p01(path):
    c = read_file(path)
    return require_all(c, [
        (r"\bbody\s*\{", "Missing element rule on 'body'"),
        (r"\.card\s*\{", "Missing class rule '.card'"),
        (r"#header\s*\{", "Missing ID rule '#header'"),
        (r"article\s+p\s*\{", "Missing descendant 'article p'"),
        (r"nav\s*>\s*ul\s*\{", "Missing child 'nav > ul'"),
        (r"h2\s*\+\s*p\s*\{", "Missing adjacent sibling 'h2 + p'"),
        (r"a\s*:hover", "Missing pseudo-class 'a:hover'"),
        (r"h1\s*,\s*h2\s*,\s*h3\s*\{", "Missing grouped 'h1, h2, h3'"),
    ])


def check_hard_p02(path):
    c = read_file(path)
    return require_all(c, [
        (r'\[\s*type\s*=\s*"text"\s*\]', 'Missing [type="text"] selector'),
        (r'\[\s*href\s*\^\=\s*"https"\s*\]',
         'Missing [href^="https"] prefix selector'),
        (r'\[\s*href\s*\$\=\s*"\.pdf"\s*\]',
         'Missing [href$=".pdf"] suffix selector'),
        (r"\[\s*disabled\s*\]", "Missing [disabled] attribute selector"),
    ])


def check_hard_p03(path):
    c = read_file(path)
    ok, msg = require_all(c, [
        (r"\bp\s*\{", "Missing element-level 'p' rule"),
        (r"\.text", "Missing class-level '.text' rule"),
        (r"#main\s*\{", "Missing ID-level '#main' rule"),
        (r"\w+\s+#main|#\w+\s+#main",
         "Missing a selector MORE specific than #main (e.g. 'body #main')"),
    ])
    if not ok:
        return ok, msg
    code = re.sub(r"/\*.*?\*/", "", c, flags=re.DOTALL)
    if re.search(r"!important", code, FLAGS):
        return False, "Do not use !important — win with higher specificity"
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
        print("  LESSON 06 — CSS SELECTORS & SPECIFICITY: AUTO-CHECK ALL")
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
