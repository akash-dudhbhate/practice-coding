"""
Auto-Check — Lesson 19: JavaScript Objects & DOM
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


# ---------- shared JS runner ----------

def js_ok(path, extra=""):
    """Run the file (+ optional assertions); fail on nonzero exit."""
    try:
        r = run_js(path, extra)
    except Exception as e:
        return False, f"could not run node: {e}"
    if r.returncode != 0:
        lines = r.stderr.strip().splitlines() or ["runtime error"]
        err = next((l.strip() for l in lines if "Error" in l), lines[-1])
        return False, f"node error — {err[:140]}"
    return True, "All tests passed!"


# ---------- easy ----------

def check_easy_p01(path):
    c = strip_comments(read_file(path))
    ok, msg = require_all(c, [
        (r"car\s*=\s*\{|const\s+car", "Missing a 'car' object"),
        (r"brand\s*:", "car needs a brand property"),
        (r"model\s*:", "car needs a model property"),
        (r"year\s*:", "car needs a year property"),
        (r"getInfo", "Missing a getInfo() method"),
        (r"this\.", "getInfo should use this.<prop>"),
    ])
    if not ok:
        return ok, msg
    return js_ok(path, """
const info = car.getInfo();
if (typeof info !== "string") throw new Error("getInfo() should return a string");
if (!info.includes(car.brand) || !info.includes(car.model) ||
    !info.includes(String(car.year)))
  throw new Error('getInfo() should include brand, model, and year — e.g. "Toyota Camry (2024)"');
""")


def check_easy_p02(path):
    c = strip_comments(read_file(path))
    return require_all(c, [
        (r'<p[^>]*id\s*=\s*"text"', 'Missing <p id="text">Hello</p>'),
        (r'getElementById\s*\(\s*"text"|getElementById\s*\(\s*.text.',
         'Missing document.getElementById("text")'),
        (r"textContent\s*=", "Set el.textContent"),
        (r"Modified by JS", 'Set the text to "Modified by JS"'),
        (r"classList\.add", "Use classList.add(...)"),
        (r"highlight", "Add the 'highlight' class"),
        (r"\.highlight", "Define a .highlight CSS rule"),
    ])


def check_easy_p03(path):
    c = strip_comments(read_file(path))
    return require_all(c, [
        (r'<button[^>]*id\s*=\s*"addBtn"|<button', "Missing the add button"),
        (r'<ul[^>]*id\s*=\s*"list"|<ul', "Missing <ul id=\"list\">"),
        (r'addEventListener\s*\(\s*"click"|addEventListener\s*\(\s*.click.',
         "Missing a click listener on the button"),
        (r'createElement\s*\(\s*"li"', 'Missing document.createElement("li")'),
        (r"appendChild|append\s*\(", "Append the new <li> to the list"),
        (r"New Item", 'New items should say "New Item"'),
    ])


# ---------- medium ----------

def check_medium_p01(path):
    c = strip_comments(read_file(path))
    ok, msg = require_all(c, [
        (r"function\s+mergeConfigs|mergeConfigs\s*=",
         "Missing 'mergeConfigs' function"),
        (r"\.\.\.", "Use spread to merge"),
    ])
    if not ok:
        return ok, msg
    return js_ok(path, """
const r = mergeConfigs({ theme: "light", fontSize: 14, lang: "en" },
                       { theme: "dark", fontSize: 16 });
if (r.theme !== "dark" || r.fontSize !== 16 || r.lang !== "en")
  throw new Error("userPrefs should override defaults, keep the rest");
""")


def check_medium_p02(path):
    c = strip_comments(read_file(path))
    return require_all(c, [
        (r'<form[^>]*id\s*=\s*"userForm"|<form', "Missing the form"),
        (r'id\s*=\s*"name"', 'Missing <input id="name">'),
        (r'id\s*=\s*"email"', 'Missing <input id="email">'),
        (r'id\s*=\s*"output"|<div[^>]*id', "Missing an #output element"),
        (r'addEventListener\s*\(\s*"click"', "Missing click listener"),
        (r"\.value", "Read inputs via .value"),
        (r"textContent|innerHTML", "Display the result on the page"),
        (r"JSON\.stringify|name\s*:", "Build a user object"),
    ])


def check_medium_p03(path):
    c = strip_comments(read_file(path))
    ok, msg = require_all(c, [
        (r'querySelectorAll\s*\(\s*"\.item"|querySelectorAll',
         "Missing querySelectorAll"),
        (r"forEach", "Use .forEach on the NodeList"),
        (r'addEventListener\s*\(\s*"click"', "Missing click listener"),
        (r"classList\.toggle", "Use classList.toggle"),
        (r"selected", "Toggle the 'selected' class"),
        (r"\.item\.selected|\.selected", "Define a .selected CSS style"),
    ])
    if not ok:
        return ok, msg
    if count(c, r'class="item"') < 3:
        return False, 'Need at least 3 elements with class="item"'
    return True, "All tests passed!"


# ---------- hard ----------

def check_hard_p01(path):
    c = strip_comments(read_file(path))
    return require_all(c, [
        (r'id\s*=\s*"todoInput"|<input', "Missing the todo input"),
        (r'id\s*=\s*"addBtn"', 'Missing button id="addBtn"'),
        (r'id\s*=\s*"todoList"|<ul', "Missing <ul id=\"todoList\">"),
        (r"todos\s*=\s*\[\s*\]|=\s*\[\s*\]", "Keep todos in an array"),
        (r"createElement", "Build rows with createElement"),
        (r"appendChild|append\s*\(", "Append rows to the list"),
        (r"splice|remove\s*\(", "Delete removes from the array/DOM"),
        (r"function\s+render|render\s*\(|render\s*=>",
         "Need a render() that re-draws the list"),
        (r'addEventListener\s*\(\s*"click"', "Missing add click listener"),
        (r"innerHTML", "render() should clear/rebuild via innerHTML"),
    ])


def check_hard_p02(path):
    c = strip_comments(read_file(path))
    return require_all(c, [
        (r'<table[^>]*id\s*=\s*"table"|<table', "Missing the <table>"),
        (r'id\s*=\s*"search"', 'Missing <input id="search">'),
        (r"Object\.keys", "Headers come from Object.keys()"),
        (r"Object\.values|Object\.entries|row\s*\[",
         "Rows read values via Object.values/entries or row[key]"),
        (r'addEventListener\s*\(\s*"input"',
         "Search needs an 'input' listener"),
        (r"\.filter\s*\(", "Filter the users array on search"),
        (r"<th", "Generate <th> headers"),
        (r"<td", "Generate <td> cells"),
        (r"function\s+renderTable|renderTable\s*=", "Missing renderTable()"),
        (r"includes|indexOf", "Search should substring-match values"),
    ])


def check_hard_p03(path):
    c = strip_comments(read_file(path))
    return require_all(c, [
        (r"\.modal-overlay|modal-overlay", "Missing .modal-overlay styles"),
        (r"position\s*:\s*fixed", "Overlay needs position: fixed"),
        (r"\.open", "Missing an .open class state"),
        (r"transition", "Need CSS transitions for open/close"),
        (r"pointer-events", "Hidden overlay needs pointer-events: none"),
        (r'id\s*=\s*"openBtn"|id\s*=\s*"open', "Missing an open button"),
        (r'id\s*=\s*"closeBtn"|close', "Missing a close button"),
        (r"classList\.add", "Open via classList.add('open')"),
        (r"classList\.remove", "Close via classList.remove('open')"),
        (r"e\.target\s*===|event\.target\s*===|closest",
         "Detect overlay clicks (e.target === overlay or closest)"),
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
        print("  LESSON 19 — JAVASCRIPT OBJECTS & DOM: AUTO-CHECK ALL")
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
