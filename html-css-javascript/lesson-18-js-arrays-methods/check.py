"""
Auto-Check — Lesson 18: JavaScript Arrays & Methods
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
        if "NoneType" in str(e):
            print(f"FAIL — a function returned None — write the body!")
        else:
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
        (r"\.map\s*\(", "Missing .map() to double"),
        (r"\.filter\s*\(", "Missing .filter() to keep evens"),
        (r"\.reduce\s*\(", "Missing .reduce() to sum"),
        (r"console\.log", "Print the results"),
    ])
    if not ok:
        return ok, msg
    return js_ok(path)


def check_easy_p02(path):
    c = strip_comments(read_file(path))
    ok, msg = require_all(c, [
        (r"\.push\s*\(", "Missing .push()"),
        (r"\.pop\s*\(", "Missing .pop()"),
        (r"\.shift\s*\(", "Missing .shift()"),
        (r"\.unshift\s*\(", "Missing .unshift()"),
    ])
    if not ok:
        return ok, msg
    if count(c, r"console\.log") < 4:
        return False, "console.log the array after EACH operation (4+ logs)"
    return js_ok(path)


def check_easy_p03(path):
    c = strip_comments(read_file(path))
    ok, msg = require_all(c, [
        (r"function\s+findUser|findUser\s*=", "Missing 'findUser' function"),
        (r"\.find\s*\(", "Use users.find(...)"),
        (r"Not found", 'Return "Not found" for a missing id'),
    ])
    if not ok:
        return ok, msg
    return js_ok(path, """
const us = [{ id: 1, name: "Alice" }, { id: 2, name: "Bob" }];
const hit = findUser(us, 2);
if (!hit || hit.name !== "Bob") throw new Error("findUser(users,2) should return Bob");
if (findUser(us, 99) !== "Not found") throw new Error('miss should return "Not found"');
""")


# ---------- medium ----------

def check_medium_p01(path):
    c = strip_comments(read_file(path))
    ok, msg = require_all(c, [
        (r"function\s+processNumbers|processNumbers\s*=",
         "Missing 'processNumbers'"),
        (r"\.map\s*\(", "Missing .map()"),
        (r"\.filter\s*\(", "Missing .filter()"),
        (r"\.sort\s*\(", "Missing .sort() with numeric comparator"),
    ])
    if not ok:
        return ok, msg
    return js_ok(path, """
const r = processNumbers([3, 7, 1, 8, 5, 12]);
if (JSON.stringify(r) !== JSON.stringify([14, 16, 24]))
  throw new Error("expected [14,16,24], got " + JSON.stringify(r));
""")


def check_medium_p02(path):
    c = strip_comments(read_file(path))
    ok, msg = require_all(c, [
        (r"function\s+groupBy|groupBy\s*=", "Missing 'groupBy' function"),
        (r"\.reduce\s*\(", "Use .reduce() to build the groups"),
        (r"item\s*\[\s*key\s*\]|\[\s*key\s*\]",
         "Index into each item with item[key]"),
    ])
    if not ok:
        return ok, msg
    return js_ok(path, """
const us = [
  { name: "Alice", city: "Mumbai" },
  { name: "Bob", city: "London" },
  { name: "Charlie", city: "Mumbai" },
];
const r = groupBy(us, "city");
if (!r.Mumbai || r.Mumbai.length !== 2) throw new Error("Mumbai should have 2 users");
if (!r.London || r.London.length !== 1) throw new Error("London should have 1 user");
""")


def check_medium_p03(path):
    c = strip_comments(read_file(path))
    ok, msg = require_all(c, [
        (r"function\s+removeDuplicates|removeDuplicates\s*=",
         "Missing 'removeDuplicates' function"),
        (r"new\s+Set|indexOf", "Use Set or filter+indexOf"),
    ])
    if not ok:
        return ok, msg
    return js_ok(path, """
const r = removeDuplicates([1, 2, 2, 3, 4, 4, 5]);
if (JSON.stringify(r) !== JSON.stringify([1, 2, 3, 4, 5]))
  throw new Error("expected [1,2,3,4,5], got " + JSON.stringify(r));
const r2 = removeDuplicates(["a", "a", "b"]);
if (r2.length !== 2) throw new Error("should dedupe strings too");
""")


# ---------- hard ----------

def check_hard_p01(path):
    c = strip_comments(read_file(path))
    ok, msg = require_all(c, [
        (r"function\s+analyzeGrades|analyzeGrades\s*=",
         "Missing 'analyzeGrades' function"),
        (r"\.map\s*\(", "Missing .map() for avg/grade"),
        (r"\.reduce\s*\(", "Missing .reduce() for the average"),
        (r"\.filter\s*\(", "Missing .filter() for passing"),
        (r"\.sort\s*\(", "Missing .sort() by avg"),
        (r"\.slice\s*\(\s*0\s*,\s*3", "Missing .slice(0, 3) for top 3"),
    ])
    if not ok:
        return ok, msg
    return js_ok(path, """
const r = analyzeGrades([
  { name: "Alice", scores: [90, 85, 92] },
  { name: "Bob", scores: [55, 60, 58] },
  { name: "Charlie", scores: [95, 88, 91] },
  { name: "Diana", scores: [70, 75, 72] },
]);
if (r.length !== 3) throw new Error("should return top 3 passing students");
if (r[0].name !== "Charlie") throw new Error("Charlie (avg ~91.3) should be first");
if (r.some(s => s.name === "Bob")) throw new Error("Bob (avg <60) should be filtered out");
if (typeof r[0].avg !== "number" || !r[0].grade)
  throw new Error("each result needs avg and grade");
""")


def check_hard_p02(path):
    c = strip_comments(read_file(path))
    ok, msg = require_all(c, [
        (r"function\s+flattenAndUnique|flattenAndUnique\s*=",
         "Missing 'flattenAndUnique' function"),
        (r"\.flat\s*\(", "Use .flat(Infinity) to flatten"),
        (r"new\s+Set", "Use new Set to dedupe"),
        (r"\.sort\s*\(", "Sort numerically"),
    ])
    if not ok:
        return ok, msg
    return js_ok(path, """
const r = flattenAndUnique([[1, 2], [3, [4, 2]], [1, 5]]);
if (JSON.stringify(r) !== JSON.stringify([1, 2, 3, 4, 5]))
  throw new Error("expected [1,2,3,4,5], got " + JSON.stringify(r));
const r2 = flattenAndUnique([[[[9, 1]], [2]], 3, [1]]);
if (JSON.stringify(r2) !== JSON.stringify([1, 2, 3, 9]))
  throw new Error("deep nesting failed: " + JSON.stringify(r2));
""")


def check_hard_p03(path):
    c = strip_comments(read_file(path))
    ok, msg = require_all(c, [
        (r"function\s+createPagination|createPagination\s*=",
         "Missing 'createPagination' function"),
        (r"\.slice\s*\(", "Use .slice() for the page's items"),
        (r"Math\.ceil", "totalPages needs Math.ceil"),
        (r"hasNext", "Return hasNext"),
        (r"hasPrev", "Return hasPrev"),
        (r"totalPages", "Return totalPages"),
        (r"currentPage", "Return currentPage"),
    ])
    if not ok:
        return ok, msg
    return js_ok(path, """
const data = Array.from({ length: 25 }, (_, i) => i + 1);
const r = createPagination(data, 2, 10);
if (r.items[0] !== 11 || r.items.length !== 10)
  throw new Error("page 2 should be items 11-20");
if (r.currentPage !== 2 || r.totalPages !== 3)
  throw new Error("currentPage/totalPages wrong");
if (r.hasNext !== true || r.hasPrev !== true)
  throw new Error("hasNext/hasPrev wrong on middle page");
const last = createPagination(data, 3, 10);
if (last.hasNext !== false) throw new Error("last page hasNext should be false");
const first = createPagination(data, 1, 10);
if (first.hasPrev !== false) throw new Error("first page hasPrev should be false");
""")


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
        print("  LESSON 18 — JAVASCRIPT ARRAYS & METHODS: AUTO-CHECK ALL")
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
