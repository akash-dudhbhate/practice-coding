"""
Fix examples in solve.py files — use actual solution files to generate accurate examples.
"""

import os
import glob
import re

AIML_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ai-ml")

def extract_example_from_solution(solution_path):
    """Extract a simple example from the solution file."""
    if not os.path.exists(solution_path):
        return None

    with open(solution_path) as f:
        content = f.read()

    # Look for test/example code at the bottom
    # Common patterns: "if __name__", "Test", "Example", "Expected output"
    lines = content.split('\n')

    # Find print statements or test code
    test_lines = []
    in_test = False
    for line in lines:
        if '__main__' in line or 'print(' in line.lower() or 'assert' in line.lower():
            in_test = True
        if in_test:
            test_lines.append(line)

    if test_lines:
        return '\n'.join(test_lines[:10])  # First 10 lines of test code

    # If no test code found, return the docstring summary
    docstring_match = re.search(r'"""(.+?)"""', content, re.DOTALL)
    if docstring_match:
        return docstring_match.group(1).strip()[:200]

    return None

def update_solve_file(filepath, solution_path):
    """Update a solve.py file with an accurate example from the solution."""
    with open(filepath) as f:
        content = f.read()

    # Get the current example section
    example_match = re.search(r'EXAMPLE:\n(.+?)\n\nWrite a function', content, re.DOTALL)
    if not example_match:
        return False

    current_example = example_match.group(1).strip()

    # Get better example from solution
    better_example = extract_example_from_solution(solution_path)
    if not better_example:
        return False

    # Clean up the example — make it a comment-style hint
    example_hint = f'''  # Expected output (from solution):
  # {better_example.replace(chr(10), chr(10) + '  # ')}'''

    # Replace the example section
    new_content = content.replace(
        f'EXAMPLE:\n{current_example}',
        f'EXPECTED OUTPUT:\n{example_hint}'
    )

    with open(filepath, "w") as f:
        f.write(new_content)
    return True

def main():
    updated = 0
    for lesson_path in sorted(glob.glob(os.path.join(AIML_DIR, "lesson-*"))):
        lesson_name = os.path.basename(lesson_path)
        for level in ["easy", "medium", "hard"]:
            for i in range(1, 4):
                solve_file = os.path.join(lesson_path, level, f"p{i:02d}-solve.py")
                solution_file = os.path.join(lesson_path, level, "solutions", f"p{i:02d}-solution.py")
                if os.path.exists(solve_file) and os.path.exists(solution_file):
                    if update_solve_file(solve_file, solution_file):
                        updated += 1

    print(f"Updated {updated} files")

if __name__ == "__main__":
    main()
