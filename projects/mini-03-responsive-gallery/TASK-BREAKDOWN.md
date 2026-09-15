# Responsive Image Gallery — Task Breakdown

> **Step-by-step implementation guide.** Follow each step in order.

---

## File Structure

```
mini-03-responsive-gallery/
├── index.html, styles.css, script.js (lightbox)
└── README.md
```

---

## Implementation Steps

### Step 1: HTML Structure

Grid container with image cards. Each card has image, caption, and data attributes.

**Checkpoint:** Step 1 is complete when the described functionality works.

### Step 2: CSS Grid Layout

Use CSS Grid with auto-fit and minmax for responsive columns. No media queries needed.

**Checkpoint:** Step 2 is complete when the described functionality works.

### Step 3: Image Cards

Style cards with border-radius, box-shadow, hover zoom effect.

**Checkpoint:** Step 3 is complete when the described functionality works.

### Step 4: Lightbox Modal

Hidden modal that shows full-size image on click. Include close button and prev/next.

**Checkpoint:** Step 4 is complete when the described functionality works.

### Step 5: JS: Open Lightbox

Click image → show modal with full image. Add keyboard support (Esc to close).

**Checkpoint:** Step 5 is complete when the described functionality works.

### Step 6: JS: Navigation

Prev/next buttons to cycle through images. Arrow key support.

**Checkpoint:** Step 6 is complete when the described functionality works.

### Step 7: CSS: Hover Effects

Scale on hover, overlay caption, smooth transitions.

**Checkpoint:** Step 7 is complete when the described functionality works.

### Step 8: Responsive

Grid auto-adjusts columns. Lightbox works on mobile (swipe optional).

**Checkpoint:** Step 8 is complete when the described functionality works.

---

## Final Checklist

- [ ] CSS Grid with auto-fit/minmax
- [ ] 6+ images with captions
- [ ] Lightbox modal on click
- [ ] Prev/next navigation in lightbox
- [ ] Keyboard support (Esc, arrows)
- [ ] Hover effects (zoom, overlay)
- [ ] Responsive (auto columns)
- [ ] Smooth transitions

---

## Common Pitfalls

1. **Skipping steps** — each step builds on the previous. Don't jump ahead.
2. **Not testing incrementally** — test after each step, not just at the end.
3. **Ignoring error states** — handle empty states, loading, and errors from the start.
4. **Not making it responsive** — test on mobile from the beginning, not as an afterthought.
