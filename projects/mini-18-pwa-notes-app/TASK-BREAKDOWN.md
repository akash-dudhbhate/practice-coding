# PWA Notes App (Quasar) — Task Breakdown

> **Step-by-step implementation guide.** Follow each step in order.

---

## File Structure

```
mini-18-pwa-notes-app/
├── src/pages/Notes.vue, src/components/NoteEditor.vue, src/stores/notes.js, src-pwa/...
└── README.md
```

---

## Implementation Steps

### Step 1: Quasar PWA Setup

quasar create app --kit pwa. Configure manifest.json.

**Checkpoint:** Step 1 is complete when the described functionality works.

### Step 2: Notes Store

Pinia: notes array, addNote, editNote, deleteNote. localStorage persistence.

**Checkpoint:** Step 2 is complete when the described functionality works.

### Step 3: Notes List Page

QList of notes with title, preview, date. Search bar. FAB to add.

**Checkpoint:** Step 3 is complete when the described functionality works.

### Step 4: NoteEditor Component

QInput for title, QTextarea for content. Auto-save. Back button.

**Checkpoint:** Step 4 is complete when the described functionality works.

### Step 5: Offline Support

Workbox config: cache app shell. Notes work offline (localStorage).

**Checkpoint:** Step 5 is complete when the described functionality works.

### Step 6: Install Prompt

beforeinstallprompt event. Custom install button in settings.

**Checkpoint:** Step 6 is complete when the described functionality works.

### Step 7: Manifest

name, icons, theme_color, display: standalone. Test install.

**Checkpoint:** Step 7 is complete when the described functionality works.

### Step 8: Responsive

Mobile-first. Desktop: list + editor side-by-side (master-detail).

**Checkpoint:** Step 8 is complete when the described functionality works.

---

## Final Checklist

- [ ] Notes store with localStorage
- [ ] Notes list with search
- [ ] Note editor with auto-save
- [ ] Works offline (PWA)
- [ ] Installable (manifest + prompt)
- [ ] App icons configured
- [ ] Responsive (master-detail on desktop)
- [ ] Create/edit/delete notes

---

## Common Pitfalls

1. **Skipping steps** — each step builds on the previous. Don't jump ahead.
2. **Not testing incrementally** — test after each step, not just at the end.
3. **Ignoring error states** — handle empty states, loading, and errors from the start.
4. **Not making it responsive** — test on mobile from the beginning, not as an afterthought.
5. **Hardcoding values** — use environment variables for API keys, URLs, and configuration.
