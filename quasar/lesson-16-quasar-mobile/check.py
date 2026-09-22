"""
Auto-Check System — Lesson 16: Quasar Mobile (Capacitor)
========================================================
.vue files can't execute without a Quasar build step; .js files get a
parse-only syntax check via `node --check` when available. Everything is
then verified STRUCTURALLY.

Usage:
    python3 check.py easy/p01     # check one problem
    python3 check.py all          # check all problems
"""

import glob
import os
import re
import shutil
import subprocess
import sys

LESSON_DIR = os.path.dirname(os.path.abspath(__file__))

NODE = "/home/akash-dev/.nvm/versions/node/v22.23.2/bin/node"
if not os.path.isfile(NODE):
    NODE = shutil.which("node")


def read_body(path):
    """Read a solution file, stripping the leading docstring comment so
    hint text in the problem description isn't mistaken for real code."""
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    content = re.sub(r"^\s*<!--.*?-->", "", content, count=1, flags=re.DOTALL)
    content = re.sub(r"^\s*/\*.*?\*/", "", content, count=1, flags=re.DOTALL)
    return content


def js_syntax_ok(path):
    """Parse-only syntax check via `node --check` (does NOT execute, so
    unresolved imports are fine). Skipped if node is missing."""
    if not NODE:
        return True, "node not found — skipped syntax check"
    try:
        result = subprocess.run(
            [NODE, "--check", path],
            capture_output=True, text=True, timeout=15,
        )
    except Exception as e:
        if "NoneType" in str(e):
            print(f"FAIL — a function returned None — write the body!")
        else:
            return True, f"syntax check skipped ({e})"
    if result.returncode != 0:
        detail = (result.stderr or result.stdout).strip().splitlines()
        return False, "syntax error: " + (detail[0] if detail else "unknown")
    return True, "ok"


def require_all(path, checks, syntax=True):
    """checks: list of (label, regex). Returns (passed, message)."""
    if not os.path.isfile(path):
        return False, f"file not found: {path}"
    if syntax and path.endswith((".js", ".mjs", ".ts")):
        ok, msg = js_syntax_ok(path)
        if not ok:
            return False, msg
    body = read_body(path)
    if len(body.strip()) < 30:
        return False, "file looks empty — write your solution first"
    for label, pattern in checks:
        if not re.search(pattern, body):
            return False, f"missing {label} (expected pattern: {pattern})"
    return True, "All tests passed!"


def check_easy_p01(path):
    """capacitor.config: appId, appName, webDir, Camera+Geolocation plugins."""
    return require_all(path, [
        ("appId", r"appId"),
        ("appName", r"appName"),
        ("webDir", r"webDir"),
        ("plugins section", r"plugins"),
        ("Camera plugin config", r"[Cc]amera"),
        ("Geolocation plugin config", r"[Gg]eolocation"),
        ("permissions documented", r"permission|Permission|Usage|uses-permission|Info\.plist|Manifest"),
        ("export", r"export|module\.exports"),
    ])


def check_easy_p02(path):
    """Adaptive layout: drawer on desktop, bottom tabs on mobile, 3 items."""
    return require_all(path, [
        ("<template> block", r"<template>"),
        ("<script setup> block", r"<script\s+setup>"),
        ("q-layout", r"<q-layout"),
        ("platform detection", r"\$q\.platform|platform\.is"),
        ("desktop check", r"desktop"),
        ("mobile check", r"mobile"),
        ("q-drawer", r"<q-drawer"),
        ("q-footer tabs", r"<q-footer"),
        ("q-tabs", r"<q-tabs|<q-tab"),
        ("3 nav items", r"home|search|profile|[Nn]av"),
        ("shared active tab", r"activeTab|v-model"),
    ])


def check_easy_p03(path):
    """Touch gestures: swipe left/right counter + hold to reset."""
    return require_all(path, [
        ("<template> block", r"<template>"),
        ("<script setup> block", r"<script\s+setup>"),
        ("swipe left directive", r"v-touch-swipe\.left|touch-swipe.*left|swipe.*left"),
        ("swipe right directive", r"v-touch-swipe\.right|touch-swipe.*right|swipe.*right"),
        ("hold directive", r"v-touch-hold|touch-hold|longpress|long-press|hold"),
        ("counter ref", r"count|counter"),
        ("increment fn", r"increment|\+\+"),
        ("decrement fn", r"decrement|--|Math\.max"),
        ("reset fn", r"reset|=\s*0"),
        ("instructions shown", r"[Ss]wipe|[Ll]ong|[Hh]old|instruction"),
    ])


def check_medium_p01(path):
    """Camera: Capacitor plugin + web file fallback + permission errors."""
    return require_all(path, [
        ("<template> block", r"<template>"),
        ("<script setup> block", r"<script\s+setup>"),
        ("useQuasar", r"useQuasar|\$q"),
        ("capacitor check", r"capacitor|platform\.is"),
        ("Camera plugin", r"Camera|@capacitor/camera|getPhoto"),
        ("result type/data", r"DataUrl|dataUrl|resultType|Uri"),
        ("file input fallback", r"type=\"file\"|type='file'|fileInput|FileReader"),
        ("photo display", r"<q-img|<img|photoUrl|photo"),
        ("take photo button", r"<q-btn|<button|[Tt]ake"),
        ("error handling", r"catch|notify|permission"),
        ("loading state", r"loading|taking"),
    ])


def check_medium_p02(path):
    """Geolocation: get position, show lat/long + map, handle denial."""
    return require_all(path, [
        ("<template> block", r"<template>"),
        ("<script setup> block", r"<script\s+setup>"),
        ("geolocation API", r"Geolocation|geolocation|getCurrentPosition"),
        ("capacitor check", r"capacitor|platform\.is"),
        ("latitude", r"latitude|lat"),
        ("longitude", r"longitude|lng|lon"),
        ("map embed/link", r"iframe|openstreetmap|maps|mapUrl|<a\s"),
        ("loading state", r"loading"),
        ("permission handling", r"permission|denied|PERMISSION_DENIED"),
        ("error handling", r"catch|notify|error"),
        ("get location button", r"<q-btn|<button|[Ll]ocation"),
    ])


def check_medium_p03(path):
    """Share: Capacitor Share → navigator.share → clipboard fallback."""
    return require_all(path, [
        ("<template> block", r"<template>"),
        ("<script setup> block", r"<script\s+setup>"),
        ("capacitor check", r"capacitor|platform\.is"),
        ("Share plugin", r"Share|@capacitor/share|\.share\s*\("),
        ("navigator.share fallback", r"navigator\.share"),
        ("clipboard fallback", r"clipboard|writeText|execCommand"),
        ("share text/url", r"shareText|shareUrl|text|url"),
        ("notify on result", r"notify"),
        ("share button", r"<q-btn|<button|[Ss]hare"),
        ("cancel handling", r"catch|AbortError|cancel"),
    ])


def check_hard_p01(path):
    """Photo gallery: camera, grid, swipe viewer, hold-delete, share."""
    return require_all(path, [
        ("<template> block", r"<template>"),
        ("<script setup> block", r"<script\s+setup>"),
        ("Camera usage", r"Camera|@capacitor/camera|getPhoto|type=\"file\""),
        ("photos array", r"photos"),
        ("grid display", r"v-for|<q-img|col-|grid"),
        ("empty state", r"empty|photos\.length|v-if|v-else"),
        ("viewer dialog", r"<q-dialog|viewer|fullscreen|full-width"),
        ("swipe navigation", r"v-touch-swipe|touch-swipe"),
        ("hold to delete", r"v-touch-hold|touch-hold|hold"),
        ("delete confirm", r"[Dd]elete|\$q\.dialog|dialog"),
        ("share per photo", r"[Ss]hare|navigator\.share|@capacitor/share"),
        ("capacitor check", r"capacitor|platform\.is"),
    ])


def check_hard_p02(path):
    """App shell: platform detect, adaptive nav, haptics, safe areas."""
    return require_all(path, [
        ("<template> block", r"<template>"),
        ("<script setup> block", r"<script\s+setup>"),
        ("q-layout", r"<q-layout"),
        ("platform detection", r"platform\.is|\$q\.platform"),
        ("ios/android detect", r"ios|android|iOS|Android"),
        ("drawer (desktop)", r"<q-drawer"),
        ("bottom tabs (mobile)", r"<q-footer|<q-tabs|<q-tab"),
        ("haptics", r"[Hh]aptic|impact|vibrat"),
        ("haptic helper fn", r"hapticTap|haptic|onTap"),
        ("safe-area CSS", r"safe-area|env\s*\("),
        ("platform class/style", r"platform-|platformClass|platformLabel"),
        ("nav items", r"navItems|home|search|profile"),
    ])


def check_hard_p03(path):
    """Offline-first: storage abstraction, sync, pull-refresh, haptics."""
    return require_all(path, [
        ("<template> block", r"<template>"),
        ("<script setup> block", r"<script\s+setup>"),
        ("storage abstraction", r"Storage|localStorage|storageGet|storageSet"),
        ("capacitor check", r"capacitor|platform\.is"),
        ("online detection", r"navigator\.onLine|['\"]online['\"]|isOnline"),
        ("offline event", r"['\"]offline['\"]|onOffline"),
        ("offline banner", r"<q-banner|offline"),
        ("sync logic", r"sync|pending|syncPending|synced"),
        ("pull-to-refresh", r"v-touch-pull|touch-pull|onPull|pull"),
        ("haptics feedback", r"[Hh]aptic|impact|notification\("),
        ("cached data load", r"cached|loadCached|persistCache|cache"),
        ("items list", r"v-for|<q-item|<q-list|items"),
        ("refresh indicator", r"refresh|q-spinner|loading"),
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
    Matches easy/p01-*.*, excluding solutions/."""
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
        if "NoneType" in str(e):
            print(f"FAIL — a function returned None — write the body!")
        else:
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
        print("  LESSON 16 — AUTO-CHECK ALL")
        print("=" * 60)
        for check_id in CHECKS:
            run_one(check_id)
        print("=" * 60)
        return

    run_one(target)


if __name__ == "__main__":
    main()
