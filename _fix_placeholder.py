"""
Fix the {num} placeholder in solve.py files.
"""

import os
import glob
import re

AIML_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ai-ml")

def fix_file(filepath, level, num):
    """Fix the {num} placeholder in a solve.py file."""
    with open(filepath) as f:
        content = f.read()

    # Replace {num} with actual problem number
    new_content = content.replace(
        '# Check your answer: compare with solutions/p{num}-solution.py',
        f'# Check your answer: compare with solutions/p{num:02d}-solution.py'
    )

    if new_content != content:
        with open(filepath, "w") as f:
            f.write(new_content)
        return True
    return False

def main():
    updated = 0
    for lesson_path in sorted(glob.glob(os.path.join(AIML_DIR, "lesson-*"))):
        for level in ["easy", "medium", "hard"]:
            for i in range(1, 4):
                filepath = os.path.join(lesson_path, level, f"p{i:02d}-solve.py")
                if os.path.exists(filepath):
                    if fix_file(filepath, level, i):
                        updated += 1

    print(f"Updated {updated} files")

if __name__ == "__main__":
    main()
