"""
Auto-Check — Lesson 20: JavaScript Events
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
        (r"<button", "Missing a <button>"),
        (r'addEventListener\s*\(\s*.click', "Missing click listener"),
        (r"e\.target|event\.target", "Use e.target inside the handler"),
        (r"textContent\s*=", "Set e.target.textContent"),
        (r"Clicked!", 'New text should be "Clicked!"'),
    ])


def check_easy_p02(path):
    c = strip_comments(read_file(path))
    return require_all(c, [
        (r"<input", "Missing the <input> field"),
        (r'<p[^>]*id\s*=\s*"output"|id\s*=\s*"output"',
         "Missing an output element"),
        (r'addEventListener\s*\(\s*.input', "Missing 'input' listener"),
        (r"e\.target\.value|event\.target\.value",
         "Read e.target.value"),
        (r"textContent\s*=", "Write it into the output element"),
    ])


def check_easy_p03(path):
    c = strip_comments(read_file(path))
    return require_all(c, [
        (r'<a\s+[^>]*href\s*=\s*"https?://', "Missing a real link with href"),
        (r'addEventListener\s*\(\s*.click', "Missing click listener"),
        (r"preventDefault", "Call e.preventDefault()"),
        (r"alert\s*\(", "Show an alert() instead of navigating"),
    ])


# ---------- medium ----------

def check_medium_p01(path):
    c = strip_comments(read_file(path))
    ok, msg = require_all(c, [
        (r"<ul", "Missing <ul>"),
        (r'addEventListener\s*\(\s*.click',
         "Missing ONE click listener on the <ul>"),
        (r"e\.target|event\.target|closest",
         "Detect which <li> via e.target or closest()"),
        (r'tagName|closest\s*\(\s*.li', "Check the clicked element is an LI"),
        (r"console\.log", "Log which item was clicked"),
    ])
    if not ok:
        return ok, msg
    if count(c, r"<li") < 5:
        return False, "Need 5 <li> items"
    if count(c, r'addEventListener\s*\(\s*.click') > 1:
        return False, "Use ONE delegated listener on the <ul>, not per-item"
    return True, "All tests passed!"


def check_medium_p02(path):
    c = strip_comments(read_file(path))
    return require_all(c, [
        (r"<form", "Missing <form>"),
        (r'id\s*=\s*"name"', 'Missing input id="name"'),
        (r'id\s*=\s*"email"', 'Missing input id="email"'),
        (r'id\s*=\s*"message"', 'Missing a message element'),
        (r'addEventListener\s*\(\s*.submit', "Missing 'submit' listener"),
        (r"preventDefault", "Call e.preventDefault()"),
        (r"\.value", "Read field values via .value"),
        (r"!\s*\w+\s*\|\||required|trim", "Validate that both fields are filled"),
        (r"textContent\s*=", "Write success/error text into the message"),
    ])


def check_medium_p03(path):
    c = strip_comments(read_file(path))
    return require_all(c, [
        (r'<input[^>]*id\s*=\s*"search"|id\s*=\s*"search"',
         'Missing <input id="search">'),
        (r'addEventListener\s*\(\s*.keydown', "Missing 'keydown' listener"),
        (r"ctrlKey", "Check e.ctrlKey for Ctrl+K"),
        (r'e\.key\s*===?\s*.k|key\s*===?\s*.k', "Check e.key === 'k'"),
        (r"\.focus\s*\(", "Ctrl+K should call search.focus()"),
        (r"Escape", "Handle the Escape key"),
        (r'value\s*=\s*.""|\.value\s*=', "Escape should clear the value"),
        (r"preventDefault", "preventDefault the Ctrl+K shortcut"),
    ])


# ---------- hard ----------

def check_hard_p01(path):
    c = strip_comments(read_file(path))
    return require_all(c, [
        (r"\.dropdown", "Missing .dropdown styles"),
        (r"dropdown-menu", "Missing .dropdown-menu element/styles"),
        (r"\.open|classList\.toggle", "Toggle an 'open' class"),
        (r"stopPropagation", "Button needs e.stopPropagation()"),
        (r'document\.addEventListener\s*\(\s*.click',
         "Document-level click closes the menu"),
        (r"classList\.(remove|toggle)", "Close removes the 'open' class"),
        (r'addEventListener\s*\(\s*.keydown', "Missing keydown listener"),
        (r"Escape", "Escape should close the dropdown"),
        (r"display\s*:\s*none|display\s*:\s*block",
         "Menu should be hidden by default, shown when open"),
    ])


def check_hard_p02(path):
    c = strip_comments(read_file(path))
    return require_all(c, [
        (r'\.draggable|id\s*=\s*"drag"', "Missing the draggable element"),
        (r'addEventListener\s*\(\s*.mousedown', "Missing mousedown listener"),
        (r'addEventListener\s*\(\s*.mousemove', "Missing mousemove listener"),
        (r'addEventListener\s*\(\s*.mouseup', "Missing mouseup listener"),
        (r"clientX|clientY", "Track position with clientX/clientY"),
        (r"isDragging|dragging", "Track drag state with a flag"),
        (r"offsetLeft|offsetX|offsetTop|offsetY",
         "Use offsets so the drag doesn't jump"),
        (r"CustomEvent", "Dispatch a CustomEvent('dropped')"),
        (r"dropped", "Name the custom event 'dropped'"),
        (r"dispatchEvent", "Fire it via dispatchEvent"),
        (r"position\s*:\s*absolute", "Element needs position: absolute"),
    ])


def check_hard_p03(path):
    c = strip_comments(read_file(path))
    return require_all(c, [
        (r'addEventListener\s*\(\s*.scroll', "Missing 'scroll' listener"),
        (r"scrollY", "Check window.scrollY"),
        (r"innerHeight", "Add window.innerHeight"),
        (r"scrollHeight|documentHeight", "Compare against document height"),
        (r"-\s*100|100\s*\)", "Trigger ~100px before the bottom"),
        (r"setTimeout", "Simulate loading with setTimeout"),
        (r"createElement|appendChild|innerHTML", "Append new items"),
        (r"loading", "Guard with a loading flag / show a loader"),
        (r"removeEventListener", "Show how removeEventListener cleans up"),
        (r'id\s*=\s*"container"|container', "Missing a #container element"),
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
        print("  LESSON 20 — JAVASCRIPT EVENTS: AUTO-CHECK ALL")
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
