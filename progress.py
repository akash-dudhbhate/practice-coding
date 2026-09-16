"""
Progress Tracker — AI/ML Track
===============================
Run this to see your progress through all lessons.

Usage:
    python3 progress.py

It checks each lesson's easy/medium/hard problems for a "DONE" marker.
Add "# DONE" to the first line of a problem file when you finish it.
"""

import os
import glob

TRACK_DIR = os.path.dirname(os.path.abspath(__file__))
LESSON_DIR = os.path.join(TRACK_DIR, "ai-ml")

def get_lessons():
    """Find all lesson directories."""
    lessons = sorted(glob.glob(os.path.join(LESSON_DIR, "lesson-*")))
    return lessons

def count_problems(lesson_path, level):
    """Count total and solved problems for a difficulty level."""
    level_dir = os.path.join(lesson_path, level)
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

def show_progress():
    lessons = get_lessons()
    if not lessons:
        print("No lessons found in", LESSON_DIR)
        return

    print("=" * 60)
    print("  AI/ML TRACK — PROGRESS")
    print("=" * 60)

    total_all = 0
    solved_all = 0
    level_totals = {"easy": 0, "medium": 0, "hard": 0}
    level_solved = {"easy": 0, "medium": 0, "hard": 0}

    for lesson_path in lessons:
        lesson_name = os.path.basename(lesson_path)
        print(f"\n  {lesson_name}")
        print(f"  {'-' * 50}")

        for level in ["easy", "medium", "hard"]:
            total, solved = count_problems(lesson_path, level)
            level_totals[level] += total
            level_solved[level] += solved
            total_all += total
            solved_all += solved

            bar_len = 20
            filled = int(bar_len * solved / total) if total > 0 else 0
            bar = "█" * filled + "░" * (bar_len - filled)
            print(f"    {level.capitalize():8} {bar} {solved}/{total}")

        # Check for project file
        projects = glob.glob(os.path.join(lesson_path, "project-*.py"))
        for proj in projects:
            proj_name = os.path.basename(proj).replace("project-", "").replace(".py", "").replace("-", " ").title()
            with open(proj) as f:
                first_line = f.readline().strip()
                done = "DONE" in first_line
            status = "DONE" if done else "TODO"
            print(f"    Project  {proj_name:30} [{status}]")

    print(f"\n  {'=' * 50}")
    print(f"  OVERALL: {solved_all}/{total_all} problems solved")
    print(f"  Easy:    {level_solved['easy']}/{level_totals['easy']}")
    print(f"  Medium:  {level_solved['medium']}/{level_totals['medium']}")
    print(f"  Hard:    {level_solved['hard']}/{level_totals['hard']}")
    print(f"  {'=' * 50}")

if __name__ == "__main__":
    show_progress()
