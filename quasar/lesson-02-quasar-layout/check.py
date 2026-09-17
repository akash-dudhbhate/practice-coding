"""
Auto-Check System — Lesson 02: Quasar Layout System
===================================================
.vue / .js files can't be executed without a Quasar build step,
so these are STRUCTURAL checks: the file must exist, have the
right blocks, and contain the required components/directives/hooks.

Usage:
    python3 check.py easy/p01
    python3 check.py medium/p02
    python3 check.py hard/p03
    python3 check.py all
"""

import os
import re
import sys
import glob

LESSON_TITLE = "LESSON 02 — QUASAR LAYOUT"


# ---------------- helpers ----------------

def _read(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            text = f.read()
    except OSError:
        return None
    # Strip comments so instruction text in the problem header (or any
    # comment the learner adds) can't satisfy the structural checks.
    text = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)
    text = re.sub(r"/\*.*?\*/", "", text, flags=re.DOTALL)
    text = re.sub(r"(?<!:)//[^\n]*", "", text)
    return text


def _vue_check(path, required):
    """Check a .vue file. `required` = list of (token, description)."""
    src = _read(path)
    if src is None:
        return False, f"could not read file: {path}"
    if "<template" not in src:
        return False, "missing <template> block"
    if "<script" not in src:
        return False, "missing <script> block"
    for token, desc in required:
        if token not in src:
            return False, f"missing {desc} — expected to find '{token}'"
    return True, "All tests passed!"


def _js_check(path, required):
    """Check a .js/.ts file. `required` = list of (token, description)."""
    src = _read(path)
    if src is None:
        return False, f"could not read file: {path}"
    for token, desc in required:
        if token not in src:
            return False, f"missing {desc} — expected to find '{token}'"
    return True, "All tests passed!"


def _count(src, pattern):
    return len(re.findall(pattern, src))


# ---------------- easy ----------------

def check_easy_p01(path):
    """Basic layout: q-layout + q-header + q-page-container + q-page."""
    return _vue_check(path, [
        ("q-layout", "a <q-layout> root"),
        ("view=", "a view prop on q-layout"),
        ("q-header", "a <q-header>"),
        ("q-toolbar", "a <q-toolbar>"),
        ("q-toolbar-title", "a <q-toolbar-title>"),
        ("q-page-container", "a <q-page-container>"),
        ("q-page", "a <q-page> inside the container"),
    ])


def check_easy_p02(path):
    """Left drawer with nav list + header toggle button."""
    ok, msg = _vue_check(path, [
        ("q-layout", "a <q-layout> root"),
        ("q-drawer", "a <q-drawer>"),
        ("v-model", "v-model on the drawer"),
        ("q-list", "a <q-list> of nav items"),
        ("q-item", "<q-item> nav entries"),
        ("q-btn", "a toggle <q-btn> in the header"),
        ("@click", "a click handler toggling the drawer"),
        ("ref(", "a ref() for the drawer state"),
    ])
    if not ok:
        return ok, msg
    if _count(_read(path), r"<q-item") < 3:
        return False, "expected at least 3 <q-item> nav entries (Home/About/Contact)"
    return True, "All tests passed!"


def check_easy_p03(path):
    """Footer with 3 q-tabs."""
    ok, msg = _vue_check(path, [
        ("q-layout", "a <q-layout> root"),
        ("q-footer", "a <q-footer>"),
        ("q-tabs", "<q-tabs>"),
        ("q-tab", "<q-tab> entries"),
        ("v-model", "v-model on q-tabs"),
        ("ref(", "a ref() for the active tab"),
    ])
    if not ok:
        return ok, msg
    if _count(_read(path), r"<q-tab ") + _count(_read(path), r"<q-tab>") < 3:
        return False, "expected 3 <q-tab> entries (Home/Search/Settings)"
    return True, "All tests passed!"


# ---------------- medium ----------------

def check_medium_p01(path):
    """Responsive drawer: show-if-above + breakpoint 1024."""
    return _vue_check(path, [
        ("q-drawer", "a <q-drawer>"),
        ("v-model", "v-model on the drawer"),
        ("show-if-above", "show-if-above for desktop"),
        ("breakpoint", "a breakpoint prop"),
        ("1024", "breakpoint of 1024px"),
        ("q-btn", "a menu toggle <q-btn>"),
        ("@click", "a click handler toggling the drawer"),
    ])


def check_medium_p02(path):
    """Left + right drawers, both toggleable from header."""
    ok, msg = _vue_check(path, [
        ("q-drawer", "q-drawer components"),
        ("q-list", "q-list content in drawers"),
        ("@click", "toggle click handlers"),
        ("ref(", "refs for drawer state"),
    ])
    if not ok:
        return ok, msg
    src = _read(path)
    if _count(src, r"<q-drawer") < 2:
        return False, "expected TWO <q-drawer> components (left + right)"
    if _count(src, r"v-model") < 2:
        return False, "each drawer needs its own v-model ref"
    if 'side="right"' not in src and "side='right'" not in src:
        return False, "right drawer needs side=\"right\""
    if _count(src, r"<q-btn") < 2:
        return False, "expected 2 header toggle buttons"
    return True, "All tests passed!"


def check_medium_p03(path):
    """Mini-mode drawer toggled from the header."""
    return _vue_check(path, [
        ("q-drawer", "a <q-drawer>"),
        ("v-model", "v-model on the drawer"),
        (":mini", "a :mini binding for mini mode"),
        ("q-btn", "a header toggle <q-btn>"),
        ("@click", "a click handler flipping mini state"),
        ("q-list", "a <q-list> with icon + label items"),
        ("q-icon", "icons in the nav items"),
    ])


# ---------------- hard ----------------

def check_hard_p01(path):
    """Reveal header + toolbar with menu, title, 2 actions."""
    ok, msg = _vue_check(path, [
        ("q-layout", "a <q-layout> root"),
        ("q-header", "a <q-header>"),
        ("reveal", "the reveal prop on q-header"),
        ("q-toolbar", "a <q-toolbar>"),
        ("q-toolbar-title", "a <q-toolbar-title>"),
        ("q-drawer", "a <q-drawer> toggled by the menu button"),
        ("v-for", "scrollable content (v-for lines)"),
    ])
    if not ok:
        return ok, msg
    if _count(_read(path), r"<q-btn") < 3:
        return False, "expected at least 3 <q-btn> (menu + 2 actions)"
    return True, "All tests passed!"


def check_hard_p02(path):
    """Admin layout: avatar dropdown, expansion sections, footer."""
    ok, msg = _vue_check(path, [
        ("q-layout", "a <q-layout> root"),
        ("q-header", "a <q-header>"),
        ("q-avatar", "a <q-avatar> in the header"),
        ("q-menu", "a <q-menu> dropdown on the avatar"),
        ("q-drawer", "a <q-drawer>"),
        ("q-expansion-item", "collapsible nav sections"),
        ("q-footer", "a <q-footer> with status"),
        ("q-item", "nav <q-item> entries"),
    ])
    if not ok:
        return ok, msg
    if _count(_read(path), r"<q-expansion-item") < 2:
        return False, "expected at least 2 <q-expansion-item> sections (Users, Settings)"
    return True, "All tests passed!"


def check_hard_p03(path):
    """Two layouts wired to routes (MainLayout implemented here)."""
    ok, msg = _vue_check(path, [
        ("q-layout", "a <q-layout> root"),
        ("q-page-container", "a <q-page-container>"),
        ("router-view", "<router-view /> for child pages"),
        ("q-drawer", "a <q-drawer> (MainLayout)"),
        ("to=", "nav items with to= route links"),
    ])
    if not ok:
        return ok, msg
    # These two requirements intentionally live in a comment (the problem
    # asks learners to describe BlankLayout + routes config), so read raw.
    with open(path, "r", encoding="utf-8") as f:
        raw = f.read()
    if "BlankLayout" not in raw and "blank" not in raw.lower():
        return False, "expected the BlankLayout template described in a comment"
    if "routes" not in raw and "path:" not in raw:
        return False, "expected the routes config described in a comment"
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


# ---------------- runner ----------------

def find_problem_file(level_dir, check_id):
    """Find easy/p01-* file (any extension), excluding the solutions dir."""
    level, num = check_id.split("/")
    pattern = os.path.join(level_dir, level, f"{num}-*")
    matches = [
        f for f in glob.glob(pattern)
        if os.path.isfile(f) and "solutions" not in f
    ]
    return matches[0] if matches else None


def run_one(level_dir, check_id):
    filepath = find_problem_file(level_dir, check_id)
    if filepath is None:
        return "NOT FOUND", f"no file matching {check_id}-* (create it first)"
    try:
        passed, msg = CHECKS[check_id](filepath)
    except Exception as e:
        if "NoneType" in str(e):
            print(f"FAIL — a function returned None — write the body!")
        else:
            return "ERROR", f"{e} (in {filepath})"
    return ("PASS" if passed else "FAIL"), msg, filepath


def main():
    level_dir = os.path.dirname(os.path.abspath(__file__))

    if len(sys.argv) < 2:
        print("Usage: python3 check.py <level>/<problem>")
        print("Example: python3 check.py easy/p01")
        print("         python3 check.py all")
        sys.exit(1)

    target = sys.argv[1]

    if target == "all":
        print("=" * 60)
        print(f"  {LESSON_TITLE} — AUTO-CHECK ALL")
        print("=" * 60)
        for check_id in CHECKS:
            result = run_one(level_dir, check_id)
            status, msg = result[0], result[1]
            print(f"  {check_id}: {status} — {msg}")
        print("=" * 60)
        return

    if "/" not in target or target not in CHECKS:
        print(f"Error: unknown problem '{target}'")
        print(f"Available: {list(CHECKS.keys())}")
        sys.exit(1)

    result = run_one(level_dir, target)
    status, msg = result[0], result[1]

    if status == "PASS":
        filepath = result[2]
        print(f"PASS — {msg}")
        print(f"  Add a DONE marker (e.g. <!-- DONE -->) to {filepath}")
    elif status == "FAIL":
        print(f"FAIL — {msg}")
    else:
        print(f"{status} — {msg}")


if __name__ == "__main__":
    main()
