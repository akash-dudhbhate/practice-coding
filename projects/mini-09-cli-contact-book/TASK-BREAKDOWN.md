# CLI Contact Book (Python) — Task Breakdown

> **Step-by-step implementation guide.** Follow each step in order.

---

## File Structure

```
mini-09-cli-contact-book/
├── contacts.py, storage.py, main.py
└── README.md
```

---

## Implementation Steps

### Step 1: Contact Class

Contact dataclass: name, phone, email, address. __str__ method.

**Checkpoint:** Step 1 is complete when the described functionality works.

### Step 2: Storage Module

Save/load contacts to JSON file. load_contacts(), save_contacts().

**Checkpoint:** Step 2 is complete when the described functionality works.

### Step 3: Add Contact

Prompt for fields. Validate phone (digits) and email (@). Add to list.

**Checkpoint:** Step 3 is complete when the described functionality works.

### Step 4: List Contacts

Display all contacts in a table format. Sort by name.

**Checkpoint:** Step 4 is complete when the described functionality works.

### Step 5: Search Contacts

Search by name, phone, or email. Case-insensitive. Partial match.

**Checkpoint:** Step 5 is complete when the described functionality works.

### Step 6: Edit Contact

Select by index or name. Update fields. Keep old value if empty.

**Checkpoint:** Step 6 is complete when the described functionality works.

### Step 7: Delete Contact

Select by index or name. Confirm before deletion.

**Checkpoint:** Step 7 is complete when the described functionality works.

### Step 8: Main Menu

Loop with menu: add, list, search, edit, delete, exit. Handle invalid input.

**Checkpoint:** Step 8 is complete when the described functionality works.

### Step 9: Error Handling

File not found, invalid input, duplicate contacts. Graceful messages.

**Checkpoint:** Step 9 is complete when the described functionality works.

---

## Final Checklist

- [ ] Add contact with validation
- [ ] List all contacts (sorted)
- [ ] Search contacts (partial match)
- [ ] Edit contact
- [ ] Delete contact (with confirm)
- [ ] JSON file persistence
- [ ] Clean CLI menu
- [ ] Error handling (graceful)

---

## Common Pitfalls

1. **Skipping steps** — each step builds on the previous. Don't jump ahead.
2. **Not testing incrementally** — test after each step, not just at the end.
3. **Ignoring error states** — handle empty states, loading, and errors from the start.
4. **Not making it responsive** — test on mobile from the beginning, not as an afterthought.
