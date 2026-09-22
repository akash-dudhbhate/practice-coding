"""
Auto-Check System — Lesson 01: Quasar Basics
=============================================
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
    """q-page wrapper with an h1 heading."""
    return _vue_check(path, [
        ("q-page", "a <q-page> wrapper"),
        ("<h1", "an <h1> heading"),
    ])


def check_easy_p02(path):
    """Two q-btn components with different colors."""
    ok, msg = _vue_check(path, [
        ("q-btn", "a <q-btn> component"),
    ])
    if not ok:
        return ok, msg
    src = _read(path)
    if _count(src, r"<q-btn") < 2:
        return False, "expected at least TWO <q-btn> components"
    if _count(src, r":?color=") < 2:
        return False, "each button needs its own color prop (e.g. color=\"primary\")"
    return True, "All tests passed!"


def check_easy_p03(path):
    """Toggle visibility with ref + v-if."""
    return _vue_check(path, [
        ("ref(", "a ref() for the visible flag"),
        ("v-if", "v-if conditional rendering"),
        ("q-btn", "a <q-btn> toggle button"),
        ("@click", "a click handler (@click)"),
    ])


# ---------------- medium ----------------

def check_medium_p01(path):
    """q-input with v-model + live display."""
    return _vue_check(path, [
        ("q-input", "a <q-input> component"),
        ("v-model", "v-model two-way binding"),
        ("ref(", "a ref() to hold the text"),
        ("{{", "interpolation displaying the text"),
    ])


def check_medium_p02(path):
    """Counter with increment/decrement/reset + disabled state."""
    ok, msg = _vue_check(path, [
        ("ref(", "a ref() for the count"),
        ("q-btn", "buttons"),
        ("@click", "click handlers"),
        (":disable", "a :disable binding for the decrement button"),
    ])
    if not ok:
        return ok, msg
    if _count(_read(path), r"<q-btn") < 3:
        return False, "expected THREE <q-btn> components (inc / dec / reset)"
    return True, "All tests passed!"


def check_medium_p03(path):
    """Add items to a list with q-input, q-btn, q-list."""
    return _vue_check(path, [
        ("q-input", "a <q-input> for the new item"),
        ("v-model", "v-model binding"),
        ("q-btn", "an Add <q-btn>"),
        ("q-list", "a <q-list>"),
        ("q-item", "<q-item> entries"),
        ("v-for", "v-for over the items array"),
    ])


# ---------------- hard ----------------

def check_hard_p01(path):
    """Full todo list: toggle done, delete, empty state."""
    return _vue_check(path, [
        ("q-input", "a <q-input> for new todos"),
        ("v-model", "v-model binding"),
        ("q-checkbox", "a <q-checkbox> for done state"),
        ("q-list", "a <q-list>"),
        ("q-item", "<q-item> entries"),
        ("v-for", "v-for over the todos"),
        ("computed", "a computed() (e.g. done count)"),
        ("v-if", "an empty-state v-if"),
    ])


def check_hard_p02(path):
    """q-color picker with live preview q-card."""
    return _vue_check(path, [
        ("q-color", "a <q-color> picker"),
        ("v-model", "v-model on the picker"),
        ("q-card", "a <q-card> preview"),
        (":style", "a :style binding for the preview box"),
        ("ref(", "a ref() holding the color string"),
    ])


def check_hard_p03(path):
    """3-step form wizard with conditional rendering."""
    ok, msg = _vue_check(path, [
        ("ref(", "a ref() for the step"),
        ("v-if", "v-if per step"),
        ("q-input", "<q-input> fields"),
        ("q-btn", "Back/Next/Submit <q-btn>s"),
        ("v-model", "v-model on the inputs"),
    ])
    if not ok:
        return ok, msg
    src = _read(path)
    if _count(src, r"v-if") < 3:
        return False, "expected at least 3 v-if blocks (one per step)"
    if "step" not in src:
        return False, "expected a 'step' state variable"
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
        print("  LESSON 01 — QUASAR BASICS — AUTO-CHECK ALL")
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
