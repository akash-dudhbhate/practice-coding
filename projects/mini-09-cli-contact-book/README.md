# Mini Project 09 — CLI Contact Book

> **Type:** Mini Project
> **Subject:** Python
> **Estimated sell price:** $50–100
> **Difficulty:** Beginner
> **Prerequisites:** Lessons 01–05 (Variables, Strings, Lists, Dicts, Control Flow)

## Project Brief

Build a command-line contact book where users can add, search, list, and delete contacts. Data is stored in memory (lists and dicts). This is a classic beginner project that demonstrates core Python skills.

## What you'll build

A Python CLI app with:
- **Add contact** — name, phone, email
- **Search contacts** — by name (case-insensitive partial match)
- **List all contacts** — sorted alphabetically
- **Delete contact** — by name
- **Exit** — quit the app
- Menu-driven interface using `input()` and `print()`

## Skills you'll demonstrate

- Variables, types, and functions
- Lists and dictionaries (storing contacts)
- Control flow (if/elif/else menu)
- Loops (while loop for app, for loop for listing)
- String methods (.lower() for case-insensitive search)
- Input/output with `input()` and `print()`

## Sellable pitch

> "I'll build you a custom CLI contact manager. Add, search, list, and delete contacts from your terminal. Great for personal use or as a base for a larger CRM. Can be extended with file storage, export, or a web interface."

## Requirements

- [ ] Menu with options: Add, Search, List, Delete, Exit
- [ ] Contacts stored as list of dicts: `{"name": ..., "phone": ..., "email": ...}`
- [ ] Add: prompts for name, phone, email; appends to list
- [ ] Search: case-insensitive, partial match (e.g., "ak" finds "Akash")
- [ ] List: all contacts sorted alphabetically by name, formatted nicely
- [ ] Delete: finds by exact name (case-insensitive), removes from list
- [ ] Handles empty list gracefully (shows "No contacts found")
- [ ] Handles contact not found gracefully (shows "Contact not found")
- [ ] Input validation: name cannot be empty
- [ ] Clean, readable output with formatting

## Getting started

1. Define the contact storage structure (list of dicts).
2. Write functions for each operation (add, search, list, delete).
3. Write the main menu loop with `input()`.
4. Connect menu choices to functions.
5. Add error handling for edge cases.
6. Test all operations manually.

## Deliverables

- `contact_book.py` — single-file CLI app
- Runs with `python contact_book.py`
- Handles all edge cases without crashing
