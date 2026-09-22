#!/usr/bin/env python3
"""Structural checker for Lesson 03 — HTML Tables & Data.

Usage:
    python3 check.py easy/p01     # check one problem
    python3 check.py medium/p02   # check one problem
    python3 check.py all          # check every problem

Each check reads your HTML file and verifies the required table elements
and attributes exist (table sections, scope, colspan/rowspan, styling).
"""
import glob
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def _code(path):
    """Return file text with comments stripped (so hints can't fake a pass)."""
    with open(path, encoding="utf-8") as f:
        text = f.read()
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    text = re.sub(r"/\*.*?\*/", "", text, flags=re.S)
    text = re.sub(r"(?<!:)//[^\n]*", "", text)
    return text


def _require(path, reqs):
    """reqs: list of (regex, description). Returns (passed, msg)."""
    try:
        text = _code(path)
    except OSError as e:
        return False, f"cannot read file: {e}"
    missing = [desc for pat, desc in reqs if not re.search(pat, text, re.I | re.S)]
    if missing:
        return False, "missing: " + ", ".join(missing)
    return True, "ok"


def _count(text, pat):
    return len(re.findall(pat, text, re.I))


# ---------------- EASY ----------------

def easy_p01(path):
    ok, msg = _require(path, [
        (r"<table\b", "<table> element"),
        (r"<th\b", "<th> header cells (Name, Age, City)"),
        (r"<td\b", "<td> data cells"),
    ])
    if not ok:
        return ok, msg
    text = _code(path)
    if _count(text, r"<th\b") < 3:
        return False, "need 3 header cells (Name, Age, City)"
    if _count(text, r"<tr\b") < 4:
        return False, "need 4 rows total (1 header + 3 data rows)"
    return True, "ok"


def easy_p02(path):
    return _require(path, [
        (r"<table\b", "<table> element"),
        (r"<caption[^>]*>\s*Student Grades", '<caption> titled "Student Grades"'),
        (r"<thead\b", "<thead> section"),
        (r"<tbody\b", "<tbody> section"),
        (r"<th\b", "<th> header cells"),
        (r"<td\b", "<td> data cells"),
    ])


def easy_p03(path):
    return _require(path, [
        (r"<table\b", "<table> element"),
        (r"<th\b", "<th> header cells"),
        (r"<td\b", "<td> data cells"),
        (r"<style\b|style=|border=", "CSS styling (a <style> block, style=, or border attribute)"),
        (r"border|padding", "border/padding CSS for the cells"),
    ])


# ---------------- MEDIUM ----------------

def medium_p01(path):
    return _require(path, [
        (r"<table\b", "<table> element"),
        (r"<thead\b", "<thead> section"),
        (r"<tbody\b", "<tbody> section"),
        (r"<tfoot\b", "<tfoot> totals row"),
        (r'scope="col"', 'scope="col" on column headers'),
        (r'scope="row"', 'scope="row" on row headers'),
        (r"<td\b", "<td> data cells"),
    ])


def medium_p02(path):
    ok, msg = _require(path, [
        (r"<table\b", "<table> element"),
        (r"<caption\b", "<caption> element"),
        (r"<colgroup\b", "<colgroup> element"),
        (r"width", "column widths (e.g. style=\"width: 50%\")"),
    ])
    if not ok:
        return ok, msg
    text = _code(path)
    if _count(text, r"<col\b") < 3:
        return False, "need 3 <col> elements inside <colgroup>"
    return True, "ok"


def medium_p03(path):
    return _require(path, [
        (r"<table\b", "<table> element"),
        (r"colspan=", "a colspan attribute (merged header)"),
        (r"rowspan=", "a rowspan attribute (cell spanning 2 rows)"),
        (r"<th\b", "<th> header cells"),
        (r"<td\b", "<td> data cells"),
    ])


# ---------------- HARD ----------------

def hard_p01(path):
    return _require(path, [
        (r"<table\b", "<table> element"),
        (r"<caption\b", "<caption> element"),
        (r"<colgroup\b", "<colgroup> element"),
        (r"<thead\b", "<thead> section"),
        (r"<tbody\b", "<tbody> section"),
        (r"<tfoot\b", "<tfoot> totals row"),
        (r'scope="col"', 'scope="col" on column headers'),
        (r'scope="row"', 'scope="row" on row headers'),
        (r"<style\b", "a <style> block"),
        (r"nth-child", "zebra striping (e.g. tr:nth-child(odd))"),
    ])


def hard_p02(path):
    return _require(path, [
        (r"<table\b", "<table> element"),
        (r"colspan=", "a colspan merged header"),
        (r"rowspan=", "a rowspan merged header"),
        (r'scope="col"', 'scope="col" on column headers'),
        (r'scope="row"', 'scope="row" on row headers'),
        (r"<style\b|style=|border=", "border styling for the cells"),
    ])


def hard_p03(path):
    return _require(path, [
        (r"<div[^>]*class=", "a wrapper <div> around the table"),
        (r"overflow-x", "overflow-x: auto on the wrapper (scrollable)"),
        (r"<table\b", "<table> element"),
        (r"<caption\b", "<caption> element"),
        (r"<thead\b", "<thead> section"),
        (r"<tbody\b", "<tbody> section"),
        (r"scope=", "scope attributes on headers"),
        (r"<style\b", "a <style> block"),
        (r"@media", "an @media query for small screens"),
    ])


CHECKS = {
    "easy/p01": easy_p01, "easy/p02": easy_p02, "easy/p03": easy_p03,
    "medium/p01": medium_p01, "medium/p02": medium_p02, "medium/p03": medium_p03,
    "hard/p01": hard_p01, "hard/p02": hard_p02, "hard/p03": hard_p03,
}

DONE_MARKERS = {".html": "<!-- DONE -->", ".css": "/* DONE */", ".js": "// DONE"}


def _find_file(cid):
    d, n = cid.split("/")
    cands = [p for p in glob.glob(os.path.join(HERE, d, f"{n}-*"))
             if os.path.isfile(p) and "solutions" not in p.split(os.sep)]
    return sorted(cands)[0] if cands else None


def run_one(cid):
    if cid not in CHECKS:
        print(f"ERROR — unknown problem id '{cid}'. Expected e.g. easy/p01")
        return False
    path = _find_file(cid)
    if not path:
        print(f"ERROR — no file matching {cid}-* (looked in {cid.split('/')[0]}/, excluding solutions/)")
        return False
    try:
        passed, msg = CHECKS[cid](path)
    except Exception as e:
        if "NoneType" in str(e):
            print(f"FAIL — a function returned None — write the body!")
        else:
            print(f"ERROR — {e}")
            return False
    if passed:
        ext = os.path.splitext(path)[1]
        print("PASS — All tests passed!")
        print(f"Add '{DONE_MARKERS.get(ext, 'DONE')}' at the top of "
              f"{os.path.relpath(path, HERE)} to mark it done.")
    else:
        print(f"FAIL — {msg}")
    return passed


def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        sys.exit(2)
    if args[0] == "all":
        results = {cid: run_one(cid) for cid in CHECKS}
        n = sum(results.values())
        print(f"\n{n}/{len(results)} problems passed")
        sys.exit(0 if n == len(results) else 1)
    ok = all(run_one(a) for a in args)
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
