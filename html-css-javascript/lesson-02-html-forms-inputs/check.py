#!/usr/bin/env python3
"""Structural checker for Lesson 02 — HTML Forms & Inputs.

Usage:
    python3 check.py easy/p01     # check one problem
    python3 check.py medium/p02   # check one problem
    python3 check.py all          # check every problem

Each check reads your HTML file and verifies the required elements and
attributes exist (tags, input types, labels, validation attributes).
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
    return _require(path, [
        (r"<form\b", "<form> element"),
        (r'<label[^>]*for="email"', '<label for="email">'),
        (r'type="email"', 'input type="email"'),
        (r'name="email"', 'name="email" on the email input'),
        (r'<label[^>]*for="password"', '<label for="password">'),
        (r'type="password"', 'input type="password"'),
        (r'name="password"', 'name="password" on the password input'),
        (r"required", "required attribute"),
        (r'type="submit"', "a submit button"),
    ])


def easy_p02(path):
    return _require(path, [
        (r"<form\b", "<form> element"),
        (r'<label[^>]*for="name"', '<label for="name">'),
        (r'type="text"', 'input type="text" for the name'),
        (r'<label[^>]*for="email"', '<label for="email">'),
        (r'type="email"', 'input type="email"'),
        (r"<textarea\b", "<textarea> for the message"),
        (r'name="message"', 'name="message" on the textarea'),
        (r'type="submit"', "a submit button"),
    ])


def easy_p03(path):
    return _require(path, [
        (r"<form\b", "<form> element"),
        (r'type="text"', 'input type="text" for the name'),
        (r'type="email"', 'input type="email"'),
        (r'type="password"', 'input type="password"'),
        (r'type="checkbox"', 'a checkbox for the terms agreement'),
        (r"name=", "name attributes on the inputs"),
        (r"required", "required attribute"),
        (r'type="submit"', "a submit button"),
    ])


# ---------------- MEDIUM ----------------

def medium_p01(path):
    ok, msg = _require(path, [
        (r"<form\b", "<form> element"),
        (r"<fieldset\b", "<fieldset> grouping"),
        (r"<legend\b", "<legend> title"),
        (r"<select\b", "<select> dropdown"),
        (r"<option\b", "<option> items in the dropdown"),
        (r'type="submit"', "a submit button"),
    ])
    if not ok:
        return ok, msg
    text = _code(path)
    if _count(text, r'type="radio"') < 3:
        return False, "need at least 3 radio buttons sharing one name"
    if _count(text, r'type="checkbox"') < 3:
        return False, "need at least 3 checkboxes"
    return True, "ok"


def medium_p02(path):
    ok, msg = _require(path, [
        (r"<form\b", "<form> element"),
        (r'type="number"', 'input type="number" for quantity'),
        (r'min="1"', 'min="1" on the quantity input'),
        (r'max="100"', 'max="100" on the quantity input'),
        (r"<select\b", "<select> for size"),
        (r"<option\b", "<option> items for size"),
        (r'type="submit"', "a submit button"),
    ])
    if not ok:
        return ok, msg
    text = _code(path)
    if _count(text, r'type="checkbox"') < 2:
        return False, "need at least 2 checkboxes for extras"
    return True, "ok"


def medium_p03(path):
    return _require(path, [
        (r"<form\b", "<form> element"),
        (r'type="email"', 'input type="email"'),
        (r"pattern=", "a pattern attribute for validation"),
        (r'type="password"', 'input type="password"'),
        (r'minlength="8"', 'minlength="8" on the password'),
        (r'type="number"', 'input type="number" for age'),
        (r'min="18"', 'min="18" on the age input'),
        (r'max="120"', 'max="120" on the age input'),
        (r"required", "required attributes"),
        (r'type="submit"', "a submit button"),
    ])


# ---------------- HARD ----------------

def hard_p01(path):
    ok, msg = _require(path, [
        (r"<form\b", "<form> element"),
        (r"<legend[^>]*>\s*Shipping", 'a "Shipping Address" fieldset/legend'),
        (r"<legend[^>]*>\s*Payment", 'a "Payment" fieldset/legend'),
        (r'type="month"', 'input type="month" for card expiry'),
        (r"pattern=", "pattern attributes (zip, card, cvv)"),
        (r"required", "required attributes"),
        (r'type="submit"', "a submit button"),
    ])
    if not ok:
        return ok, msg
    text = _code(path)
    if _count(text, r"<fieldset\b") < 2:
        return False, "need 2 <fieldset> groups (shipping + payment)"
    if _count(text, r"pattern=") < 3:
        return False, "need at least 3 pattern attributes (zip, card, cvv)"
    if _count(text, r"<label\b") < 6:
        return False, "need labels for every field"
    return True, "ok"


def hard_p02(path):
    ok, msg = _require(path, [
        (r"<form\b", "<form> element"),
        (r'type="file"', 'input type="file" for the resume'),
        (r"accept=", "accept attribute limiting file types"),
        (r'type="date"', 'input type="date" for availability'),
        (r"<textarea\b", "<textarea> for the cover letter"),
        (r"<select\b", "<select> for the position"),
        (r'type="submit"', "a submit button"),
    ])
    if not ok:
        return ok, msg
    text = _code(path)
    if _count(text, r'type="radio"') < 2:
        return False, "need at least 2 radio buttons for availability"
    return True, "ok"


def hard_p03(path):
    ok, msg = _require(path, [
        (r"<form\b", "<form> element"),
        (r"<legend\b", "<legend> titles for each group"),
        (r"<select\b", "<select> dropdowns"),
        (r'type="reset"', "a reset button"),
        (r'type="submit"', "a submit button"),
        (r"checked", "checked attribute for defaults"),
    ])
    if not ok:
        return ok, msg
    text = _code(path)
    if _count(text, r"<fieldset\b") < 3:
        return False, "need 3 <fieldset> groups (notifications, privacy, preferences)"
    if _count(text, r'type="checkbox"') < 3:
        return False, "need at least 3 checkboxes"
    if _count(text, r'type="radio"') < 2:
        return False, "need at least 2 radio buttons"
    if _count(text, r"<select\b") < 2:
        return False, "need at least 2 <select> dropdowns"
    return True, "ok"


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
