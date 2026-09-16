"""
Auto-Check System — Lesson 15: Quasar PWA
=========================================
.vue files can't execute without a Quasar build step; .js files get a
parse-only syntax check via `node --check` where appropriate (skipped for
files whose content is intentionally non-JS, like a manifest object).
Everything is then verified STRUCTURALLY.

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
    """manifest.json: name, short_name, standalone, colors, 2 icons."""
    return require_all(path, [
        ("name field", r"['\"]?name['\"]?\s*:"),
        ("short_name", r"short_name"),
        ("description", r"description"),
        ("start_url", r"start_url"),
        ("standalone display", r"standalone"),
        ("theme_color", r"theme_color"),
        ("background_color", r"background_color"),
        ("icons array", r"icons"),
        ("128 icon", r"128"),
        ("512 icon", r"512"),
        ("icon src/sizes/type", r"src|sizes|type"),
    ], syntax=False)


def check_easy_p02(path):
    """Detect standalone display-mode; banner for PWA vs browser."""
    return require_all(path, [
        ("<template> block", r"<template>"),
        ("<script setup> block", r"<script\s+setup>"),
        ("matchMedia standalone", r"matchMedia|display-mode|standalone"),
        ("isPWA state", r"isPWA|standalone|installed|pwa"),
        ("banner output", r"<q-banner|<div|<q-card"),
        ("PWA vs browser text", r"PWA|browser|[Bb]rowser"),
        ("mounted check", r"onMounted|created|mounted"),
        ("change listener or cleanup", r"addEventListener|change|removeEventListener|onUnmounted"),
    ])


def check_easy_p03(path):
    """Install button: beforeinstallprompt → prompt() → userChoice."""
    return require_all(path, [
        ("<template> block", r"<template>"),
        ("<script setup> block", r"<script\s+setup>"),
        ("beforeinstallprompt listener", r"beforeinstallprompt"),
        ("preventDefault", r"preventDefault"),
        ("deferredPrompt stored", r"deferredPrompt|deferred|prompt\s*="),
        ("prompt() call", r"\.prompt\s*\("),
        ("userChoice awaited", r"userChoice"),
        ("canInstall/show flag", r"canInstall|v-if|showInstall|installed"),
        ("install button", r"<q-btn|<button"),
        ("outcome/notify", r"accepted|outcome|notify|appinstalled|installed"),
    ])


def check_medium_p01(path):
    """Workbox config: CacheFirst assets, NetworkFirst API, SWR images."""
    return require_all(path, [
        ("GenerateSW mode", r"GenerateSW|workboxPluginMode|workbox"),
        ("navigateFallback", r"navigateFallback|index\.html"),
        ("runtimeCaching", r"runtimeCaching"),
        ("CacheFirst handler", r"CacheFirst"),
        ("NetworkFirst handler", r"NetworkFirst"),
        ("StaleWhileRevalidate", r"StaleWhileRevalidate"),
        ("urlPattern(s)", r"urlPattern"),
        ("cacheName(s)", r"cacheName"),
        ("expiration limits", r"expiration|maxEntries|maxAgeSeconds"),
        ("network timeout", r"networkTimeoutSeconds|TimeoutSeconds|timeout"),
        ("export", r"export|module\.exports"),
    ])


def check_medium_p02(path):
    """Offline indicator: navigator.onLine + online/offline events + banner."""
    return require_all(path, [
        ("<template> block", r"<template>"),
        ("<script setup> block", r"<script\s+setup>"),
        ("navigator.onLine", r"navigator\.onLine|onLine"),
        ("online event listener", r"['\"]online['\"]"),
        ("offline event listener", r"['\"]offline['\"]"),
        ("offline banner", r"<q-banner|v-if|offline"),
        ("notify when back online", r"notify|online"),
        ("listener cleanup", r"onUnmounted|removeEventListener"),
    ])


def check_medium_p03(path):
    """Push permission request: status display, test notification, iOS note."""
    return require_all(path, [
        ("<template> block", r"<template>"),
        ("<script setup> block", r"<script\s+setup>"),
        ("permission state", r"permission"),
        ("requestPermission", r"requestPermission|Notification"),
        ("status display", r"permission|granted|denied|default"),
        ("test notification", r"new\s+Notification|sendTest|test"),
        ("iOS detection", r"iOS|iPad|iPhone|userAgent|iosLimitation"),
        ("standalone check", r"standalone|display-mode|matchMedia"),
        ("request button", r"<q-btn|<button"),
    ])


def check_hard_p01(path):
    """PWA onboarding: installed check, benefits, install, persisted dismiss."""
    return require_all(path, [
        ("<template> block", r"<template>"),
        ("<script setup> block", r"<script\s+setup>"),
        ("installed detection", r"standalone|display-mode|matchMedia|installed"),
        ("beforeinstallprompt", r"beforeinstallprompt"),
        ("deferred prompt", r"deferredPrompt|deferred"),
        ("install action", r"\.prompt\s*\(|install"),
        ("dismiss action", r"dismiss|later|close"),
        ("localStorage persist", r"localStorage"),
        ("benefits list", r"<q-list|<q-item|offline|installable|push|notification"),
        ("benefit icons", r"<q-icon|icon"),
        ("conditional show", r"v-if|showOnboarding|canInstall"),
    ])


def check_hard_p02(path):
    """Offline sync: queue in storage, smartFetch, replay on online, 409."""
    return require_all(path, [
        ("queue storage key", r"localStorage|indexedDB|QUEUE|queue"),
        ("getQueue function", r"getQueue|get.*[Qq]ueue"),
        ("addToQueue/push", r"addToQueue|push|enqueue"),
        ("smartFetch wrapper", r"smartFetch|queueFetch|offlineFetch"),
        ("navigator.onLine check", r"navigator\.onLine|onLine"),
        ("fetch call", r"fetch\s*\("),
        ("sync/replay function", r"syncQueue|replay|sync"),
        ("online event", r"['\"]online['\"]"),
        ("offline event", r"['\"]offline['\"]"),
        ("conflict handling (409)", r"409|conflict"),
        ("exports", r"export"),
    ])


def check_hard_p03(path):
    """PWA settings: install status, update row, push toggle, storage, clear."""
    return require_all(path, [
        ("<template> block", r"<template>"),
        ("<script setup> block", r"<script\s+setup>"),
        ("install status", r"standalone|display-mode|installed|matchMedia"),
        ("update available", r"update|updatefound|waiting|SKIP_WAITING|reload"),
        ("push toggle", r"<q-toggle|pushEnabled|Notification|push"),
        ("permission request", r"requestPermission|permission"),
        ("storage usage", r"storage|estimate|usage|quota"),
        ("clear cache", r"caches|clearCache|[Cc]lear"),
        ("persist settings", r"localStorage"),
        ("confirm dialog", r"\$q\.dialog|dialog|confirm"),
        ("settings rows", r"<q-item|<q-card|v-if"),
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
        print("  LESSON 15 — AUTO-CHECK ALL")
        print("=" * 60)
        for check_id in CHECKS:
            run_one(check_id)
        print("=" * 60)
        return

    run_one(target)


if __name__ == "__main__":
    main()
