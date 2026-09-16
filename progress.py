"""
Progress Tracker — AI/ML Track
===============================
Run this to see your progress through all levels.

Usage:
    python3 progress.py                    # show progress
    python3 progress.py --verify 07        # check all level-07 problems,
                                           # auto-mark # DONE on PASS
    python3 progress.py --verify 07 easy/p01   # verify one problem

It checks each level's easy/medium/hard problems for a "DONE" marker.
--verify runs the level's check.py and adds "# DONE" automatically
when a problem passes.
"""

import os
import glob
import subprocess
import sys

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


def find_problem_file(level_path, difficulty, num):
    """Locate the learner's problem file for a check id."""
    num_clean = num.lstrip("p")
    d = os.path.join(level_path, difficulty)
    exact = os.path.join(d, f"p{num_clean}-solve.py")
    if os.path.exists(exact):
        return exact
    matches = [f for f in glob.glob(os.path.join(d, f"p{num_clean}-*.py"))
               if "solutions" not in f]
    return matches[0] if matches else None


def mark_done(filepath):
    """Add '# DONE' to the first line if not already present."""
    with open(filepath) as f:
        content = f.read()
    if content.lstrip().startswith("# DONE") or "DONE" in content.split("\n")[0]:
        return False
    with open(filepath, "w") as f:
        f.write("# DONE\n" + content)
    return True


def verify(level_arg, problem_arg=None):
    """Run a level's check.py and auto-mark DONE on pass."""
    levels = get_levels()
    matches = [l for l in levels if f"level-{level_arg.zfill(2)}" in os.path.basename(l)]
    if not matches:
        print(f"No level matching '{level_arg}'")
        return
    level_path = matches[0]
    check_py = os.path.join(level_path, "check.py")
    if not os.path.exists(check_py):
        print(f"No check.py in {os.path.basename(level_path)}")
        return

    if problem_arg:
        targets = [problem_arg]
    else:
        targets = [f"{d}/p{n:02d}" for d in ["easy", "medium", "hard"]
                   for n in range(1, 4)]

    for target in targets:
        difficulty, num = target.split("/")
        filepath = find_problem_file(level_path, difficulty, num)
        if not filepath:
            print(f"  {target}: FILE NOT FOUND")
            continue
        r = subprocess.run([sys.executable, "check.py", target],
                           cwd=level_path, capture_output=True, text=True)
        out = r.stdout.strip()
        first = out.split("\n")[0] if out else r.stderr.split("\n")[0]
        if first.startswith("PASS"):
            marked = mark_done(filepath)
            print(f"  {target}: PASS" + (" (marked DONE)" if marked else " (already DONE)"))
        else:
            print(f"  {target}: {first}")


if __name__ == "__main__":
    if len(sys.argv) >= 3 and sys.argv[1] == "--verify":
        verify(sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else None)
    else:
        show_progress()
