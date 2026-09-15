# File Organizer (Python) — Task Breakdown

> **Step-by-step implementation guide.** Follow each step in order.

---

## File Structure

```
mini-10-file-organizer/
├── organizer.py, config.py, main.py
└── README.md
```

---

## Implementation Steps

### Step 1: Config

Define file categories: images (.jpg, .png), docs (.pdf, .docx), videos (.mp4), etc.

**Checkpoint:** Step 1 is complete when the described functionality works.

### Step 2: Scan Directory

Walk directory, list all files with extensions. Return file list.

**Checkpoint:** Step 2 is complete when the described functionality works.

### Step 3: Categorize Files

Map each file to a category based on extension. Unknown → 'misc'.

**Checkpoint:** Step 3 is complete when the described functionality works.

### Step 4: Create Folders

Create category folders if they don't exist. Handle permissions.

**Checkpoint:** Step 4 is complete when the described functionality works.

### Step 5: Move Files

Move each file to its category folder. Handle name collisions (append number).

**Checkpoint:** Step 5 is complete when the described functionality works.

### Step 6: Dry Run Mode

--dry-run flag: show what would happen without moving. Log actions.

**Checkpoint:** Step 6 is complete when the described functionality works.

### Step 7: Undo Feature

Log all moves. --undo flag reverses the last operation.

**Checkpoint:** Step 7 is complete when the described functionality works.

### Step 8: CLI Interface

argparse: directory path, --dry-run, --undo, --verbose. Help text.

**Checkpoint:** Step 8 is complete when the described functionality works.

### Step 9: Logging

Log all actions to file. Show summary at end (X files moved to Y categories).

**Checkpoint:** Step 9 is complete when the described functionality works.

---

## Final Checklist

- [ ] Scan directory for files
- [ ] Categorize by extension
- [ ] Create category folders
- [ ] Move files to folders
- [ ] Handle name collisions
- [ ] Dry run mode
- [ ] Undo feature
- [ ] CLI with argparse
- [ ] Logging + summary

---

## Common Pitfalls

1. **Skipping steps** — each step builds on the previous. Don't jump ahead.
2. **Not testing incrementally** — test after each step, not just at the end.
3. **Ignoring error states** — handle empty states, loading, and errors from the start.
4. **Not making it responsive** — test on mobile from the beginning, not as an afterthought.
