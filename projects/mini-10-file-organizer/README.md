# Mini Project 10 — File Organizer Script

> **Type:** Mini Project
> **Subject:** Python
> **Estimated sell price:** $50–150
> **Difficulty:** Beginner–Intermediate
> **Prerequisites:** Lessons 01–10 (Python basics through OOP)

## Project Brief

Build a Python script that organizes files in a directory by their extension. It scans a folder, creates subfolders by file type (Images, Documents, Videos, etc.), and moves files into the appropriate folder. This is a sellable utility — people pay for tools that clean up their Downloads folder.

## What you'll build

A CLI script that:
- Takes a directory path as argument
- Scans all files in the directory
- Categorizes by extension (Images: .jpg/.png, Documents: .pdf/.docx, etc.)
- Creates category folders if they don't exist
- Moves files into the appropriate folder
- Reports what was moved (summary)

## Skills you'll demonstrate

- File I/O (os module, shutil)
- Dictionaries (extension → category mapping)
- Loops and conditionals
- Error handling (permission errors, missing files)
- CLI arguments (sys.argv or argparse)

## Requirements

- [ ] Script accepts directory path as CLI argument
- [ ] Categories: Images (.jpg, .png, .gif, .svg), Documents (.pdf, .docx, .txt, .xlsx), Videos (.mp4, .avi, .mov), Audio (.mp3, .wav, .flac), Archives (.zip, .tar, .gz), Code (.py, .js, .html, .css), Others (everything else)
- [ ] Creates category folders if they don't exist
- [ ] Moves files to appropriate folder
- [ ] Handles files with no extension (goes to "Others")
- [ ] Prints summary: "Moved 15 files: 5 Images, 7 Documents, 3 Others"
- [ ] Handles errors gracefully (permission denied, file not found)
- [ ] Doesn't move folders (only files)
- [ ] Dry-run mode (--dry-run flag): shows what would be moved without actually moving

## Deliverables

- `organizer.py` — single-file script
- Runs with `python organizer.py /path/to/directory`
- `--dry-run` flag for safe preview
