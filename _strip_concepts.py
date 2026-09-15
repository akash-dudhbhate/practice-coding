#!/usr/bin/env python3
"""
Strip CONCEPTS EXPLAINED sections from all problem files.
Replace with a one-line reference to concepts.md.
This makes problem files small (fixes IDE crashing) while keeping
all detailed explanations in the separate concepts.md file.
"""
import os, re

ROOT = os.path.dirname(os.path.abspath(__file__))

# Map each subject's lesson folder to its concepts.md reference
LESSON_DIRS = [
    "python/lesson-01-variables-types-functions",
    "html-css-javascript/lesson-01-html-structure",
    "react/lesson-01-components-jsx-props",
    "ai-ml/lesson-01-what-is-ml",
    "quasar/lesson-01-quasar-basics",
]

# Different comment styles per file extension
COMMENT_STYLES = {
    ".py":   "# {text}",
    ".js":   "// {text}",
    ".jsx":  "// {text}",
    ".html": "<!-- {text} -->",
    ".vue":  "<!-- {text} -->",
}

def strip_concepts(filepath):
    """Remove CONCEPTS EXPLAINED section, add reference line."""
    ext = os.path.splitext(filepath)[1]
    if ext not in COMMENT_STYLES:
        return False, "unknown extension"

    with open(filepath, "r") as f:
        content = f.read()

    # Pattern: from "CONCEPTS EXPLAINED" marker to the TODO marker (exclusive)
    # The CONCEPTS section starts with a comment line containing "CONCEPTS EXPLAINED"
    # and ends right before the TODO line.
    # We need to handle both the marker and everything until TODO.

    # Find the CONCEPTS EXPLAINED section
    # It starts with a line containing "CONCEPTS EXPLAINED" and ends before "TODO"
    lines = content.split("\n")

    # Find start: first line containing "CONCEPTS EXPLAINED"
    start_idx = None
    for i, line in enumerate(lines):
        if "CONCEPTS EXPLAINED" in line:
            start_idx = i
            break

    if start_idx is None:
        return False, "no CONCEPTS EXPLAINED section found"

    # Find end: first line containing "TODO" after start_idx
    end_idx = None
    for i in range(start_idx + 1, len(lines)):
        if "TODO" in lines[i]:
            end_idx = i
            break

    if end_idx is None:
        # No TODO found — remove from CONCEPTS to end of file
        end_idx = len(lines)

    # Build the reference line
    ref_text = "See concepts.md in this lesson folder for detailed explanations (WHY/WHERE/WHAT-GOES-WRONG)."
    comment_prefix = COMMENT_STYLES[ext].split("{")[0].strip()
    ref_line = COMMENT_STYLES[ext].format(text=ref_text)

    # Replace the section: keep everything before start_idx,
    # add reference line, then keep from end_idx onward
    new_lines = lines[:start_idx]
    new_lines.append(ref_line)
    new_lines.append("")  # blank line before TODO
    new_lines.extend(lines[end_idx:])

    new_content = "\n".join(new_lines)

    with open(filepath, "w") as f:
        f.write(new_content)

    return True, f"stripped {end_idx - start_idx} lines, added reference"


def main():
    total = 0
    stripped = 0
    skipped = 0

    for lesson_dir in LESSON_DIRS:
        full_lesson = os.path.join(ROOT, lesson_dir)
        if not os.path.isdir(full_lesson):
            print(f"SKIP (not found): {lesson_dir}")
            continue

        for difficulty in ["easy", "medium", "hard"]:
            diff_dir = os.path.join(full_lesson, difficulty)
            if not os.path.isdir(diff_dir):
                continue

            for filename in sorted(os.listdir(diff_dir)):
                filepath = os.path.join(diff_dir, filename)
                if not os.path.isfile(filepath):
                    continue
                total += 1
                ok, msg = strip_concepts(filepath)
                if ok:
                    stripped += 1
                    print(f"  STRIPPED: {lesson_dir}/{difficulty}/{filename} ({msg})")
                else:
                    skipped += 1
                    print(f"  SKIP: {lesson_dir}/{difficulty}/{filename} ({msg})")

    print(f"\nDone. Total: {total}, Stripped: {stripped}, Skipped: {skipped}")


if __name__ == "__main__":
    main()
