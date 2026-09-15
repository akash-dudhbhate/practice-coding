#!/usr/bin/env python3
"""
progress.py — Practice Coding Progress Tracker (v2 — 100 lessons + projects)
============================================================================

Run:    python3 progress.py          # compact: only lessons with progress
        python3 progress.py --all    # show all 100 lessons
        python3 progress.py --projects  # show project status only

Scans all subject folders, detects completed problems (files with no
remaining "TODO" markers), and prints horizontal bar-chart progress
per subject broken down by easy / medium / hard.

Also scans the projects/ folder for sellable project completion.

Completed bars are shown in GREEN.

How "completed" is detected:
    A problem file is considered COMPLETED when it contains NO
    "TODO" (case-insensitive) markers. Every problem file ships with
    a single TODO marker; once you write your solution and remove the
    TODO line, the file counts as done.

    For Python files, a function body that is just `pass` (the placeholder)
    also counts as incomplete.

    A project is considered COMPLETED when its README.md has no
    "(Filled in per project)" or "(Detailed requirements" placeholders.
"""

import os
import re
import sys

# ── ANSI Colors ────────────────────────────────────────────────────────
GREEN = "\033[32m"
BOLD = "\033[1m"
DIM = "\033[90m"
RESET = "\033[0m"
YELLOW = "\033[33m"
RED = "\033[31m"
CYAN = "\033[36m"

# ── Configuration ──────────────────────────────────────────────────────
ROOT = os.path.dirname(os.path.abspath(__file__))

SUBJECTS = [
    ("HTML / CSS / JS", "html-css-javascript"),
    ("React", "react"),
    ("Python", "python"),
    ("AI / ML", "ai-ml"),
    ("Quasar", "quasar"),
]

DIFFICULTIES = ["easy", "medium", "hard"]

# File extensions that count as problem files
TASK_EXTENSIONS = {".py", ".html", ".jsx", ".vue", ".js", ".css"}


# ── Helpers ────────────────────────────────────────────────────────────
def is_task_file(filename: str) -> bool:
    """Return True if filename is a problem file (by extension)."""
    ext = os.path.splitext(filename)[1].lower()
    return ext in TASK_EXTENSIONS


def file_is_completed(filepath: str) -> bool:
    """
    A file is completed if it has NO 'TODO' markers (case-insensitive)
    AND (for .py files) no function body that is just `pass`.
    """
    try:
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
    except OSError:
        return False

    # Check for TODO markers (covers # TODO, // TODO, <!-- TODO, TODO:)
    if "todo" in content.lower():
        return False

    # For Python files: check for standalone `pass` as a placeholder.
    if filepath.lower().endswith(".py"):
        if re.search(r"^\s*pass\s*$", content, re.MULTILINE):
            return False

    return True


def bar(pct: float, width: int = 30) -> str:
    """Return a colored horizontal bar string for a percentage (0-100).
    Filled portion is green, empty portion is dim."""
    filled = int(round(pct / 100 * width))
    filled_str = f"{GREEN}{'█' * filled}{RESET}"
    empty_str = f"{DIM}{'░' * (width - filled)}{RESET}"
    return f"[{filled_str}{empty_str}]"


def colored_pct(pct: float) -> str:
    """Return percentage string, green if 100%, yellow if partial, dim if 0%."""
    s = f"{pct:5.1f}%"
    if pct >= 100.0:
        return f"{GREEN}{BOLD}{s}{RESET}"
    elif pct > 0.0:
        return f"{YELLOW}{s}{RESET}"
    else:
        return f"{DIM}{s}{RESET}"


# ── Scanner ────────────────────────────────────────────────────────────
def scan_subject(subject_dir: str) -> dict:
    """
    Scan a subject folder and return:
    {
        "lessons": [ { "name": ..., "difficulties": {easy: {done, total}, ... } } ],
        "totals": { "easy": {"done": n, "total": n}, ... },
    }
    """
    subject_path = os.path.join(ROOT, subject_dir)
    if not os.path.isdir(subject_path):
        return {"lessons": [], "totals": None}

    lessons = []
    totals = {d: {"done": 0, "total": 0} for d in DIFFICULTIES}

    # Find lesson folders (lesson-XX-...)
    lesson_dirs = sorted(
        d for d in os.listdir(subject_path)
        if d.startswith("lesson-") and os.path.isdir(os.path.join(subject_path, d))
    )

    for lesson_dir in lesson_dirs:
        lesson_path = os.path.join(subject_path, lesson_dir)
        lesson_info = {"name": lesson_dir, "difficulties": {}}

        # Check each difficulty folder
        for diff in DIFFICULTIES:
            diff_path = os.path.join(lesson_path, diff)
            done = 0
            total = 0
            if os.path.isdir(diff_path):
                problem_files = sorted(
                    f for f in os.listdir(diff_path)
                    if is_task_file(f) and os.path.isfile(os.path.join(diff_path, f))
                )
                total = len(problem_files)
                for pf in problem_files:
                    if file_is_completed(os.path.join(diff_path, pf)):
                        done += 1
            lesson_info["difficulties"][diff] = {"done": done, "total": total}
            totals[diff]["done"] += done
            totals[diff]["total"] += total

        lessons.append(lesson_info)

    return {"lessons": lessons, "totals": totals}


def scan_projects() -> dict:
    """Scan projects/ folder and return completion status."""
    projects_path = os.path.join(ROOT, "projects")
    if not os.path.isdir(projects_path):
        return {"projects": [], "totals": {"done": 0, "total": 0}}

    projects = []
    project_dirs = sorted(
        d for d in os.listdir(projects_path)
        if os.path.isdir(os.path.join(projects_path, d))
    )

    for pdir in project_dirs:
        readme_path = os.path.join(projects_path, pdir, "README.md")
        is_done = False
        if os.path.isfile(readme_path):
            try:
                with open(readme_path, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()
                # A project is "done" when its README no longer has placeholder text
                if "(Filled in per project)" not in content and "(Detailed requirements" not in content:
                    is_done = True
            except OSError:
                pass

        # Determine type from folder name
        ptype = "mini"
        if pdir.startswith("medium"):
            ptype = "medium"
        elif pdir.startswith("capstone"):
            ptype = "capstone"

        projects.append({"name": pdir, "type": ptype, "done": is_done})

    done_count = sum(1 for p in projects if p["done"])
    return {"projects": projects, "totals": {"done": done_count, "total": len(projects)}}


# ── Renderer ───────────────────────────────────────────────────────────
def print_section_header(title: str, width: int = 64) -> None:
    print()
    print(f"{BOLD}{'=' * width}{RESET}")
    print(f"{BOLD}  {title}{RESET}")
    print(f"{BOLD}{'=' * width}{RESET}")


def print_bar_line(label: str, done: int, total: int, bar_width: int = 30) -> None:
    pct = (done / total * 100) if total > 0 else 0.0
    status = ""
    if total > 0 and done == total:
        status = f"{GREEN}✓ done{RESET}"
    elif total == 0:
        status = f"{DIM}— no problems yet{RESET}"
    print(f"  {label:<10} {bar(pct, bar_width)} {done}/{total}  ({colored_pct(pct)}) {status}")


def render_subject(name: str, data: dict, show_all: bool) -> None:
    lessons = data["lessons"]
    totals = data["totals"]

    print_section_header(f"{name}")

    if not lessons:
        print("  (no lessons found)")
        return

    # Per-lesson breakdown
    for lesson in lessons:
        # Count total problems in this lesson
        lesson_total = sum(lesson["difficulties"][d]["total"] for d in DIFFICULTIES)
        lesson_done = sum(lesson["difficulties"][d]["done"] for d in DIFFICULTIES)

        if lesson_total > 0 and lesson_done == lesson_total:
            lesson_status = f"{GREEN}✓ complete{RESET}"
        elif lesson_done > 0:
            lesson_status = f"{YELLOW}○ in progress{RESET}"
        else:
            lesson_status = f"{DIM}○ not started{RESET}"

        # In compact mode, skip lessons with no progress
        if not show_all and lesson_done == 0:
            continue

        print(f"\n  {BOLD}{lesson['name']}{RESET}  [{lesson_status}]")
        for diff in DIFFICULTIES:
            d = lesson["difficulties"][diff]
            print_bar_line(diff.capitalize(), d["done"], d["total"])

    # Subject totals
    print(f"\n  {DIM}{'─' * 50}{RESET}")
    print(f"  {BOLD}{name} — Totals{RESET}")
    for diff in DIFFICULTIES:
        d = totals[diff]
        print_bar_line(diff.capitalize(), d["done"], d["total"])

    # Overall subject percentage
    all_done = sum(totals[d]["done"] for d in DIFFICULTIES)
    all_total = sum(totals[d]["total"] for d in DIFFICULTIES)
    overall_pct = (all_done / all_total * 100) if all_total > 0 else 0.0
    print(f"\n  {BOLD}{'OVERALL':<10}{RESET} {bar(overall_pct)} {all_done}/{all_total}  ({colored_pct(overall_pct)})")


def render_projects(project_data: dict) -> None:
    print_section_header("SELLABLE PROJECTS")

    projects = project_data["projects"]
    if not projects:
        print("  (no projects found)")
        return

    # Group by type
    for ptype in ["mini", "medium", "capstone"]:
        type_projects = [p for p in projects if p["type"] == ptype]
        if not type_projects:
            continue

        type_label = f"{ptype.title()} Projects"
        done_count = sum(1 for p in type_projects if p["done"])
        total_count = len(type_projects)
        pct = (done_count / total_count * 100) if total_count > 0 else 0.0

        print(f"\n  {BOLD}{type_label}{RESET} ({done_count}/{total_count})")
        for p in type_projects:
            status = f"{GREEN}✓{RESET}" if p["done"] else f"{DIM}○{RESET}"
            print(f"    {status} {p['name']}")

    # Totals
    totals = project_data["totals"]
    print(f"\n  {DIM}{'─' * 50}{RESET}")
    print_bar_line("Projects", totals["done"], totals["total"])


def render_global_summary(all_data: list, project_data: dict) -> None:
    print_section_header("GLOBAL SUMMARY")

    grand_done = 0
    grand_total = 0

    for name, data in all_data:
        totals = data["totals"]
        if totals is None:
            print_bar_line(name, 0, 0)
            continue
        done = sum(totals[d]["done"] for d in DIFFICULTIES)
        total = sum(totals[d]["total"] for d in DIFFICULTIES)
        grand_done += done
        grand_total += total
        print_bar_line(name, done, total)

    # Projects
    p_totals = project_data["totals"]
    print_bar_line("Projects", p_totals["done"], p_totals["total"])

    print(f"\n  {DIM}{'─' * 50}{RESET}")
    grand_pct = (grand_done / grand_total * 100) if grand_total > 0 else 0.0
    print_bar_line("ALL LESSONS", grand_done, grand_total, bar_width=40)

    print(f"\n  {DIM}Legend:{RESET}  {GREEN}█{RESET} = completed   {DIM}░{RESET} = pending")
    print(f"  {DIM}A file is 'completed' when it has no TODO markers{RESET}")
    print(f"  {DIM}(and no bare `pass` in Python files).{RESET}")
    print(f"  {DIM}Use --all to see all 100 lessons, --projects for project details.{RESET}")


# ── Main ───────────────────────────────────────────────────────────────
def main() -> int:
    show_all = "--all" in sys.argv
    projects_only = "--projects" in sys.argv

    print()
    print(f"{BOLD}╔{'═' * 62}╗{RESET}")
    print(f"{BOLD}║{'  PRACTICE CODING — PROGRESS TRACKER v2'.center(62)}║{RESET}")
    print(f"{BOLD}║{'  100 Lessons + 34 Sellable Projects'.center(62)}║{RESET}")
    print(f"{BOLD}╚{'═' * 62}╝{RESET}")

    # Always scan projects
    project_data = scan_projects()

    if projects_only:
        render_projects(project_data)
        print()
        return 0

    all_data = []
    for display_name, folder in SUBJECTS:
        data = scan_subject(folder)
        all_data.append((display_name, data))

    for display_name, data in all_data:
        render_subject(display_name, data, show_all)

    render_projects(project_data)
    render_global_summary(all_data, project_data)
    print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
