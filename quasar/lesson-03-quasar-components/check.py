"""
Auto-Check System — Lesson 03: Quasar Components
================================================
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

LESSON_TITLE = "LESSON 03 — QUASAR COMPONENTS"


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
    """q-card with image, title, body, 2 action buttons."""
    ok, msg = _vue_check(path, [
        ("q-card", "a <q-card>"),
        ("q-img", "a <q-img> image"),
        ("q-card-section", "<q-card-section> blocks"),
        ("q-card-actions", "a <q-card-actions> block"),
        ("q-btn", "action <q-btn>s"),
    ])
    if not ok:
        return ok, msg
    src = _read(path)
    if _count(src, r"<q-btn") < 2:
        return False, "expected 2 <q-btn> actions (Share, Read More)"
    if _count(src, r"<q-card-section") < 2:
        return False, "expected at least 2 <q-card-section> blocks (title + body)"
    return True, "All tests passed!"


def check_easy_p02(path):
    """q-list of 3 items: avatar icon, label, caption, side badge."""
    ok, msg = _vue_check(path, [
        ("q-list", "a <q-list>"),
        ("q-item", "<q-item> entries"),
        ("q-item-section", "<q-item-section> slots"),
        ("q-badge", "a <q-badge> status"),
        ("v-for", "v-for over the users array"),
        ("avatar", "an avatar q-item-section"),
    ])
    if not ok:
        return ok, msg
    if _count(_read(path), r"side") < 1:
        return False, "expected a side q-item-section for the badge"
    return True, "All tests passed!"


def check_easy_p03(path):
    """q-tabs + q-tab-panels with 3 matching tabs."""
    ok, msg = _vue_check(path, [
        ("q-tabs", "<q-tabs>"),
        ("q-tab", "<q-tab> entries"),
        ("q-tab-panels", "<q-tab-panels>"),
        ("q-tab-panel", "<q-tab-panel> blocks"),
        ("v-model", "v-model shared by tabs and panels"),
        ("ref(", "a ref() for the active tab"),
    ])
    if not ok:
        return ok, msg
    src = _read(path)
    if _count(src, r"<q-tab-panel") < 3:
        return False, "expected 3 <q-tab-panel> blocks (Overview/Details/Reviews)"
    if _count(src, r"<q-tab ") + _count(src, r"<q-tab>") < 3:
        return False, "expected 3 <q-tab> entries"
    return True, "All tests passed!"


# ---------------- medium ----------------

def check_medium_p01(path):
    """q-table: 3 columns, 5 rows, sorting on Name/Email."""
    ok, msg = _vue_check(path, [
        ("q-table", "a <q-table>"),
        (":rows", "a :rows binding"),
        (":columns", "a :columns binding"),
        ("row-key", "a row-key prop"),
        ("sortable", "sortable columns"),
    ])
    if not ok:
        return ok, msg
    src = _read(path)
    if _count(src, r"sortable:\s*true") < 2:
        return False, "expected sortable: true on at least 2 columns (Name, Email)"
    return True, "All tests passed!"


def check_medium_p02(path):
    """q-dialog opened by a button, containing a form card."""
    ok, msg = _vue_check(path, [
        ("q-dialog", "a <q-dialog>"),
        ("v-model", "v-model on the dialog"),
        ("q-card", "a <q-card> inside the dialog"),
        ("q-input", "<q-input> fields"),
        ("v-close-popup", "v-close-popup on the buttons"),
        ("q-btn", "an opener <q-btn> plus dialog buttons"),
        ("@click", "a click handler opening the dialog"),
    ])
    if not ok:
        return ok, msg
    if _count(_read(path), r"<q-input") < 2:
        return False, "expected 2 <q-input> fields (name, email)"
    return True, "All tests passed!"


def check_medium_p03(path):
    """Filter bar of 4 removable q-chips."""
    return _vue_check(path, [
        ("q-chip", "<q-chip> entries"),
        ("removable", "the removable prop on chips"),
        ("@remove", "a @remove handler"),
        ("v-for", "v-for over the chips array"),
        ("ref(", "a ref() holding the chips"),
        ("filter", "array filtering to remove the chip"),
        ("v-if", "a v-if for the empty state"),
    ])


# ---------------- hard ----------------

def check_hard_p01(path):
    """q-table with body-cell-status slot rendering q-badge."""
    return _vue_check(path, [
        ("q-table", "a <q-table>"),
        (":rows", "a :rows binding"),
        (":columns", "a :columns binding"),
        ("row-key", "a row-key prop"),
        ("body-cell", "a #body-cell-* slot"),
        ("q-badge", "a <q-badge> inside the slot"),
        ("q-td", "a <q-td> wrapper in the slot"),
    ])


def check_hard_p02(path):
    """Profile card: avatar, chips, separators, contact list."""
    ok, msg = _vue_check(path, [
        ("q-card", "a <q-card>"),
        ("q-avatar", "a <q-avatar>"),
        ("q-chip", "<q-chip> skills"),
        ("q-separator", "<q-separator> between sections"),
        ("q-list", "a <q-list> for contact info"),
        ("q-item", "<q-item> contact entries"),
        ("v-for", "v-for over skills/contacts"),
        ("ref(", "a ref() holding the user object"),
    ])
    if not ok:
        return ok, msg
    if _count(_read(path), r"<q-separator") < 2:
        return False, "expected at least 2 <q-separator> dividers"
    return True, "All tests passed!"


def check_hard_p03(path):
    """Settings page: 3 expansion sections with toggles."""
    ok, msg = _vue_check(path, [
        ("q-expansion-item", "<q-expansion-item> sections"),
        ("q-toggle", "<q-toggle> switches"),
        ("v-model", "v-model on the toggles"),
        ("q-list", "a <q-list> inside each section"),
        ("q-separator", "<q-separator> between sections"),
        ("ref(", "a ref() settings object"),
    ])
    if not ok:
        return ok, msg
    src = _read(path)
    if _count(src, r"<q-expansion-item") < 3:
        return False, "expected 3 <q-expansion-item> sections (Profile/Privacy/Notifications)"
    if _count(src, r"<q-toggle") < 4:
        return False, "expected at least 4 <q-toggle> switches (2 per section)"
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
