"""
Inject problem descriptions from task-explanation.md into solve.py files.

For each lesson, reads the task list from task-explanation.md and writes
the problem description into the corresponding solve.py file.
"""

import os
import re
import glob

AIML_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ai-ml")

def extract_problems(task_md_path):
    """Extract problem descriptions from task-explanation.md."""
    with open(task_md_path) as f:
        content = f.read()

    # Match lines like: `easy/p01-solve.py` — **Title**: Description
    # or: `easy/p01-solve.py` — Description (no bold)
    problems = {}
    patterns = [
        r'`(easy|medium|hard)/p(\d+)-solve\.py`\s*—\s*\*\*(.+?)\*\*[:.]?\s*(.+?)(?=\n\d+\.|\n###|$)',
        r'`(easy|medium|hard)/p(\d+)-solve\.py`\s*—\s*(.+?)(?=\n\d+\.|\n###|$)',
    ]
    for pattern in patterns:
        for match in re.finditer(pattern, content, re.DOTALL):
            groups = match.groups()
            level, num = groups[0], int(groups[1])
            if len(groups) == 4:
                title, desc = groups[2], groups[3]
            else:
                title, desc = groups[2], groups[2]
            desc = desc.strip().rstrip('.')
            problems[(level, num)] = {"title": title.strip(), "desc": desc}
        if problems:
            break

    return problems

def get_lesson_title(lesson_path):
    """Extract lesson title from directory name."""
    name = os.path.basename(lesson_path)
    # lesson-01-what-is-ml -> What is ML?
    parts = name.split("-", 2)
    if len(parts) >= 3:
        title = parts[2].replace("-", " ").title()
        return title
    return name

def update_solve_file(filepath, lesson_title, level, num, problem):
    """Update a solve.py file with the problem description."""
    title = problem["title"]
    desc = problem["desc"]

    level_num = {"easy": 1, "medium": 2, "hard": 3}
    problem_num = (level_num[level] - 1) * 3 + num

    new_content = f'''"""
LESSON — {lesson_title}
{level.upper()} P{num:02d} — {title}
{"=" * 50}

CONCEPT:
  See concepts.md in this lesson folder for detailed explanations.

PROBLEM:
  {desc}

Write a function `solve()` that implements the solution.
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
'''

    with open(filepath, "w") as f:
        f.write(new_content)
    print(f"  Updated {level}/p{num:02d}-solve.py")

def process_lesson(lesson_path):
    """Process one lesson directory."""
    task_md = os.path.join(lesson_path, "task-explanation.md")
    if not os.path.exists(task_md):
        print(f"  Skipping (no task-explanation.md)")
        return

    lesson_title = get_lesson_title(lesson_path)
    problems = extract_problems(task_md)

    if not problems:
        print(f"  No problems found in task-explanation.md")
        return

    print(f"\n{os.path.basename(lesson_path)} ({len(problems)} problems)")

    for (level, num), problem in sorted(problems.items()):
        filepath = os.path.join(lesson_path, level, f"p{num:02d}-solve.py")
        if os.path.exists(filepath):
            update_solve_file(filepath, lesson_title, level, num, problem)
        else:
            print(f"  WARNING: {level}/p{num:02d}-solve.py not found")

def main():
    lessons = sorted(glob.glob(os.path.join(AIML_DIR, "lesson-*")))
    print(f"Found {len(lessons)} lessons")

    for lesson_path in lessons:
        process_lesson(lesson_path)

    print("\nDone.")

if __name__ == "__main__":
    main()
