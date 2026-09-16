"""Remove the bad TRY THIS sections added by the previous script."""
import os, glob, re

AIML_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ai-ml")

def fix_file(filepath):
    with open(filepath) as f:
        content = f.read()

    # Remove the TRY THIS section
    pattern = r'\n\nTRY THIS:\n.+?\n\n# === WRITE YOUR CODE BELOW ==='
    new_content = re.sub(pattern, '\n\n# === WRITE YOUR CODE BELOW ===', content, flags=re.DOTALL)

    if new_content != content:
        with open(filepath, "w") as f:
            f.write(new_content)
        return True
    return False

count = 0
for f in glob.glob(os.path.join(AIML_DIR, "*/**/*.py"), recursive=True):
    if fix_file(f):
        count += 1
print(f"Cleaned {count} files")
