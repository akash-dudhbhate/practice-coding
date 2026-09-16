"""
Fix corrupted "Write a function" lines in solve.py files.
The pattern was duplicated during the example injection.
"""

import os
import glob
import re

AIML_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ai-ml")

def fix_file(filepath):
    """Fix corrupted 'Write a function' line."""
    with open(filepath) as f:
        content = f.read()

    # Pattern: "that implements the solution. `solve()` that implements the solution."
    # Or: "that implements the solution. `funcname()` that implements the solution."
    bad_pattern = r'that implements the solution\. `\w+\(\)` that implements the solution\.'
    if not re.search(bad_pattern, content):
        return False

    # Fix it — keep only the first part
    new_content = re.sub(bad_pattern, 'that implements the solution.', content)

    with open(filepath, "w") as f:
        f.write(new_content)
    return True

def main():
    fixed = 0
    for solve_file in glob.glob(os.path.join(AIML_DIR, "*/**/p*-solve.py"), recursive=True):
        if fix_file(solve_file):
            fixed += 1
            print(f"Fixed: {solve_file}")

    print(f"\nFixed {fixed} files")

if __name__ == "__main__":
    main()
