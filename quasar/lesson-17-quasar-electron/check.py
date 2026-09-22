"""
Auto-Check System — Lesson 17: Quasar Electron
==============================================
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
    """Main process: BrowserWindow 1200x800, loadURL/loadFile, lifecycle."""
    return require_all(path, [
        ("electron import", r"electron"),
        ("BrowserWindow", r"BrowserWindow"),
        ("window size", r"width|1200|height|800"),
        ("preload/webPreferences", r"preload|webPreferences"),
        ("load app", r"loadURL|loadFile"),
        ("whenReady", r"whenReady|ready"),
        ("closed handler", r"['\"]closed['\"]|closed"),
        ("window-all-closed", r"window-all-closed"),
        ("macOS check", r"darwin|platform"),
        ("activate handler", r"activate"),
    ])


def check_easy_p02(path):
    """Preload: contextBridge exposes readFile/saveFile/onMenuAction."""
    return require_all(path, [
        ("contextBridge", r"contextBridge"),
        ("ipcRenderer", r"ipcRenderer"),
        ("exposeInMainWorld", r"exposeInMainWorld"),
        ("api name", r"electronAPI|api"),
        ("readFile", r"readFile|read-file"),
        ("saveFile", r"saveFile|save-file"),
        ("onMenuAction", r"onMenuAction|menu-action"),
        ("invoke", r"invoke"),
    ])


def check_easy_p03(path):
    """IPC handlers: read-file + save-file with dialogs and try/catch."""
    return require_all(path, [
        ("ipcMain", r"ipcMain"),
        ("handle read-file", r"read-file|readFile"),
        ("handle save-file", r"save-file|saveFile"),
        ("open dialog", r"showOpenDialog"),
        ("save dialog", r"showSaveDialog"),
        ("fs read", r"readFileSync|readFile"),
        ("fs write", r"writeFileSync|writeFile"),
        ("cancel handling", r"canceled|cancelled"),
        ("error handling", r"try|catch|error"),
        ("handle() registration", r"ipcMain\.handle|\.handle\("),
    ])


def check_medium_p01(path):
    """App menu: File/Edit/View menus with accelerators + IPC sends."""
    return require_all(path, [
        ("Menu import", r"Menu"),
        ("buildFromTemplate", r"buildFromTemplate"),
        ("setApplicationMenu", r"setApplicationMenu"),
        ("File menu", r"['\"]File['\"]|File"),
        ("Edit menu", r"['\"]Edit['\"]|Edit"),
        ("View menu", r"['\"]View['\"]|View"),
        ("accelerators", r"accelerator|CmdOrCtrl"),
        ("menu-action IPC", r"menu-action|webContents\.send|\.send\("),
        ("Open item", r"Open"),
        ("Save item", r"Save"),
        ("DevTools", r"DevTools|toggleDevTools"),
        ("export", r"export"),
    ])


def check_medium_p02(path):
    """File editor component using window.electronAPI."""
    return require_all(path, [
        ("<template> block", r"<template>"),
        ("<script setup> block", r"<script\s+setup>"),
        ("electronAPI usage", r"electronAPI|window\.electron"),
        ("readFile call", r"readFile"),
        ("saveFile call", r"saveFile"),
        ("textarea input", r"textarea|<q-input|v-model"),
        ("open button", r"<q-btn|<button|[Oo]pen"),
        ("save button", r"[Ss]ave"),
        ("cancel handling", r"null|cancel"),
        ("error handling", r"catch|notify|error"),
        ("dirty/fileName state", r"dirty|fileName|content"),
    ])


def check_medium_p03(path):
    """System tray: Tray icon, context menu, click toggle, cleanup."""
    return require_all(path, [
        ("Tray import", r"Tray"),
        ("tray icon", r"new Tray|nativeImage|icon"),
        ("tooltip", r"setToolTip|tooltip|ToolTip"),
        ("context menu", r"setContextMenu|buildFromTemplate|contextMenu"),
        ("Show item", r"Show|\.show\("),
        ("Hide item", r"Hide|\.hide\("),
        ("Quit item", r"Quit|app\.quit"),
        ("click toggle", r"on\(['\"]click|isVisible"),
        ("close-to-tray", r"['\"]close['\"]|preventDefault"),
        ("destroy/export", r"destroy|export"),
    ])


def check_hard_p01(path):
    """Full text editor: dirty tracking, beforeunload, recent files, menu."""
    return require_all(path, [
        ("<template> block", r"<template>"),
        ("<script setup> block", r"<script\s+setup>"),
        ("electronAPI usage", r"electronAPI|window\.electron"),
        ("readFile/saveFile", r"readFile|saveFile"),
        ("dirty tracking", r"dirty"),
        ("unsaved indicator", r"•|unsaved|dirty"),
        ("beforeunload guard", r"beforeunload|confirmDiscard|dialog"),
        ("recent files", r"recent|recentFiles"),
        ("persist recents", r"localStorage|settings|persist"),
        ("menu action listener", r"onMenuAction|menu-action"),
        ("textarea editor", r"textarea|<q-input|v-model"),
        ("onMounted wiring", r"onMounted"),
    ])


def check_hard_p02(path):
    """Complete main process: single instance, menu, tray, IPC, updater."""
    return require_all(path, [
        ("electron import", r"electron"),
        ("BrowserWindow", r"BrowserWindow"),
        ("single instance", r"requestSingleInstanceLock|second-instance"),
        ("menu setup", r"setupMenu|Menu"),
        ("tray setup", r"createTray|Tray|tray"),
        ("whenReady", r"whenReady"),
        ("window-all-closed", r"window-all-closed"),
        ("ipcMain handlers", r"ipcMain\.handle|ipcMain"),
        ("file handlers", r"read-file|save-file|readFileSync|writeFileSync"),
        ("clipboard handler", r"clipboard"),
        ("notification", r"Notification|notification"),
        ("auto-update", r"autoUpdater|electron-updater|update"),
        ("export/tray cleanup", r"destroyTray|quit"),
    ])


def check_hard_p03(path):
    """Settings app: persisted settings, theme, shortcuts list."""
    return require_all(path, [
        ("<template> block", r"<template>"),
        ("<script setup> block", r"<script\s+setup>"),
        ("settings object", r"settings"),
        ("persistence get/set", r"electronAPI\.settings|localStorage|\.get\(|\.set\("),
        ("dark mode", r"darkMode|\$q\.dark|dark"),
        ("window size settings", r"windowWidth|windowHeight|[Ww]idth|[Hh]eight"),
        ("position settings", r"windowX|windowY|position|Position"),
        ("minimize to tray", r"minimizeToTray|tray|[Tt]ray"),
        ("auto-update toggle", r"autoUpdate|update"),
        ("shortcuts list", r"shortcuts|CmdOrCtrl|keys"),
        ("save on change", r"save|update:model-value"),
        ("loadSettings on mount", r"loadSettings|onMounted"),
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
        print("  LESSON 17 — AUTO-CHECK ALL")
        print("=" * 60)
        for check_id in CHECKS:
            run_one(check_id)
        print("=" * 60)
        return

    run_one(target)


if __name__ == "__main__":
    main()
