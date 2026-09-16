"""
Extract test data from solution files and inject into problem files.
"""

import os
import glob
import re

AIML_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ai-ml")


def extract_test_data(solution_path):
    """Extract test data setup from a solution file."""
    if not os.path.exists(solution_path):
        return None

    with open(solution_path) as f:
        content = f.read()

    # Find the __main__ block
    main_match = re.search(
        r'if __name__\s*==\s*["\']__main__["\']\s*:\s*\n((?:    .+\n?)*)',
        content
    )
    if not main_match:
        return None

    main_block = main_match.group(1)
    lines = main_block.split('\n')

    # Extract data setup lines (variable assignments, not function calls)
    data_lines = []
    for line in lines:
        stripped = line.strip()
        if not stripped or stripped.startswith('#'):
            continue
        if '=' in stripped and not stripped.startswith(('print', 'return', 'import', 'from', 'if ', 'for ', 'result =')):
            if not any(x in stripped for x in ['fit(', 'predict(', 'transform(', 'score(', 'cross_val', 'GridSearch', 'plt.', 'savefig']):
                data_lines.append(stripped)

    return data_lines


def get_function_name(content):
    """Extract function name from 'Write a function `name()`' line."""
    match = re.search(r'Write a function `(\w+)\(\)`', content)
    if match:
        return match.group(1)
    return "solve"


def update_problem_file(problem_path, solution_path):
    """Add TRY THIS INPUT with real test data to a problem file."""
    with open(problem_path) as f:
        content = f.read()

    # Skip if already has real test data (not the generic template)
    if "Your test data here" not in content:
        return False

    func_name = get_function_name(content)
    data_lines = extract_test_data(solution_path)

    if not data_lines:
        return False

    # Build the new TRY THIS INPUT section
    test_section = "TRY THIS INPUT:\n"
    test_section += "  Add this test code at the bottom of your file:\n\n"
    test_section += "  ```python\n"
    for line in data_lines[:12]:
        test_section += f"  {line}\n"
    test_section += f"\n  # Call your function\n"
    test_section += f"  result = {func_name}(...)\n"
    test_section += f"  print(result)\n"
    test_section += "  ```"

    # Replace the generic TRY THIS INPUT section
    pattern = r'TRY THIS INPUT:\n  Add this test code at the bottom of your file:\n\n  ```python\n  # Your test data here\n  result = solve\(\.\.\.\)\n  print\(result\)\n  ```'
    new_content = re.sub(pattern, test_section, content, flags=re.DOTALL)

    if new_content != content:
        with open(problem_path, "w") as f:
            f.write(new_content)
        return True
    return False


def main():
    updated = 0
    skipped = 0

    for level_path in sorted(glob.glob(os.path.join(AIML_DIR, "level-*"))):
        for difficulty in ["easy", "medium", "hard"]:
            for i in range(1, 4):
                problem_file = os.path.join(level_path, difficulty, f"p{i:02d}-*.py")
                matches = [f for f in glob.glob(problem_file) if "solutions" not in f]
                if not matches:
                    continue

                problem_file = matches[0]
                solution_file = os.path.join(level_path, difficulty, "solutions", f"p{i:02d}-solution.py")

                if not os.path.exists(solution_file):
                    skipped += 1
                    continue

                if update_problem_file(problem_file, solution_file):
                    updated += 1
                else:
                    skipped += 1

    print(f"Updated {updated} files, skipped {skipped}")


if __name__ == "__main__":
    main()
