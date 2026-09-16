"""
Progress Tracker — AI/ML Track
===============================
Run this to see your progress through all levels.

Usage:
    python3 progress.py

It checks each level's easy/medium/hard problems for a "DONE" marker.
Add "# DONE" to the first line of a problem file when you finish it.
"""

import os
import glob

TRACK_DIR = os.path.dirname(os.path.abspath(__file__))
LEVEL_DIR = os.path.join(TRACK_DIR, "ai-ml")


def get_levels():
    """Find all level directories."""
    levels = sorted(glob.glob(os.path.join(LEVEL_DIR, "level-*")))
    return levels


def count_problems(level_path, difficulty):
    """Count total and solved problems for a difficulty level."""
    level_dir = os.path.join(level_path, difficulty)
    if not os.path.isdir(level_dir):
        return 0, 0

    problems = glob.glob(os.path.join(level_dir, "p*.py"))
    # Exclude solutions dir and project files
    problems = [p for p in problems if "solutions" not in p and "project" not in os.path.basename(p)]
    total = len(problems)

    solved = 0
    for p in problems:
        with open(p) as f:
            first_line = f.readline().strip()
            if "DONE" in first_line:
                solved += 1
    return total, solved


def check_project(level_path):
    """Check if the project file is done."""
    project_dir = os.path.join(level_path, "project")
    if not os.path.isdir(project_dir):
        return None
    projects = glob.glob(os.path.join(project_dir, "*.py"))
    if not projects:
        return None
    with open(projects[0]) as f:
        first_line = f.readline().strip()
        return "DONE" in first_line


def show_progress():
    levels = get_levels()
    if not levels:
        print("No levels found in", LEVEL_DIR)
        return

    print("=" * 70)
    print("  AI/ML TRACK — PROGRESS")
    print("=" * 70)

    total_all = 0
    solved_all = 0
    level_totals = {"easy": 0, "medium": 0, "hard": 0}
    level_solved = {"easy": 0, "medium": 0, "hard": 0}
    level_stats = []

    for level_path in levels:
        level_name = os.path.basename(level_path)
        level_done = 0
        level_total = 0

        stats = {"name": level_name, "easy": (0, 0), "medium": (0, 0), "hard": (0, 0)}

        for level in ["easy", "medium", "hard"]:
            total, solved = count_problems(level_path, level)
            stats[level] = (solved, total)
            level_totals[level] += total
            level_solved[level] += solved
            total_all += total
            solved_all += solved
            level_done += solved
            level_total += total

        stats["project"] = check_project(level_path)
        stats["done"] = level_done
        stats["total"] = level_total
        level_stats.append(stats)

    # Show per-level breakdown
    print("\n  PER-LEVEL BREAKDOWN")
    print("  " + "-" * 66)

    for stats in level_stats:
        name = stats["name"]
        e_s, e_t = stats["easy"]
        m_s, m_t = stats["medium"]
        h_s, h_t = stats["hard"]
        proj = stats["project"]
        done = stats["done"]
        total = stats["total"]

        # Status icon
        if done == total and total > 0:
            icon = "✓"
        elif done > 0:
            icon = "◐"
        else:
            icon = "○"

        proj_str = "P" if proj else " "
        print(f"  {icon} {name[:40]:40} E:{e_s}/{e_t} M:{m_s}/{m_t} H:{h_s}/{h_t} [{proj_str}]")

    # Show totals
    print(f"\n  {'=' * 66}")
    print("  TOTALS BY LEVEL")
    print("  " + "-" * 66)

    for level in ["easy", "medium", "hard"]:
        solved = level_solved[level]
        total = level_totals[level]
        pct = int(100 * solved / total) if total > 0 else 0
        bar_len = 30
        filled = int(bar_len * solved / total) if total > 0 else 0
        bar = "█" * filled + "░" * (bar_len - filled)
        print(f"  {level.capitalize():8} {bar} {solved:3}/{total:3} ({pct:3}%)")

    print("  " + "-" * 66)
    overall_pct = int(100 * solved_all / total_all) if total_all > 0 else 0
    print(f"  OVERALL: {solved_all}/{total_all} problems ({overall_pct}%)")
    print("  " + "=" * 66)


if __name__ == "__main__":
    show_progress()
