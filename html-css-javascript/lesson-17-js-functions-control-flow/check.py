"""
Auto-Check — Lesson 17: JavaScript Functions & Control Flow
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
        (r"multiply\s*=\s*\([^)]*\)\s*=>|multiply\s*=\s*\w+\s*=>",
         "Missing arrow function 'multiply'"),
        (r"b\s*=\s*1", "b needs a default value of 1"),
        (r"console\.log", "Log the two test calls"),
    ])
    if not ok:
        return ok, msg
    return js_ok(path, """
if (multiply(5, 3) !== 15) throw new Error("multiply(5,3) should be 15");
if (multiply(5) !== 5) throw new Error("multiply(5) should be 5 (b defaults to 1)");
""")


def check_easy_p02(path):
    c = strip_comments(read_file(path))
    ok, msg = require_all(c, [
        (r"function\s+formatName|formatName\s*=",
         "Missing a 'formatName' function"),
        (r"\{\s*first\s*,\s*last\s*\}",
         "Destructure { first, last } in the parameters"),
        (r"toUpperCase", "Uppercase the last name"),
    ])
    if not ok:
        return ok, msg
    return js_ok(path, """
if (formatName({ first: "Akash", last: "dev" }) !== "Akash DEV")
  throw new Error('formatName({first:"Akash",last:"dev"}) should be "Akash DEV"');
""")


def check_easy_p03(path):
    c = strip_comments(read_file(path))
    ok, msg = require_all(c, [
        (r"function\s+classifyNumber|classifyNumber\s*=",
         "Missing 'classifyNumber' (if/else version)"),
        (r"\?", "Missing the ternary version"),
        (r"classifyNumberTernary|ternary",
         "Missing a ternary version (e.g. classifyNumberTernary)"),
        (r"if\s*\(", "The first version should use if/else"),
    ])
    if not ok:
        return ok, msg
    return js_ok(path, """
if (classifyNumber(5) !== "positive") throw new Error("5 -> positive");
if (classifyNumber(-3) !== "negative") throw new Error("-3 -> negative");
if (classifyNumber(0) !== "zero") throw new Error("0 -> zero");
if (typeof classifyNumberTernary === "function") {
  if (classifyNumberTernary(-3) !== "negative")
    throw new Error("ternary version gave wrong answer");
}
""")


# ---------- medium ----------

def check_medium_p01(path):
    c = strip_comments(read_file(path))
    ok, msg = require_all(c, [
        (r"function\s+sumAll\s*\(\s*\.\.\.|\.\.\.\s*nums",
         "Missing rest parameter (...nums)"),
        (r"reduce", "Sum with nums.reduce(...)"),
    ])
    if not ok:
        return ok, msg
    return js_ok(path, """
if (sumAll(1, 2, 3, 4, 5) !== 15) throw new Error("sumAll(1..5) should be 15");
if (sumAll() !== 0) throw new Error("sumAll() should be 0");
if (sumAll(10) !== 10) throw new Error("sumAll(10) should be 10");
""")


def check_medium_p02(path):
    c = strip_comments(read_file(path))
    ok, msg = require_all(c, [
        (r"function\s+mergeObjects|mergeObjects\s*=",
         "Missing a 'mergeObjects' function"),
        (r"\.\.\.\s*obj1|\{\s*\.\.\.", "Use spread to merge the objects"),
    ])
    if not ok:
        return ok, msg
    return js_ok(path, """
const r = mergeObjects({ a: 1, b: 2 }, { b: 3, c: 4 });
if (r.a !== 1 || r.b !== 3 || r.c !== 4)
  throw new Error("merged object should be {a:1,b:3,c:4} (obj2 wins)");
""")


def check_medium_p03(path):
    c = strip_comments(read_file(path))
    ok, msg = require_all(c, [
        (r"function\s+getDayType|getDayType\s*=",
         "Missing a 'getDayType' function"),
        (r"switch", "Use a switch statement"),
        (r"default", "Need a default case for Invalid"),
        (r"case", "Need case labels"),
    ])
    if not ok:
        return ok, msg
    return js_ok(path, """
if (getDayType("Saturday") !== "Weekend") throw new Error("Sat -> Weekend");
if (getDayType("Sunday") !== "Weekend") throw new Error("Sun -> Weekend");
if (getDayType("Monday") !== "Weekday") throw new Error("Mon -> Weekday");
if (getDayType("Funday") !== "Invalid") throw new Error("bad day -> Invalid");
""")


# ---------- hard ----------

def check_hard_p01(path):
    c = strip_comments(read_file(path))
    ok, msg = require_all(c, [
        (r"function\s+calculateGrade|calculateGrade\s*=",
         "Missing a 'calculateGrade' function"),
        (r"sort|Math\.min", "Drop the lowest via sort/Math.min"),
        (r"reduce", "Average with reduce()"),
        (r"\?", "Use a ternary chain for the letter grade"),
    ])
    if not ok:
        return ok, msg
    return js_ok(path, """
if (calculateGrade([85, 90, 78, 92]) !== "B")
  throw new Error("[85,90,78,92] drops 78, avg 89 -> B");
if (calculateGrade([95, 96, 90, 99]) !== "A")
  throw new Error("should be A");
if (calculateGrade([50, 45, 40, 60]) !== "F")
  throw new Error("should be F");
""")


def check_hard_p02(path):
    c = strip_comments(read_file(path))
    ok, msg = require_all(c, [
        (r"function\s+analyzeData|analyzeData\s*=",
         "Missing an 'analyzeData' function"),
        (r"for\s*\(", "Use a for...of loop"),
        (r"\{\s*name\s*,\s*age\s*,\s*city\s*\}|\{\s*\w+\s*\}",
         "Destructure {name, age, city} in the loop"),
        (r"averageAge", "Return averageAge"),
        (r"usersPerCity", "Return usersPerCity"),
        (r"oldestUser", "Return oldestUser"),
    ])
    if not ok:
        return ok, msg
    return js_ok(path, """
const r = analyzeData([
  { name: "Alice", age: 30, city: "Mumbai" },
  { name: "Bob", age: 25, city: "Delhi" },
  { name: "Charlie", age: 35, city: "Mumbai" },
]);
if (r.averageAge !== 30) throw new Error("averageAge should be 30");
if (r.usersPerCity.Mumbai !== 2 || r.usersPerCity.Delhi !== 1)
  throw new Error("usersPerCity wrong");
if (r.oldestUser.name !== "Charlie") throw new Error("oldest should be Charlie");
""")


def check_hard_p03(path):
    c = strip_comments(read_file(path))
    ok, msg = require_all(c, [
        (r"function\s+createCounter|createCounter\s*=",
         "Missing a 'createCounter' function"),
        (r"increment", "Return an increment method"),
        (r"decrement", "Return a decrement method"),
        (r"reset", "Return a reset method"),
        (r"getValue", "Return a getValue method"),
        (r"start\s*=\s*0|start\s*=\s*0\s*\)", "start should default to 0"),
    ])
    if not ok:
        return ok, msg
    return js_ok(path, """
const a = createCounter(10);
const b = createCounter();
if (a.increment() !== 11) throw new Error("increment should return 11");
if (a.increment() !== 12) throw new Error("increment should return 12");
if (a.getValue() !== 12) throw new Error("getValue should be 12");
if (a.decrement() !== 11) throw new Error("decrement should return 11");
if (a.reset() !== 10) throw new Error("reset should return 10");
if (b.increment() !== 1) throw new Error("second counter is not independent");
if (b.getValue() !== 1) throw new Error("b should be unaffected by a");
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
        print("  LESSON 17 — JAVASCRIPT FUNCTIONS & CONTROL FLOW: AUTO-CHECK ALL")
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
