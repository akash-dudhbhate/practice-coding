"""
Update all problem files with a clear INPUT/OUTPUT section.
Shows test input code and tells user to run the solution to see expected output.
"""

import os
import glob
import re

AIML_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ai-ml")


def extract_main_block(solution_path):
    """Extract the __main__ block from a solution file."""
    if not os.path.exists(solution_path):
        return None

    with open(solution_path) as f:
        content = f.read()

    main_match = re.search(
        r'if __name__\s*==\s*["\']__main__["\']\s*:\s*\n((?:    .+\n?)*)',
        content
    )
    if not main_match:
        return None

    return main_match.group(1).strip()


def extract_test_data(main_block):
    """Extract the test data setup — variable assignments only."""
    lines = main_block.split('\n')
    data_lines = []
    for line in lines:
        stripped = line.strip()
        if not stripped or stripped.startswith('#'):
            continue
        if '=' in stripped and not stripped.startswith(('print', 'return', 'import', 'from', 'if ', 'for ')):
            if not any(x in stripped for x in ['fit(', 'predict(', 'transform(', 'score(', 'cross_val', 'GridSearch', 'plt.', 'savefig']):
                data_lines.append(stripped)
    return data_lines


def get_function_name(content):
    """Extract function name from 'Write a function `name()`' line."""
    match = re.search(r'Write a function `(\w+)\(\)`', content)
    if match:
        return match.group(1)
    return "solve"


def get_solution_filename(solution_path):
    """Get the relative path to the solution file."""
    # Extract lesson/level/filename from the path
    parts = solution_path.split('/')
    for i, part in enumerate(parts):
        if part.startswith('lesson-'):
            lesson = part
            level = parts[i+1]
            filename = os.path.basename(solution_path)
            return f"{level}/solutions/{filename}"
    return "solutions/p01-solution.py"


def update_problem_file(filepath, solution_path):
    """Add INPUT/OUTPUT section to a problem file."""
    with open(filepath) as f:
        content = f.read()

    # Skip if already has TRY THIS section
    if "TRY THIS INPUT:" in content:
        return False

    func_name = get_function_name(content)
    main_block = extract_main_block(solution_path)
    if not main_block:
        return False

    data_lines = extract_test_data(main_block)
    if not data_lines:
        return False

    sol_rel = get_solution_filename(solution_path)

    # Build the section
    section = []
    section.append("TRY THIS INPUT:")
    section.append("  Add this test code at the bottom of your file:")
    section.append("")
    section.append("  ```python")
    for line in data_lines[:12]:
        section.append(f"  {line}")
    section.append("")
    section.append(f"  # Call your function")
    section.append(f"  result = {func_name}(...)")
    section.append(f"  print(result)")
    section.append("  ```")
    section.append("")
    section.append("EXPECTED OUTPUT:")
    section.append(f"  Run the solution file to see expected output:")
    section.append(f"    python3 {sol_rel}")
    section.append("")
    section.append("  Then compare your output format with theirs.")

    section_text = '\n'.join(section)

    # Insert before "# === WRITE YOUR CODE BELOW ==="
    marker = "# === WRITE YOUR CODE BELOW ==="
    if marker in content:
        new_content = content.replace(marker, f"{section_text}\n\n{marker}")
    else:
        new_content = content + f"\n\n{section_text}\n"

    with open(filepath, "w") as f:
        f.write(new_content)
    return True


def main():
    updated = 0
    skipped = 0

    for lesson_path in sorted(glob.glob(os.path.join(AIML_DIR, "lesson-*"))):
        for level in ["easy", "medium", "hard"]:
            for i in range(1, 4):
                problem_file = os.path.join(lesson_path, level, f"p{i:02d}-solve.py")
                solution_file = os.path.join(lesson_path, level, "solutions", f"p{i:02d}-solution.py")

                if not os.path.exists(problem_file):
                    pattern = os.path.join(lesson_path, level, f"p{i:02d}-*.py")
                    matches = [f for f in glob.glob(pattern) if "solutions" not in f and "solve" not in f]
                    if matches:
                        problem_file = matches[0]

                if not os.path.exists(problem_file):
                    continue

                if not os.path.exists(solution_file):
                    continue

                if update_problem_file(problem_file, solution_file):
                    updated += 1
                else:
                    skipped += 1

    print(f"Updated {updated} files, skipped {skipped}")


if __name__ == "__main__":
    main()
