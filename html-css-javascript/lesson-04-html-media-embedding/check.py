#!/usr/bin/env python3
"""Structural checker for Lesson 04 — HTML Media & Embedding.

Usage:
    python3 check.py easy/p01     # check one problem
    python3 check.py medium/p02   # check one problem
    python3 check.py all          # check every problem

Each check reads your HTML file and verifies the required media elements
and attributes exist (img alt text, audio/video sources, iframes, etc.).
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
        (r"<img\b", "<img> elements"),
        (r"src=", "src attribute on the images"),
        (r"alt=", "alt text on the images"),
        (r"width=", "width attribute on the images"),
    ])
    if not ok:
        return ok, msg
    text = _code(path)
    if _count(text, r"<img\b") < 3:
        return False, "need at least 3 <img> elements"
    if _count(text, r"alt=") < 3:
        return False, "every image needs alt text"
    return True, "ok"


def easy_p02(path):
    return _require(path, [
        (r"<audio\b", "<audio> element"),
        (r"controls", "controls attribute on the audio"),
        (r"<source\b", "<source> inside the audio"),
        (r'type="audio/', 'type="audio/..." on the source'),
        (r"does not support", "fallback text inside <audio>"),
    ])


def easy_p03(path):
    return _require(path, [
        (r"<video\b", "<video> element"),
        (r"controls", "controls attribute on the video"),
        (r"width=", "width attribute on the video"),
        (r"<source\b", "<source> inside the video"),
        (r'type="video/', 'type="video/..." on the source'),
        (r"does not support", "fallback text inside <video>"),
    ])


# ---------------- MEDIUM ----------------

def medium_p01(path):
    ok, msg = _require(path, [
        (r"<picture\b", "<picture> element"),
        (r"<img\b", "a fallback <img> inside <picture>"),
        (r"alt=", "alt text on the fallback image"),
    ])
    if not ok:
        return ok, msg
    text = _code(path)
    if _count(text, r"<source\b") < 2:
        return False, "need at least 2 <source> elements with media conditions"
    if _count(text, r"media=") < 2:
        return False, "each <source> needs a media= condition"
    if not re.search(r"srcset=", text, re.I):
        return False, "sources need srcset= attributes"
    return True, "ok"


def medium_p02(path):
    return _require(path, [
        (r"<iframe\b", "<iframe> element"),
        (r"youtube\.com/embed", "a YouTube embed URL in src"),
        (r"title=", "title attribute on the iframe (accessibility)"),
        (r"width=", "width attribute"),
        (r"height=", "height attribute"),
        (r"allowfullscreen", "allowfullscreen attribute"),
    ])


def medium_p03(path):
    ok, msg = _require(path, [
        (r"<audio\b", "<audio> elements"),
        (r"controls", "controls attribute on the players"),
        (r"<source\b", "<source> elements"),
        (r"<ul\b|<ol\b", "a list wrapping the playlist"),
        (r"<li\b", "<li> items for each track"),
    ])
    if not ok:
        return ok, msg
    text = _code(path)
    if _count(text, r"<audio\b") < 2:
        return False, "need at least 2 <audio> players in the playlist"
    return True, "ok"


# ---------------- HARD ----------------

def hard_p01(path):
    ok, msg = _require(path, [
        (r"<figure\b", "<figure> wrappers"),
        (r"<video\b", "<video> elements"),
        (r"controls", "controls attribute on the videos"),
        (r"<source\b", "<source> elements"),
        (r"<figcaption\b", "<figcaption> under each video"),
        (r"<track\b", "a <track> for subtitles/captions"),
        (r'kind="subtitles"|kind="captions"', 'kind="subtitles" on the track'),
    ])
    if not ok:
        return ok, msg
    text = _code(path)
    if _count(text, r"<figure\b") < 2:
        return False, "need at least 2 <figure> video entries"
    if _count(text, r"<figcaption\b") < 2:
        return False, "every <figure> needs a <figcaption>"
    return True, "ok"


def hard_p02(path):
    return _require(path, [
        (r"<iframe\b", "<iframe> element"),
        (r"google\.com/maps|maps\.google", "a Google Maps embed URL in src"),
        (r'loading="lazy"', 'loading="lazy" on the iframe'),
        (r"allowfullscreen", "allowfullscreen attribute"),
        (r"width=", "width attribute"),
        (r"height=", "height attribute"),
    ])


def hard_p03(path):
    ok, msg = _require(path, [
        (r"<style\b", "a <style> block"),
        (r"<header\b", "a <header> section"),
        (r"<video\b", "a hero <video>"),
        (r"autoplay", "autoplay on the hero video"),
        (r"muted", "muted (required for autoplay)"),
        (r"loop", "loop on the hero video"),
        (r"<footer\b", "a <footer> section"),
        (r"object-fit", "object-fit CSS for the media"),
    ])
    if not ok:
        return ok, msg
    text = _code(path)
    if _count(text, r"<img\b") < 3:
        return False, "need at least 3 gallery <img> elements"
    if _count(text, r"alt=") < 3:
        return False, "every gallery image needs alt text"
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
