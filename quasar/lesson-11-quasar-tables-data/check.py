"""
Auto-Check System — Lesson 11: Quasar Tables & Data
==================================================
.vue files can't execute without a Quasar build step, so these checks are
STRUCTURAL: they verify the required components, props, directives, and
hooks are present in your solution file.

Usage:
    python3 check.py easy/p01     # check one problem
    python3 check.py all          # check all problems
"""

import glob
import os
import re
import sys

LESSON_DIR = os.path.dirname(os.path.abspath(__file__))


def read_body(path):
    """Read a solution file, stripping the leading docstring comment so
    hint text in the problem description isn't mistaken for real code."""
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    content = re.sub(r"^\s*<!--.*?-->", "", content, count=1, flags=re.DOTALL)
    content = re.sub(r"^\s*/\*.*?\*/", "", content, count=1, flags=re.DOTALL)
    return content


def require_all(path, checks):
    """checks: list of (label, regex). Returns (passed, message)."""
    if not os.path.isfile(path):
        return False, f"file not found: {path}"
    body = read_body(path)
    if len(body.strip()) < 30:
        return False, "file looks empty — write your solution first"
    for label, pattern in checks:
        if not re.search(pattern, body):
            return False, f"missing {label} (expected pattern: {pattern})"
    return True, "All tests passed!"


def check_easy_p01(path):
    """Basic QTable with sorting on name and age."""
    return require_all(path, [
        ("<q-table> component", r"<q-table"),
        ("rows bound via :rows", r":rows\s*="),
        ("columns bound via :columns", r":columns\s*="),
        ("row-key attribute", r"row-key\s*="),
        ("sortable column flag", r"sortable"),
        ("'name' column/field", r"['\"]name['\"]"),
        ("'email' column/field", r"['\"]email['\"]"),
        ("'age' column/field", r"['\"]age['\"]"),
        ("at least 5 data rows", r"id:\s*5|length:\s*5|\{[^}]*email[^}]*\}"),
    ])


def check_easy_p02(path):
    """Search filter: QInput with debounce + filtered rows."""
    return require_all(path, [
        ("<q-input> search box", r"<q-input"),
        ("debounce on input", r"debounce"),
        ("v-model binding", r"v-model"),
        ("<q-table> component", r"<q-table"),
        ("filtering logic (computed/:filter/.filter)", r"computed|:filter|\.filter\("),
        ("search state", r"search"),
    ])


def check_easy_p03(path):
    """Custom cells: status badge + edit/delete action buttons."""
    return require_all(path, [
        ("body-cell-status slot", r"body-cell-status"),
        ("<q-badge> in status cell", r"<q-badge"),
        ("active/inactive handling", r"active"),
        ("red/green colors", r"green|red|positive|negative"),
        ("body-cell-actions slot", r"body-cell-actions"),
        ("edit button/icon", r"edit"),
        ("delete button/icon", r"delete"),
        ("<q-td> cell wrapper", r"<q-td"),
    ])


def check_medium_p01(path):
    """Pagination: 50 rows, 10/page, rows-per-page options."""
    return require_all(path, [
        ("<q-table> component", r"<q-table"),
        ("rows-per-page-options", r"rows-per-page-options"),
        ("50 generated rows", r"\b50\b"),
        ("row-key attribute", r"row-key\s*="),
        ("columns definition", r":columns\s*="),
    ])


def check_medium_p02(path):
    """Multiple row selection + Delete Selected with confirm dialog."""
    return require_all(path, [
        ("selection enabled", r"selection\s*="),
        ("v-model:selected binding", r"v-model:selected"),
        ("selected state", r"selected"),
        ("<q-table> component", r"<q-table"),
        ("confirm dialog ($q.dialog)", r"dialog\s*\("),
        ("Delete Selected button", r"[Dd]elete"),
        ("clear selection after delete", r"=\s*\[\s*\]"),
    ])


def check_medium_p03(path):
    """Server-side pagination: @request, loading, simulated API."""
    return require_all(path, [
        ("<q-table> component", r"<q-table"),
        ("@request handler", r"@request|v-on:request"),
        (":loading binding", r":loading"),
        ("pagination state", r"pagination"),
        ("rowsNumber for total count", r"rowsNumber"),
        ("simulated async fetch", r"setTimeout|fetch\s*\(|axios"),
        ("server-side sort handling", r"sortBy"),
        ("initial load on mount", r"onMounted"),
    ])


def check_hard_p01(path):
    """Admin table: search, sort, pagination, selection, CSV export."""
    return require_all(path, [
        ("<q-table> component", r"<q-table"),
        ("search input", r"<q-input"),
        ("row selection", r"v-model:selected"),
        ("status badge cell", r"body-cell-status"),
        ("actions cell", r"body-cell-actions"),
        ("CSV export", r"csv|CSV|Blob"),
        ("bulk delete with dialog", r"dialog\s*\("),
        ("loading state", r"loading"),
        ("no-data empty state", r"no-data|no data|empty"),
        ("100 generated users", r"\b100\b"),
    ])


def check_hard_p02(path):
    """Virtual scroll table with 10,000 rows + search."""
    return require_all(path, [
        ("<q-table> component", r"<q-table"),
        ("virtual-scroll enabled", r"virtual-scroll"),
        ("10,000 rows generated", r"10000|10_000|10,000"),
        ("search input", r"<q-input"),
        ("filtered rows", r"computed|\.filter\("),
        ("row count display", r"length|rows"),
        ("pagination disabled for vscroll", r"rows-per-page-options"),
    ])


def check_hard_p03(path):
    """Editable table: dblclick edit, Enter save, Escape cancel."""
    return require_all(path, [
        ("<q-table> component", r"<q-table"),
        ("double-click to edit", r"dblclick|dbl-click|double-click"),
        ("inline <q-input> editor", r"<q-input"),
        ("Enter saves", r"enter"),
        ("Escape cancels", r"escape|esc\b"),
        ("editing state tracking", r"editing|editValue|edit"),
        ("add row button/function", r"[Aa]dd\s*[Rr]ow|addRow"),
        ("delete row", r"delete"),
        ("notify on save", r"notify"),
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


def find_problem_file(check_id):
    """Find the student's file for a check id like 'easy/p01'.
    Matches easy/p01-*.vue (or other extensions), excluding solutions/."""
    level, num = check_id.split("/")
    pattern = os.path.join(LESSON_DIR, level, f"{num}-*")
    matches = [
        f for f in glob.glob(pattern)
        if os.path.isfile(f) and "solutions" not in f
    ]
    return matches[0] if matches else None


def run_one(check_id):
    if check_id not in CHECKS:
        print(f"ERROR — unknown problem '{check_id}'")
        print(f"Available: {', '.join(CHECKS)}")
        return False
    filepath = find_problem_file(check_id)
    if not filepath:
        print(f"ERROR — file not found: {check_id}-* (create it first)")
        return False
    try:
        passed, msg = CHECKS[check_id](filepath)
    except Exception as e:
        print(f"ERROR — {e}")
        return False
    if passed:
        print(f"PASS — {msg}")
        rel = os.path.relpath(filepath, LESSON_DIR)
        print(f"  Done? Add a DONE marker to the top of {rel}")
    else:
        print(f"FAIL — {msg}")
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
        print("  LESSON 11 — AUTO-CHECK ALL")
        print("=" * 60)
        ok = True
        for check_id in CHECKS:
            ok = run_one(check_id) and ok
        print("=" * 60)
        return

    run_one(target)


if __name__ == "__main__":
    main()
