"""
Auto-Check — Lesson 16: JavaScript Variables & Types
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
        (r"\bconst\b", "Declare at least one variable with const"),
        (r"\blet\b", "Declare the mutable one with let"),
        (r"\$\{", "Use a template literal (${...} inside backticks)"),
        (r"\[", "hobbies should be an array"),
        (r"console\.log", "Print the greeting with console.log"),
    ])
    if not ok:
        return ok, msg
    try:
        r = run_js(path)
    except Exception as e:
        return False, f"could not run node: {e}"
    if r.returncode != 0:
        return False, "file should run under node without errors"
    if not r.stdout.strip():
        return False, "file should console.log a greeting"
    return True, "All tests passed!"


def check_easy_p02(path):
    c = strip_comments(read_file(path))
    ok, msg = require_all(c, [
        (r"function\s+transform|transform\s*=\s*\(?\w*\)?\s*=>|transform\s*=\s*function",
         "Missing a 'transform' function"),
        (r"toUpperCase", "Use toUpperCase()"),
        (r"reverse", "Use reverse()"),
    ])
    if not ok:
        return ok, msg
    return js_ok(path, """
if (transform("hello") !== "OLLEH (length: 5)")
  throw new Error('transform("hello") should be "OLLEH (length: 5)"');
if (transform("abc") !== "CBA (length: 3)")
  throw new Error('transform("abc") should be "CBA (length: 3)"');
""")


def check_easy_p03(path):
    c = strip_comments(read_file(path))
    ok, msg = require_all(c, [
        (r"function\s+isTruthy|isTruthy\s*=",
         "Missing an 'isTruthy' function"),
    ])
    if not ok:
        return ok, msg
    return js_ok(path, """
const falsy = [0, "", null, undefined, NaN, false];
const truthy = [[], {}, "0", "false", 1];
for (const v of falsy)
  if (isTruthy(v) !== false) throw new Error("isTruthy falsy case failed: " + String(v));
for (const v of truthy)
  if (isTruthy(v) !== true) throw new Error("isTruthy truthy case failed: " + String(v));
""")


# ---------- medium ----------

def check_medium_p01(path):
    c = strip_comments(read_file(path))
    ok, msg = require_all(c, [
        (r"function\s+formatPrice|formatPrice\s*=",
         "Missing a 'formatPrice' function"),
        (r"toFixed", "Use toFixed(2) for the decimals"),
        (r"\$\{|`", "Use a template literal for the output"),
    ])
    if not ok:
        return ok, msg
    return js_ok(path, """
if (formatPrice(1234.5, "USD") !== "$1,234.50")
  throw new Error('formatPrice(1234.5,"USD") should be "$1,234.50", got ' + formatPrice(1234.5,"USD"));
if (formatPrice(99.999, "EUR") !== "€100.00")
  throw new Error('formatPrice(99.999,"EUR") should be "€100.00", got ' + formatPrice(99.999,"EUR"));
""")


def check_medium_p02(path):
    c = strip_comments(read_file(path))
    ok, msg = require_all(c, [
        (r"function\s+coerceDemo|coerceDemo\s*=",
         "Missing a 'coerceDemo' function"),
        (r"addition", "Result object needs an 'addition' key"),
        (r"strictEquality|===", "Include the === comparison"),
        (r"==", "Include the loose == comparison"),
    ])
    if not ok:
        return ok, msg
    return js_ok(path, """
const r = coerceDemo("5", 5);
if (r.addition !== "55") throw new Error('addition should be "55" (string concat)');
if (r.subtraction !== 0) throw new Error("subtraction should be 0");
if (r.equality !== true) throw new Error("equality (==) should be true");
if (r.strictEquality !== false) throw new Error("strictEquality (===) should be false");
""")


def check_medium_p03(path):
    c = strip_comments(read_file(path))
    ok, msg = require_all(c, [
        (r"function\s+parseNumber|parseNumber\s*=",
         "Missing a 'parseNumber' function"),
    ])
    if not ok:
        return ok, msg
    return js_ok(path, """
if (parseNumber("42") !== 42) throw new Error('"42" -> 42');
if (parseNumber("3.14") !== 3.14) throw new Error('"3.14" -> 3.14');
if (!Number.isNaN(parseNumber("abc"))) throw new Error('"abc" -> NaN');
if (parseNumber("") !== 0) throw new Error('"" -> 0');
if (parseNumber("42px") !== 42) throw new Error('"42px" -> 42');
""")


# ---------- hard ----------

def check_hard_p01(path):
    c = strip_comments(read_file(path))
    ok, msg = require_all(c, [
        (r"function\s+deepTypeCheck|deepTypeCheck\s*=",
         "Missing a 'deepTypeCheck' function"),
        (r"Array\.isArray", "Use Array.isArray to detect arrays"),
        (r"===\s*null|null\s*===", "Check === null before typeof"),
        (r"typeof", "Fall back to typeof for the rest"),
    ])
    if not ok:
        return ok, msg
    return js_ok(path, """
const cases = [[null,"null"],[[ ],"array"],[{},"object"],["hi","string"],
               [42,"number"],[undefined,"undefined"],[()=>{},"function"],
               [true,"boolean"]];
for (const [v, t] of cases)
  if (deepTypeCheck(v) !== t)
    throw new Error("deepTypeCheck(" + String(v) + ') should be "' + t + '", got "' + deepTypeCheck(v) + '"');
""")


def check_hard_p02(path):
    c = strip_comments(read_file(path))
    ok, msg = require_all(c, [
        (r"function\s+safeMath|safeMath\s*=",
         "Missing a 'safeMath' function"),
        (r"typeof", "Validate inputs with typeof"),
    ])
    if not ok:
        return ok, msg
    return js_ok(path, """
if (safeMath("divide", 10, 0) !== "Cannot divide by zero")
  throw new Error("divide by 0 should return 'Cannot divide by zero'");
if (safeMath("add", "5", 3) !== "Invalid input")
  throw new Error("non-number input should return 'Invalid input'");
if (safeMath("add", 5, 3) !== 8) throw new Error("5+3 should be 8");
if (safeMath("multiply", 4, 5) !== 20) throw new Error("4*5 should be 20");
if (safeMath("bogus", 1, 2) !== "Unknown operation")
  throw new Error("unknown op should return 'Unknown operation'");
""")


def check_hard_p03(path):
    c = strip_comments(read_file(path))
    ok, msg = require_all(c, [
        (r"function\s+analyzeString|analyzeString\s*=",
         "Missing an 'analyzeString' function"),
        (r"split", "Use split() for words/reversal"),
        (r"reverse", "Use reverse() for the reversed string"),
        (r"isPalindrome", "Result needs an isPalindrome key"),
    ])
    if not ok:
        return ok, msg
    return js_ok(path, """
const r = analyzeString("race car");
if (r.original !== "race car") throw new Error("original wrong");
if (r.wordCount !== 2) throw new Error("wordCount should be 2");
if (r.isPalindrome !== true) throw new Error('"race car" is a palindrome');
if (!Array.isArray(r.wordList) || r.wordList.length !== 2)
  throw new Error("wordList should be the 2 words");
const r2 = analyzeString("hello world");
if (r2.isPalindrome !== false) throw new Error('"hello world" is not a palindrome');
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
        print("  LESSON 16 — JAVASCRIPT VARIABLES & TYPES: AUTO-CHECK ALL")
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
