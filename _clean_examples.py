"""
Clean up solve.py files — simplify the example section to point to solutions.
"""

import os
import glob
import re

AIML_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ai-ml")

def update_solve_file(filepath):
    """Clean up a solve.py file — simplify example section."""
    with open(filepath) as f:
        content = f.read()

    # Remove the old EXAMPLE/EXPECTED OUTPUT section
    # Pattern: "EXAMPLE:...Write a function" or "EXPECTED OUTPUT:...Write a function"
    patterns = [
        r'\nEXAMPLE:\n.+?\n\nWrite a function `\w+\(\)` that implements the solution\.',
        r'\nEXPECTED OUTPUT:\n.+?\n\nWrite a function `\w+\(\)` that implements the solution\.',
    ]

    new_content = content
    for pattern in patterns:
        new_content = re.sub(pattern, '\n\nWrite a function `solve()` that implements the solution.\n\n# Check your answer: compare with solutions/p{num}-solution.py', new_content, flags=re.DOTALL)

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
                    if update_solve_file(filepath):
                        updated += 1

    print(f"Updated {updated} files")

if __name__ == "__main__":
    main()
